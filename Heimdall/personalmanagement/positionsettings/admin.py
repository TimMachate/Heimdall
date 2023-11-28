#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import admin
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from personalmanagement.positionsettings.models import PositionSettings
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(PositionSettings)
class PositionSettingsAdmin(admin.ModelAdmin):
    list_display = ['user_id',]
    search_fields = []
    list_filter = []
    list_editable = []
    ordering = []
    fieldsets = (
        (None, {'fields':(
            ('user_id'),
            )}),
        ('Urls', {'fields':(
            'api_url_overview_view',
            'api_url_list_view',
            'api_url_table_view',
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