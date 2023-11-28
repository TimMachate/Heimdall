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
from relationshipmanagement.person.models import Person,EmailPerson,TelephonePerson
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
class EmailInlineAdmin(admin.StackedInline):
    model = EmailPerson
    extra = 1
#--------------------------------------------------------------------------------
class TelephoneInlineAdmin(admin.StackedInline):
    model = TelephonePerson
    extra = 1
    fieldsets=(
        (None,{'fields':(
            ('type','number'),
        )}),
    )
#--------------------------------------------------------------------------------
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['last_name','company_id']
    search_fields = []
    list_filter = ['company_id',]
    list_editable = []
    ordering = ['company_id','last_name','first_name']
    fieldsets = (
        (None, {'fields':(
            'company_id',
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