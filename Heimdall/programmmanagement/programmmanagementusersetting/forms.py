"""
#--------------------------------------------------------------------------------
# Forms File from Model Programm
# 17.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.forms import ModelForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from programmmanagement.programmmanagementusersetting.models import (
    ProgrammManagementProgrammListUserSetting,
    ProgrammManagementProgrammTableUserSetting,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class ProgrammManagementProgrammListUserSettingForm(ModelForm):
    """
    ProgrammManagementProgrammListUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(ProgrammManagementProgrammListUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = ProgrammManagementProgrammListUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class ProgrammManagementProgrammTableUserSettingForm(ModelForm):
    """
    ProgrammManagementProgrammTableUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(ProgrammManagementProgrammTableUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = ProgrammManagementProgrammTableUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
