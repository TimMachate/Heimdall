"""
#--------------------------------------------------------------------------------
# Forms File from Model Supplier Contact
# 30.12.2023
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
from storagemanagement.storagemanagementusersetting.suppliercontact.models import (
    StorageManagementSupplierContactOverviewUserSetting,
    StorageManagementSupplierContactListUserSetting,
    StorageManagementSupplierContactTableUserSetting,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class StorageManagementSupplierContactOverviewUserSettingForm(ModelForm):
    """
    StorageManagementSupplierContactOverviewUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(
            StorageManagementSupplierContactOverviewUserSettingForm,
            self
        ).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementSupplierContactOverviewUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class StorageManagementSupplierContactListUserSettingForm(ModelForm):
    """
    StorageManagementSupplierContactListUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(
            StorageManagementSupplierContactListUserSettingForm,
            self
        ).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementSupplierContactListUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class StorageManagementSupplierContactTableUserSettingForm(ModelForm):
    """
    StorageManagementSupplierContactTableUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(
            StorageManagementSupplierContactTableUserSettingForm,
            self
        ).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementSupplierContactTableUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
