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
from relationshipmanagement.company.models import Company, Telephone, Email
from relationshipmanagement.customer.models import Customer
from relationshipmanagement.general.models import General
from relationshipmanagement.supplier.models import Supplier
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class CompanyForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in []:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in ['customer','supplier']:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Company
        fields = '__all__'
#--------------------------------------------------------------------------------
class CustomerFormSet(BaseInlineFormSet):

    class Meta:
        model = Customer
        fields = '__all__'
#--------------------------------------------------------------------------------
class EmailFormSet(BaseInlineFormSet):

    class Meta:
        model = Email
        fields = '__all__'
#--------------------------------------------------------------------------------
class GeneralFormSet(BaseInlineFormSet):

    class Meta:
        model = General
        fields = '__all__'
#--------------------------------------------------------------------------------
class SupplierFormSet(BaseInlineFormSet):

    class Meta:
        model = Supplier
        fields = '__all__'
#--------------------------------------------------------------------------------
class TelephoneFormSet(BaseInlineFormSet):

    class Meta:
        model = Telephone
        fields = '__all__'
#--------------------------------------------------------------------------------

CustomerFormset = inlineformset_factory(
    extra = 1,
    fields = ('status',),
    fk_name = 'company_id',
    form = CompanyForm,
    formset = CustomerFormSet,
    model = Customer,
    parent_model = Company,
)

EmailFormset = inlineformset_factory(
    extra = 1,
    fields = ('email','target'),
    fk_name = 'company_id',
    form = CompanyForm,
    formset = EmailFormSet,
    model = Email,
    parent_model = Company,
)

GeneralFormset = inlineformset_factory(
    extra = 1,
    fields = (),
    fk_name = 'company_id',
    form = CompanyForm,
    formset = GeneralFormSet,
    model = General,
    parent_model = Company,
)

SupplierFormset = inlineformset_factory(
    extra = 1,
    fields = (),
    fk_name = 'company_id',
    form = CompanyForm,
    formset = SupplierFormSet,
    model = Supplier,
    parent_model = Company,
)

TelephoneFormset = inlineformset_factory(
    extra = 1,
    fields = ('type','number','target',),
    fk_name = 'company_id',
    form = CompanyForm,
    formset = TelephoneFormSet,
    model = Telephone,
    parent_model = Company,
)