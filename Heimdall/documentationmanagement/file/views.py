#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.file.models import File
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
#from django.forms import inlineformset_factory
from documentationmanagement.file.forms import FileForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class FileView(PermissionRequiredMixin,MainView):

    permission_required = 'documentationmanagement.view_file'

    template_name = 'file/templates/file_overview.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance=self.context["api_data"])
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj = form.save()
            messages.success(request,'Die eingegebenen Daten konnten validiert werden!')
        else:
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        self.context['form'] = form
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    def get_queryset(self, *args, **kwargs):
        queryset = {}
        queryset["direction"]={}
        queryset["direction"]["count"]=File.objects.filter(type=File.Types("DI")).count()
        queryset["direction"]["name"]="Betriebsanweisung"
        queryset["direction"]["url_detail"]=reverse("documentationmanagement:direction_list")
        queryset["documents"]={}
        queryset["documents"]["count"]=File.objects.filter(type=File.Types("DO")).count()
        queryset["documents"]["name"]="Dokumente"
        queryset["documents"]["url_detail"]=reverse("documentationmanagement:document_list")
        queryset["formular"]={}
        queryset["formular"]["count"]=File.objects.filter(type=File.Types("FO")).count()
        queryset["formular"]["name"]="Formular"
        queryset["formular"]["url_detail"]=reverse("documentationmanagement:formular_list")
        queryset["general"]={}
        queryset["general"]["count"]=File.objects.filter(type=File.Types("GE")).count()
        queryset["general"]["name"]="Sonstiges"
        queryset["general"]["url_detail"]=reverse("documentationmanagement:general_list")
        queryset["manual"]={}
        queryset["manual"]["count"]=File.objects.filter(type=File.Types("MA")).count()
        queryset["manual"]["name"]="Handbuch"
        queryset["manual"]["url_detail"]=reverse("documentationmanagement:manual_list")
        queryset["picture"]={}
        queryset["picture"]["count"]=File.objects.filter(type=File.Types("PI")).count()
        queryset["picture"]["name"]="Bild"
        queryset["picture"]["url_detail"]=reverse("documentationmanagement:picture_overview")
        queryset["processinstruction"]={}
        queryset["processinstruction"]["count"]=File.objects.filter(type=File.Types("PR")).count()
        queryset["processinstruction"]["name"]="Verfahrensanweisung"
        queryset["processinstruction"]["url_detail"]=reverse("documentationmanagement:processinstruction_list")
        queryset["protocol"]={}
        queryset["protocol"]["count"]=File.objects.filter(type=File.Types("PO")).count()
        queryset["protocol"]["name"]="Protokoll"
        queryset["protocol"]["url_detail"]=reverse("documentationmanagement:protocol_list")
        queryset["safetydatasheet"]={}
        queryset["safetydatasheet"]["count"]=File.objects.filter(type=File.Types("SA")).count()
        queryset["safetydatasheet"]["name"]="Sicherheits Datenblatt"
        queryset["safetydatasheet"]["url_detail"]=reverse("documentationmanagement:safetydatasheet_list")
        queryset["technicaldatasheet"]={}
        queryset["technicaldatasheet"]["count"]=File.objects.filter(type=File.Types("TE")).count()
        queryset["technicaldatasheet"]["name"]="Technisches Datenblatt"
        queryset["technicaldatasheet"]["url_detail"]=reverse("documentationmanagement:technicaldatasheet_list")
        queryset["workingdescription"]={}
        queryset["workingdescription"]["count"]=File.objects.filter(type=File.Types("WD")).count()
        queryset["workingdescription"]["name"]="Arbeitsplatzbeschreibung"
        queryset["workingdescription"]["url_detail"]=reverse("documentationmanagement:workingdescription_list")
        queryset["workinginstruction"]={}
        queryset["workinginstruction"]["count"]=File.objects.filter(type=File.Types("WO")).count()
        queryset["workinginstruction"]["name"]="Arbeitsanweisung"
        queryset["workinginstruction"]["url_detail"]=reverse("documentationmanagement:workinginstruction_list")
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'documentationmanagement'
        self.context['model'] = 'file'
        # Data Url
        fields = "id,name,reference_number,url_detail"
        #self.context["api_data_url"] = reverse("documentationmanagementAPI:file_overview")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class FileListView(FileView):

    permission_required = 'documentationmanagement.list_file'

    template_name = 'file/templates/file_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = File.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,url_detail,url_update,url_delete,reference_number,name,version,type,url_file,url_file_qrcode"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:file_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class FileTableView(FileView):

    permission_required = 'documentationmanagement.table_file'

    template_name = 'file/templates/file_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = File.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,reference_number,name,version,type,create,update"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:file_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class FileCreateUpdateDetailView(FileView):

    permission_required = ('documentationmanagement.add_file','documentationmanagement.change_file')

    template_name = 'file/templates/file_createupdatedetail.html'
    
    form_class = FileForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'])
        return render(request, self.template_name, self.context)

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance=self.context['queryset'])
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj = form.save(commit=False)
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            obj.save()
            self.context['form'] = form
            messages.success(request,'Die eingegeben Daten wurden validiert!')
            return redirect('documentationmanagement:file_detail',file=obj.slug)
        else:
            self.context['form'] = form
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
            return redirect('documentationmanagement:file_detail',file=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('file'):
            queryset = File.objects.get(slug=self.kwargs.get('file'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class FileDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'documentationmanagement.delete_file'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('slug'):
            File.objects.get(slug = self.kwargs.get('slug')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('documentationmanagement:file_list')
#--------------------------------------------------------------------------------