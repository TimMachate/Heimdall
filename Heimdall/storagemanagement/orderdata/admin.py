"""
#--------------------------------------------------------------------------------
# Admin File from Model Order Data
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
from storagemanagement.orderdata.models import OrderData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
class OrderDataFormsetAdmin(admin.TabularInline):
    """
    OrderDataFormsetAdmin

    Args:
        admin (_type_): _description_
    """
    model = OrderData
    extra = 1
    min_num = 5
    fieldsets = (
        ('Artikel', {'fields':(
            'supplieritem',
            )}),
        ('Angebot', {'fields':(
            'offer',
            )}),
        ('Daten', {'fields':(
            ('amount','amount_recived'),
            'price',
            )}),
        ('Autorisiert', {'fields':(
            'authorized',
            ('authorized_datetime','authorized_user_id')
            )}),
        ('Buchung', {'fields':(
            'booking',
            ('booking_datetime','booking_user_id')
            )}),
        ('Erledigt', {'fields':(
            'done',
            )}),
    )

@admin.register(OrderData)
class OrderDataAdmin(admin.ModelAdmin):
    """
    OrderDataAdmin

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ['__str__','order','amount','authorized','booking','done']
    search_fields = []
    list_filter = []
    list_editable = ['authorized','booking','done']
    ordering = []
    fieldsets = (
        ('Bestellung', {'fields':(
            'order',
            )}),
        ('Artikel', {'fields':(
            'supplieritem',
            )}),
        ('Daten', {'fields':(
            ('amount','amount_recived'),
            'price',
            )}),
        ('Autorisiert', {'fields':(
            'authorized',
            ('authorized_datetime','authorized_user_id')
            )}),
        ('Buchung', {'fields':(
            'booking',
            ('booking_datetime','booking_user_id')
            )}),
        ('Erledigt', {'fields':(
            'done',
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
