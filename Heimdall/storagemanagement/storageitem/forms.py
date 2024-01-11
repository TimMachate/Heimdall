"""
#--------------------------------------------------------------------------------
# Forms File from Model StorageItem
# 15.10.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.forms import ModelForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.storageitem.models import StorageItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class StorageItemForm(ModelForm):
    """
    StorageItemForm

    Args:
        ModelForm (_type_): _description_
    """
    def __init__(self, *args, **kwargs):
        super(StorageItemForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['supplieritem']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in []:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        """
        contains all Meta data of the form
        """
        model = StorageItem
        fields = '__all__'
#--------------------------------------------------------------------------------
