"""
#--------------------------------------------------------------------------------
# Admin File from Model Supplier Contact
# 30.12.2023
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
from storagemanagement.storagemanagementusersetting.suppliercontact.models import (
    StorageManagementSupplierContactOverviewUserSetting,
    StorageManagementSupplierContactListUserSetting,
    StorageManagementSupplierContactTableUserSetting,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(StorageManagementSupplierContactOverviewUserSetting)
class StorageManagementSupplierContactOverviewUserSettingAdmin(admin.ModelAdmin):
    """
    StorageManagementSupplierContactOverviewUserSettingAdmin

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
@admin.register(StorageManagementSupplierContactListUserSetting)
class StorageManagementSupplierContactListUserSettingAdmin(admin.ModelAdmin):
    """
    StorageManagementSupplierContactListUserSettingAdmin

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
@admin.register(StorageManagementSupplierContactTableUserSetting)
class StorageManagementSupplierContactTableUserSettingAdmin(admin.ModelAdmin):
    """
    StorageManagementSupplierContactTableUserSettingAdmin

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
