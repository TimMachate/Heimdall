"""
#--------------------------------------------------------------------------------
# Models File from Model Supplier
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
class StorageManagementSupplierOverviewUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementSupplierOverviewUserSetting
    """
    # api
    api = models.CharField(
        default = 'storagemanagementAPI:supplier_list',
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

    name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Firmennamen',
        name = 'name',
        verbose_name = 'Firmenname',
    )

    logo = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Logos',
        name = 'logo',
        verbose_name = 'Logo',
    )

    phone = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Telefonnummer',
        name = 'phone',
        verbose_name = 'phone',
    )

    email = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Email',
        name = 'email',
        verbose_name = 'E-Mail',
    )

    contact = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Anzahl der Kontakte',
        name = 'contact',
        verbose_name = 'Kontakte',
    )

    item = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikel',
        name = 'item',
        verbose_name = 'Artikel',
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
        field_string += "logo," if self.logo else ""
        field_string += "telephone," if self.phone else ""
        field_string += "email," if self.email else ""
        field_string += "suppliercontact_count," if self.contact else ""
        field_string += "supplieritem_count," if self.item else ""
        field_string += "url_detail," if self.url_detail else ""
        return  str(field_string)

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'storagemanagementsupplieroverviewusersetting_user',
        to = get_user_model(),
        verbose_name = 'Benutzer',
    )

    def __str__(self):
        """
        __str__

        Returns:
            string: _description_
        """
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
                'storagemanagement_supplier_overview_setting',
                'Storagemanagement Supplier Overview can view Setting'
            ),
        )
        verbose_name = "Einstellung Lagermanagement Lieferanten Übersicht"
        verbose_name_plural = "Einstellungen Lagermanagement Lieferanten Übersicht"
