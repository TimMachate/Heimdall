#--------------------------------------------------------------------------------
# Forms File from Model CompanyContact
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

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
from storagemanagement.companycontact.models import CompanyContact,CompanyContactEmail,CompanyContactTelephone
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class CompanyContactEmailFormSet(BaseInlineFormSet):

    class Meta:
        model = CompanyContactEmail
        fields = '__all__'
#--------------------------------------------------------------------------------
class CompanyContactForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CompanyContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['company']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in []:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CompanyContact
        fields = '__all__'
#--------------------------------------------------------------------------------
class CompanyContactTelephoneFormSet(BaseInlineFormSet):

    class Meta:
        model = CompanyContactTelephone
        fields = '__all__'
#--------------------------------------------------------------------------------

CompanyContactEmailFormset = inlineformset_factory(
    extra = 1,
    fields = ('email',),
    fk_name = 'companycontact',
    form = CompanyContactForm,
    formset = CompanyContactEmailFormSet,
    model = CompanyContactEmail,
    parent_model = CompanyContact,
)

CompanyContactTelephoneFormset = inlineformset_factory(
    extra = 1,
    fields = ('types','number'),
    fk_name = 'companycontact',
    form = CompanyContactForm,
    formset = CompanyContactTelephoneFormSet,
    model = CompanyContactTelephone,
    parent_model = CompanyContact,
)