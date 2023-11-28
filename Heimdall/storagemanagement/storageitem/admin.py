#--------------------------------------------------------------------------------
# Admin File from Model StorageItem
# 15.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models

from django.apps import apps
from django.contrib import admin
from django.utils import timezone
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.storageitem.models import StorageItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(StorageItem)
class StorageItemAdmin(admin.ModelAdmin):
    list_display = ['__str__','minimum','warning','maximum']
    search_fields = ['name']
    list_filter = []
    list_editable = ['minimum','warning','maximum']
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            )}),
        ('Standardartikel', {'fields':(
            'companyitem',
            )}),
        ('Bestand', {'fields':(
            ('minimum','warning','maximum')
            )}),
    )
    inlines = []
    def save_model(self, request, instance, form, change):
        user = request.user 
        instance = form.save(commit=False)
        if not change or not instance.create_user_id:
            instance.create_user_id = user
        instance.update_user_id = user
        instance.update_datetime = timezone.now()
        instance.save()
        form.save_m2m()
        return instance
#--------------------------------------------------------------------------------