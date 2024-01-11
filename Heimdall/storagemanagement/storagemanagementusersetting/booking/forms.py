"""
#--------------------------------------------------------------------------------
# Forms File from Model Booking User Setting
# 07.01.2024
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
from storagemanagement.storagemanagementusersetting.booking.models import (
    StorageManagementBookingOverviewUserSetting,
    StorageManagementBookingListUserSetting,
    StorageManagementBookingTableUserSetting,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class StorageManagementBookingOverviewUserSettingForm(ModelForm):
    """
    StorageManagementBookingOverviewUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(StorageManagementBookingOverviewUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementBookingOverviewUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class StorageManagementBookingListUserSettingForm(ModelForm):
    """
    StorageManagementBookingListUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(StorageManagementBookingListUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementBookingListUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class StorageManagementBookingTableUserSettingForm(ModelForm):
    """
    StorageManagementBookingTableUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(StorageManagementBookingTableUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementBookingTableUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
