from django.forms import ModelForm
from visualisation.models import ItemGroup, Item

class ItemGroupForm(ModelForm):
    class Meta:
        model = ItemGroup
        fields = '__all__'

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'