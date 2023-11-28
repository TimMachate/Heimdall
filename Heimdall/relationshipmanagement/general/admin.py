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
from relationshipmanagement.company.admin import EmailInlineAdmin,TelephoneInlineAdmin,GeneralInlineAdmin
from relationshipmanagement.company.models import GeneralProxy
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(GeneralProxy)
class GeneralAdmin(admin.ModelAdmin):
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
    inlines = [TelephoneInlineAdmin, EmailInlineAdmin, GeneralInlineAdmin]
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