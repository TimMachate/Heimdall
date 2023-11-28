#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, reverse
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from personalmanagement.departmentsettings.models import DepartmentSettings
from structuremanagement.device.models import Device
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from personalmanagement.departmentsettings.forms import DepartmentSettingsListForm, DepartmentSettingsTableForm
from structuremanagement.device.forms import DeviceForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
from structuremanagement.error.views import ErrorDataView, ErrorDataTableView, ErrorDataCreateUpdateDetailView
from structuremanagement.process.views import ProcessDataView, ProcessDataTableView, ProcessDataCreateUpdateDetailView
from structuremanagement.status.views import StatusDataView, StatusDataTableView, StatusDataCreateUpdateDetailView
#--------------------------------------------------------------------------------
class DeviceView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.view_device'

    template_name = 'device/templates/device_overview.html'

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
        queryset = Device.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'structuremanagement'
        self.context['model'] = 'device'
        self.context['menubar'] = {}
        self.context['menubar']['left'] = {}
        self.context['menubar']['left']['overview'] = {
            'url':reverse(self.context['app']+':'+self.context['model']+'_overview'),
            'icon':'icons/view.png',
            'alt':'Übersicht',
            'permission':self.context['app']+'.view_'+self.context['model'],
            }
        self.context['menubar']['left']['list'] = {
            'url':reverse(self.context['app']+':'+self.context['model']+'_list'),
            'icon':'icons/list.png',
            'alt':'Liste',
            'permission':self.context['app']+'.list_'+self.context['model'],
            }
        self.context['menubar']['left']['table'] = {
            'url':reverse(self.context['app']+':'+self.context['model']+'_table'),
            'icon':'icons/table.png',
            'alt':'Tabelle',
            'permission':self.context['app']+'.table_'+self.context['model'],
            }
        self.context['menubar']['left']['create'] = {
            'url':reverse(self.context['app']+':'+self.context['model']+'_create'),
            'icon':'icons/add.png',
            'alt':'Hinzufügen',
            'permission':self.context['app']+'.add_'+self.context['model'],
            }
        if self.kwargs.get(self.context['model']):
            self.context['menubar']['left']['detail'] = {
                'url':reverse(self.context['app']+':'+self.context['model']+'_detail',kwargs={self.context['model']:self.kwargs.get(self.context['model'])}),
                'icon':'icons/detail.png',
                'alt':'Detail',
                'permission':self.context['app']+'.detail_'+self.context['model'],
                }
            self.context['menubar']['left']['update'] = {
                'url':reverse(self.context['app']+':'+self.context['model']+'_update',kwargs={self.context['model']:self.kwargs.get(self.context['model'])}),
                'icon':'icons/bearbeiten.png',
                'alt':'Update',
                'permission':self.context['app']+'.change_'+self.context['model'],
                }
            self.context['menubar']['left']['delete'] = {
                'url':reverse(self.context['app']+':'+self.context['model']+'_delete',kwargs={self.context['model']:self.kwargs.get(self.context['model'])}),
                'icon':'icons/delete.png',
                'alt':'Löschen',
                'permission':self.context['app']+'.delete_'+self.context['model'],
                }
        self.context['menubar']['right'] = None
        self.context["api_data"] = DepartmentSettings.objects.get(user_id=self.request.user)
        self.context["api_data_url"] = reverse("structuremanagementAPI:device_list")
#--------------------------------------------------------------------------------
class DeviceListView(DeviceView):

    permission_required = 'structuremanagement.list_device'

    template_name = 'device/templates/device_list.html'

    form_class = DepartmentSettingsListForm

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        self.context["form_data"] = self.form_class(
            instance = self.context["api_data"]
            )
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,name,url"
        self.context["api_data_url"] = reverse("structuremanagementAPI:device_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class DeviceTableView(DeviceView):

    permission_required = 'structuremanagement.table_device'

    template_name = 'device/templates/device_table.html'

    form_class = DepartmentSettingsTableForm

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        self.context["form_data"] = self.form_class(
            instance = self.context["api_data"]
            )
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,name,documents_count,manuals_count,fabricator,maintenance,working_instructions_count,fabricator_label,power,serial_number,voltage,year_of_manufacture"
        self.context["api_data_url"] = reverse("structuremanagementAPI:device_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class DeviceCreateUpdateDetailView(DeviceView):

    permission_required = 'structuremanagement.add_device'

    template_name = 'device/templates/device_createupdatedetail.html'
    
    form_class = DeviceForm

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

        return redirect('structuremanagement:device_detail', device=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('device'):
            queryset = Device.objects.get(slug = self.kwargs.get('device'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class DeviceDeleteView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.delete_device'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('device'):
            Device.objects.get(slug = self.kwargs.get('device')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------