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
from structuremanagement.device.models import Device
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name',]
    list_filter = []
    list_editable = []
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            )}),
        ('Herstellerangaben', {'fields':(
            'fabricator_id',
            'fabricator_label',
            'serial_number',
            'year_of_manufacture',
            )}),
        ('Maschinenangaben', {'fields':(
            'voltage',
            'power',
            'count',
            )}),
        ('Prozesse', {'fields':(
            'processes',
            )}),
        ('Status', {'fields':(
            'status',
            )}),
        ('Fehler', {'fields':(
            'errors',
            )}),
        ('Dateien', {'fields':(
            'picture_id',
            'manuals',
            'working_instructions',
            'documents',
            )}),
    )
    filter_horizontal = ['documents','errors','manuals','processes','status','working_instructions',]

    def save_model(self, request, instance, form, change):
        user = request.user 
        instance = form.save(commit=False)
        if not change or not instance.create_user_id:
            instance.create_user_id = user
        instance.update_user_id = user
        instance.update_time = timezone.now()
        instance.save()
        form.save_m2m()
        return instance
#--------------------------------------------------------------------------------