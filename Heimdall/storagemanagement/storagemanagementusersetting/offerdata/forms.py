"""
#--------------------------------------------------------------------------------
# Forms File from Model Offerdata User Setting
# 14.01.2024
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
from storagemanagement.storagemanagementusersetting.offerdata.models import (
    StorageManagementOfferdataOverviewUserSetting,
    StorageManagementOfferdataListUserSetting,
    StorageManagementOfferdataTableUserSetting,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class StorageManagementOfferdataOverviewUserSettingForm(ModelForm):
    """
    StorageManagementOfferdataOverviewUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(StorageManagementOfferdataOverviewUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementOfferdataOverviewUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class StorageManagementOfferdataListUserSettingForm(ModelForm):
    """
    StorageManagementOfferdataListUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(StorageManagementOfferdataListUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementOfferdataListUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class StorageManagementOfferdataTableUserSettingForm(ModelForm):
    """
    StorageManagementOfferdataTableUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(StorageManagementOfferdataTableUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementOfferdataTableUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
