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
from programmmanagement.programm.models import Programm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Programm)
class ProgrammAdmin(admin.ModelAdmin):
    """
    ProgrammAdmin

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ['name','update_datetime']
    search_fields = []
    list_filter = []
    list_editable = []
    ordering = []
    fieldsets = (
        ('Allgemein', {'fields':(
            'name',
            'description'
            )}),
        ('Dateien', {'fields':(
            'htmlfile',
            )}),
        ('Benutzer', {'fields':(
            'users',
            )}),
    )
    filter_horizontal = ['users']
    def save_model(self, request, obj, form, change):
        user = request.user
        obj = form.save(commit=False)
        if not change or not obj.create_user_id:
            obj.create_user_id = user
        obj.update_user_id = user
        obj.update_datetime = timezone.now()
        obj.save()
        form.save_m2m()
        return obj
#--------------------------------------------------------------------------------
