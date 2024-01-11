"""
#--------------------------------------------------------------------------------
# Views File from App Storagementsystem
# 08.11.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
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
#from storagemanagement.booking.models import Booking
from storagemanagement.supplier.models import Supplier
from storagemanagement.suppliercontact.models import SupplierContact
from storagemanagement.supplieritem.models import SupplierItem
#from storagemanagement.offer.models import Offer
#from storagemanagement.order.models import Order
#from storagemanagement.requestdata.models import RequestData
#from storagemanagement.storage.models import Storage
#from storagemanagement.storageitem.models import StorageItem
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
    """
    StorageManagementView

    Args:
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """
    permission_required = 'storagemanagement'

    template_name = 'storagemanagement.html'

    def get(self, request, *args, **kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.get_context_data()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dic: contains context data
        """
        super().get_context_data(**kwargs)

        #booking = Booking.objects.all()
        suppliers = Supplier.objects.all()
        #suppliercontact = SupplierContact.objects.all()
        #supplieritem =  SupplierItem.objects.all()
        #storageitem = StorageItem.objects.all()
        #stock = Storage.objects.all()

        self.context['supplier_count'] = suppliers.count()
        #self.context['suppliercontact_count'] = suppliercontact.count()
        #self.context['supplieritem_count'] = supplieritem.count()
        #self.context['storageitem_count'] = storageitem.count()
        #self.context['booking_last'] = booking.order_by('-create_datetime')[:5]

        #result = 0
        #for i in storageitem:
        #    if i.status() == 'warning':
        #        result += 1
        #self.context['storageitem_warning'] = result

        #result = 0
        #for i in storageitem:
        #    if i.status() == 'alarm':
        #        result += 1
        #self.context['storageitem_alarm'] = result

        #result = 0
        #for i in storageitem:
        #    result += i.stock_percentage()
        #if self.context["storageitem_count"] > 0:
        #    result = int(result / self.context["storageitem_count"])
        #else:
        #    result = 0
        #self.context['stock_percentage'] = result

        #result = 0
        #for i in stock:
        #    result += i.value()
        #self.context['stock_value'] = result

        #result = 0
        #for i in storageitem:
        #    if i.supplieritem:
        #        result += (i.maximum - i.stock_count()) * i.supplieritem.price
        #self.context['stock_miss_value'] = result

        #result = 0
        #for i in storageitem:
        #    if i.supplieritem:
        #        result += i.maximum * i.supplieritem.price
        #self.context['stock_max_value'] = result

        #self.context['requestdata_open'] = RequestData.objects.filter(done=False).count()
        #self.context['offer_open'] = Offer.objects.filter(done=False).count()
        #self.context['order_open'] = Order.objects.filter(done=False).count()
        return self.context
#--------------------------------------------------------------------------------
class OrderProcessView(MainView):
    """
    OrderProcessView

    Args:
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """
    permission_required = 'storagemanagement:orderprocess'

    template_name = 'orderprocess.html'

    def get(self, request, *args, **kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.get_context_data()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dic: contains context data
        """

        super().get_context_data(**kwargs)
        #self.context['requestdata_open'] = RequestData.objects.filter(done=False).count()
        #self.context['offer_open'] = Offer.objects.filter(done=False).count()
        #self.context['order_open'] = Order.objects.filter(done=False).count()
        return self.context
#--------------------------------------------------------------------------------
