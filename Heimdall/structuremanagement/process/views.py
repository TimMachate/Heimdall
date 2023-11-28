#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import formset_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse,get_object_or_404
from django.templatetags.static import static
from django.utils import timezone
from django.views import View

import json
from urllib.request import urlopen
from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from structuremanagement.process.models import Process, ProcessData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from structuremanagement.process.forms import ProcessForm,ProcessDataForm,ProcessDataFormSet
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Views
#--------------------------------------------------------------------------------
from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class ProcessView(PermissionRequiredMixin,MainView):

    permission_required = "structuremanagement.view_process"

    template_name = 'process/templates/process_overview.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

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
        queryset = Process.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'structuremanagement'
        self.context['model'] = 'process'

        # Data Url
        self.context["api_data_url"] = reverse("structuremanagementAPI:process_list")
#--------------------------------------------------------------------------------
class ProcessListView(ProcessView):

    permission_required = 'structuremanagement.list_process'

    template_name = 'process/templates/process_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)
    
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,reference_number,name,duration,count,utilization,processes,picture,technical_data_sheet,url"
        self.context["api_data_url"] = reverse("structuremanagementAPI:process_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class ProcessTableView(ProcessView):

    permission_required = 'structuremanagement.table_process'

    template_name = 'process/templates/process_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,reference_number,name,duration,count,utilization,processes,create,update"
        self.context["api_data_url"] = reverse("structuremanagementAPI:process_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class ProcessCreateUpdateDetailView(ProcessView):

    permission_required = ('structuremanagement.add_process','structuremanagement.change_process')

    template_name = 'process/templates/process_createupdatedetail.html'

    form_class = ProcessForm

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
        return redirect('structuremanagement:process_update',process=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('process'):
            queryset = get_object_or_404(Process,slug=self.kwargs.get('process'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class ProcessDeleteView(ProcessView):

    permission_required = 'structuremanagement.delete_process'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('process'):
            Process.objects.get(slug = self.kwargs.get('process')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class ProcessDataView(PermissionRequiredMixin,MainView):

    permission_required = "structuremanagement.view_processdata"

    template_name = 'process/templates/processdata_overview.html'

    form_class = ProcessDataFormSet

    formset_class = formset_factory(
            form = ProcessDataFormSet,
            extra = 0,
        )
    

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        self.context["form"] = self.form_class(
            initial={
                "device_id": Device.objects.get(slug=self.kwargs.get("device")).id if self.kwargs.get("device") else None,
                "process_id": Process.objects.get(slug=self.kwargs.get("process")).id if self.kwargs.get("process") else None,
            }
        )
        self.context["formset"] = self.formset_class(
            initial = self.get_initial()
        )
        return render(request, self.template_name, self.context)

    def get_initial(self):
        LIST = []
        for query in self.get_queryset():
            DICT = {}
            DICT["begin_datetime"] = query.begin_datetime.strftime("%d.%m.%Y %H:%M:%S") if query.begin_datetime else None
            DICT["count"] = query.count
            DICT["device_id"] = query.device_id
            DICT["end_datetime"] = query.end_datetime.strftime("%d.%m.%Y %H:%M:%S") if query.end_datetime else None
            DICT["notice"] = query.notice
            DICT["process_id"] = query.process_id
            DICT["reference_number"] = query.reference_number
            DICT["slug"] = query.slug
            DICT["url_delete"] = query.url_delete if query.url_delete else None
            DICT["url_detail"] = query.url_detail if query.url_detail else None
            DICT["url_detail_device"] = query.device_id.url_detail if query.device_id else None
            DICT["url_detail_process"] = query.process_id.url_detail if query.process_id else None
            DICT["utilization"] = query.utilization_percentage if query.utilization_percentage else None
            LIST.append(DICT)
        return LIST

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        formset = self.formset_class(request.POST,request.FILES)
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid() and form.cleaned_data['process_id']:
            obj = form.save()
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            obj.save()
            self.context['form'] = form
        if formset.is_valid():
            for f in formset:
                if f.is_valid():
                    pd,created = ProcessData.objects.update_or_create(
                        slug=f.cleaned_data['slug'] if 'slug' in f.cleaned_data else None,
                        defaults = {
                            'device_id' : Device.objects.get(id=f.cleaned_data['device_id'].id) if 'device_id' in f.cleaned_data else None,
                            'process_id' : Process.objects.get(id=f.cleaned_data['process_id'].id) if 'process_id' in f.cleaned_data else None,
                            'count' : f.cleaned_data['count'] if 'count' in f.cleaned_data else None,
                            'update_user_id' : user,
                            'update_datetime' : timezone.now(),
                            'notice' : f.cleaned_data['notice'] if 'notice' in f.cleaned_data else None,
                        }
                        )
                    if pd.begin_datetime != f.cleaned_data['begin_datetime']:
                        pd.begin_user_id = user
                        pd.begin_datetime = f.cleaned_data['begin_datetime']
                    if pd.end_datetime != f.cleaned_data['end_datetime']:
                        pd.end_user_id = user
                        pd.end_datetime = f.cleaned_data['end_datetime']
                    pd.save()
            messages.success(request,'Die eingegebenen Daten konnten validiert werden!')
        else:
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        self.context['form'] = form
        self.context['formset'] = formset
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('processdata'):
            queryset = ProcessData.objects.get(slug=self.kwargs.get('processdata'))
        else:
            queryset = ProcessData.objects.filter(end_datetime=None)
            if self.kwargs.get('process'):
                queryset = queryset.filter(process_id__slug=self.kwargs.get('process'))
            if self.kwargs.get('device'):
                queryset = queryset.filter(device_id__slug=self.kwargs.get('device'))
            queryset = queryset.order_by('begin_datetime')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'structuremanagement'
        self.context['model'] = 'processdata'
        # Data Url
        self.context["api_data"] = None #DepartmentSettings.objects.get(user_id=self.request.user)
        self.context["api_data_url"] = reverse("structuremanagementAPI:processdata_list")
#--------------------------------------------------------------------------------
class ProcessDataListView(ProcessDataView):

    permission_required = 'structuremanagement.list_processdata'

    template_name = 'process/templates/processdata_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = ProcessData.objects.all()
        if self.kwargs.get('process'):
            queryset = queryset.filter(process_id__slug=self.kwargs.get('process'))
        if self.kwargs.get('device'):
            queryset = queryset.filter(device_id__slug=self.kwargs.get('device'))
        return queryset.order_by('begin_datetime')
    
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        device = self.kwargs.get('device') if self.kwargs.get('device') else ""
        process = self.kwargs.get('process') if self.kwargs.get('process') else ""
        fields = "begin,duration_formated,end,reference_number,process,device,count,utilization,url"
        self.context["api_data_url"] = reverse("structuremanagementAPI:processdata_list")+"?values={}&device_id__slug={}&process_id__slug={}".format(fields,device,process)
#--------------------------------------------------------------------------------
class ProcessDataTableView(ProcessDataView):

    permission_required = 'structuremanagement.table_processdata'

    template_name = 'process/templates/processdata_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = ProcessData.objects.all()
        if self.kwargs.get('process'):
            queryset = queryset.filter(process_id__slug=self.kwargs.get('process'))
        if self.kwargs.get('device'):
            queryset = queryset.filter(device_id__slug=self.kwargs.get('device'))
        return queryset.order_by('begin_datetime')
    
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        device = self.kwargs.get('device') if self.kwargs.get('device') else ""
        process = self.kwargs.get('process') if self.kwargs.get('process') else ""
        fields = "begin,duration_formated,end,reference_number,process,device,count,utilization,create"
        self.context["api_data_url"] = reverse("structuremanagementAPI:processdata_list")+"?values={}&device_id__slug={}&process_id__slug={}".format(fields,device,process)
#--------------------------------------------------------------------------------
class ProcessDataCreateUpdateDetailView(ProcessDataView):

    permission_required = ('structuremanagement.add_processdata','structuremanagement.change_processdata')

    template_name = 'process/templates/processdata_createupdatedetail.html'

    form_class = ProcessDataForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(
            instance=self.context['queryset'],
            initial = self.get_initial(request),
            )
        return render(request, self.template_name, self.context)
    
    def get_initial(self,request):
        DICT = {}
        if self.context['process']:
            DICT['process_id'] = self.context['process'].id
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
        if self.kwargs.get('processdata'):
            queryset = get_object_or_404(ProcessData,slug=self.kwargs.get('processdata'))
        else:
            queryset = None
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        if self.kwargs.get('device'):
            self.context['device'] = Device.objects.get(slug = self.kwargs.get('device'))
        else:
            self.context['device'] = None
        if self.kwargs.get('status'):
            self.context['process'] = Process.objects.get(slug = self.kwargs.get('process'))
        else:
            self.context['process'] = None
#--------------------------------------------------------------------------------
class ProcessDataCreateView(ProcessDataCreateUpdateDetailView):

    permission_required = 'structuremanagement.add_processdata'
#--------------------------------------------------------------------------------
class ProcessDataDetailView(ProcessDataCreateUpdateDetailView):

    permission_required = 'structuremanagement.detail_processdata'
#--------------------------------------------------------------------------------        
class ProcessDataUpdateView(ProcessDataCreateUpdateDetailView):

    permission_required = 'structuremanagement.change_processdata'
#--------------------------------------------------------------------------------       
class ProcessDataUpdateEndTimeView(ProcessDataView):

    permission_required = 'structuremanagement.change_processdata'

    def get(self,request, *args, **kwargs):
        obj = self.get_queryset()
        user = get_user_model().objects.get(id=request.user.id)
        if obj:
            obj.end_datetime = timezone.now()
            obj.end_user_id = user
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.save()
            messages.success(request,'Die Eingegebenen Daten wurden validiert!')
        else:
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------        
class ProcessDataUpdateBeginTimeView(ProcessDataView):

    permission_required = 'structuremanagement.change_processdata'

    def get(self,request, *args, **kwargs):
        obj = self.get_queryset()
        user = get_user_model().objects.get(id=request.user.id)
        if obj:
            obj.begin_datetime = timezone.now()
            obj.begin_user_id = user
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.save()
            messages.success(request,'Die Eingegebenen Daten wurden validiert!')
        else:
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class ProcessDataUpdateCountView(ProcessDataView):

    permission_required = 'structuremanagement.change_processdata'

    def get(self,request, *args, **kwargs):
        obj = self.get_queryset()
        user = get_user_model().objects.get(id=request.user.id)
        if obj:
            obj.count = obj.device_id.count
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.save()
            messages.success(request,'Die Eingegebenen Daten wurden validiert!')
        else:
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class ProcessDataDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'structuremanagement.delete_processdata'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('processdata'):
            ProcessData.objects.get(slug = self.kwargs.get('processdata')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))