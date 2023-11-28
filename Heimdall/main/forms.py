from django import forms

class SearchfieldForm(forms.Form):
    searchfield = forms.CharField(
            required=True,
            widget=forms.TextInput(
                attrs={
                    'list': 'searchfield',
                    'placeholder':'Eingabe/Suche',
                    }
                )
        )