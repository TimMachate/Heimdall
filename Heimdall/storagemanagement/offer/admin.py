"""
#--------------------------------------------------------------------------------
# Admin File from Model Offer
# 09.11.2023
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
    """
    OfferAdmin

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ['__str__']
    search_fields = []
    list_filter = []
    list_editable = []
    ordering = []
    fieldsets = (
        ('Dateien', {'fields':(
            'offer_file',
            )}),
        ('Anfrage', {'fields':(
            'sent',
            ('sent_datetime','sent_user_id')
            )}),
        ('Anfrage erhalten', {'fields':(
            'recived',
            ('recived_datetime','recived_user_id')
            )}),
        ('Bestellt', {'fields':(
            'ordered',
            ('ordered_datetime','ordered_user_id')
            )}),
        ('Erledigt', {'fields':(
            'done',
            )}),
    )
    inlines = [OfferDataFormsetAdmin]
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
