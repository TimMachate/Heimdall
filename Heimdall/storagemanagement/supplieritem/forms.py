"""
#--------------------------------------------------------------------------------
# Forms File from Model SupplierItem
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
from storagemanagement.supplieritem.models import SupplierItem, SupplierItemBaseModel
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class SupplierItemBaseFormset(BaseInlineFormSet):
    """
    SupplierBaseForm

    Args:
        BaseInlineFormSet object: form object
    """

    class Meta:
        """
        Meta Data from Form
        """
        model = SupplierItemBaseModel
        fields = '__all__'
#--------------------------------------------------------------------------------
class SupplierItemForm(ModelForm):
    """
    SupplierItemForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(SupplierItemForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['company','unit','storageitem']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in ['store']:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        """
        contains all Meta data of the form
        """
        model = SupplierItem
        fields = '__all__'
#--------------------------------------------------------------------------------
SupplierItemFormset = inlineformset_factory(
    extra = 0,
    fields = '__all__',
    fk_name = 'supplieritem',
    form = SupplierItemForm,
    formset = SupplierItemBaseFormset,
    max_num = 1,
    min_num = 1,
    model = SupplierItemBaseModel,
    parent_model = SupplierItem,
)
#--------------------------------------------------------------------------------
