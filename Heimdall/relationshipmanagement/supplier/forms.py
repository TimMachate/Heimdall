#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.forms import ModelForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.supplier.models import Supplier
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
#--------------------------------------------------------------------------------