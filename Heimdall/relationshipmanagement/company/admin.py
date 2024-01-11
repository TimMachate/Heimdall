"""
#--------------------------------------------------------------------------------
# Admin File from Model Company
# 16.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
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
from relationshipmanagement.company.models import Company
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    CompanyAdmin

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ['name','email','telephone']
    search_fields = ['name','notice',]
    list_filter = ['country',]
    list_editable = []
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            )}),
        ('Bild', {'fields':(
            'logo',
            )}),
        ('Adresse', {'fields':(
            ('street','house_number'),
            ('post_code','city'),
            'country',
            )}),
        ('Kontakt', {'fields':(
            'email',
            'telephone',
            )}),
        (None, {'fields':(
            'notice',
            )}),
        ('Typ', {'fields':(
            'supplier',
            )}),
    )
    inlines = []
    def save_model(self, request, obj, form, change):
        user = request.user
        obj = form.save(commit=False)
        if not change or not obj.create_user_id:
            obj.create_user_id = user
        obj.update_user_id = user
        obj.update_datetime = timezone.now()
        obj.save()
        form.save_m2m()
        return obj
#--------------------------------------------------------------------------------
