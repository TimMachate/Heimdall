#--------------------------------------------------------------------------------
# Admin File from Model Storage
# 03.11.2023
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
from storagemanagement.storage.models import Storage
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ['slug','companyitem','booking','unload_user_id', 'unload_datetime']
    search_fields = []
    list_filter = []
    list_editable = []
    ordering = ['-create_datetime']
    fieldsets = (
        ("Artikel", {'fields':(
            'companyitem',
            )}),
        ("Buchung", {'fields':(
            'booking',
            )}),
        ("Entnahme", {'fields':(
            'unload_user_id',
            'unload_datetime',
            )}),
        ("Menge", {'fields':(
            'notice',
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