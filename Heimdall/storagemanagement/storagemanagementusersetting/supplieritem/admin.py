"""
#--------------------------------------------------------------------------------
# Admin File from Model Supplier
# 06.01.2024
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import admin
from django.utils import timezone
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.storagemanagementusersetting.supplieritem.models import (
    StorageManagementSupplierItemOverviewUserSetting,
    StorageManagementSupplierItemListUserSetting,
    StorageManagementSupplierItemTableUserSetting,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(StorageManagementSupplierItemOverviewUserSetting)
class StorageManagementSupplierItemOverviewUserSettingAdmin(admin.ModelAdmin):
    """
    StorageManagementSupplierItemOverviewUserSettingAdmin

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ['user','update_datetime','update_user_id']
    ordering = ['user',]
    inlines = [

    ]
    def save_model(self, request, obj, form, change):
        user = request.user
        obj = form.save(commit=False)
        if not change or not obj.create_user_id:
            obj.create_user_id = user
        obj.update_user_id = user
        obj.update_datetime = timezone.now()
        obj.save()
        form.save_m2m()
        return obj
#--------------------------------------------------------------------------------
@admin.register(StorageManagementSupplierItemListUserSetting)
class StorageManagementSupplierItemListUserSettingAdmin(admin.ModelAdmin):
    """
    StorageManagementSupplierItemListUserSettingAdmin

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ['user','update_datetime','update_user_id']
    ordering = ['user',]
    inlines = [

    ]
    def save_model(self, request, obj, form, change):
        user = request.user
        obj = form.save(commit=False)
        if not change or not obj.create_user_id:
            obj.create_user_id = user
        obj.update_user_id = user
        obj.update_datetime = timezone.now()
        obj.save()
        form.save_m2m()
        return obj
#--------------------------------------------------------------------------------
@admin.register(StorageManagementSupplierItemTableUserSetting)
class StorageManagementSupplierItemTableUserSettingAdmin(admin.ModelAdmin):
    """
    StorageManagementSupplierItemTableUserSettingAdmin

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ['user','update_datetime','update_user_id']
    ordering = ['user',]
    inlines = [

    ]
    def save_model(self, request, obj, form, change):
        user = request.user
        obj = form.save(commit=False)
        if not change or not obj.create_user_id:
            obj.create_user_id = user
        obj.update_user_id = user
        obj.update_datetime = timezone.now()
        obj.save()
        form.save_m2m()
        return obj
#--------------------------------------------------------------------------------
