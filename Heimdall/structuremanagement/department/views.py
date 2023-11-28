#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from personalmanagement.departmentsettings.models import DepartmentSettings
from structuremanagement.department.models import Department
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from personalmanagement.departmentsettings.forms import DepartmentSettingsListForm, DepartmentSettingsTableForm
from structuremanagement.department.forms import DepartmentForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class DepartmentView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.view_department'

    template_name = 'department/templates/department_overview.html'

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
        queryset = Department.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'structuremanagement'
        self.context['model'] = 'department'
        # Data Url
        fields = "id,name,reference_number,responsible,substitute,url"
        self.context["api_data_url"] = reverse("structuremanagementAPI:department_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class DepartmentListView(DepartmentView):

    permission_required = 'structuremanagement.list_department'

    template_name = 'department/templates/department_list.html'

    form_class = DepartmentSettingsListForm

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        self.context["form_data"] = self.form_class(
            #instance = self.context["api_data"]
            )
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "reference_number,name,color,process_instruction,picture,url"
        self.context["api_data_url"] = reverse("structuremanagementAPI:department_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class DepartmentTableView(DepartmentView):

    permission_required = 'structuremanagement.table_department'

    template_name = 'department/templates/department_table.html'

    form_class = DepartmentSettingsTableForm

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        self.context["form_data"] = self.form_class(
            #instance = self.context["api_data"]
            )
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "reference_number,name,responsible,substitute,section_count,position_count,employee_count"
        self.context["api_data_url"] = reverse("structuremanagementAPI:department_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class DepartmentCreateUpdateDetailView(DepartmentView):

    permission_required = 'structuremanagement.add_department'

    template_name = 'department/templates/department_createupdatedetail.html'
    
    form_class = DepartmentForm

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
            messages.success(request,'Die!')
        else:
            self.context['form'] = form
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')

        return redirect('structuremanagement:department_update', department=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('department'):
            queryset = get_object_or_404(Department, slug=self.kwargs.get('department'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class DepartmentDeleteView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.delete_department'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('department'):
            Department.objects.get(slug = self.kwargs.get('department')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------