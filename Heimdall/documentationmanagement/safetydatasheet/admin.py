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
from documentationmanagement.safetydatasheet.models import SafetyDataSheet
from documentationmanagement.file.models import File, SafetyDataSheetProxy
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Admins
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
class SafetyDataSheetInlineAdmin(admin.StackedInline):
    model = SafetyDataSheet
    max_num = 1
    fieldsets = (
        ("Nächste Aktualisierung",{"fields":(
            "actualization",
            "warning",
        )}),
    )

@admin.register(SafetyDataSheetProxy)
class SafetyDataSheetAdmin(admin.ModelAdmin):
    list_display = ['reference_number','name','version_prefix','version_suffix']
    search_fields = ['name']
    list_filter = []
    list_editable = []
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            'version_prefix',
            )}),
        (None, {'fields':(
            'file',
            )}),
        ('Beschreibung', {'fields':(
            'keywords',
        )}),
    )

    inlines = [SafetyDataSheetInlineAdmin]
    filter_horizontal = []
    radio_fields = {}
    def save_model(self, request, instance, form, change):
        user = request.user
        instance.type=instance.Types.SAFETYDATASHEET
        instance = form.save(commit=False)
        if not change or not instance.create_user_id:
            instance.create_user_id = user
        instance.update_user_id = user
        instance.update_datetime = timezone.now()
        instance.save()
        form.save_m2m()
        return instance
#--------------------------------------------------------------------------------