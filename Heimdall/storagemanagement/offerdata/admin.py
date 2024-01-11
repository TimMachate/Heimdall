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
from storagemanagement.offerdata.models import OfferData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
class OfferDataFormsetAdmin(admin.TabularInline):
    """
    OfferDataFormsetAdmin

    Args:
        admin (_type_): _description_
    """
    model = OfferData
    extra = 1
    min_num = 5
    fieldsets = (
        ('Artikel', {'fields':(
            'supplieritem',
            )}),
        ('Daten', {'fields':(
            'amount',
            'price',
            )}),
        ('Autorisiert', {'fields':(
            'authorized',
            ('authorized_datetime','authorized_user_id')
            )}),
        ('Erledigt', {'fields':(
            'done',
            )}),
    )

@admin.register(OfferData)
class OfferDataAdmin(admin.ModelAdmin):
    """
    OfferDataAdmin

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ['__str__','offer','storageitem','supplieritem','amount','authorized','done']
    search_fields = []
    list_filter = []
    list_editable = ['authorized',]
    ordering = []
    fieldsets = (
        ('Angebot', {'fields':(
            'offer',
            )}),
        ('Artikel', {'fields':(
            'supplieritem',
            )}),
        ('Daten', {'fields':(
            'amount',
            'price',
            )}),
        ('Daten', {'fields':(
            'authorized',
            ('authorized_datetime','authorized_user_id'),
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
