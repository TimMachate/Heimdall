"""
#--------------------------------------------------------------------------------
# Forms File from Model Offer User Setting
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
from storagemanagement.storagemanagementusersetting.offer.models import (
    StorageManagementOfferOverviewUserSetting,
    StorageManagementOfferListUserSetting,
    StorageManagementOfferTableUserSetting,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class StorageManagementOfferOverviewUserSettingForm(ModelForm):
    """
    StorageManagementOfferOverviewUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(StorageManagementOfferOverviewUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementOfferOverviewUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class StorageManagementOfferListUserSettingForm(ModelForm):
    """
    StorageManagementOfferListUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(StorageManagementOfferListUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementOfferListUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class StorageManagementOfferTableUserSettingForm(ModelForm):
    """
    StorageManagementOfferTableUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(StorageManagementOfferTableUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementOfferTableUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
