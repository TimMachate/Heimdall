"""
#--------------------------------------------------------------------------------
# Forms File from Model Supplier
# 25.10.2023
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
from storagemanagement.supplier.models import Supplier,SupplierBaseModel
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class SupplierBaseFormset(BaseInlineFormSet):
    """
    SupplierBaseForm

    Args:
        BaseInlineFormSet object: form object
    """

    class Meta:
        """
        Meta Data from Form
        """
        model = SupplierBaseModel
        fields = '__all__'

class SupplierForm(ModelForm):
    """
    SupplierForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(SupplierForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in []:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in []:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        """
        Meta Data from Form
        """
        model = Supplier
        fields = '__all__'
#--------------------------------------------------------------------------------
SupplierFormset = inlineformset_factory(
    extra = 0,
    fields = '__all__',
    fk_name = 'company',
    form = SupplierForm,
    formset = SupplierBaseFormset,
    max_num = 1,
    min_num = 1,
    model = SupplierBaseModel,
    parent_model = Supplier,
)
#--------------------------------------------------------------------------------
