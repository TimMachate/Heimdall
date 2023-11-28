#--------------------------------------------------------------------------------
# Admin File from Model Order
# 15.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

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
from storagemanagement.order.models import Order
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
from storagemanagement.orderdata.admin import OrderDataFormsetAdmin
#--------------------------------------------------------------------------------
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = []
    list_filter = []
    list_editable = []
    ordering = []
    fieldsets = (
        ('Dateien', {'fields':(
            'order_file',
            'delivery_note',
            )}),
        ('Bestellt', {'fields':(
            'sent',
            ('sent_datetime','sent_user_id')
            )}),
        ('Erhalten', {'fields':(
            'recived',
            ('recived_datetime','recived_user_id')
            )}),
        ('Erledigt', {'fields':(
            'done',
            )}),
    )
    inlines = [OrderDataFormsetAdmin]
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