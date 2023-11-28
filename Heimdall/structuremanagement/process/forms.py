#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django import forms
from django.forms import ModelForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from structuremanagement.process.models import Process, ProcessData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class ProcessForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProcessForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ["picture_id","technical_data_sheet_id"]:
                visible.field.widget.attrs['class'] = 'form-select'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )

    class Meta:
        model = Process
        fields = '__all__'
#--------------------------------------------------------------------------------
class ProcessDataFormSet(ModelForm):

    begin_datetime = forms.DateTimeField(
        input_formats=[
            '%d.%m.%Y %H:%M:%S',
            '%d.%m.%Y %H:%M',
        ],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'dd.mm.YYYY hh:mm:ss',
                "class":"form-control"
                }
            ),
        required=False,
    )

    end_datetime = forms.DateTimeField(
        input_formats=[
            '%d.%m.%Y %H:%M:%S',
            '%d.%m.%Y %H:%M',
        ],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'dd.mm.YYYY hh:mm:ss',
                "class":"form-control"
                }
            ),
        required=False,
    )

    reference_number = forms.CharField(required=False,)

    slug = forms.SlugField(required=False,)

    url_delete = forms.URLField(required=False,)

    url_detail = forms.URLField(required=False,)

    url_detail_device = forms.URLField(required=False,)

    url_detail_process = forms.URLField(required=False,)

    utilization = forms.CharField(required=False,)

    def __init__(self, *args, **kwargs):
        super(ProcessDataFormSet, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ["process_id","device_id","begin_user_id","end_user_id"]:
                visible.field.widget.attrs['class'] = 'form-select'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )
        self.queryset = ProcessData.objects.filter(end_datetime=None)

    class Meta:
        model = ProcessData
        exclude = ['begin_user_id','end_user_id','protocol_id']
#--------------------------------------------------------------------------------
class ProcessDataForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProcessDataForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ["process_id","device_id","begin_user_id","end_user_id"]:
                visible.field.widget.attrs['class'] = 'form-select'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )

    class Meta:
        model = ProcessData
        fields = '__all__'
#--------------------------------------------------------------------------------