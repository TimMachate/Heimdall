#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.forms import ModelForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.file.models import File
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class FileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['type',]:
                visible.field.widget.attrs['class'] = 'form-select'
            elif visible.name in ['protocol']:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )

    class Meta:
        model = File
        fields = '__all__'
#--------------------------------------------------------------------------------