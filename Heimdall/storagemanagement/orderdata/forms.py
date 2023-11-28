#--------------------------------------------------------------------------------
# Forms File from Model Order Data
# 10.11.2023
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
from storagemanagement.orderdata.models import OrderData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class OrderDataForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderDataForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['storageitem','companyitem','order']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in ['authorized','done','recived','sent']:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )

    class Meta:
        model = OrderData
        fields = '__all__'
#--------------------------------------------------------------------------------