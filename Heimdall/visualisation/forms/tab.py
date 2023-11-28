from django.forms import IntegerField, ModelForm
from django.forms import HiddenInput
from visualisation.models import Tab

class TabForm(ModelForm):
    id = IntegerField(widget=HiddenInput(),required=False)
    class Meta:
        model = Tab
        exclude = ('user',)