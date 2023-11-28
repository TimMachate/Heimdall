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
from structuremanagement.maintenance.models import Maintenance
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from personalmanagement.departmentsettings.forms import DepartmentSettingsListForm, DepartmentSettingsTableForm
from structuremanagement.maintenance.forms import MaintenanceForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class MaintenanceView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.view_maintenance'

    template_name = 'maintenance/templates/maintenance_overview.html'

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
        queryset = Maintenance.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'structuremanagement'
        self.context['model'] = 'maintenance'
        # API data
        fields = "id,name,reference_number,url,device,maintenance_last,maintenance_next,status"
        self.context["api_data_url"] = reverse("structuremanagementAPI:maintenance_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class MaintenanceListView(MaintenanceView):

    permission_required = 'structuremanagement.list_maintenance'

    template_name = 'maintenance/templates/maintenance_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # API data
        fields = "id,name,reference_number,url,device,status,maintenance_last,maintenance_next"
        self.context["api_data_url"] = reverse("structuremanagementAPI:maintenance_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class MaintenanceTableView(MaintenanceView):

    permission_required = 'structuremanagement.table_maintenance'

    template_name = 'maintenance/templates/maintenance_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,name,reference_number,device,maintenance_count,warning,repetition,create,update"
        self.context["api_data_url"] = reverse("structuremanagementAPI:maintenance_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class MaintenanceCreateUpdateDetailView(MaintenanceView):

    permission_required = 'structuremanagement.add_maintenance'

    template_name = 'maintenance/templates/maintenance_createupdatedetail.html'
    
    form_class = MaintenanceForm

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
            messages.success(request,'Die eingegebenen Daten wurden validiert!')
        else:
            self.context['form'] = form
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')

        return redirect('structuremanagement:maintenance_update', maintenance=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('maintenance'):
            queryset = get_object_or_404(Maintenance,slug = self.kwargs.get('maintenance'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class MaintenanceDeleteView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.delete_maintenance'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('maintenance'):
            Maintenance.objects.get(slug = self.kwargs.get('maintenance')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------