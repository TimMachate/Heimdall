"""
#--------------------------------------------------------------------------------
# View File from Model StorageItem
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
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.storageitem.models import StorageItem
from storagemanagement.storagemanagementusersetting.storageitem.models import (
    StorageManagementStorageItemOverviewUserSetting,
    StorageManagementStorageItemListUserSetting,
    StorageManagementStorageItemTableUserSetting
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.storageitem.forms import StorageItemForm
from storagemanagement.storagemanagementusersetting.storageitem.forms import (
    StorageManagementStorageItemOverviewUserSettingForm,
    StorageManagementStorageItemListUserSettingForm,
    StorageManagementStorageItemTableUserSettingForm
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class StorageItemBaseView(PermissionRequiredMixin,MainView):
    """
    StorageItemBaseView

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

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains all context data
        """
        super().get_context_data(**kwargs)
        self.context['model'] = 'storageitem'
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
            queryset: contains one supplier
        """
        if self.kwargs.get('storageitem'):
            queryset = StorageItem.objects.get(slug=self.kwargs.get('storageitem'))
        else:
            queryset = StorageItem.objects.all()
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
class StorageItemView(StorageItemBaseView):
    """
    StorageItemView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.view_storageitem'

    template_name = 'storageitem_overview.html'

    form_setting = StorageManagementStorageItemOverviewUserSettingForm
    model_setting = StorageManagementStorageItemOverviewUserSetting
#--------------------------------------------------------------------------------
class StorageItemListView(StorageItemBaseView):
    """
    StorageItemListView

    Args:
        StorageItemView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.list_storageitem'

    template_name = 'storageitem_list.html'

    form_setting = StorageManagementStorageItemListUserSettingForm
    model_setting = StorageManagementStorageItemListUserSetting
#--------------------------------------------------------------------------------
class StorageItemTableView(StorageItemBaseView):
    """
    StorageItemTableView

    Args:
        StorageItemView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.table_storageitem'

    template_name = 'storageitem_table.html'

    form_setting = StorageManagementStorageItemTableUserSettingForm
    model_setting = StorageManagementStorageItemTableUserSetting
#--------------------------------------------------------------------------------
class StorageItemCreateUpdateDetailView(StorageItemBaseView):
    """
    StorageItemCreateUpdateDetailView

    Args:
        StorageItemView (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name = 'storageitem_createupdatedetail.html'

    form_class = StorageItemForm

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
            form.save_m2m()
        self.context['form'] = form

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:storageitem_update', storageitem=obj.slug)

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset

        Returns:
            queryset: contains one supplier
        """
        if self.kwargs.get('storageitem'):
            queryset = StorageItem.objects.get(slug=self.kwargs.get('storageitem'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class StorageItemCreateView(StorageItemCreateUpdateDetailView):
    """
    StorageItemCreateView

    Args:
        StorageItemCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.add_storageitem',)
#--------------------------------------------------------------------------------
class StorageItemDetailView(StorageItemCreateUpdateDetailView):
    """
    StorageItemDetailView

    Args:
        StorageItemCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.detail_storageitem',)
#--------------------------------------------------------------------------------
class StorageItemUpdateView(StorageItemCreateUpdateDetailView):
    """
    StorageItemUpdateView

    Args:
        StorageItemCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.change_storageitem',)
#--------------------------------------------------------------------------------
class StorageItemDeleteView(PermissionRequiredMixin,MainView):
    """
    StorageItemDeleteView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.delete_storageitem'

    def get(self, request, *args, **kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('storageitem'):
            get_object_or_404(StorageItem,slug = self.kwargs.get('storageitem')).delete()
            messages.success(request,'StorageItem wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'StorageItem konnte nicht gelöscht werden!')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:storageitem_list')
#--------------------------------------------------------------------------------
