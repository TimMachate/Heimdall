#--------------------------------------------------------------------------------
# Forms File from Model CompanyItem
# 27.10.2023
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
from storagemanagement.companyitem.models import CompanyItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class CompanyItemForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CompanyItemForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['company','unit','storageitem']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in ['store']:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CompanyItem
        fields = '__all__'
#--------------------------------------------------------------------------------