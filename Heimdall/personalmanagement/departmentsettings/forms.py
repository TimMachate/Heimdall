#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.forms import ModelForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from personalmanagement.departmentsettings.models import DepartmentSettings
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class DepartmentSettingsListForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DepartmentSettingsListForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.widget.template_name == "django/forms/widgets/checkbox.html":
                visible.field.widget.attrs['class'] = 'form-check-input'
                visible.field.label_classes = ('form-check-label', )
            else:
                visible.field.widget.attrs['class'] = 'form-control'
                visible.field.label_classes = ('form-label', )

    class Meta:
        model = DepartmentSettings
        fields = ['api_url_list_view',]
#--------------------------------------------------------------------------------
class DepartmentSettingsTableForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DepartmentSettingsTableForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.widget.template_name == "django/forms/widgets/checkbox.html":
                visible.field.widget.attrs['class'] = 'form-check-input'
                visible.field.label_classes = ('form-check-label', )
            else:
                visible.field.widget.attrs['class'] = 'form-control'
                visible.field.label_classes = ('form-label', )

    class Meta:
        model = DepartmentSettings
        fields = ['api_url_table_view',]
#--------------------------------------------------------------------------------