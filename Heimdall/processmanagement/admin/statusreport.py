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
from processmanagement.models.statusreport import StatusReport
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(StatusReport)
class StatusReportAdmin(admin.ModelAdmin):
    list_display = ['name','startRunThrough','updateTime','updateUser',]
    search_fields = ['name']
    list_filter = []
    list_editable = ['startRunThrough',]
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            'defects',
            'startRunThrough',
            )}),
    )
    filter_horizontal = ['defects']
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