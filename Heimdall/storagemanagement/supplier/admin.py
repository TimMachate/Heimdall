"""
#--------------------------------------------------------------------------------
# Admin File from Model Supplier
# 25.10.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
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
from relationshipmanagement.company.admin import CompanyAdmin
from storagemanagement.supplier.models import Supplier,SupplierBaseModel
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
class SupplierBaseAdmin(admin.StackedInline):
    """
    SupplierBaseAdmin

    Args:
        admin (_type_): _description_
    """
    extra = 0
    fieldsets = (
        ('Angebot', {'fields':(
            'email_address_offer',
            'email_address_cc_offer',
            'email_subject_offer',
            'email_body_offer',
            )}),
        ("Bestellung", {'fields':(
            'email_address_order',
            'email_address_cc_order',
            'email_subject_order',
            'email_body_order',
            )}),
    )
    filter_horizontal = []
    min_num = 1
    model = SupplierBaseModel
#--------------------------------------------------------------------------------
@admin.register(Supplier)
class SupplierAdmin(CompanyAdmin):
    """
    SupplierAdmin

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ['__str__']
    inlines = [SupplierBaseAdmin,]
#--------------------------------------------------------------------------------
