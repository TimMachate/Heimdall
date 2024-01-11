"""
#--------------------------------------------------------------------------------
# Admin File from Model Company
# 16.12.2023
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
from relationshipmanagement.relationshipmanagementusersetting.models import (
    RelationshipManagementCompanyListUserSetting,
    RelationshipManagementCompanyTableUserSetting,
    RelationshipManagementCompanyContactListUserSetting,
    RelationshipManagementCompanyContactTableUserSetting,
    RelationshipManagementCompanyItemListUserSetting,
    RelationshipManagementCompanyItemTableUserSetting,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(RelationshipManagementCompanyListUserSetting)
class RelationshipManagementCompanyListUserSettingAdmin(admin.ModelAdmin):
    """
    RelationshipManagementListUserSettingAdmin

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
@admin.register(RelationshipManagementCompanyTableUserSetting)
class RelationshipManagementCompanyTableUserSettingAdmin(admin.ModelAdmin):
    """
    RelationshipManagementTableUserSettingAdmin

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
@admin.register(RelationshipManagementCompanyContactListUserSetting)
class RelationshipManagementCompanyContactListUserSettingAdmin(admin.ModelAdmin):
    """
    RelationshipManagementCompanyContactListUserSettingAdmin

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
@admin.register(RelationshipManagementCompanyContactTableUserSetting)
class RelationshipManagementCompanyContactTableUserSettingAdmin(admin.ModelAdmin):
    """
    RelationshipManagementCompanyContactTableUserSettingAdmin

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
@admin.register(RelationshipManagementCompanyItemListUserSetting)
class RelationshipManagementCompanyItemListUserSettingAdmin(admin.ModelAdmin):
    """
    RelationshipManagementCompanyItemListUserSettingAdmin

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
@admin.register(RelationshipManagementCompanyItemTableUserSetting)
class RelationshipManagementCompanyItemTableUserSettingAdmin(admin.ModelAdmin):
    """
    RelationshipManagementCompanyItemTableUserSettingAdmin

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
