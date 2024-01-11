"""
#--------------------------------------------------------------------------------
# Forms File from Model Supplier Item
# 06.01.2024
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
from storagemanagement.storagemanagementusersetting.supplieritem.models import (
    StorageManagementSupplierItemOverviewUserSetting,
    StorageManagementSupplierItemListUserSetting,
    StorageManagementSupplierItemTableUserSetting,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class StorageManagementSupplierItemOverviewUserSettingForm(ModelForm):
    """
    StorageManagementSupplierItemOverviewUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(StorageManagementSupplierItemOverviewUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementSupplierItemOverviewUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class StorageManagementSupplierItemListUserSettingForm(ModelForm):
    """
    StorageManagementSupplierItemListUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(StorageManagementSupplierItemListUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementSupplierItemListUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class StorageManagementSupplierItemTableUserSettingForm(ModelForm):
    """
    StorageManagementSupplierItemTableUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(StorageManagementSupplierItemTableUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = StorageManagementSupplierItemTableUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
