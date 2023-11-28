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
from processmanagement.models.defect import Defect
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Defect)
class DefectAdmin(admin.ModelAdmin):
    list_display = ['name','createTime','createUser','updateTime','updateUser',]
    search_fields = ['name']
    list_filter = []
    list_editable = []
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            )}),
    )
    filter_horizontal = []
    radio_fields = {}
    def save_model(self, request, instance, form, change):
        user = request.user 
        instance = form.save(commit=False)
        if not change or not instance.createUser:
            instance.createUser = user
        instance.updateUser = user
        instance.updateTime = timezone.now()
        instance.save()
        form.save_m2m()
        return instance
#--------------------------------------------------------------------------------