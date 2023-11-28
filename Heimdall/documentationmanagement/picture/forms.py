#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.forms import ModelForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.picture.models import Picture
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class PictureForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PictureForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in []:
                visible.field.widget.attrs['class'] = 'form-select'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )

    class Meta:
        model = Picture
        fields = '__all__'
#--------------------------------------------------------------------------------