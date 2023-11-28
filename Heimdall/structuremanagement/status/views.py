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
from structuremanagement.device.models import Device
from structuremanagement.status.models import Status,StatusData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from structuremanagement.status.forms import StatusForm,StatusDataForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class StatusView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.view_status'

    template_name = 'status/templates/status_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Status.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'structuremanagement'
        self.context['model'] = 'status'
        # API Data
        fields = "id,create,reference_number,name,stati_last,url"
        self.context["api_data_url"] = reverse("structuremanagementAPI:status_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class StatusListView(StatusView):

    permission_required = 'structuremanagement.list_status'

    template_name = 'status/templates/status_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # API Data
        fields = "reference_number,name,background_color,description,url"
        self.context["api_data_url"] = reverse("structuremanagementAPI:status_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class StatusTableView(StatusView):

    permission_required = 'structuremanagement.table_status'

    template_name = 'status/templates/status_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # API Data
        fields = "reference_number,name,background_color,create,update"
        self.context["api_data_url"] = reverse("structuremanagementAPI:status_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class StatusCreateUpdateDetailView(StatusView):

    permission_required = 'structuremanagement.add_status'

    template_name = 'status/templates/status_createupdatedetail.html'
    
    form_class = StatusForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(
            instance=self.context['queryset']
            )
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

        return redirect('structuremanagement:status_update', status=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('status'):
            queryset = get_object_or_404(Status,slug=self.kwargs.get('status'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class StatusDeleteView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.delete_status'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('status'):
            Status.objects.get(slug = self.kwargs.get('status')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class StatusDataView(PermissionRequiredMixin,MainView):

    permission_required = 'structuremanagement.view_statusdata'

    template_name = 'status/templates/statusdata_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = StatusData.objects.all()
        if self.kwargs.get("device"):
            queryset = queryset.filter(slug=self.kwargs.get("device"))
        if self.kwargs.get("status"):
            queryset = queryset.filter(slug=self.kwargs.get("status"))
        return queryset.order_by('-create_datetime')
    
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'structuremanagement'
        self.context['model'] = 'statusdata'
        # API Data
        fields = "create,reference_number,device,status,url"
        self.context["api_data_url"] = reverse("structuremanagementAPI:statusdata_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class StatusDataListView(StatusDataView):

    permission_required = 'structuremanagement.list_statusdata'

    template_name = 'status/templates/statusdata_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # API Data
        device = self.kwargs.get('device') if self.kwargs.get('device') else ""
        status = self.kwargs.get('status') if self.kwargs.get('status') else ""
        fields = "create,reference_number,device,status,url"
        self.context["api_data_url"] = reverse("structuremanagementAPI:statusdata_list")+"?values={}&device_id__slug={}&status_id__slug={}".format(fields,device,status)
#--------------------------------------------------------------------------------
class StatusDataTableView(StatusDataView):

    permission_required = 'structuremanagement.table_statusdata'

    template_name = 'status/templates/statusdata_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # API Data
        device = self.kwargs.get('device') if self.kwargs.get('device') else ""
        status = self.kwargs.get('status') if self.kwargs.get('status') else ""
        fields = "create,reference_number,device,status,update"
        self.context["api_data_url"] = reverse("structuremanagementAPI:statusdata_list")+"?values={}&device_id__slug={}&status_id__slug={}".format(fields,device,status)
#--------------------------------------------------------------------------------
class StatusDataCreateUpdateDetailView(StatusDataView):

    permission_required = ('structuremanagement.add_statusdata','structuremanagement.change_statusdata')

    template_name = 'status/templates/statusdata_createupdatedetail.html'

    form_class = StatusDataForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(
            instance=self.context['queryset'],
            initial = self.get_initial(),
            )
        return render(request, self.template_name, self.context)

    def get_initial(self):
        DICT = {}
        if self.context['status']:
            DICT['status_id'] = self.context['status'].id
        if self.context['device']:
            DICT['device_id'] = self.context['device'].id
        return DICT

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
        if request.GET.get("next"):
            return redirect(request.GET.get("next"))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('statusdata'):
            queryset = get_object_or_404(StatusData,slug=self.kwargs.get('statusdata'))
        else:
            queryset = None
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        if self.kwargs.get('device'):
            self.context['device'] = get_object_or_404(Device,slug = self.kwargs.get('device'))
        else:
            self.context['device'] = None
        if self.kwargs.get('status'):
            self.context['status'] = get_object_or_404(Status,slug = self.kwargs.get('status'))
        else:
            self.context['status'] = None
#--------------------------------------------------------------------------------
class StatusDataDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'structuremanagement.delete_statusdata'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('statusdata'):
            StatusData.objects.get(slug = self.kwargs.get('statusdata')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------