from django.forms import ModelForm
from visualisation.models import Table, TableItem

class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(TableForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder':'Titel der Tabelle'})
        self.fields['name'].label = {
            'class':'DYNAMO',
            'name':self.fields['name'].label
            }
        self.fields['dataURL'].widget.attrs.update({'placeholder':'URL'})
        self.fields['time'].widget.attrs.update({'placeholder':'Zeit'})
        

class TableItemForm(ModelForm):
    class Meta:
        model = TableItem
        fields = '__all__'