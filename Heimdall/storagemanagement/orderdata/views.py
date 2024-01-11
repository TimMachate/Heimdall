"""
#--------------------------------------------------------------------------------
# View File from Model Order Data
# 10.11.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
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
from storagemanagement.order.models import Order
from storagemanagement.orderdata.models import OrderData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.orderdata.forms import OrderDataForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class OrderDataView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.view_orderdata'

    template_name = 'storagemanagement_orderdata_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = OrderData.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'orderdata'
        # Urls
        if self.kwargs.get('order'):
            self.context['url_overview'] = reverse('storagemanagement:order_orderdata_overview',kwargs={'order':self.kwargs.get('order')})
            self.context['url_list'] = reverse('storagemanagement:order_orderdata_list',kwargs={'order':self.kwargs.get('order')})
            self.context['url_table'] = reverse('storagemanagement:order_orderdata_table',kwargs={'order':self.kwargs.get('order')})
            self.context['url_create'] = reverse('storagemanagement:order_orderdata_create',kwargs={'order':self.kwargs.get('order')})
        else:
            self.context['url_overview'] = reverse('storagemanagement:orderdata_overview')
            self.context['url_list'] = reverse('storagemanagement:orderdata_list')
            self.context['url_table'] = reverse('storagemanagement:orderdata_table')
            self.context['url_create'] = reverse('storagemanagement:orderdata_create')
        # Data Url
        self.context["fields"] = ""
        self.context["api_data_url"] = reverse("storagemanagementAPI:orderdata_list")+"?values={}&done=false".format(
            self.context["fields"]
        )
#--------------------------------------------------------------------------------
class OrderDataListView(OrderDataView):

    permission_required = 'storagemanagement.list_orderdata'

    template_name = 'storagemanagement_orderdata_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,authorized,booking,create_date,create_time,companyitem_name,companyitem_url_detail,company_name,company_url_detail,price,amount,unit,value,url_detail,url_authorize_true,url_authorize_false,url_booking_true,url_booking_false"
        self.context["api_data_url"] = reverse("storagemanagementAPI:orderdata_list")+"?values={}".format(
            self.context["fields"]
        )
#--------------------------------------------------------------------------------
class OrderDataTableView(OrderDataView):

    permission_required = 'storagemanagement.table_orderdata'

    template_name = 'storagemanagement_orderdata_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,authorized,authorized_date,authorized_time,authorized_username,booking,booking_date,booking_time,booking_username,companyitem_name,storageitem_name,company_name,amount,price,unit,value,amount_recived"
        self.context["api_data_url"] = reverse("storagemanagementAPI:orderdata_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class OrderDataCreateUpdateDetailView(OrderDataView):
    """
    OrderDataCreateUpdateDetailView

    Args:
        OrderDataView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = ('storagemanagement.add_orderdata','storagemanagement.change_orderdata')

    template_name = 'storagemanagement_orderdata_createupdatedetail.html'

    form_class = OrderDataForm

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'])
        return render(request, self.template_name, self.context)

    def post(self,request):
        """
        post

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        form = self.form_class(request.POST,request.FILES,instance=self.context['queryset'])
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj = form.save(commit=False)
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()

            if obj.price:
                companyitem = obj.companyitem
                companyitem.price = obj.price
                companyitem.update_datetime = timezone.now()
                companyitem.update_user_id = user
                companyitem.save()
            else:
                obj.price = obj.companyitem.price

            if not obj.order:
                orderdatas = OrderData.objects.filter(
                    companyitem__company = obj.companyitem.company
                ).exclude(order__sent = True)
                if orderdatas.exists():
                    orderdata = orderdatas.first()
                    orderdatas = orderdata.order.orderdata().filter(companyitem=obj.companyitem)
                    if orderdatas.exists():
                        orderdata = orderdatas.first()
                        orderdata.amount += obj.amount
                        obj = orderdata
                    else:
                        obj.order = orderdata.order

                else:
                    order = Order(
                        create_user_id=user,
                        update_user_id=user
                    )
                    order.save()
                    obj.order = order

            obj.save()
        self.context['form'] = form

        return redirect('storagemanagement:orderdata_update', orderdata=obj.slug)

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset

        Returns:
            queryset: contains order data obj
        """
        if self.kwargs.get('orderdata'):
            queryset = OrderData.objects.get(slug=self.kwargs.get('orderdata'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class OrderDataCreateView(OrderDataCreateUpdateDetailView):
    """
    OrderDataCreateView

    Args:
        OrderDataCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.add_orderdata',)
#--------------------------------------------------------------------------------
class OrderDataDetailView(OrderDataCreateUpdateDetailView):
    """
    OrderDataDetailView

    Args:
        OrderDataCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.detail_orderdata',)
#--------------------------------------------------------------------------------
class OrderDataUpdateView(OrderDataCreateUpdateDetailView):
    """
    OrderDataUpdateView

    Args:
        OrderDataCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.change_orderdata',)
#--------------------------------------------------------------------------------
class OrderDataDeleteView(PermissionRequiredMixin,MainView):
    """
    OrderDataDeleteView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.delete_orderdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('orderdata'):
            get_object_or_404(OrderData,slug = self.kwargs.get('orderdata')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OrderDataAuthorizedTrueView(PermissionRequiredMixin,MainView):
    """
    OrderDataAuthorizedTrueView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.authorize_true_orderdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('orderdata'):
            obj = OrderData.objects.get(slug=self.kwargs.get('orderdata'))
            if obj.done is False:
                obj.authorized = True
                obj.authorized_user_id = user
                obj.authorized_datetime = timezone.now()
                obj.update_user_id = user
                obj.update_datetime = timezone.now()
                obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OrderDataAuthorizedFalseView(PermissionRequiredMixin,MainView):
    """
    OrderDataAuthorizedFalseView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.authorize_false_orderdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('orderdata'):
            obj = OrderData.objects.get(slug=self.kwargs.get('orderdata'))
            if obj.done is False:
                obj.authorized = False
                obj.authorized_user_id = user
                obj.authorized_datetime = timezone.now()
                obj.update_user_id = user
                obj.update_datetime = timezone.now()
                obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OrderDataAuthorizedTrueAllView(PermissionRequiredMixin,MainView):
    """
    OrderDataAuthorizedTrueAllView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.authorize_true_orderdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        for obj in OrderData.objects.filter(done=False):
            obj.authorized = True
            obj.authorized_user_id = user
            obj.authorized_datetime = timezone.now()
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OrderDataAuthorizedFalseAllView(PermissionRequiredMixin,MainView):
    """
    OrderDataAuthorizedFalseAllView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.authorize_false_orderdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        for obj in OrderData.objects.filter(done=False):
            obj.authorized = False
            obj.authorized_user_id = user
            obj.authorized_datetime = timezone.now()
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OrderDataBookingTrueView(PermissionRequiredMixin,MainView):
    """
    OrderDataBookingTrueView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.booking_true_orderdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('orderdata'):
            obj = OrderData.objects.get(slug=self.kwargs.get('orderdata'))
            if obj.done is False:
                obj.booking = True
                obj.booking_user_id = user
                obj.booking_datetime = timezone.now()
                obj.update_user_id = user
                obj.update_datetime = timezone.now()
                obj.done = True
                obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OrderDataBookingFalseView(PermissionRequiredMixin,MainView):
    """
    OrderDataBookingFalseView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.booking_false_orderdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('orderdata'):
            obj = OrderData.objects.get(slug=self.kwargs.get('orderdata'))
            if obj.done is False:
                obj.booking = True
                obj.booking_user_id = user
                obj.booking_datetime = timezone.now()
                obj.update_user_id = user
                obj.update_datetime = timezone.now()
                obj.done = True
                obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OrderDataBookingTrueAllView(PermissionRequiredMixin,MainView):
    """
    OrderDataBookingTrueAllView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.booking_true_orderdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        for obj in OrderData.objects.filter(done=False):
            obj.booking = True
            obj.booking_user_id = user
            obj.booking_datetime = timezone.now()
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            obj.done = True
            obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OrderDataBookingFalseAllView(PermissionRequiredMixin,MainView):
    """
    OrderDataBookingFalseAllView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.booking_false_orderdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        for obj in OrderData.objects.filter(done=False):
            obj.booking = True
            obj.booking_user_id = user
            obj.booking_datetime = timezone.now()
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            obj.done = True
            obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
