#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, reverse
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from processmanagement.models.statusreport import StatusReport
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from processmanagement.forms.statusreport import StatusReportForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class StatusReportView(MainView):
    template_name = 'statusreport/statusreport.html'

    def get_queryset(self, *args, **kwargs):
        queryset = StatusReport.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'statusreport'
#--------------------------------------------------------------------------------
class StatusReportListView(StatusReportView):
    template_name = 'statusreport/statusreport_list.html'
#--------------------------------------------------------------------------------
class StatusReportTableView(StatusReportView):
    template_name = 'statusreport/statusreport_table.html'

    def get_queryset(self, *args, **kwargs):
        queryset = StatusReport.objects.all().order_by('name')
        return queryset
#--------------------------------------------------------------------------------
class StatusReportCreateUpdateView(StatusReportView):
    template_name = 'statusreport/statusreport_createupdate.html'
    form_class = StatusReportForm

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
            if not obj.createUser:
                obj.createUser = user
            obj.updateUser = user
            obj.updateTime = timezone.now()
            obj.save()
            self.context['form'] = form
            messages.success(request,'Die!')
        else:
            self.context['form'] = form
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        return redirect('processmanagement:statusreport_update', id=obj.id)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('id'):
            queryset = StatusReport.objects.get(id=self.kwargs.get('id'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class StatusReportDetailView(StatusReportView):
    template_name = 'statusreport/statusreport_table.html'

    def get_queryset(self, *args, **kwargs):
        queryset = StatusReport.objects.get(id=self.kwargs.get('id'))
        return queryset
#--------------------------------------------------------------------------------
class StatusReportDeleteView(MainView):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get('id'):
            StatusReport.objects.get(id = self.kwargs.get('id')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('processmanagement:statusreport_table')
#--------------------------------------------------------------------------------