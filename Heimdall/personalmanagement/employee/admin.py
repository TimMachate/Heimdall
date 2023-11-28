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
from personalmanagement.employee.models import Employee
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['reference_number','user','shortName',]
    search_fields = []
    list_filter = []
    list_editable = []
    ordering = []
    fieldsets = (
        (None, {'fields':(
            'user',
            'shortName',
            )}),
        ('Geburtsdaten', {'fields':(
            'birthday',
            'nation',
            )}),
        ('Adresse', {'fields':(
            ('street','houseNumber'),
            ('postCode','city'),
            'country',
            )}),
        ('Kontakt', {'fields':(
            'telephone',
            'email',
            )}),    
        (None, {'fields':(
            'notice',
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