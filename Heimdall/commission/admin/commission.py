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
from commission.models.commission import Commission
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ['name','sos','ticket','done','createTime','createUser','updateTime','updateUser',]
    search_fields = ['name']
    list_filter = []
    list_editable = ['sos','ticket','done']
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            'sos',
            'ticket',
            'done'
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