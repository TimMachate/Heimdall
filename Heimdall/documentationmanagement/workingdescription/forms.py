#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.forms import ModelForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.workingdescription.models import WorkingDescription
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class WorkingDescriptionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(WorkingDescriptionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in []:
                visible.field.widget.attrs['class'] = 'form-select'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )

    class Meta:
        model = WorkingDescription
        fields = '__all__'
#--------------------------------------------------------------------------------