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
from documentationmanagement.safetydatasheet.models import SafetyDataSheet
from documentationmanagement.file.models import File, SafetyDataSheetProxy
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from django.forms import inlineformset_factory
from documentationmanagement.safetydatasheet.forms import SafetyDataSheetForm
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
class SafetyDataSheetView(FileView):
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'documentationmanagement'
        self.context['model'] = 'safetydatasheet'
#--------------------------------------------------------------------------------
class SafetyDataSheetListView(SafetyDataSheetView):

    permission_required = 'documentationmanagement.list_safetydatasheet'

    template_name = 'safetydatasheet/templates/safetydatasheet_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = SafetyDataSheetProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,url_detail,url_update,url_delete,reference_number,name,version,type,url_file,url_file_qrcode"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:safetydatasheet_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class SafetyDataSheetTableView(SafetyDataSheetView):

    permission_required = 'documentationmanagement.table_safetydatasheet'

    template_name = 'safetydatasheet/templates/safetydatasheet_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = SafetyDataSheetProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,reference_number,name,version,type,create,update"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:safetydatasheet_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class SafetyDataSheetCreateUpdateDetailView(SafetyDataSheetView):

    permission_required = ('documentationmanagement.add_safetydatasheet','documentationmanagement.change_safetydatasheet')

    template_name = 'safetydatasheet/templates/safetydatasheet_createupdatedetail.html'
    
    form_class = FileForm
    formset_class = SafetyDataSheetForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(
            instance=self.context['queryset'],
            initial=self.get_initial()["file"]
            )
        self.context['formset'] = self.formset_class(
            initial=self.get_initial()["safetydatasheet"]
            )
        return render(request, self.template_name, self.context)

    def get_initial(self):
        result = {}
        result["file"]={}
        result["safetydatasheet"] = {}
        if self.get_queryset():
            result["file"]["type"] = "SA"
            if self.get_queryset().content():
                result["safetydatasheet"]["file_id"] = self.get_queryset().id
                result["safetydatasheet"]["actualization"] = self.get_queryset().content().actualization
                result["safetydatasheet"]["warning"] = self.get_queryset().content().warning
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
            safetydatasheet = formset.save(commit=False)
            safetydatasheet.file_id = obj
            obj.save()
            safetydatasheet.save()
            self.context['form'] = form
            self.context['formset'] = formset
        else:
            self.context['form'] = form
            self.context['formset'] = formset
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
            return redirect('documentationmanagement:safetydatasheet_detail',safetydatasheet=obj.slug)
        messages.success(request,'Die eingegeben Daten wurden validiert!')
        return redirect('documentationmanagement:safetydatasheet_detail',safetydatasheet=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('safetydatasheet'):
            queryset=SafetyDataSheetProxy.objects.get(slug=self.kwargs.get('safetydatasheet'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class SafetyDataSheetDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'documentationmanagement.delete_safetydatasheet'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('safetydatasheet'):
            File.objects.get(slug = self.kwargs.get('safetydatasheet')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('documentationmanagement:safetydatasheet_list')
#--------------------------------------------------------------------------------