"""
#--------------------------------------------------------------------------------
# Admin File from Model StorageItem
# 15.10.2023
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
from storagemanagement.storageitem.models import StorageItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(StorageItem)
class StorageItemAdmin(admin.ModelAdmin):
    """
    StorageItemAdmin

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ['__str__','minimum','warning','maximum']
    search_fields = ['name']
    list_filter = []
    list_editable = ['minimum','warning','maximum']
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            )}),
        ('Standardartikel', {'fields':(
            'supplieritem',
            )}),
        ('Bestand', {'fields':(
            ('minimum','warning','maximum')
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
