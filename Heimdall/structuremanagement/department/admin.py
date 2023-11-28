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
from structuremanagement.department.models import Department
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['reference_number','name','responsible_employee_id','substitute_employee_id','rgba_value']
    search_fields = ['name',]
    list_filter = []
    list_editable = []
    ordering = []
    fieldsets = (
        (None, {'fields':(
            'name',
            )}),
        ('Verantwortliche', {'fields':(
            'responsible_employee_id',
            'substitute_employee_id',
            )}),
        ('Farbe', {'fields':(
            'rgba_red',
            'rgba_green',
            'rgba_blue',
            'rgba_alpha',
            )}),
        ('Dateien', {'fields':(
            'picture_file_id',
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
        instance.save()
        form.save_m2m()
        return instance
#--------------------------------------------------------------------------------