#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.forms import ModelForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from structuremanagement.department.models import Department
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class DepartmentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ["picture_id","process_instruction_id","responsible_employee_id","substitute_employee_id"]:
                visible.field.widget.attrs['class'] = 'form-select'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.label_classes = ('form-label', )

    class Meta:
        model = Department
        fields = '__all__'
#--------------------------------------------------------------------------------