from django.contrib import admin
from django.utils import timezone

from visualisation.models import Tab

@admin.register(Tab)
class TabAdmin(admin.ModelAdmin):
    list_display = ['name','user','create_user','create_time','update_user','update_time','order']
    search_fields = ['name',]
    list_filter = ['user']
    list_editable = ['order',]
    ordering = ['user', 'order', 'name']
    filter_horizontal = []
    radio_fields = {}

    def save_model(self, request, instance, form, change):
        if not instance.create_user:
            instance.create_user = request.user
        if not instance.create_time:
            instance.create_time = timezone.now()
        instance.update_user = request.user
        instance.update_time = timezone.now()
        return super().save_model(request, instance, form, change = True)