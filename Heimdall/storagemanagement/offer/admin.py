#--------------------------------------------------------------------------------
# Admin File from Model Offer
# 09.11.2023
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
from storagemanagement.offer.models import Offer
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
from storagemanagement.offerdata.admin import OfferDataFormsetAdmin
#--------------------------------------------------------------------------------
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = []
    list_filter = []
    list_editable = []
    ordering = []
    fieldsets = (
        ('Dateien', {'fields':(
            'offer_file',
            )}),
        ('Berechtigungen', {'fields':(
            'sent',
            ('sent_datetime','sent_user_id')
            )}),
        ('Berechtigungen', {'fields':(
            'recived',
            ('recived_datetime','recived_user_id')
            )}),
        ('Berechtigungen', {'fields':(
            'ordered',
            ('ordered_datetime','ordered_user_id')
            )}),
        ('Erledigt', {'fields':(
            'done',
            )}),
    )
    inlines = [OfferDataFormsetAdmin]
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