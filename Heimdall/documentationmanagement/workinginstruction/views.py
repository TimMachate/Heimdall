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
from documentationmanagement.workinginstruction.models import WorkingInstruction
from documentationmanagement.file.models import File, WorkingInstructionProxy
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from django.forms import inlineformset_factory
from documentationmanagement.workinginstruction.forms import WorkingInstructionForm
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
class WorkingInstructionView(FileView):
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'documentationmanagement'
        self.context['model'] = 'workinginstruction'
#--------------------------------------------------------------------------------
class WorkingInstructionListView(WorkingInstructionView):

    permission_required = 'documentationmanagement.list_workinginstruction'

    template_name = 'workinginstruction/templates/workinginstruction_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = WorkingInstructionProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,url_detail,url_update,url_delete,reference_number,name,version,type,url_file,url_file_qrcode"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:workinginstruction_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class WorkingInstructionTableView(WorkingInstructionView):

    permission_required = 'documentationmanagement.table_workinginstruction'

    template_name = 'workinginstruction/templates/workinginstruction_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = WorkingInstructionProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,reference_number,name,version,type,create,update"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:workinginstruction_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class WorkingInstructionCreateUpdateDetailView(WorkingInstructionView):

    permission_required = ('documentationmanagement.add_workinginstruction','documentationmanagement.change_workinginstruction')

    template_name = 'workinginstruction/templates/workinginstruction_createupdatedetail.html'
    
    form_class = FileForm
    formset_class = WorkingInstructionForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(
            instance=self.context['queryset'],
            initial=self.get_initial()["file"]
            )
        self.context['formset'] = self.formset_class(
            initial=self.get_initial()["workinginstruction"]
            )
        return render(request, self.template_name, self.context)

    def get_initial(self):
        result = {}
        result["file"]={}
        result["workinginstruction"] = {}
        if self.get_queryset():
            result["file"]["type"] = "WO"
            if self.get_queryset().content():
                result["workinginstruction"]["file_id"] = self.get_queryset().id
                result["workinginstruction"]["content"] = self.get_queryset().content().content
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
            workinginstruction = formset.save(commit=False)
            workinginstruction.file_id = obj
            obj.save()
            workinginstruction.save()
            self.context['form'] = form
            self.context['formset'] = formset
        else:
            self.context['form'] = form
            self.context['formset'] = formset
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
            return redirect('documentationmanagement:workinginstruction_detail',workinginstruction=obj.slug)
        messages.success(request,'Die eingegeben Daten wurden validiert!')
        return redirect('documentationmanagement:workinginstruction_detail',workinginstruction=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('workinginstruction'):
            queryset=WorkingInstructionProxy.objects.get(slug=self.kwargs.get('workinginstruction'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class WorkingInstructionDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'documentationmanagement.delete_workinginstruction'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('workinginstruction'):
            File.objects.get(slug = self.kwargs.get('workinginstruction')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('documentationmanagement:workinginstruction_list')
#--------------------------------------------------------------------------------