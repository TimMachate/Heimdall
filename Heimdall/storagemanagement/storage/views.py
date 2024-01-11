"""
#--------------------------------------------------------------------------------
# View File from Model Storage
# 03.01.2024
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
from storagemanagement.supplieritem.models import SupplierItem
from storagemanagement.storage.models import Storage
from storagemanagement.storageitem.models import StorageItem
from storagemanagement.storagemanagementusersetting.storage.models import (
    StorageManagementStorageOverviewUserSetting,
    StorageManagementStorageListUserSetting,
    StorageManagementStorageTableUserSetting
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.storage.forms import StorageForm
from storagemanagement.storagemanagementusersetting.storage.forms import (
    StorageManagementStorageOverviewUserSettingForm,
    StorageManagementStorageListUserSettingForm,
    StorageManagementStorageTableUserSettingForm
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class StorageBaseView(PermissionRequiredMixin,MainView):
    """
    StorageBaseView

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
        if self.kwargs.get('supplieritem'):
            result['supplieritem'] = SupplierItem.objects.get(slug=self.kwargs.get('supplieritem'))
        if self.kwargs.get('booking'):
            result['booking'] = Booking.objects.get(slug=self.kwargs.get('booking'))
        if not result:
            result = None
        return result

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains all context data
        """
        super().get_context_data(**kwargs)
        self.context['model'] = 'storageitem'
        # Urls
        if self.kwargs.get('supplier') and not self.kwargs.get('supplieritem'):
            self.context['url_overview'] = reverse('storagemanagement:supplier_storage_overview',kwargs={'supplier':self.kwargs.get('supplier')})
            self.context['url_list'] = reverse('storagemanagement:supplier_storage_list',kwargs={'supplier':self.kwargs.get('supplier')})
            self.context['url_table'] = reverse('storagemanagement:supplier_storage_table',kwargs={'supplier':self.kwargs.get('supplier')})
            self.context['url_create'] = reverse('storagemanagement:supplier_storage_create',kwargs={'supplier':self.kwargs.get('supplier')})
        elif self.kwargs.get('supplieritem'):
            self.context['url_overview'] = reverse('storagemanagement:supplieritem_storage_overview',kwargs={'supplieritem':self.kwargs.get('supplieritem')})
            self.context['url_list'] = reverse('storagemanagement:supplieritem_storage_list',kwargs={'supplieritem':self.kwargs.get('supplieritem')})
            self.context['url_table'] = reverse('storagemanagement:supplieritem_storage_table',kwargs={'supplieritem':self.kwargs.get('supplieritem')})
            self.context['url_create'] = reverse('storagemanagement:supplieritem_storage_create',kwargs={'supplieritem':self.kwargs.get('supplieritem')})
        elif self.kwargs.get('storageitem'):
            self.context['url_overview'] = reverse('storagemanagement:storageitem_storage_overview',kwargs={'storageitem':self.kwargs.get('storageitem')})
            self.context['url_list'] = reverse('storagemanagement:storageitem_storage_list',kwargs={'storageitem':self.kwargs.get('storageitem')})
            self.context['url_table'] = reverse('storagemanagement:storageitem_storage_table',kwargs={'storageitem':self.kwargs.get('storageitem')})
            self.context['url_create'] = reverse('storagemanagement:storageitem_storage_create',kwargs={'storageitem':self.kwargs.get('storageitem')})
        else:
            self.context['url_overview'] = reverse('storagemanagement:storage_overview')
            self.context['url_list'] = reverse('storagemanagement:storage_list')
            self.context['url_table'] = reverse('storagemanagement:storage_table')
            self.context['url_create'] = reverse('storagemanagement:storage_create')
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

    def get_queryset(self):
        """
        get_queryset

        Returns:
            queryset: contains a storage object
        """
        if self.kwargs.get('storage'):
            queryset = Storage.objects.get(slug=self.kwargs.get('storage'))
        else:
            queryset = Storage.objects.filter(unload_datetime=None)
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
class StorageView(StorageBaseView):
    """
    StorageView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.view_storage'

    template_name = 'storagemanagement_storage_overview.html'

    form_setting = StorageManagementStorageOverviewUserSettingForm
    model_setting = StorageManagementStorageOverviewUserSetting

    #def get_queryset(self):
    #    """
    #    get_queryset

    #    Returns:
    #        queryset: contains all storage objects
    #    """
    #    if Storage.objects.all().count()>0:
    #        objects = set(
    #            [
    #                obj.supplieritem.storageitem.id for obj in Storage.objects.filter(
    #                    unload_datetime=None
    #                )
    #            ]
    #        )
    #        queryset = StorageItem.objects.filter(id__in = objects)
    #    else:
    #        queryset = None
    #    return queryset
