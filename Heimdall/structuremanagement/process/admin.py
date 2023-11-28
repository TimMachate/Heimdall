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
from structuremanagement.process.models import Process, ProcessData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]
    list_filter = []
    list_editable = []
    ordering = []
    fieldsets = (
        (None, {'fields':(
            'name',
            )}),
        ('Dauer', {'fields':(
            ('duration_days','duration_hours','duration_minutes','duration_seconds'),
            )}),
        ('Dateien', {'fields':(
            'picture_id',
            'technical_data_sheet_id',
            )}),
    )
    filter_horizontal = []
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
@admin.register(ProcessData)
class ProcessDataAdmin(admin.ModelAdmin):
    list_display = ['reference_number','device_id','process_id','begin_datetime','end_datetime','count']
    search_fields = ['device_id','process_id']
    list_filter = []
    list_editable = []
    ordering = ['-id']
    fieldsets = (
        (None, {'fields':(
            'device_id',
            'process_id',
            'count',
            )}),
        ('Zeiten', {'fields':(
            ('begin_datetime','begin_user_id'),
            ('end_datetime','end_user_id'),
            )}),
        ('Dateien', {'fields':(
            'protocol_id',
            )}),
    )
    filter_horizontal = []
    inlines = []

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.create_user_id:
            instance.create_user_id = user
        instance.update_user_id = user
        instance.save()
        form.save_m2m()
        return instance
#--------------------------------------------------------------------------------