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
from relationshipmanagement.ware.models import Ware
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Ware)
class WareAdmin(admin.ModelAdmin):
    list_display = ['company_id','name','ware_number','unit','price']
    search_fields = []
    list_filter = ['name',]
    list_editable = []
    ordering = ['name',]
    fieldsets = (
        ('Firma', {'fields':(
            'company_id',
            )}),
        ('Bild', {'fields':(
            'image_id',
            )}),
        ('Name', {'fields':(
            'name',
            'ware_number',
            )}),
        (None, {'fields':(
            ('unit','unit_package'),
            'price',
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