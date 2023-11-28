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
from relationshipmanagement.company.admin import EmailInlineAdmin, TelephoneInlineAdmin,SupplierInlineAdmin
from relationshipmanagement.company.models import SupplierProxy
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(SupplierProxy)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name','notice',]
    list_filter = ['country',]
    list_editable = []
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            )}),
        ('Adresse', {'fields':(
            ('street','house_number'),
            ('post_code','city'),
            'country',
            )}),
        (None, {'fields':(
            'notice',
            )}),
    )
    inlines = [TelephoneInlineAdmin, EmailInlineAdmin, SupplierInlineAdmin]
    def save_model(self, request, instance, form, change):
        user = request.user 
        instance = form.save(commit=False)
        if not change or not instance.create_user_id:
            instance.create_user_id = user
        instance.update_user_id = user
        instance.update_datetime = timezone.now()
        instance.supplier = True
        instance.save()
        form.save_m2m()
        return instance
#--------------------------------------------------------------------------------