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
from documentationmanagement.document.models import Document
from documentationmanagement.file.models import File, DocumentProxy
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from django.forms import inlineformset_factory
from documentationmanagement.document.forms import DocumentForm
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
class DocumentView(FileView):
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'documentationmanagement'
        self.context['model'] = 'document'
#--------------------------------------------------------------------------------
class DocumentListView(DocumentView):

    permission_required = 'documentationmanagement.list_document'

    template_name = 'document/templates/document_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = DocumentProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,url_detail,url_update,url_delete,reference_number,name,version,type,url_file,url_file_qrcode"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:document_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class DocumentTableView(DocumentView):

    permission_required = 'documentationmanagement.table_document'

    template_name = 'document/templates/document_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = DocumentProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,reference_number,name,version,type,create,update"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:document_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class DocumentCreateUpdateDetailView(DocumentView):

    permission_required = ('documentationmanagement.add_document','documentationmanagement.change_document')

    template_name = 'document/templates/document_createupdatedetail.html'
    
    form_class = FileForm
    formset_class = DocumentForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(
            instance=self.context['queryset'],
            initial=self.get_initial()["file"]
            )
        self.context['formset'] = self.formset_class(
            initial=self.get_initial()["document"]
            )
        return render(request, self.template_name, self.context)

    def get_initial(self):
        result = {}
        result["file"]={}
        result["document"] = {}
        if self.get_queryset():
            result["file"]["type"] = "DO"
            if self.get_queryset().content():
                result["document"]["file_id"] = self.get_queryset().id
                result["document"]["content"] = self.get_queryset().content().content
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
            documentation = formset.save(commit=False)
            documentation.file_id = obj
            obj.save()
            documentation.save()
            self.context['form'] = form
            self.context['formset'] = formset
        else:
            self.context['form'] = form
            self.context['formset'] = formset
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        messages.success(request,'Die eingegeben Daten wurden validiert!')
        return redirect('documentationmanagement:document_detail',document=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('document'):
            queryset=DocumentProxy.objects.get(slug=self.kwargs.get('document'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class DocumentDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'documentationmanagement.delete_document'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('document'):
            File.objects.get(slug = self.kwargs.get('document')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('documentationmanagement:document_list')
#--------------------------------------------------------------------------------