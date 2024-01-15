"""
#--------------------------------------------------------------------------------
# View File from Model Booking
# 07.01.2024
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
from storagemanagement.booking.models import Booking
from storagemanagement.supplier.models import Supplier
from storagemanagement.supplieritem.models import SupplierItem
from storagemanagement.storage.models import Storage
from storagemanagement.storageitem.models import StorageItem
from storagemanagement.storagemanagementusersetting.booking.models import (
    StorageManagementBookingListUserSetting,
    StorageManagementBookingOverviewUserSetting,
    StorageManagementBookingTableUserSetting
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.booking.forms import BookingForm
from storagemanagement.storagemanagementusersetting.booking.forms import (
    StorageManagementBookingListUserSettingForm,
    StorageManagementBookingOverviewUserSettingForm,
    StorageManagementBookingTableUserSettingForm
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class BookingBaseView(PermissionRequiredMixin,MainView):
    """
    BookingBaseView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    form_setting = None
    model_setting = None

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

    def post(self,request, *args, **kwargs):
        """
        post

        Args:
            request (_type_): _description_
        """
        form = self.form_setting(
            request.POST,
            request.FILES,
            instance=self.context["form_setting_queryset"]
        )
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj = form.save()
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            obj.save()
        self.context['form'] = form
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    def get_initial(self, *args, **kwargs):
        """
        get_initial

        Returns:
            dict: contains all initial values
        """
        result = {}
        if self.kwargs.get("storageitem"):
            result["storageitem"] = StorageItem.objects.get(slug=self.kwargs.get("storageitem"))
            result["amount"] = result["storageitem"].maximum - result["storageitem"].stock_count()
            supplieritem = result["storageitem"].supplieritem if result["storageitem"].supplieritem else None
            supplieritem = SupplierItem.objects.filter(
                storageitem=result["storageitem"]
            ).order_by('price').first() if not supplieritem else supplieritem
            result["supplieritem"] = supplieritem
        return result if not result else None

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains all context data
        """
        super().get_context_data(**kwargs)
        self.context['model'] = 'booking'
        # Urls
        if self.kwargs.get('supplier') and not self.kwargs.get('supplieritem'):
            self.context['url_overview'] = reverse(
                'storagemanagement:supplier_booking_overview',
                kwargs={'supplier':self.kwargs.get('supplier')}
            )
            self.context['url_list'] = reverse(
                'storagemanagement:supplier_booking_list',
                kwargs={'supplier':self.kwargs.get('supplier')}
            )
            self.context['url_table'] = reverse(
                'storagemanagement:supplier_booking_table',
                kwargs={'supplier':self.kwargs.get('supplier')}
            )
            self.context['url_create'] = reverse(
                'storagemanagement:supplier_booking_create',
                kwargs={'supplier':self.kwargs.get('supplier')}
            )
        elif self.kwargs.get('supplieritem'):
            self.context['url_overview'] = reverse(
                'storagemanagement:supplieritem_booking_overview',
                kwargs={'supplieritem':self.kwargs.get('supplieritem')}
            )
            self.context['url_list'] = reverse(
                'storagemanagement:supplieritem_booking_list',
                kwargs={'supplieritem':self.kwargs.get('supplieritem')}
            )
            self.context['url_table'] = reverse(
                'storagemanagement:supplieritem_booking_table',
                kwargs={'supplieritem':self.kwargs.get('supplieritem')}
            )
            self.context['url_create'] = reverse(
                'storagemanagement:supplieritem_booking_create',
                kwargs={'supplieritem':self.kwargs.get('supplieritem')}
            )
        elif self.kwargs.get('storageitem'):
            self.context['url_overview'] = reverse(
                'storagemanagement:storageitem_booking_overview',
                kwargs={'storageitem':self.kwargs.get('storageitem')}
            )
            self.context['url_list'] = reverse(
                'storagemanagement:storageitem_booking_list',
                kwargs={'storageitem':self.kwargs.get('storageitem')}
            )
            self.context['url_table'] = reverse(
                'storagemanagement:storageitem_booking_table',
                kwargs={'storageitem':self.kwargs.get('storageitem')}
            )
            self.context['url_create'] = reverse(
                'storagemanagement:storageitem_booking_create',
                kwargs={'storageitem':self.kwargs.get('storageitem')}
            )
        else:
            self.context['url_overview'] = reverse('storagemanagement:booking_overview')
            self.context['url_list'] = reverse('storagemanagement:booking_list')
            self.context['url_table'] = reverse('storagemanagement:booking_table')
            self.context['url_create'] = reverse('storagemanagement:booking_create')
        # Setting
        if self.model_setting and self.form_setting:
            self.context["form_setting_queryset"] = self.model_setting.objects.get_or_create(
                user=self.request.user
            )[0]
            # Data Url
            if self.kwargs.get("supplier"):
                self.context["supplier"]=self.kwargs.get("supplier")
            else:
                self.context["supplier"]=""
            if self.kwargs.get("supplieritem"):
                self.context["supplieritem"]=self.kwargs.get("supplieritem")
            else:
                self.context["supplieritem"]=""
            if self.kwargs.get("storageitem"):
                self.context["storageitem"]=self.kwargs.get("storageitem")
            else:
                self.context["storageitem"]=""
            self.context["api_data_url"] = self.get_url_api(
                queryset=self.context["form_setting_queryset"],
                supplier=self.context["supplier"],
                supplieritem=self.context["supplieritem"],
                storageitem=self.context["storageitem"]
            )
            # Form
            self.context["form_setting"] = self.form_setting(
                instance = self.context["form_setting_queryset"]
            )
        else:
            self.context["supplier"]=None
            self.context["supplieritem"]=None
            self.context["storageitem"]=None
            self.context["form_setting_queryset"] = None
            self.context["form_setting"] = None
            self.context["api_data_url"] = None

        # Queryset
        self.context["queryset"]= self.get_queryset()
        return self.context

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset

        Returns:
            queryset: contains the booking object
        """
        if self.kwargs.get('supplier') and not self.kwargs.get('supplieritem'):
            queryset = Booking.objects.filter(
                supplieritem__company__slug=self.kwargs.get('supplier')
            )
        elif self.kwargs.get('supplieritem'):
            queryset = Booking.objects.filter(
                supplieritem__slug=self.kwargs.get('supplieritem')
            )
        elif self.kwargs.get('storageitem'):
            queryset = Booking.objects.filter(
                storageitem__slug=self.kwargs.get('storageitem')
            )
        else:
            queryset = Booking.objects.all()
        return queryset

    def get_url_api(self,queryset,supplier,supplieritem,storageitem):
        """
        get_url_api

        Returns:
            string: url to api
        """
        url = queryset.api_url() + "&supplieritem__company__slug={}&supplieritem__slug={}&storageitem__slug={}".format(
            supplier,
            supplieritem,
            storageitem
        )
        return url