#--------------------------------------------------------------------------------
class StorageListView(StorageBaseView):
    """
    StorageListView

    Args:
        StorageView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.list_storage'

    template_name = 'storagemanagement_storage_list.html'

    form_setting = StorageManagementStorageListUserSettingForm
    model_setting = StorageManagementStorageListUserSetting
#--------------------------------------------------------------------------------
class StorageTableView(StorageBaseView):
    """
    StorageTableView

    Args:
        StorageView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.table_storage'

    template_name = 'storagemanagement_storage_table.html'

    form_setting = StorageManagementStorageTableUserSettingForm
    model_setting = StorageManagementStorageTableUserSetting
#--------------------------------------------------------------------------------
class StorageCreateUpdateDetailView(StorageBaseView):
    """
    StorageCreateUpdateDetailView

    Args:
        StorageView (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name = 'storagemanagement_storage_createupdatedetail.html'

    form_class = StorageForm

    def get(self, request, *args, **kwargs):
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
        if self.kwargs.get("storageitem"):
            self.context['form'].fields["supplieritem"].queryset = StorageItem.objects.get(
                slug=self.kwargs.get("storageitem")
            ).supplieritems()
        if self.kwargs.get("supplier"):
            self.context['form'].fields["supplieritem"].queryset = SupplierItem.objects.filter(
                company__slug = self.kwargs.get("supplier")
            )
        if self.get_initial():
            self.context['form'].initial = self.get_initial()
        return render(request, self.template_name, self.context)

    def post(self,request, *args, **kwargs):
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
            obj.save()

        self.context['form'] = form
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:storage_update', storage=obj.slug)

    def get_queryset(self):
        """
        get_queryset

        Returns:
            queryset: contains a storage object
        """
        if self.kwargs.get('storage'):
            queryset = Storage.objects.get(slug=self.kwargs.get('storage'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class StorageCreateView(StorageCreateUpdateDetailView):
    """
    StorageCreateView

    Args:
        StorageCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.add_storage',)
#--------------------------------------------------------------------------------
class StorageDetailView(StorageCreateUpdateDetailView):
    """
    StorageDetailView

    Args:
        StorageCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.detail_storage',)
#--------------------------------------------------------------------------------
class StorageUpdateView(StorageCreateUpdateDetailView):
    """
    StorageUpdateView

    Args:
        StorageCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.change_storage',)
#--------------------------------------------------------------------------------
class StorageDeleteView(PermissionRequiredMixin,MainView):
    """
    StorageDeleteView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.delete_storage'

    def get(self, request, *args, **kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('storage'):
            get_object_or_404(Storage,slug = self.kwargs.get('storage')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:storage_list')
#--------------------------------------------------------------------------------
class StorageUnloadView(PermissionRequiredMixin,MainView):
    """
    StorageUnloadView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """
    permission_required = 'storagemanagement.unload_storage'

    def get(self, request, *args, **kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        query = self.get_queryset()
        query.unload_user_id = user
        query.unload_datetime = timezone.now()
        query.save()

        old_stock = Booking.objects.filter(
            supplieritem = query.supplieritem
        ).last().stock if Booking.objects.filter(
            supplieritem = query.supplieritem
        ) else 0
        new_stock = old_stock -1

        # set stock to 0 if new_stock is smaller then 0
        if new_stock <0:
            new_stock = 0

        booking = Booking(
            amount = -1,
            create_user_id = user,
            price = query.supplieritem.price,
            stock = new_stock,
            supplieritem = SupplierItem.objects.get(id=query.supplieritem.id),
            update_user_id = user,
            update_datetime = timezone.now(),
        )
        booking.save()
        if 'next' in request.GET:
            return redirect(request.GET.get('next'))
        else:
            return redirect("storagemanagement:storage_overview")

    def get_queryset(self):
        """
        get_queryset

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('storage'):
            queryset = get_object_or_404(Storage,slug = self.kwargs.get('storage'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
