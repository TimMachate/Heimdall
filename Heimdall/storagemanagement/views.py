#--------------------------------------------------------------------------------
# Views File from App Storagementsystem
# 08.11.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.booking.models import Booking
from storagemanagement.company.models import Company
from storagemanagement.companycontact.models import CompanyContact
from storagemanagement.companyitem.models import CompanyItem
from storagemanagement.offer.models import Offer
from storagemanagement.order.models import Order
from storagemanagement.requestdata.models import RequestData
from storagemanagement.storage.models import Storage
from storagemanagement.storageitem.models import StorageItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
# There are no Forms necessary
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class StorageManagementView(MainView):
    permission_required = 'storagemanagement'

    template_name = 'storagemanagement.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        
        booking = Booking.objects.all()
        suppliers = Company.objects.all()
        companycontact = CompanyContact.objects.all()
        companyitem =  CompanyItem.objects.all()
        storageitem = StorageItem.objects.all()
        stock = Storage.objects.all()

        self.context['supplier_count'] = suppliers.count()
        self.context['companycontact_count'] = companycontact.count()
        self.context['companyitem_count'] = companyitem.count()
        self.context['storageitem_count'] = storageitem.count()
        self.context['booking_last'] = booking.order_by('-create_datetime')[:5]

        result = 0
        for i in storageitem:
            if i.status() == 'warning':
                result += 1
        self.context['storageitem_warning'] = result

        result = 0
        for i in storageitem:
            if i.status() == 'alarm':
                result += 1
        self.context['storageitem_alarm'] = result

        result = 0
        for i in storageitem:
            result += i.stock_percentage()
        if self.context["storageitem_count"] > 0:
            result = int(result / self.context["storageitem_count"])
        else:
            result = 0
        self.context['stock_percentage'] = result

        result = 0
        for i in stock:
            result += i.value()
        self.context['stock_value'] = result

        result = 0
        for i in storageitem:
            if i.companyitem:
                result += (i.maximum - i.stock_count()) * i.companyitem.price
        self.context['stock_miss_value'] = result

        result = 0
        for i in storageitem:
            if i.companyitem:
                result += i.maximum * i.companyitem.price
        self.context['stock_max_value'] = result

        self.context['requestdata_open'] = RequestData.objects.filter(done=False).count()
        self.context['offer_open'] = Offer.objects.filter(done=False).count()
        self.context['order_open'] = Order.objects.filter(done=False).count()
#--------------------------------------------------------------------------------
class OrderProcessView(MainView):
    permission_required = 'storagemanagement:orderprocess'

    template_name = 'orderprocess.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['requestdata_open'] = RequestData.objects.filter(done=False).count()
        self.context['offer_open'] = Offer.objects.filter(done=False).count()
        self.context['order_open'] = Order.objects.filter(done=False).count()