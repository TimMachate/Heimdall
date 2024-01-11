"""
#--------------------------------------------------------------------------------
# Admin File from Model Request
# 10.11.2023
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
from storagemanagement.requestdata.models import RequestData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(RequestData)
class RequestDataAdmin(admin.ModelAdmin):
    """
    RequestDataAdmin

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ['__str__','storageitem','supplieritem','amount','authorized','done']
    search_fields = []
    list_filter = []
    list_editable = ['authorized','done']
    ordering = []
    fieldsets = (
        ('Artikel', {'fields':(
            'storageitem',
            'supplieritem',
            )}),
        ('Daten', {'fields':(
            'amount',
            ('authorized','done')
            )}),
    )
    inlines = []
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.create_user_id:
            instance.create_user_id = user
        instance.update_user_id = user
        instance.update_datetime = timezone.now()
        instance.save()
        form.save_m2m()
        return instance
#--------------------------------------------------------------------------------
