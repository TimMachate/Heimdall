"""
#--------------------------------------------------------------------------------
# Forms File from Model RequestData
# 05.01.2024
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
from storagemanagement.storagemanagementusersetting.requestdata.models import (
    StorageManagementRequestDataListUserSetting,
    StorageManagementRequestDataTableUserSetting,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class StorageManagementRequestDataListUserSettingForm(ModelForm):
    """
    StorageManagementRequestDataListUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(StorageManagementRequestDataListUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementRequestDataListUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class StorageManagementRequestDataTableUserSettingForm(ModelForm):
    """
    StorageManagementRequestDataTableUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(StorageManagementRequestDataTableUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementRequestDataTableUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
