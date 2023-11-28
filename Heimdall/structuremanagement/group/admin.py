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
from structuremanagement.group.models import Group
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]
    list_filter = []
    list_editable = []
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            'description',
            'devices',
            )}),
    )
    filter_horizontal = ['devices',]
    inlines = []

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