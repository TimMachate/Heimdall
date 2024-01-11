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
from django.forms import ModelForm, BaseInlineFormSet
from django.forms.models import inlineformset_factory
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.offer.models import Offer
from storagemanagement.offerdata.models import OfferData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class OfferForm(ModelForm):
    """
    OfferForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['supplieritem']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in []:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )

    class Meta:
        """
        Meta Data from Form
        """
        model = Offer
        fields = '__all__'
#--------------------------------------------------------------------------------
class OfferDataFormSet(BaseInlineFormSet):
    """
    OfferDataFormSet

    Args:
        BaseInlineFormSet (_type_): _description_
    """

    class Meta:
        """
        Meta Data from Form
        """
        model = OfferData
        fields = '__all__'
#--------------------------------------------------------------------------------
OfferDataFormset = inlineformset_factory(
    extra = 1,
    fields = ('supplieritem','amount','price'),
    fk_name = 'offer',
    form = OfferForm,
    formset = OfferDataFormSet,
    model = OfferData,
    parent_model = Offer,
)
#--------------------------------------------------------------------------------
