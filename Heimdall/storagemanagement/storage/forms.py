"""
#--------------------------------------------------------------------------------
# Forms File from Model Storage
# 03.11.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.apps import apps
from django.forms import ModelForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.storage.models import Storage
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class StorageForm(ModelForm):
    """
    StorageForm

    Args:
        ModelForm (_type_): _description_
    """
    def __init__(self, *args, **kwargs):
        super(StorageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['companyitem']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in ['store']:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        """
        Meta Data from Form
        """
        model = Storage
        fields = '__all__'
#--------------------------------------------------------------------------------
