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
from structuremanagement.maintenance.models import Maintenance
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ['reference_number','device_id','name','protocol_id',]
    search_fields = ['name',]
    list_filter = []
    list_editable = []
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'device_id',
            'name',
            'protocol_id',
            )}),
        ('Wiederholung', {'fields':(
            ('repetition_days','repetition_hours','repetition_minutes','repetition_seconds'),
            )}),
        ('Warnung', {'fields':(
            ('warning_days','warning_hours','warning_minutes','warning_seconds'),
            )}),
    )
    filter_horizontal = []

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