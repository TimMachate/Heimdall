#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.technicaldatasheet.models import TechnicalDataSheet
from documentationmanagement.file.models import File, TechnicalDataSheetProxy
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from django.forms import inlineformset_factory
from documentationmanagement.technicaldatasheet.forms import TechnicalDataSheetForm
from documentationmanagement.file.forms import FileForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
from documentationmanagement.file.views import FileView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class TechnicalDataSheetView(FileView):
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'documentationmanagement'
        self.context['model'] = 'technicaldatasheet'
#--------------------------------------------------------------------------------
class TechnicalDataSheetListView(TechnicalDataSheetView):

    permission_required = 'documentationmanagement.list_technicaldatasheet'

    template_name = 'technicaldatasheet/templates/technicaldatasheet_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = TechnicalDataSheetProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,url_detail,url_update,url_delete,reference_number,name,version,type,url_file,url_file_qrcode"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:technicaldatasheet_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class TechnicalDataSheetTableView(TechnicalDataSheetView):

    permission_required = 'documentationmanagement.table_technicaldatasheet'

    template_name = 'technicaldatasheet/templates/technicaldatasheet_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = TechnicalDataSheetProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,reference_number,name,version,type,create,update"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:technicaldatasheet_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class TechnicalDataSheetCreateUpdateDetailView(TechnicalDataSheetView):

    permission_required = ('documentationmanagement.add_technicaldatasheet','documentationmanagement.change_technicaldatasheet')

    template_name = 'technicaldatasheet/templates/technicaldatasheet_createupdatedetail.html'
    
    form_class = FileForm
    formset_class = TechnicalDataSheetForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(
            instance=self.context['queryset'],
            initial=self.get_initial()["file"]
            )
        self.context['formset'] = self.formset_class(
            initial=self.get_initial()["technicaldatasheet"]
            )
        return render(request, self.template_name, self.context)

    def get_initial(self):
        result = {}
        result["file"]={}
        result["technicaldatasheet"] = {}
        if self.get_queryset():
            result["file"]["type"] = "TE"
            if self.get_queryset().content():
                result["technicaldatasheet"]["file_id"] = self.get_queryset().id
                result["technicaldatasheet"]["content"] = self.get_queryset().content().content
        return result

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance=self.get_queryset())
        formset = self.formset_class(request.POST,request.FILES, instance=self.get_queryset().content() if self.get_queryset() else None)
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid() and formset.is_valid():
            obj = form.save(commit=False)
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            technicaldatasheet = formset.save(commit=False)
            technicaldatasheet.file_id = obj
            obj.save()
            technicaldatasheet.save()
            self.context['form'] = form
            self.context['formset'] = formset
        else:
            self.context['form'] = form
            self.context['formset'] = formset
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
            return redirect('documentationmanagement:technicaldatasheet_detail',technicaldatasheet=obj.slug)
        messages.success(request,'Die eingegeben Daten wurden validiert!')
        return redirect('documentationmanagement:technicaldatasheet_detail',technicaldatasheet=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('technicaldatasheet'):
            queryset=TechnicalDataSheetProxy.objects.get(slug=self.kwargs.get('technicaldatasheet'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class TechnicalDataSheetDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'documentationmanagement.delete_technicaldatasheet'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('technicaldatasheet'):
            File.objects.get(slug = self.kwargs.get('technicaldatasheet')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('documentationmanagement:technicaldatasheet_list')
#--------------------------------------------------------------------------------