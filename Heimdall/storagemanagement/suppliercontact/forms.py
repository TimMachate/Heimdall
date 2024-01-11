"""
#--------------------------------------------------------------------------------
# Forms File from Model SupplierContact
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.forms import ModelForm, BaseInlineFormSet
from django.forms.models import inlineformset_factory
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.suppliercontact.models import (
    SupplierContact,
    SupplierContactEmail,
    SupplierContactTelephone
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class SupplierContactEmailFormSet(BaseInlineFormSet):
    """
    SupplierContactEmailFormSet

    Args:
        BaseInlineFormSet (_type_): _description_
    """

    class Meta:
        """
        contains all Meta data of the Formset
        """
        model = SupplierContactEmail
        fields = '__all__'
#--------------------------------------------------------------------------------
class SupplierContactForm(ModelForm):
    """
    SupplierContactForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(SupplierContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['company','types']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in []:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        """
        contains all Meta data of the Formset
        """
        model = SupplierContact
        fields = '__all__'
#--------------------------------------------------------------------------------
class SupplierContactTelephoneFormSet(BaseInlineFormSet):
    """
    SupplierContactTelephoneFormSet

    Args:
        BaseInlineFormSet (_type_): _description_
    """

    class Meta:
        """
        contains all Meta data of the Formset
        """
        model = SupplierContactTelephone
        fields = '__all__'
#--------------------------------------------------------------------------------

SupplierContactEmailFormset = inlineformset_factory(
    extra = 1,
    fields = ('email',),
    fk_name = 'companycontact',
    form = SupplierContactForm,
    formset = SupplierContactEmailFormSet,
    model = SupplierContactEmail,
    parent_model = SupplierContact,
)

SupplierContactTelephoneFormset = inlineformset_factory(
    extra = 1,
    fields = ('types','number'),
    fk_name = 'companycontact',
    form = SupplierContactForm,
    formset = SupplierContactTelephoneFormSet,
    model = SupplierContactTelephone,
    parent_model = SupplierContact,
)
