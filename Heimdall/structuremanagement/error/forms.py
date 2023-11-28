#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.forms import ModelForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from structuremanagement.error.models import Error, ErrorData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class ErrorForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ErrorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ["error_id","device_id"]:
                visible.field.widget.attrs['class'] = 'form-select'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )

    class Meta:
        model = Error
        fields = '__all__'
#--------------------------------------------------------------------------------
class ErrorDataForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ErrorDataForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ["error_id","device_id"]:
                visible.field.widget.attrs['class'] = 'form-select'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )

    class Meta:
        model = ErrorData
        fields = '__all__'
#--------------------------------------------------------------------------------