#--------------------------------------------------------------------------------
class BookingView(BookingBaseView):
    """
    Booking View

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: Booking View
    """

    permission_required = 'storagemanagement.view_booking'

    template_name = 'storagemanagement_booking_overview.html'

    form_setting = StorageManagementBookingOverviewUserSettingForm
    model_setting = StorageManagementBookingOverviewUserSetting
#--------------------------------------------------------------------------------
class BookingListView(BookingBaseView):
    """
    BookingListView

    Args:
        BookingView (_type_): _description_

    Returns:
        _type_: _description_
    """
    permission_required = 'storagemanagement.list_booking'

    template_name = 'storagemanagement_booking_list.html'

    form_setting = StorageManagementBookingListUserSettingForm
    model_setting = StorageManagementBookingListUserSetting
#--------------------------------------------------------------------------------
class BookingTableView(BookingBaseView):
    """
    BookingTableView

    Args:
        BookingView (_type_): _description_

    Returns:
        _type_: _description_
    """
    permission_required = 'storagemanagement.table_booking'

    template_name = 'storagemanagement_booking_table.html'

    form_setting = StorageManagementBookingTableUserSettingForm
    model_setting = StorageManagementBookingTableUserSetting
#--------------------------------------------------------------------------------
class BookingCreateUpdateDetailView(BookingBaseView):
    """
    BookingCreateUpdateDetailView

    Args:
        BookingView (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name = 'storagemanagement_booking_createupdatedetail.html'

    form_class = BookingForm

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context['queryset'] = self.get_queryset()
        self.context['form'] = self.form_class(
            instance=self.context['queryset'],
            initial=self.get_initial()
        )
        if self.kwargs.get("supplier"):
            self.context['form'].fields["supplieritem"].queryset = Supplier.objects.get(
                slug=self.kwargs.get("supplier")
            ).supplieritem_data()
        if self.kwargs.get("storageitem"):
            self.context['form'].fields["supplieritem"].queryset = StorageItem.objects.get(
                slug=self.kwargs.get('storageitem')
            ).supplieritem_data.all()
        return render(request, self.template_name, self.context)

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance=self.context['queryset'])
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj = form.save(commit=False)
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            # add storageitem
            obj.storageitem = StorageItem.objects.filter(supplieritem_data = obj.supplieritem).first()

            if 'add_value' in request.POST:
                # take amount and abs
                obj.amount = abs(obj.amount)

            if 'remove_value' in request.POST:
                # take amount and abs
                obj.amount = 0-abs(obj.amount)

            old_stock = Booking.objects.filter(
                supplieritem = obj.supplieritem
            ).last().stock if Booking.objects.filter(supplieritem = obj.supplieritem) else 0
            new_stock = old_stock + obj.amount

            # set stock to 0 if new_stock is smaller then 0
            if new_stock <0:
                new_stock = 0

            # save the new stock value in stock of booking model
            obj.stock = new_stock
            obj.price = obj.supplieritem.price
            obj.save()

            # load items in stock or unload items in stock
            if obj.amount > 0:
                # create the items in stock
                i=0
                for i in range(0,obj.amount,1):
                    storage = Storage(
                        booking = Booking.objects.get(id=obj.id),
                        supplieritem = SupplierItem.objects.get(id=obj.supplieritem.id),
                        create_user_id = user,
                        update_user_id = user,
                        update_datetime = timezone.now(),
                    )
                    storage.save()
                    i+=1
            if obj.amount < 0:
                # unload the items in stock
                storages = Storage.objects.filter(
                    supplieritem = obj.supplieritem,
                    unload_datetime = None,
                ).values_list('id',flat=True)[0:abs(obj.amount)]
                Storage.objects.filter(id__in = list(storages)).update(
                    unload = True,
                    unload_user_id = user,
                    unload_datetime = timezone.now(),
                    update_user_id = user,
                    update_datetime = timezone.now(),
                )

        self.context['form'] = form
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:booking_update', booking=obj.slug)

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset

        Returns:
            queryset: contains the booking object
        """
        if self.kwargs.get('booking'):
            queryset = Booking.objects.get(
                slug=self.kwargs.get('booking')
            )
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class BookingCreateView(BookingCreateUpdateDetailView):
    """
    BookingCreateView

    Args:
        BookingCreateUpdateDetailView (_type_): _description_
    """

    permission_required = ('storagemanagement.add_booking',)
#--------------------------------------------------------------------------------
class BookingDetailView(BookingCreateUpdateDetailView):
    """
    BookingDetailView

    Args:
        BookingCreateUpdateDetailView (_type_): _description_
    """

    permission_required = ('storagemanagement.detail_booking',)
#--------------------------------------------------------------------------------
class BookingUpdateView(BookingCreateUpdateDetailView):
    """
    BookingUpdateView

    Args:
        BookingCreateUpdateDetailView (_type_): _description_
    """

    permission_required = ('storagemanagement.change_booking',)
#--------------------------------------------------------------------------------
class BookingDeleteView(PermissionRequiredMixin,MainView):
    """
    BookingDeleteView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.delete_booking'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('booking'):
            get_object_or_404(Booking,slug = self.kwargs.get('booking')).delete()
            messages.success(request,'Booking wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Booking konnte nicht gelöscht werden!')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:booking_list')
#--------------------------------------------------------------------------------
