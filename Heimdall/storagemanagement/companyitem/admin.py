#--------------------------------------------------------------------------------
# Admin File from Model CompanyItem
# 27.10.2023
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
from storagemanagement.companyitem.models import CompanyItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(CompanyItem)
class CompanyItemAdmin(admin.ModelAdmin):
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