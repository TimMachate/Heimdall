"""
#--------------------------------------------------------------------------------
# Views File from Model SupplierItem
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.supplier.models import Supplier
from storagemanagement.supplieritem.models import SupplierItem
from storagemanagement.storagemanagementusersetting.supplieritem.models import (
    StorageManagementSupplierItemOverviewUserSetting,
    StorageManagementSupplierItemListUserSetting,
    StorageManagementSupplierItemTableUserSetting
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.supplieritem.forms import SupplierItemForm
from storagemanagement.storagemanagementusersetting.supplieritem.forms import (
    StorageManagementSupplierItemOverviewUserSettingForm,
    StorageManagementSupplierItemListUserSettingForm,
    StorageManagementSupplierItemTableUserSettingForm
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class SupplierItemBaseView(PermissionRequiredMixin, MainView):
    """
    SupplierItemBaseView

    Args:
        PermissionRequiredMixin (class): permission class
        MainView (class): main class of the app

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

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains all context data
        """
        super().get_context_data(**kwargs)
        self.context['model'] = 'supplieritem'
        # Urls
        if self.kwargs.get('supplier'):
            self.context['url_overview'] = reverse(
                'storagemanagement:supplier_supplieritem_overview',
                kwargs={'supplier':self.kwargs.get('supplier')}
            )
            self.context['url_list'] = reverse(
                'storagemanagement:supplier_supplieritem_list',
                kwargs={'supplier':self.kwargs.get('supplier')}
            )
            self.context['url_table'] = reverse(
                'storagemanagement:supplier_supplieritem_table',
                kwargs={'supplier':self.kwargs.get('supplier')}
            )
            self.context['url_create'] = reverse(
                'storagemanagement:supplier_supplieritem_create',
                kwargs={'supplier':self.kwargs.get('supplier')}
            )
        else:
            self.context['url_overview'] = reverse('storagemanagement:supplieritem_overview')
            self.context['url_list'] = reverse('storagemanagement:supplieritem_list')
            self.context['url_table'] = reverse('storagemanagement:supplieritem_table')
            self.context['url_create'] = reverse('storagemanagement:supplieritem_create')
        # Setting
        if self.model_setting and self.form_setting:
            self.context["form_setting_queryset"] = self.model_setting.objects.get_or_create(
                user=self.request.user
            )[0]
            if self.kwargs.get('supplier'):
                self.context["supplier"] = self.kwargs.get('supplier')
            else:
                self.context["supplier"] = ""
            # Data Url
            self.context["api_data_url"] = self.get_url_api(
                queryset=self.context["form_setting_queryset"],
                supplier=self.context["supplier"]
            )
            # Form
            self.context["form_setting"] = self.form_setting(
                instance = self.context["form_setting_queryset"]
            )
        else:
            self.context["supplier"] = None
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
            queryset: contains all supplier items
        """
        if self.kwargs.get('supplieritem'):
            queryset = SupplierItem.objects.get(slug = self.kwargs.get('supplieritem'))
        elif self.kwargs.get('supplier'):
            queryset = SupplierItem.objects.filter(company__slug = self.kwargs.get('supplier'))
        else:
            queryset = SupplierItem.objects.all()
        return queryset

    def get_url_api(self,queryset,supplier):
        """
        get_url_api

        Returns:
            string: url to api
        """
        url = queryset.api_url()+f"&company__slug={supplier}"
        return url
#--------------------------------------------------------------------------------
class SupplierItemView(SupplierItemBaseView):
    """
    SupplierItemView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.view_supplieritem'

    template_name = 'storagemanagement_supplieritem_overview.html'

    form_setting = StorageManagementSupplierItemOverviewUserSettingForm
    model_setting = StorageManagementSupplierItemOverviewUserSetting
#--------------------------------------------------------------------------------
class SupplierItemListView(SupplierItemBaseView):
    """
    SupplierItemListView

    Args:
        SupplierItemView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.list_supplieritem'

    template_name = 'storagemanagement_supplieritem_list.html'

    form_setting = StorageManagementSupplierItemListUserSettingForm
    model_setting = StorageManagementSupplierItemListUserSetting
#--------------------------------------------------------------------------------
class SupplierItemTableView(SupplierItemBaseView):
    """
    SupplierItemTableView

    Args:
        SupplierItemView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.table_supplieritem'

    template_name = 'storagemanagement_supplieritem_table.html'

    form_setting = StorageManagementSupplierItemTableUserSettingForm
    model_setting = StorageManagementSupplierItemTableUserSetting
#--------------------------------------------------------------------------------
class SupplierItemCreateUpdateDetailView(SupplierItemBaseView):
    """
    SupplierItemCreateUpdateDetailView

    Args:
        SupplierItemView (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name = 'storagemanagement_supplieritem_createupdatedetail.html'

    form_class = SupplierItemForm

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
        self.context['form'] = self.form_class(
            instance=self.context['queryset']
        )
        if self.get_initial():
            self.context['form'].initial = self.get_initial()
        return render(request, self.template_name, self.context)

    def get_initial(self):
        """
        get_initial

        Returns:
            dict: contains all initial data
        """
        result = {}
        if self.kwargs.get('supplier'):
            result['company'] = Supplier.objects.get(slug=self.kwargs.get('supplier'))
        if not result:
            result = None
        return result

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
            obj.save()
        self.context['form'] = form

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:supplieritem_update', supplieritem=obj.slug)

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset

        Returns:
            queryset: contains all supplier items
        """
        if self.kwargs.get('supplieritem'):
            queryset = SupplierItem.objects.get(slug = self.kwargs.get('supplieritem'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class SupplierItemCreateView(SupplierItemCreateUpdateDetailView):
    """
    SupplierItemCreateView

    Args:
        SupplierItemCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.add_supplieritem',)
#--------------------------------------------------------------------------------
class SupplierItemDetailView(SupplierItemCreateUpdateDetailView):
    """
    SupplierItemDetailView

    Args:
        SupplierItemCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.detail_supplieritem',)
#--------------------------------------------------------------------------------
class SupplierItemUpdateView(SupplierItemCreateUpdateDetailView):
    """
    SupplierItemUpdateView

    Args:
        SupplierItemCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.update_supplieritem',)
#--------------------------------------------------------------------------------
class SupplierItemDeleteView(PermissionRequiredMixin, MainView):
    """
    SupplierItemDeleteView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.delete_supplieritem'

    def get(self, request, *args, **kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('supplieritem'):
            get_object_or_404(SupplierItem, slug = self.kwargs.get('supplieritem')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:supplieritem_list')
#--------------------------------------------------------------------------------
