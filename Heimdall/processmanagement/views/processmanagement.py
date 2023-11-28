#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.shortcuts import render

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from commission.models.commission import Commission
from processmanagement.models.statusreport import StatusReport
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class ProcessManagementView(MainView):
    template_name = 'processmanagement.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        statusreports = StatusReport.objects.all()
        commission = Commission.objects.filter(done=False).order_by('-createTime')
        self.context['data'] = {}
        for sr in statusreports:
            self.context['data'][sr.name] = []
        for o in commission:
            if o.getLastStatusReport():
                self.context['data'][o.getLastStatusReport().statusreport.name].append(o)
        self.context['age'] = {}
        for i in range(1,31,1):
            self.context['age'][i] = []
        self.context['age']['+30'] = []
        for o in commission:
            if o.getAge():
                if o.getAge() > 30:
                    self.context['age']['+30'].append(o)
                else:
                    self.context['age'][o.getAge()].append(o)
        
#--------------------------------------------------------------------------------