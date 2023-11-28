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
from storagemanagement.offerdata.models import OfferData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
class OfferDataFormsetAdmin(admin.TabularInline):
    model = OfferData
    extra = 1
    min_num = 5
    fieldsets = (
        ('Artikel', {'fields':(
            'companyitem',
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
    list_display = ['__str__','offer','storageitem','companyitem','amount','authorized','done']
    search_fields = []
    list_filter = []
    list_editable = ['authorized',]
    ordering = []
    fieldsets = (
        ('Angebot', {'fields':(
            'offer',
            )}),
        ('Artikel', {'fields':(
            'companyitem',
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