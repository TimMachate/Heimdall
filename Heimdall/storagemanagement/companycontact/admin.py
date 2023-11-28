#--------------------------------------------------------------------------------
# Admin File from Model CompanyContact
# 28.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

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
from storagemanagement.companycontact.models import CompanyContact,CompanyContactEmail,CompanyContactTelephone
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
class EmailInlineAdmin(admin.StackedInline):
    model = CompanyContactEmail
    extra = 1
#--------------------------------------------------------------------------------
class TelephoneInlineAdmin(admin.StackedInline):
    model = CompanyContactTelephone
    extra = 1
    fieldsets=(
        (None,{'fields':(
            ('types','number'),
        )}),
    )
#--------------------------------------------------------------------------------
@admin.register(CompanyContact)
class CompanyContactAdmin(admin.ModelAdmin):
    list_display = ['last_name','company']
    search_fields = []
    list_filter = ['company',]
    list_editable = []
    ordering = ['company','last_name','first_name']
    fieldsets = (
        (None, {'fields':(
            'company',
            )}),
        ('Name', {'fields':(
            'last_name',
            'first_name',
            )}),
        (None, {'fields':(
            'notice',
            )}),
    )
    inlines = [EmailInlineAdmin,TelephoneInlineAdmin]
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