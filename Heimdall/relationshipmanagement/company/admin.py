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
from relationshipmanagement.company.models import Company, Email, Telephone
from relationshipmanagement.customer.models import Customer
from relationshipmanagement.general.models import General
from relationshipmanagement.supplier.models import Supplier
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
class CustomerInlineAdmin(admin.StackedInline):
    model = Customer
    extra = 0
    max_num = 1
    fieldsets = (
        (None, {'fields':(
            'company_id',
            'status',
            )}),
    )
#--------------------------------------------------------------------------------
class EmailInlineAdmin(admin.StackedInline):
    model = Email
    extra = 0
    fieldsets = [(None, {'fields':(('email','target'))})]
#--------------------------------------------------------------------------------
class GeneralInlineAdmin(admin.StackedInline):
    model = General
    extra = 0
    max_num = 1
    fieldsets = (
        (None, {'fields':(
            'company_id',
            )}),
    )
#--------------------------------------------------------------------------------
class SupplierInlineAdmin(admin.StackedInline):
    model = Supplier
    extra = 0
    max_num = 1
    fieldsets = (
        (None, {'fields':(
            'company_id',
            )}),
    )
#--------------------------------------------------------------------------------
class TelephoneInlineAdmin(admin.StackedInline):
    model = Telephone
    extra = 0
    fieldsets = [(None, {'fields':(('type','number','target'))})]
#--------------------------------------------------------------------------------
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','customer','supplier']
    search_fields = ['name','notice',]
    list_filter = ['country',]
    list_editable = []
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            ('customer','supplier'),
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
    inlines = [TelephoneInlineAdmin,EmailInlineAdmin,CustomerInlineAdmin,SupplierInlineAdmin]
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