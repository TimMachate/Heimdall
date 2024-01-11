"""
#--------------------------------------------------------------------------------
# Forms File from Model Booking
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
from storagemanagement.booking.models import Booking
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class BookingForm(ModelForm):
    """
    BookingForm

    Args:
        ModelForm (_type_): _description_
    """
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
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
        model = Booking
        fields = '__all__'
#--------------------------------------------------------------------------------
