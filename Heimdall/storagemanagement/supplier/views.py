"""
#--------------------------------------------------------------------------------
# View File from Model Supplier
# 25.10.2023
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
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.supplier.models import Supplier
from storagemanagement.storagemanagementusersetting.supplier.models import (
    StorageManagementSupplierOverviewUserSetting,
    StorageManagementSupplierListUserSetting,
    StorageManagementSupplierTableUserSetting
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.supplier.forms import SupplierForm,SupplierFormset
from storagemanagement.storagemanagementusersetting.supplier.forms import (
    StorageManagementSupplierOverviewUserSettingForm,
    StorageManagementSupplierListUserSettingForm,
    StorageManagementSupplierTableUserSettingForm
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class SupplierBaseView(PermissionRequiredMixin,MainView):
    """
    SupplierBaseView

    Args:
        PermissionRequiredMixin (class): _description_
        MainView (class): _description_

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

    def get_context_data(self, *args, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains all context data
        """
        super().get_context_data(**kwargs)
        # Setting
        if self.model_setting and self.form_setting:
            self.context["form_setting_queryset"] = self.model_setting.objects.get_or_create(
                user=self.request.user
            )[0]
            # Data Url
            self.context["api_data_url"] = self.get_url_api(
                queryset=self.context["form_setting_queryset"]
            )
            # Form
            self.context["form_setting"] = self.form_setting(
                instance = self.context["form_setting_queryset"]
            )
        else:
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
            queryset: contains all suppliers
        """
        if self.kwargs.get('supplier'):
            queryset = Supplier.objects.get(slug=self.kwargs.get('supplier'))
        else:
            queryset = Supplier.objects.all()
        return queryset

    def get_url_api(self,queryset):
        """
        get_url_api

        Returns:
            string: url to api
        """
        url = queryset.api_url()
        return url
#--------------------------------------------------------------------------------
class SupplierView(SupplierBaseView):
    """
    SupplierView

    Args:
        SupplierBaseView (class): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.view_supplier'

    template_name = 'storagemanagement_supplier_overview.html'

    form_setting = StorageManagementSupplierOverviewUserSettingForm
    model_setting = StorageManagementSupplierOverviewUserSetting
#--------------------------------------------------------------------------------
class SupplierListView(SupplierBaseView):
    """
    SupplierListView

    Args:
        SupplierView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.list_supplier'

    template_name = 'storagemanagement_supplier_list.html'

    form_setting = StorageManagementSupplierListUserSettingForm
    model_setting = StorageManagementSupplierListUserSetting
#--------------------------------------------------------------------------------
class SupplierTableView(SupplierBaseView):
    """
    SupplierTableView

    Args:
        SupplierView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.table_supplier'

    template_name = 'storagemanagement_supplier_table.html'

    form_setting = StorageManagementSupplierTableUserSettingForm
    model_setting = StorageManagementSupplierTableUserSetting
#--------------------------------------------------------------------------------
class SupplierCreateUpdateDetailView(SupplierBaseView):
    """
    SupplierCreateUpdateDetailView

    Args:
        SupplierView (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name = 'storagemanagement_supplier_createupdatedetail.html'

    form_class = SupplierForm
    formset_supplier = SupplierFormset

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
        self.context['formset_supplier'] = self.formset_supplier(instance=self.context['queryset'])
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
            obj = form.save()
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            obj.supplier = True
            obj.save()
        self.context['form'] = form

        formset_supplier = self.formset_supplier(request.POST,request.FILES,instance=obj)
        if formset_supplier.is_valid():
            for form in formset_supplier:
                if form.is_valid():
                    supplier = form.save(commit=False)
                    supplier.company = obj
                    supplier.save()
        self.context['formset_supplier'] = formset_supplier

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset

        Returns:
            queryset: contains all suppliers
        """
        if self.kwargs.get('supplier'):
            queryset = Supplier.objects.get(slug=self.kwargs.get('supplier'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class SupplierCreateView(SupplierCreateUpdateDetailView):
    """
    SupplierCreateView

    Args:
        SupplierCreateUpdateDetailView (_type_): _description_
    """

    permission_required = ('storagemanagement.add_supplier',)
#--------------------------------------------------------------------------------
class SupplierDetailView(SupplierCreateUpdateDetailView):
    """
    SupplierDetailView

    Args:
        SupplierCreateUpdateDetailView (_type_): _description_
    """

    permission_required = ('storagemanagement.detail_supplier',)
#--------------------------------------------------------------------------------
class SupplierUpdateView(SupplierCreateUpdateDetailView):
    """
    SupplierUpdateView

    Args:
        SupplierCreateUpdateDetailView (_type_): _description_
    """

    permission_required = ('storagemanagement.change_supplier',)
#--------------------------------------------------------------------------------
class SupplierDeleteView(PermissionRequiredMixin,MainView):
    """
    SupplierDeleteView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.delete_supplier'

    def get(self, request, *args, **kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('supplier'):
            get_object_or_404(Supplier,slug = self.kwargs.get('supplier')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:supplier_list')
#--------------------------------------------------------------------------------
