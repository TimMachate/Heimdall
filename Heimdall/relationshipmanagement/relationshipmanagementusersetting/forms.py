"""
#--------------------------------------------------------------------------------
# Forms File from Model Company
# 16.12.2023
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
from relationshipmanagement.relationshipmanagementusersetting.models import (
    RelationshipManagementCompanyListUserSetting,
    RelationshipManagementCompanyTableUserSetting,
    RelationshipManagementCompanyContactListUserSetting,
    RelationshipManagementCompanyContactTableUserSetting,
    RelationshipManagementCompanyItemListUserSetting,
    RelationshipManagementCompanyItemTableUserSetting,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Forms
#--------------------------------------------------------------------------------
class RelationshipManagementCompanyListUserSettingForm(ModelForm):
    """
    RelationshipManagementCompanyListUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(RelationshipManagementCompanyListUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = RelationshipManagementCompanyListUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class RelationshipManagementCompanyTableUserSettingForm(ModelForm):
    """
    RelationshipManagementCompanyTableUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(RelationshipManagementCompanyTableUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = RelationshipManagementCompanyTableUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class RelationshipManagementCompanyContactListUserSettingForm(ModelForm):
    """
    RelationshipManagementCompanyContactListUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(
            RelationshipManagementCompanyContactListUserSettingForm,
            self
        ).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = RelationshipManagementCompanyContactListUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class RelationshipManagementCompanyContactTableUserSettingForm(ModelForm):
    """
    RelationshipManagementCompanyContactTableUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(
            RelationshipManagementCompanyContactTableUserSettingForm,
            self
        ).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = RelationshipManagementCompanyContactTableUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class RelationshipManagementCompanyItemListUserSettingForm(ModelForm):
    """
    RelationshipManagementCompanyItemListUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(RelationshipManagementCompanyItemListUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = RelationshipManagementCompanyItemListUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
class RelationshipManagementCompanyItemTableUserSettingForm(ModelForm):
    """
    RelationshipManagementCompanyItemTableUserSettingForm

    Args:
        ModelForm (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        super(RelationshipManagementCompanyItemTableUserSettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        """
        Meta Data from Form
        """
        model = RelationshipManagementCompanyItemTableUserSetting
        exclude = ['api','user']
#--------------------------------------------------------------------------------
