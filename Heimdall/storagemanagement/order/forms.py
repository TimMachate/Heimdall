"""
#--------------------------------------------------------------------------------
# Forms File from Model Order
# 09.11.2023
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
from storagemanagement.order.models import Order
from storagemanagement.orderdata.models import OrderData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class OrderForm(ModelForm):
    """
    OrderForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['supplieritem']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in ['sent','recived','done',]:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )

    class Meta:
        """
        Meta Data from Form
        """
        model = Order
        fields = '__all__'
#--------------------------------------------------------------------------------
class OrderDataFormSet(BaseInlineFormSet):
    """
    OrderDataFormSet

    Args:
        BaseInlineFormSet (_type_): _description_
    """

    class Meta:
        """
        Meta Data from Form
        """
        model = OrderData
        fields = '__all__'
#--------------------------------------------------------------------------------
OrderDataFormset = inlineformset_factory(
    extra = 1,
    fields = ('id','supplieritem','amount','amount_recived','price'),
    fk_name = 'order',
    form = OrderForm,
    formset = OrderDataFormSet,
    model = OrderData,
    parent_model = Order,
)
#--------------------------------------------------------------------------------
