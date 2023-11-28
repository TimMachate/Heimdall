#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
import json

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import formset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.file.models import File, ProtocolProxy
from documentationmanagement.protocol.models import Protocol, ProtocolData, ProtocolStep, Variable
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from django.forms import inlineformset_factory
from documentationmanagement.protocol.forms import ProtocolForm, ProtocolFormset, ProtocolDataForm, ProtocolStepFormset
from documentationmanagement.file.forms import FileForm
from documentationmanagement.protocol.forms import VariableForm
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
class ProtocolView(FileView):
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'documentationmanagement'
        self.context['model'] = 'protocol'
#--------------------------------------------------------------------------------
class ProtocolListView(ProtocolView):

    permission_required = 'documentationmanagement.list_protocol'

    template_name = 'protocol/templates/protocol_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,keywords,reference_number,name,version,url"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:protocol_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class ProtocolTableView(ProtocolView):

    permission_required = 'documentationmanagement.table_protocol'

    template_name = 'protocol/templates/protocol_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,keywords,reference_number,name,version,type,update"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:protocol_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class ProtocolCreateUpdateDetailView(ProtocolView):

    permission_required = ('documentationmanagement.add_protocol','documentationmanagement.change_protocol')

    template_name = 'protocol/templates/protocol_createupdatedetail.html'
    
    form_class = FileForm
    formset_class_protocol = ProtocolFormset
    formset_class_protocolstep = ProtocolStepFormset

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context['queryset'] = self.get_queryset()
        if self.context['queryset']:
            self.context['file'] = ProtocolProxy.objects.get(slug=self.context['queryset'].file_id.slug)
        else:
            self.context['file'] = None
        self.context['form'] = self.form_class(
            instance=self.context['file'],
            initial = {"type":"PO"}
            )
        self.context['formset_protocol'] = self.formset_class_protocol(
            instance=self.context['file']
            )
        self.context['formset_protocolstep'] = self.formset_class_protocolstep(
            instance=self.context['queryset']
            )
        return render(request, self.template_name, self.context)

    def post(self,request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        form = self.form_class(request.POST,request.FILES,instance=self.context['file'])
        if form.is_valid():
            obj = form.save(commit=False)
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            obj.save()
        formset_protocol = self.formset_class_protocol(request.POST,request.FILES,instance=self.context['file'])
        if formset_protocol.is_valid():
            for form in formset_protocol:
                if form.is_valid():
                    protocol=form.save(commit=False)
                    protocol.file_id=obj
                    protocol.save()
        formset_protocolstep = self.formset_class_protocolstep(request.POST,request.FILES,instance=self.context['queryset'])
        if formset_protocolstep.is_valid():
            for form in formset_protocolstep:
                if form.is_valid() and not form.empty_permitted:
                    protocolstep=form.save(commit=False)
                    protocolstep.protocol_id = protocol
                    protocolstep.save()
                    form.save_m2m()
        if protocol:
            return redirect("documentationmanagement:protocol_update",protocol=protocol.slug)
        elif obj:
            return redirect("documentationmanagement:file_update",file=obj.slug)
        else:
            self.context['form'] = self.form_class
            self.context['formset_protocol'] = self.formset_class_protocol
            self.context['formset_protocolstep'] = self.formset_class_protocolstep
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('protocol'):
            queryset = get_object_or_404(Protocol, slug=self.kwargs.get('protocol'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class ProtocolDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'documentationmanagement.delete_protocol'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('protocol'):
            if Protocol.objects.get(slug = self.kwargs.get('protocol')).file_id:
                File.objects.get(slug=Protocol.objects.get(slug = self.kwargs.get('protocol')).file_id.slug).delete()
            else:
                Protocol.objects.get(slug = self.kwargs.get('protocol')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('documentationmanagement:protocol_list')
#--------------------------------------------------------------------------------
class ProtocolDataView(FileView):

    permission_required = 'documentationmanagement.view_protocoldata'

    template_name = 'protocol/templates/protocoldata_overview.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self,*args,**kwargs):
        if self.kwargs.get('protocol'):
            result = ProtocolData.objects.filter(protocol_id__slug=self.kwargs.get('protocol'))
        else:
            result = ProtocolData.objects.all()
        return result
    
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'documentationmanagement'
        self.context['model'] = 'protocoldata'
#--------------------------------------------------------------------------------
class ProtocolDataListView(ProtocolDataView):

    permission_required = 'documentationmanagement.list_protocoldata'

    template_name = 'protocol/templates/protocoldata_list.html'

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,reference_number,protocol_id,protocol,version,url"
        begin = ""
        end = ""
        protocol = self.kwargs.get('protocol') if self.kwargs.get('protocol') else ""
        self.context["api_data_url"] = reverse("documentationmanagementAPI:protocoldata_list")+"?values={}&protocol_id__slug={}&begin={}&end={}".format(fields,protocol,begin,end)
#--------------------------------------------------------------------------------
class ProtocolDataTableView(ProtocolDataView):

    permission_required = 'documentationmanagement.table_protocoldata'

    template_name = 'protocol/templates/protocoldata_table.html'

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,reference_number,protocol,update,create,version"
        begin = ""
        end = ""
        protocol = self.kwargs.get('protocol') if self.kwargs.get('protocol') else ""
        self.context["api_data_url"] = reverse("documentationmanagementAPI:protocoldata_list")+"?values={}&protocol_id__slug={}&begin={}&end={}".format(fields,protocol,begin,end)
#--------------------------------------------------------------------------------
class ProtocolDataCreateUpdateDetailView(ProtocolDataView):

    permission_required = ('documentationmanagement.add_protocoldata','documentationmanagement.change_protocoldata')

    template_name = 'protocol/templates/protocoldata_createupdatedetail.html'
    form_class = ProtocolDataForm

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context['queryset'] = self.get_queryset()
        if self.kwargs.get('protocol'):
            self.context['protocol'] = Protocol.objects.get(slug=self.kwargs.get('protocol'))
            self.context['form'] = self.form_class(
                instance=self.get_queryset(),
                initial={"protocol_id":self.context['protocol']}
            )
        elif self.context['queryset']:
            self.context['protocol'] = Protocol.objects.get(slug=self.kwargs.get('protocol')) if self.kwargs.get('protocol') else self.context['queryset'].protocol_id
            self.context['form'] = self.form_class(
                instance=self.get_queryset()
            )
        else:
            self.context['protocol'] = None
            self.context['form'] = self.form_class()
        return render(request, self.template_name, self.context)

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance=self.get_queryset())
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj = form.save(commit=False)
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            if not request.FILES.get('file'):
                result = {}
                for step in obj.protocol_id.steps():
                    for variable in step.variables.all():
                        input_type=slugify(variable.InputTypes(variable.input_type).name)
                        result[str(step.id)+'-'+str(variable.id)]=request.POST.get(input_type+'-'+str(step.id)+'-'+str(variable.id))
                obj.json = json.dumps(result)
            obj.save()
            messages.success(request,'Die eingegeben Daten wurden validiert!')
            return redirect('documentationmanagement:protocoldata_update', protocoldata=obj.slug)
        else:
            self.context['form'] = form
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('protocoldata'):
            queryset = get_object_or_404(ProtocolData, slug=self.kwargs.get('protocoldata'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class ProtocolDataDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'documentationmanagement.delete_protocoldata'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('protocoldata'):
            ProtocolData.objects.get(slug = self.kwargs.get('protocoldata')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class VariableView(PermissionRequiredMixin,MainView):

    permission_required = 'documentationmanagement.view_variable'

    template_name = 'protocol/templates/variable_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Variable.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'documentationmanagement'
        self.context['model'] = 'variable'
#--------------------------------------------------------------------------------
class VariableListView(VariableView):

    permission_required = 'documentationmanagement.table_variable'

    template_name = 'protocol/templates/variable_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = Variable.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "reference_number,name,symbol,unit,url_update,url_delete,url_detail"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:variable_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class VariableTableView(VariableView):

    permission_required = 'documentationmanagement.table_variable'

    template_name = 'protocol/templates/variable_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = Variable.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "reference_number,name,symbol,unit,input_type,update"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:variable_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class VariableCreateUpdateDetailView(VariableView):

    permission_required = ('documentationmanagement.add_variable','documentationmanagement.change_variable')

    template_name = 'protocol/templates/variable_createupdatedetail.html'
    form_class = VariableForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'])
        return render(request, self.template_name, self.context)

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance=self.context['queryset'])
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj = form.save()
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            obj.save()
            self.context['form'] = form
            messages.success(request,'Die eingegeben Daten wurden validiert!')
        else:
            self.context['form'] = form
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        return redirect('documentationmanagement:variable_detail', variable=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('variable'):
            queryset = get_object_or_404(Variable, slug=self.kwargs.get('variable'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class VariableDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'documentationmanagement.delete_variable'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('variable'):
            Variable.objects.get(slug = self.kwargs.get('variable')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------