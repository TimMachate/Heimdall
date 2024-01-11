"""
#--------------------------------------------------------------------------------
# Models File from Model Supplier Contact
# 30.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from tools.createdata.models import CreateData
from tools.updatedata.models import UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class StorageManagementSupplierContactOverviewUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementSupplierContactOverviewUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:suppliercontact_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    def api_url(self):
        """
        api_url

        Returns:
            _type_: _description_
        """
        return reverse(
            self.api
        )+f"?values={self.fields()}"

    name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Namen [Nachname, Vorname]',
        name = 'name',
        verbose_name = 'Name',
    )

    supplier_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Firmennamen',
        name = 'supplier_name',
        verbose_name = 'Firma',
    )

    supplier_url_detail = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Firmen Link',
        name = 'supplier_url_detail',
        verbose_name = 'Firmen Link',
    )

    url_detail = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Detail-Links',
        name = 'url_detail',
        verbose_name = 'Detail-Link',
    )

    # urls
    def fields(self):
        """
        url_api

        Returns:
            string: url to api
        """
        field_string = "id,"
        field_string += "name," if self.name else ""
        field_string += "supplier_name," if self.supplier_name else ""
        field_string += "supplier_url_detail," if self.supplier_url_detail else ""
        field_string += "url_detail," if self.url_detail else ""
        return str(field_string)

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'storagemanagementsuppliercontactoverviewusersetting_user',
        to = get_user_model(),
        verbose_name = 'Benutzer',
    )

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        """
        Meta Data from Model
        """
        app_label = 'storagemanagement'
        default_permissions = ()
        ordering = ['user']
        permissions = (
            (
                'storagemanagement_supplierontact_overview_setting',
                'Storagemanagement Supplier Contact Overview can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Kontakt Übersicht"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Kontakt Übersicht"
#--------------------------------------------------------------------------------
class StorageManagementSupplierContactListUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementSupplierContactListUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:suppliercontact_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    def api_url(self):
        """
        api_url

        Returns:
            _type_: _description_
        """
        return reverse(
            self.api
        )+f"?values={self.fields()}"

    # supplier
    reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Referenz Nummer',
        name = 'reference_number',
        verbose_name = 'Referenznummer',
    )

    name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Namen [Nachname, Vorname]',
        name = 'name',
        verbose_name = 'Name',
    )

    supplier = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Firma',
        name = 'supplier',
        verbose_name = 'Firma',
    )

    first_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Vornamen',
        name = 'first_name',
        verbose_name = 'Vorname',
    )

    last_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Nachname',
        name = 'last_name',
        verbose_name = 'Nachname',
    )

    phone = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Telefonnummer',
        name = 'phone',
        verbose_name = 'Telefon',
    )

    email = models.BooleanField(
        default = True,
        help_text = 'Darstellung der E-Mails',
        name = 'email',
        verbose_name = 'E-Mail',
    )

    notice = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Bemerkung',
        name = 'notice',
        verbose_name = 'Bemerkung',
    )

    create_date = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Erstellerdatums',
        name = 'create_date',
        verbose_name = 'Erstellerdatum',
    )

    create_time = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Erstellerzeit',
        name = 'create_time',
        verbose_name = 'Erstellerzeit',
    )

    create_user = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Erstellers',
        name = 'create_user',
        verbose_name = 'Ersteller',
    )

    update_date = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Update-Datum',
        name = 'update_date',
        verbose_name = 'Update-Datum',
    )

    update_time = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Update-Zeit',
        name = 'update_time',
        verbose_name = 'Update-Zeit',
    )

    update_user = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Update-Benutzer',
        name = 'update_user',
        verbose_name = 'Update-Benutzer',
    )

    url_detail = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Detail-Links',
        name = 'url_detail',
        verbose_name = 'Detail-Link',
    )

    url_update = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Update-links',
        name = 'url_update',
        verbose_name = 'Update-Link',
    )

    url_delete = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Löschen-Links',
        name = 'url_delete',
        verbose_name = 'Löschen-Link',
    )

    url_block = models.BooleanField(
        default = True,
        help_text = 'Darstellung aller Links in einem Block',
        name = 'url_block',
        verbose_name = 'Links',
    )

    # urls
    def fields(self):
        """
        url_api

        Returns:
            string: url to api
        """
        field_string = "id,"
        field_string += "reference_number," if self.reference_number else ""
        field_string += "name," if self.name else ""
        field_string += "supplier_name," if self.supplier else ""
        field_string += "first_name," if self.first_name else ""
        field_string += "last_name," if self.last_name else ""
        field_string += "telephone_data," if self.phone else ""
        field_string += "email_data," if self.email else ""
        field_string += "notice," if self.notice else ""
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "update_date," if self.update_date else ""
        field_string += "update_time," if self.update_time else ""
        field_string += "update_username," if self.update_user else ""
        field_string += "url_detail," if self.url_detail else ""
        field_string += "url_update," if self.url_update else ""
        field_string += "url_delete," if self.url_delete else ""
        field_string += "url_block," if self.url_block else ""
        return str(field_string)

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'storagemanagementsuppliercontactlistusersetting_user',
        to = get_user_model(),
        verbose_name = 'Benutzer',
    )

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        """
        Meta Data from Model
        """
        app_label = 'storagemanagement'
        default_permissions = ()
        ordering = ['user']
        permissions = (
            (
                'storagemanagement_supplierontact_list_setting',
                'Storagemanagement Supplier Contact List can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Kontakt Liste"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Kontakt Liste"
#--------------------------------------------------------------------------------
class StorageManagementSupplierContactTableUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementSupplierContactTableUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:suppliercontact_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    def api_url(self):
        """
        api_url

        Returns:
            _type_: _description_
        """
        return reverse(
            self.api
        )+f"?values={self.fields()}"

    # supplier
    reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Referenz Nummer',
        name = 'reference_number',
        verbose_name = 'Referenznummer',
    )

    name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Namen [Nachname, Vorname]',
        name = 'name',
        verbose_name = 'Name',
    )

    supplier = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Firma',
        name = 'supplier',
        verbose_name = 'Firma',
    )

    first_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Vornamen',
        name = 'first_name',
        verbose_name = 'Vorname',
    )

    last_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Nachname',
        name = 'last_name',
        verbose_name = 'Nachname',
    )

    phone = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Telefonnummer',
        name = 'phone',
        verbose_name = 'Telefon',
    )

    email = models.BooleanField(
        default = True,
        help_text = 'Darstellung der E-Mails',
        name = 'email',
        verbose_name = 'E-Mail',
    )

    notice = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Bemerkung',
        name = 'notice',
        verbose_name = 'Bemerkung',
    )

    create_date = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Erstellerdatums',
        name = 'create_date',
        verbose_name = 'Erstellerdatum',
    )

    create_time = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Erstellerzeit',
        name = 'create_time',
        verbose_name = 'Erstellerzeit',
    )

    create_user = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Erstellers',
        name = 'create_user',
        verbose_name = 'Ersteller',
    )

    update_date = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Update-Datum',
        name = 'update_date',
        verbose_name = 'Update-Datum',
    )

    update_time = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Update-Zeit',
        name = 'update_time',
        verbose_name = 'Update-Zeit',
    )

    update_user = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Update-Benutzer',
        name = 'update_user',
        verbose_name = 'Update-Benutzer',
    )

    url_detail = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Detail-Links',
        name = 'url_detail',
        verbose_name = 'Detail-Link',
    )

    url_update = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Update-links',
        name = 'url_update',
        verbose_name = 'Update-Link',
    )

    url_delete = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Löschen-Links',
        name = 'url_delete',
        verbose_name = 'Löschen-Link',
    )

    url_block = models.BooleanField(
        default = True,
        help_text = 'Darstellung aller Links in einem Block',
        name = 'url_block',
        verbose_name = 'Links',
    )

    # urls
    def fields(self):
        """
        url_api

        Returns:
            string: url to api
        """
        field_string = "id,"
        field_string += "reference_number," if self.reference_number else ""
        field_string += "name," if self.name else ""
        field_string += "supplier_name," if self.supplier else ""
        field_string += "first_name," if self.first_name else ""
        field_string += "last_name," if self.last_name else ""
        field_string += "telephone_data," if self.phone else ""
        field_string += "email_data," if self.email else ""
        field_string += "notice," if self.notice else ""
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "update_date," if self.update_date else ""
        field_string += "update_time," if self.update_time else ""
        field_string += "update_username," if self.update_user else ""
        field_string += "url_detail," if self.url_detail else ""
        field_string += "url_update," if self.url_update else ""
        field_string += "url_delete," if self.url_delete else ""
        field_string += "url_block," if self.url_block else ""
        return str(field_string)

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'storagemanagementsuppliercontacttableusersetting_user',
        to = get_user_model(),
        verbose_name = 'Benutzer',
    )

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        """
        Meta Data from Model
        """
        app_label = 'storagemanagement'
        default_permissions = ()
        ordering = ['user']
        permissions = (
            (
                'storagemanagement_suppliercontact_table_setting',
                'Storagemanagement Supplier Contact Table can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Kontakt Tabelle"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Kontakt Tabelle"
#--------------------------------------------------------------------------------
