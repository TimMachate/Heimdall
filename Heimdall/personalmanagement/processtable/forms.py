#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.forms import ModelForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from personalmanagement.processtable.models import ProcessTable
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class ProcessTableForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProcessTableForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.widget.template_name == "django/forms/widgets/checkbox.html":
                visible.field.widget.attrs['class'] = 'form-check-input'
                visible.field.label_classes = ('form-check-label', )
            else:
                visible.field.widget.attrs['class'] = 'form-control'
                visible.field.label_classes = ('form-label', )

    class Meta:
        model = ProcessTable
        exclude = ['user',]
#--------------------------------------------------------------------------------