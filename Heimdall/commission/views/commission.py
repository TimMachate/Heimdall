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
from commission.models.commission import Commission
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from commission.forms.commission import CommissionForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class CommissionView(MainView):
    template_name = 'commission/commission.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Commission.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'commission'
#--------------------------------------------------------------------------------
class CommissionTableView(CommissionView):
    template_name = 'commission/commission_table.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Commission.objects.all().order_by('name')
        return queryset
#--------------------------------------------------------------------------------
class CommissionCreateUpdateView(CommissionView):
    template_name = 'commission/commission_createupdate.html'
    form_class = CommissionForm

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
        return redirect('commission:commission_update', id=obj.id)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('id'):
            queryset = Commission.objects.get(id=self.kwargs.get('id'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class CommissionDetailView(CommissionView):
    template_name = 'commission/commission_detail.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Commission.objects.get(id=self.kwargs.get('id'))
        return queryset
#--------------------------------------------------------------------------------
class CommissionDeleteView(MainView):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get('id'):
            Commission.objects.get(id = self.kwargs.get('id')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('commission:commission_table')
#--------------------------------------------------------------------------------
class CommissionSOSChangeView(MainView):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get('id'):
            obj = Commission.objects.get(id=self.kwargs.get('id'))
            obj.sos = False if obj.sos == True else True
            obj.save()
            messages.success(request,'SOS-Status wurde geändert!')
        else:
            messages.error(request,'SOS-Status wurde nicht geändert!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class CommissionTicketChangeView(MainView):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get('id'):
            obj = Commission.objects.get(id=self.kwargs.get('id'))
            obj.ticket = False if obj.ticket == True else True
            obj.save()
            messages.success(request,'Ticket-Status wurde geändert!')
        else:
            messages.error(request,'Ticket-Status wurde nicht geändert!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class CommissionDeliveryChangeView(MainView):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get('id'):
            obj = Commission.objects.get(id=self.kwargs.get('id'))
            obj.done = False if obj.done == True else True
            obj.save()
            messages.success(request,'Liefer-Status wurde geändert!')
        else:
            messages.error(request,'Liefer-Status wurde nicht geändert!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class CommissionSOSView(MainView):
    template_name = 'commission/commission_sos.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Commission.objects.filter(sos=True).order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'commission'
#--------------------------------------------------------------------------------
class CommissionTicketView(MainView):
    template_name = 'commission/commission_ticket.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Commission.objects.filter(ticket=True).order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'commission'
#--------------------------------------------------------------------------------