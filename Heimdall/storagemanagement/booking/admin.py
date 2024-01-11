"""
#--------------------------------------------------------------------------------
# Admin File from Model Booking
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
from storagemanagement.booking.models import Booking
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    BookingAdmin
    Settings for the Booking Admin Page
    """
    list_display = ['__str__','supplieritem','storageitem','amount']
    search_fields = []
    list_filter = []
    list_editable = []
    ordering = ['-create_datetime']
    fieldsets = (
        ("Artikel", {'fields':(
            'storageitem',
            'supplieritem',
            )}),
        ("Menge", {'fields':(
            'amount',
            )}),
        ("Preis", {'fields':(
            'price',
            )}),
        ("Bemerkung", {'fields':(
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
