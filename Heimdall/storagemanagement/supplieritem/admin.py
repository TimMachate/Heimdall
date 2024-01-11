"""
#--------------------------------------------------------------------------------
# Admin File from Model SupplierItem
# 27.10.2023
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
from storagemanagement.supplieritem.models import SupplierItem,SupplierItemBaseModel
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
class SupplierItemBaseAdmin(admin.StackedInline):
    """
    SupplierItemBaseAdmin

    Args:
        admin (_type_): _description_
    """
    extra = 0
    fieldsets = (
        ('Angebot', {'fields':(
            'storageitem',
            )}),
    )
    filter_horizontal = []
    min_num = 1
    model = SupplierItemBaseModel
#--------------------------------------------------------------------------------
@admin.register(SupplierItem)
class SupplierItemAdmin(admin.ModelAdmin):
    """
    SupplierItemAdmin

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
            'storageitem',
            )}),
    )
    inlines = [SupplierItemBaseAdmin]
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
