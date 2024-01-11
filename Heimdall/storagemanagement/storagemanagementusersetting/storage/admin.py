"""
#--------------------------------------------------------------------------------
# Admin File from Model Supplier
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
from storagemanagement.storagemanagementusersetting.storage.models import (
    StorageManagementStorageOverviewUserSetting,
    StorageManagementStorageListUserSetting,
    StorageManagementStorageTableUserSetting,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(StorageManagementStorageOverviewUserSetting)
class StorageManagementStorageOverviewUserSettingAdmin(admin.ModelAdmin):
    """
    StorageManagementStorageOverviewUserSettingAdmin

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
@admin.register(StorageManagementStorageListUserSetting)
class StorageManagementStorageListUserSettingAdmin(admin.ModelAdmin):
    """
    StorageManagementStorageListUserSettingAdmin

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
@admin.register(StorageManagementStorageTableUserSetting)
class StorageManagementStorageTableUserSettingAdmin(admin.ModelAdmin):
    """
    StorageManagementStorageTableUserSettingAdmin

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
