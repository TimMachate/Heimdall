"""
#--------------------------------------------------------------------------------
# Forms File from Model Programm
# 17.12.2023
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
from programmmanagement.programm.models import Programm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class ProgrammForm(ModelForm):
    """
    ProgrammForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(ProgrammForm, self).__init__(*args, **kwargs)
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
        model = Programm
        fields = '__all__'
#--------------------------------------------------------------------------------
