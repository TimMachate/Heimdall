"""
#--------------------------------------------------------------------------------
# Admin File from Model CompanyContact
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
from relationshipmanagement.companycontact.models import (
    CompanyContact,
    CompanyContactEmail,
    CompanyContactTelephone
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
class EmailInlineAdmin(admin.StackedInline):
    """
    EmailInlineAdmin

    Args:
        admin (_type_): _description_
    """
    model = CompanyContactEmail
    extra = 1
#--------------------------------------------------------------------------------
class TelephoneInlineAdmin(admin.StackedInline):
    """
    TelephoneInlineAdmin

    Args:
        admin (_type_): _description_
    """
    model = CompanyContactTelephone
    extra = 1
    fieldsets=(
        (None,{'fields':(
            ('types','number'),
        )}),
    )
#--------------------------------------------------------------------------------
@admin.register(CompanyContact)
class CompanyContactAdmin(admin.ModelAdmin):
    """
    CompanyContactAdmin

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ['last_name','company']
    search_fields = []
    list_filter = ['company',]
    list_editable = []
    ordering = ['company','last_name','first_name']
    fieldsets = (
        (None, {'fields':(
            'company',
            )}),
        ('Name', {'fields':(
            'last_name',
            'first_name',
            )}),
        (None, {'fields':(
            'notice',
            )}),
    )
    inlines = [EmailInlineAdmin,TelephoneInlineAdmin]
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