#--------------------------------------------------------------------------------
class StorageManagementSupplierListUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementSupplierListUserSetting
    """
    # api
    api = models.CharField(
        default = 'storagemanagementAPI:supplier_list',
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
        help_text = 'Darstellung des Firmennamen',
        name = 'name',
        verbose_name = 'Firmenname',
    )

    street = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Straße',
        name = 'street',
        verbose_name = 'Straße',
    )

    house_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Straßennummer',
        name = 'house_number',
        verbose_name = 'Straßennummer',
    )

    postcode = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Postleitzahl',
        name = 'postcode',
        verbose_name = 'Postleitzahl',
    )

    city = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Stadt',
        name = 'city',
        verbose_name = 'Stadt',
    )

    country = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Landes',
        name = 'country',
        verbose_name = 'Land',
    )

    phone = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Telefonnummer',
        name = 'phone',
        verbose_name = 'phone',
    )

    email = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Email',
        name = 'email',
        verbose_name = 'E-Mail',
    )

    email_address_offer = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Email Adresse für das Einholen von Angeboten.',
        name = 'email_address_offer',
        verbose_name = 'Angebot E-Mail',
    )

    email_address_cc_offer = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Email Adressen im CC für das Einholen von Angeboten.',
        name = 'email_address_cc_offer',
        verbose_name = 'Angebot E-Mail CC',
    )

    email_subject_offer = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Email Betreff des Angebotes.',
        name = 'email_subject_offer',
        verbose_name = 'Angebot E-Mail Betreff',
    )

    email_body_offer = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Email Inhaltes des Angebotes.',
        name = 'email_body_offer',
        verbose_name = 'Angebot E-Mail Inhalt',
    )

    email_address_order = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Email Adresse für die Bestellung.',
        name = 'email_address_order',
        verbose_name = 'Bestellung E-Mail',
    )

    email_address_cc_order = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Email Adressen im CC für die Bestellung.',
        name = 'email_address_cc_order',
        verbose_name = 'Bestellung E-Mail CC',
    )

    email_subject_order = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Email Betreff der Bestellung.',
        name = 'email_subject_order',
        verbose_name = 'Bestellung E-Mail Betreff',
    )

    email_body_order = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Email Inhaltes der Bestellung.',
        name = 'email_body_order',
        verbose_name = 'Bestellung E-Mail Inhalt',
    )

    contact = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Anzahl der Kontakte',
        name = 'contact',
        verbose_name = 'Kontakte',
    )

    item = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikel',
        name = 'item',
        verbose_name = 'Artikel',
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

    notice = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Bemerkung',
        name = 'notice',
        verbose_name = 'Bemerkung',
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
        field_string += "street," if self.street else ""
        field_string += "house_number," if self.house_number else ""
        field_string += "post_code," if self.postcode else ""
        field_string += "city," if self.city else ""
        field_string += "country," if self.country else ""
        field_string += "telephone," if self.phone else ""
        field_string += "email," if self.email else ""
        field_string += "email_address_offer," if self.email_address_offer else ""
        field_string += "email_address_cc_offer," if self.email_address_cc_offer else ""
        field_string += "email_body_offer," if self.email_body_offer else ""
        field_string += "email_subject_offer," if self.email_subject_offer else ""
        field_string += "email_address_order," if self.email_address_order else ""
        field_string += "email_address_cc_order," if self.email_address_cc_order else ""
        field_string += "email_body_order," if self.email_body_order else ""
        field_string += "email_subject_order," if self.email_subject_order else ""
        field_string += "suppliercontact_count," if self.contact else ""
        field_string += "supplieritem_count," if self.item else ""
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "update_date," if self.update_date else ""
        field_string += "update_time," if self.update_time else ""
        field_string += "update_username," if self.update_user else ""
        field_string += "notice," if self.notice else ""
        field_string += "url_detail," if self.url_detail else ""
        field_string += "url_update," if self.url_update else ""
        field_string += "url_delete," if self.url_delete else ""
        field_string += "url_block," if self.url_block else ""
        return  str(field_string)

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'storagemanagementsupplierlistusersetting_user',
        to = get_user_model(),
        verbose_name = 'Benutzer',
    )

    def __str__(self):
        """
        __str__

        Returns:
            string: _description_
        """
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
                'storagemanagement_supplier_list_setting',
                'Storagemanagement Supplier List can view Setting'
            ),
        )
        verbose_name = "Einstellung Lagermanagement Lieferanten Liste"
        verbose_name_plural = "Einstellungen Lagermanagement Lieferanten Liste"
#--------------------------------------------------------------------------------
class StorageManagementSupplierTableUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementSupplierTableUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:supplier_list',
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
        help_text = 'Darstellung des Firmennamen',
        name = 'name',
        verbose_name = 'Firmenname',
    )

    street = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Straße',
        name = 'street',
        verbose_name = 'Straße',
    )

    house_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Straßennummer',
        name = 'house_number',
        verbose_name = 'Straßennummer',
    )

    postcode = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Postleitzahl',
        name = 'postcode',
        verbose_name = 'Postleitzahl',
    )

    city = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Stadt',
        name = 'city',
        verbose_name = 'Stadt',
    )

    country = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Landes',
        name = 'country',
        verbose_name = 'Land',
    )

    phone = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Telefonnummer',
        name = 'phone',
        verbose_name = 'phone',
    )

    email = models.BooleanField(
        default = True,
        help_text = 'Darstellung der email',
        name = 'email',
        verbose_name = 'E-Mail',
    )

    email_address_offer = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Email Adresse für das Einholen von Angeboten.',
        name = 'email_address_offer',
        verbose_name = 'Angebot E-Mail',
    )

    email_address_cc_offer = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Email Adressen im CC für das Einholen von Angeboten.',
        name = 'email_address_cc_offer',
        verbose_name = 'Angebot E-Mail CC',
    )

    email_subject_offer = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Email Betreff des Angebotes.',
        name = 'email_subject_offer',
        verbose_name = 'Angebot E-Mail Betreff',
    )

    email_body_offer = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Email Inhaltes des Angebotes.',
        name = 'email_body_offer',
        verbose_name = 'Angebot E-Mail Inhalt',
    )

    email_address_order = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Email Adresse für die Bestellung.',
        name = 'email_address_order',
        verbose_name = 'Bestellung E-Mail',
    )

    email_address_cc_order = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Email Adressen im CC für die Bestellung.',
        name = 'email_address_cc_order',
        verbose_name = 'Bestellung E-Mail CC',
    )

    email_subject_order = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Email Betreff der Bestellung.',
        name = 'email_subject_order',
        verbose_name = 'Bestellung E-Mail Betreff',
    )

    email_body_order = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Email Inhaltes der Bestellung.',
        name = 'email_body_order',
        verbose_name = 'Bestellung E-Mail Inhalt',
    )

    contact = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Anzahl der Kontakte',
        name = 'contact',
        verbose_name = 'Kontakte',
    )

    item = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikel',
        name = 'item',
        verbose_name = 'Artikel',
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

    notice = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Bemerkung',
        name = 'notice',
        verbose_name = 'Bemerkung',
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
        field_string += "street," if self.street else ""
        field_string += "house_number," if self.house_number else ""
        field_string += "post_code," if self.postcode else ""
        field_string += "city," if self.city else ""
        field_string += "country," if self.country else ""
        field_string += "telephone," if self.phone else ""
        field_string += "email," if self.email else ""
        field_string += "email_address_offer," if self.email_address_offer else ""
        field_string += "email_address_cc_offer," if self.email_address_cc_offer else ""
        field_string += "email_body_offer," if self.email_body_offer else ""
        field_string += "email_subject_offer," if self.email_subject_offer else ""
        field_string += "email_address_order," if self.email_address_order else ""
        field_string += "email_address_cc_order," if self.email_address_cc_order else ""
        field_string += "email_body_order," if self.email_body_order else ""
        field_string += "email_subject_order," if self.email_subject_order else ""
        field_string += "suppliercontact_count," if self.contact else ""
        field_string += "supplieritem_count," if self.item else ""
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "update_date," if self.update_date else ""
        field_string += "update_time," if self.update_time else ""
        field_string += "update_username," if self.update_user else ""
        field_string += "notice," if self.notice else ""
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
        related_name = 'storagemanagementsuppliertableusersetting_user',
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
                'storagemanagement_supplier_table_setting',
                'Storagemanagement Supplier Table can view Setting'
            ),
        )
        verbose_name = "Einstellung Lagermanagement Lieferanten Tabelle"
        verbose_name_plural = "Einstellungen Lagermanagement Lieferanten Tabelle"
#--------------------------------------------------------------------------------
