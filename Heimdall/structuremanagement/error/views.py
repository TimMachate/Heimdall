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
from structuremanagement.error.models import Error, ErrorData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from structuremanagement.error.forms import ErrorForm, ErrorDataForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class ErrorView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.view_error'

    template_name = 'error/templates/error_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Error.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'structuremanagement'
        self.context['model'] = 'error'
        # API Data
        fields = "id,name,reference_number,url,error_last"
        self.context["api_data_url"] = reverse("structuremanagementAPI:error_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class ErrorListView(ErrorView):

    permission_required = 'structuremanagement.list_error'

    template_name = 'error/templates/error_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # API Data
        fields = "id,name,reference_number,url,error_last,errors_count"
        self.context["api_data_url"] = reverse("structuremanagementAPI:error_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class ErrorTableView(ErrorView):

    permission_required = 'structuremanagement.table_error'

    template_name = 'error/templates/error_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # API Data
        fields = "id,name,reference_number,error_last,errors_count,create,update"
        self.context["api_data_url"] = reverse("structuremanagementAPI:error_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class ErrorCreateUpdateDetailView(ErrorView):

    permission_required = 'structuremanagement.add_error'

    template_name = 'error/templates/error_createupdatedetail.html'
    
    form_class = ErrorForm

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

        return redirect('structuremanagement:error_update', error=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('error'):
            queryset = get_object_or_404(Error,slug = self.kwargs.get('error'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class ErrorDeleteView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.delete_error'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('error'):
            Error.objects.get(slug = self.kwargs.get('error')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class ErrorDataView(PermissionRequiredMixin,MainView):

    permission_required = 'structuremanagement.view_errordata'

    template_name = 'error/templates/errordata_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = ErrorData.objects.all()
        if self.kwargs.get("device"):
            queryset = queryset.filter(slug=self.kwargs.get("device"))
        if self.kwargs.get("error"):
            queryset = queryset.filter(slug=self.kwargs.get("error"))
        return queryset.order_by('-create_datetime')

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'structuremanagement'
        self.context['model'] = 'errordata'
        if self.kwargs.get('device'):
            self.context['device'] = Device.objects.get(slug = self.kwargs.get('device'))
        else:
            self.context['device'] = None
        if self.kwargs.get('error'):
            self.context['error'] = Error.objects.get(slug = self.kwargs.get('error'))
        else:
            self.context['error'] = None
        self.context["api_data_url"] = reverse("structuremanagementAPI:errordata_list")
#--------------------------------------------------------------------------------
class ErrorDataListView(ErrorDataView):

    permission_required = 'structuremanagement.list_errordata'

    template_name = 'error/templates/errordata_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        device = self.kwargs.get('device') if self.kwargs.get('device') else ""
        error = self.kwargs.get('error') if self.kwargs.get('error') else ""
        fields = "create,reference_number,device,error,notice,url"
        self.context["api_data_url"] = reverse("structuremanagementAPI:errordata_list")+"?values={}&device_id__slug={}&error_id__slug={}".format(fields,device,error)
#--------------------------------------------------------------------------------
class ErrorDataTableView(ErrorDataView):

    permission_required = 'structuremanagement.table_errordata'

    template_name = 'error/templates/errordata_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        device = self.kwargs.get('device') if self.kwargs.get('device') else ""
        error = self.kwargs.get('error') if self.kwargs.get('error') else ""
        fields = "create,reference_number,device,error,notice,update"
        self.context["api_data_url"] = reverse("structuremanagementAPI:errordata_list")+"?values={}&device_id__slug={}&error_id__slug={}".format(fields,device,error)
#--------------------------------------------------------------------------------
class ErrorDataCreateUpdateDetailView(ErrorDataView):

    permission_required = ('structuremanagement.add_errordata','structuremanagement.change_errordata')

    template_name = 'error/templates/errordata_createupdatedetail.html'
    form_class = ErrorDataForm

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
        if self.context['error']:
            DICT['error_id'] = self.context['error'].id
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
            return redirect('structuremanagement:errordata_update', errordata=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('errordata'):
            queryset = get_object_or_404(ErrorData,slug=self.kwargs.get('errordata'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class ErrorDataDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'structuremanagement.delete_errordata'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('errordata'):
            ErrorData.objects.get(id = self.kwargs.get('errordata')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------