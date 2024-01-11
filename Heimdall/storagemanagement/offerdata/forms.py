"""
#--------------------------------------------------------------------------------
# Form File from Model Offer
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
from storagemanagement.offerdata.models import OfferData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class OfferDataForm(ModelForm):
    """
    OfferDataForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(OfferDataForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['offer','supplieritem','storageitem']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in ['authorized','done','booking']:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )

    class Meta:
        """
        Meta Data from Form
        """
        model = OfferData
        fields = '__all__'
#--------------------------------------------------------------------------------
