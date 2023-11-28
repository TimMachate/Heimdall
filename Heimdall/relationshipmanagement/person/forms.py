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
from relationshipmanagement.person.models import Person,EmailPerson,TelephonePerson
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class EmailFormSet(BaseInlineFormSet):

    class Meta:
        model = EmailPerson
        fields = '__all__'
#--------------------------------------------------------------------------------
class PersonForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['company_id']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in []:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Person
        fields = '__all__'
#--------------------------------------------------------------------------------
class TelephoneFormSet(BaseInlineFormSet):

    class Meta:
        model = TelephonePerson
        fields = '__all__'
#--------------------------------------------------------------------------------

EmailFormset = inlineformset_factory(
    extra = 1,
    fields = ('email',),
    fk_name = 'person_id',
    form = PersonForm,
    formset = EmailFormSet,
    model = EmailPerson,
    parent_model = Person,
)

TelephoneFormset = inlineformset_factory(
    extra = 1,
    fields = ('type','number'),
    fk_name = 'person_id',
    form = PersonForm,
    formset = TelephoneFormSet,
    model = TelephonePerson,
    parent_model = Person,
)