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
from documentationmanagement.formular.models import Formular
from documentationmanagement.file.models import File, FormularProxy
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from django.forms import inlineformset_factory
from documentationmanagement.formular.forms import FormularForm
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
class FormularView(FileView):
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'documentationmanagement'
        self.context['model'] = 'formular'
#--------------------------------------------------------------------------------
class FormularListView(FormularView):

    permission_required = 'documentationmanagement.list_formular'

    template_name = 'formular/templates/formular_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = FormularProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,url_detail,url_update,url_delete,reference_number,name,version,type,url_file,url_file_qrcode"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:formular_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class FormularTableView(FormularView):

    permission_required = 'documentationmanagement.table_formular'

    template_name = 'formular/templates/formular_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = FormularProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,reference_number,name,version,type,create,update"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:formular_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class FormularCreateUpdateDetailView(FormularView):

    permission_required = ('documentationmanagement.add_formular','documentationmanagement.change_formular')

    template_name = 'formular/templates/formular_createupdatedetail.html'
    
    form_class = FileForm
    formset_class = FormularForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(
            instance=self.context['queryset'],
            initial=self.get_initial()["file"]
            )
        self.context['formset'] = self.formset_class(
            initial=self.get_initial()["formular"]
            )
        return render(request, self.template_name, self.context)

    def get_initial(self):
        result = {}
        result["file"]={}
        result["formular"] = {}
        if self.get_queryset():
            result["file"]["type"] = "FO"
            if self.get_queryset().content():
                result["formular"]["file_id"] = self.get_queryset().id
                result["formular"]["content"] = self.get_queryset().content().content
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
            formular = formset.save(commit=False)
            formular.file_id = obj
            obj.save()
            formular.save()
            self.context['form'] = form
            self.context['formset'] = formset
        else:
            self.context['form'] = form
            self.context['formset'] = formset
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
            return redirect('documentationmanagement:formular_detail',formular=obj.slug)
        messages.success(request,'Die eingegeben Daten wurden validiert!')
        return redirect('documentationmanagement:formular_detail',formular=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('formular'):
            queryset=FormularProxy.objects.get(slug=self.kwargs.get('formular'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class FormularDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'documentationmanagement.delete_formular'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('formular'):
            File.objects.get(slug = self.kwargs.get('formular')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('documentationmanagement:formular_list')
#--------------------------------------------------------------------------------