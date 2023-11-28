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
from documentationmanagement.file.models import ProtocolProxy
from documentationmanagement.protocol.models import Protocol, ProtocolData, ProtocolStep, Variable
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from documentationmanagement.file.forms import FileForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class ProtocolForm(BaseInlineFormSet):

    class Meta:
        model = Protocol
        fields = '__all__'
#--------------------------------------------------------------------------------
ProtocolFormset = inlineformset_factory(
    max_num = 1,
    fields = ('topic','procedure','protocol',),
    fk_name = 'file_id',
    form = FileForm,
    formset = ProtocolForm,
    model = Protocol,
    parent_model = ProtocolProxy,
)
#--------------------------------------------------------------------------------
class ProtocolDataForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProtocolDataForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['protocol_id']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in []:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )

    class Meta:
        model = ProtocolData
        fields = '__all__'
#--------------------------------------------------------------------------------
class ProtocolStepForm(BaseInlineFormSet):

    class Meta:
        model = ProtocolStep
        fields = '__all__'
#--------------------------------------------------------------------------------
ProtocolStepFormset = inlineformset_factory(
    extra = 1,
    fields = ('name','order','text','variables'),
    fk_name = 'protocol_id',
    form = FileForm,
    formset = ProtocolStepForm,
    model = ProtocolStep,
    parent_model = Protocol,
)
#--------------------------------------------------------------------------------
class VariableForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(VariableForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['input_type']:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in []:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )

    class Meta:
        model = Variable
        fields = '__all__'
#--------------------------------------------------------------------------------