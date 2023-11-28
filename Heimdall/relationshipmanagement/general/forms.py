#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.forms import ModelForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.supplier.models import General
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class GeneralForm(ModelForm):
    class Meta:
        model = General
        fields = '__all__'
#--------------------------------------------------------------------------------