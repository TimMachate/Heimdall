#--------------------------------------------------------------------------------
# View File from Model Order
# 09.11.2023
# Tim Machate
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
from storagemanagement.companyitem.models import CompanyItem
from storagemanagement.order.models import Order
from storagemanagement.orderdata.models import OrderData
from storagemanagement.storage.models import Storage
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.order.forms import OrderForm, OrderDataFormset
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class OrderView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.view_order'

    template_name = 'storagemanagement_order_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Order.objects.filter(done=False)
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'order'
        # Urls
        self.context['url_overview'] = reverse('storagemanagement:order_overview')
        self.context['url_list'] = reverse('storagemanagement:order_list')
        self.context['url_table'] = reverse('storagemanagement:order_table')
        self.context['url_create'] = reverse('storagemanagement:order_create')
        # Data Url
        self.context["fields"] = ""
        self.context["api_data_url"] = reverse("storagemanagementAPI:order_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class OrderListView(OrderView):

    permission_required = 'storagemanagement.list_order'

    template_name = 'storagemanagement_order_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,done,authorized,booked,sent,recived,reference_number,company_name,item_count,value,notice,url_detail,url_update,url_delete"
        self.context["api_data_url"] = reverse("storagemanagementAPI:order_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class OrderTableView(OrderView):

    permission_required = 'storagemanagement.table_order'

    template_name = 'storagemanagement_order_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,done,authorized,booked,sent,sent_date,sent_time,recived,recived_date,recived_time,create_date,create_time,reference_number,company_name,item_count,value,notice"
        self.context["api_data_url"] = reverse("storagemanagementAPI:order_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class OrderCreateUpdateDetailView(OrderView):

    permission_required = ('storagemanagement.add_order','storagemanagement.change_order')

    template_name = 'storagemanagement_order_createupdatedetail.html'
    
    form_class = OrderForm
    formset_class = OrderDataFormset

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(
            instance=self.context['queryset']
        )
        self.context['formset'] = self.formset_class(
            instance=self.context['queryset'],
            queryset=OrderData.objects.all().order_by('id')
        )
        if self.context['queryset']:
            for form in self.context['formset']:
                form.fields["companyitem"].queryset = CompanyItem.objects.filter(company=self.context['queryset'].company())
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

        formset = self.formset_class(request.POST,request.FILES,instance=obj)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    orderdata = form.save(commit=False)
                    if not orderdata.create_user_id:
                        orderdata.create_user_id = user
                    orderdata.update_datetime = timezone.now()
                    orderdata.update_user_id = user
                    
                    if orderdata.amount != 0:
                        if orderdata.price:
                            companyitem = orderdata.companyitem
                            companyitem.price = orderdata.price
                            companyitem.update_datetime = timezone.now()
                            companyitem.update_user_id = user
                            companyitem.save()
                        else:
                            orderdata.price = orderdata.companyitem.price
                        orderdata.save()
        self.context['formset'] = formset


        return redirect('storagemanagement:order_update', order=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('order'):
            queryset = Order.objects.get(slug=self.kwargs.get('order'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class OrderCreateView(OrderCreateUpdateDetailView):
    permission_required = ('storagemanagement.add_order',)
#--------------------------------------------------------------------------------
class OrderDetailView(OrderCreateUpdateDetailView):
    permission_required = ('storagemanagement.detail_order',)
#--------------------------------------------------------------------------------
class OrderUpdateView(OrderCreateUpdateDetailView):
    permission_required = ('storagemanagement.change_order',)
#--------------------------------------------------------------------------------
class OrderDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.delete_order'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('order'):
            get_object_or_404(Order,slug = self.kwargs.get('order')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OrderAuthorizeTrueView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.authorize_true_order'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('order'):
            order = Order.objects.get(slug=self.kwargs.get('order'))
            if order.done == False and order.sent == False:
                orderdatas = order.orderdata()
                for orderdata in orderdatas:
                    orderdata.authorized = True
                    orderdata.authorized_datetime = timezone.now()
                    orderdata.authorized_user_id = user
                    orderdata.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OrderAuthorizeFalseView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.authorize_false_order'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('order'):
            order = Order.objects.get(slug=self.kwargs.get('order'))
            if order.done == False and order.sent == False:
                orderdatas = order.orderdata()
                for orderdata in orderdatas:
                    orderdata.authorized = False
                    orderdata.authorized_datetime = timezone.now()
                    orderdata.authorized_user_id = user
                    orderdata.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OrderBookingTrueView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.booking_true_order'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('order'):
            order = Order.objects.get(slug=self.kwargs.get('order'))
            if order.done == False and order.recived == True:
                orderdatas = order.orderdata()
                for orderdata in orderdatas:
                    orderdata.booking = True
                    orderdata.booking_datetime = timezone.now()
                    orderdata.booking_user_id = user
                    if order.done == False and orderdata.authorized:
                        old_stock = Booking.objects.filter(companyitem = orderdata.companyitem).last().stock if Booking.objects.filter(companyitem = orderdata.companyitem) else 0
                        new_stock = old_stock + orderdata.amount
                        booking = Booking(
                            amount=orderdata.amount,
                            companyitem=orderdata.companyitem,
                            create_user_id=user,
                            price=orderdata.price,
                            stock=new_stock,
                            update_user_id=user,
                        )
                        booking.save()
                        # load items in stock or unload items in stock
                        for i in range(0,booking.amount,1):
                            storage = Storage(
                                booking = booking,
                                companyitem = orderdata.companyitem,
                                create_user_id = user,
                                update_user_id = user,
                            )
                            storage.save()
                    orderdata.done = True
                    orderdata.save()
            done = True
            for orderdata in order.orderdata():
                if orderdata.done == False:
                    done = False
            order.done = done
            order.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OrderBookingFalseView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.booking_false_order'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('order'):
            order = Order.objects.get(slug=self.kwargs.get('order'))
            if order.done == False and order.recived == True:
                orderdatas = order.orderdata()
                for orderdata in orderdatas:
                    orderdata.booking = False
                    orderdata.booking_datetime = timezone.now()
                    orderdata.booking_user_id = user
                    orderdata.done = True
                    orderdata.save()
            done = True
            for orderdata in order.orderdata():
                if orderdata.done == False:
                    done = False
            order.done = done
            order.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OrderRecivedView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.recived_order'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('order'):
            order = Order.objects.get(slug=self.kwargs.get('order'))
            if order.sent and order.order_file and order.done == False:
                order.recived = True
                order.recived_datetime = timezone.now()
                order.recived_user_id = user
                order.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OrderSentView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.sent_order'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('order'):
            order = Order.objects.get(slug=self.kwargs.get('order'))
            if order.authorized() and order.done == False:
                order.sent = True
                order.sent_datetime = timezone.now()
                order.sent_user_id = user
                order.save()
        
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
