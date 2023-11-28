#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import admin
from django.db import models
from django.utils import timezone
from tinymce.widgets import TinyMCE
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from structuremanagement.position.models import Position
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name',]
    list_filter = []
    list_editable = []
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'section_id',
            'name',
            'description',
            )}),
        ('Verantwortliche', {'fields':(
            'responsible_employee_id',
            'substitute_employee_id',
            )}),
        ('Dateien', {'fields':(
            'working_description_id',
            'working_instructions',
            'directions',
            'safety_data_sheets',
            'documents'
            )}),
    )

    filter_horizontal = ['working_instructions','directions','safety_data_sheets','documents']

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