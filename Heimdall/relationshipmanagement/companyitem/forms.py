"""
#--------------------------------------------------------------------------------
# Forms File from Model CompanyItem
# 15.12.2023
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
from relationshipmanagement.companyitem.models import CompanyItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class CompanyItemForm(ModelForm):
    """
    CompanyItemForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(CompanyItemForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['company','unit']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in ['store']:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        """
        contains all Meta data of the form
        """
        model = CompanyItem
        fields = '__all__'
#--------------------------------------------------------------------------------
