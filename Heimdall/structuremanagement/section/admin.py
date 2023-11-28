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
from structuremanagement.section.models import Section
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name','short_form','department_id']
    search_fields = ['name',]
    list_filter = []
    list_editable = []
    ordering = []
    fieldsets = (
        (None, {'fields':(
            'department_id',
            'name',
            'short_form',
            )}),
        ('Verantwortliche', {'fields':(
            'responsible_user_id',
            'substitute_user_id',
            )}),
        ('Farbe', {'fields':(
            'rgba_red',
            'rgba_green',
            'rgba_blue',
            'rgba_alpha',
            )}),
        ('Dateien', {'fields':(
            'image_file_id',
            'process_instruction_file_id',
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