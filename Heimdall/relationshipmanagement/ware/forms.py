#--------------------------------------------------------------------------------
# Forms File from Model Ware
# 15.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.forms import ModelForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.ware.models import Ware
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class WareForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(WareForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['company_id','unit']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in []:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Ware
        fields = '__all__'
#--------------------------------------------------------------------------------