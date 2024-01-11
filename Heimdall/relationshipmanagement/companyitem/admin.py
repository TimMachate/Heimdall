"""
#--------------------------------------------------------------------------------
# Admin File from Model CompanyItem
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
from relationshipmanagement.companyitem.models import CompanyItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(CompanyItem)
class CompanyItemAdmin(admin.ModelAdmin):
    """
    CompanyItemAdmin

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ['__str__','company','unit','price']
    search_fields = ['name']
    list_filter = ['company',]
    list_editable = []
    ordering = ['company__name','name']
    fieldsets = (
        ('Firma', {'fields':(
            'company',
            )}),
        ('Bild', {'fields':(
            'image',
            )}),
        ('Name', {'fields':(
            'name',
            'item_number',
            )}),
        (None, {'fields':(
            ('unit','price'),
            #'storageitem',
            )}),
    )
    inlines = []
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
