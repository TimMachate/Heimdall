"""
#--------------------------------------------------------------------------------
# Admin File from Model Storage
# 03.11.2023
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
from storagemanagement.storage.models import Storage
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    """
    StorageAdmin

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ['slug','supplieritem','booking','unload','unload_user_id', 'unload_datetime']
    search_fields = []
    list_filter = []
    list_editable = ['unload']
    ordering = ['-create_datetime']
    fieldsets = (
        ("Artikel", {'fields':(
            'supplieritem',
            )}),
        ("Buchung", {'fields':(
            'booking',
            )}),
        ("Entnahme", {'fields':(
            'unload',
            'unload_user_id',
            'unload_datetime',
            )}),
        ("Menge", {'fields':(
            'notice',
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
