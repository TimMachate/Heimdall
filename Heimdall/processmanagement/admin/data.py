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
from processmanagement.models.data import Data
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['commission','statusreport','defect','createTime','createUser',]
    search_fields = []
    list_filter = ['statusreport']
    list_editable = []
    ordering = ['-createTime',]
    fieldsets = (
        (None, {'fields':(
            'commission',
            'statusreport',
            'defect',
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