"""
#--------------------------------------------------------------------------------
# Models File from Model Company
# 16.12.2023
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
from programmmanagement.models import CreateData,UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class RelationshipManagementCompanyListUserSetting(
    CreateData,
    UpdateData
):
    """
    RelationshipManagementCompanyListUserSetting
    """
    # api
    api = models.CharField(
        default = 'relationshipmanagementAPI:company_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    # company
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

    supplier = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lieferanten',
        name = 'supplier',
        verbose_name = 'Lieferant',
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
        field_string += "companycontact_count," if self.contact else ""
        field_string += "companyitem_count," if self.item else ""
        field_string += "supplier," if self.supplier else ""
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
        field_string += "url_detail,url_update,url_delete,url_block," if self.url_block else ""
        return reverse(
            self.api
        )+f"?values={field_string}"

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'relationshipmanagementcompanylistusersetting_user',
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
        app_label = 'relationshipmanagement'
        default_permissions = ()
        ordering = ['user']
        permissions = (
            (
                'relationshipmanagement_company_list_setting',
                'Relationshipmanagement Company List can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Firmen Liste"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Firmen Liste"

#--------------------------------------------------------------------------------
class RelationshipManagementCompanyTableUserSetting(
    CreateData,
    UpdateData
):
    """
    RelationshipManagementCompanyTableUserSetting
    """

    # api
    api = models.CharField(
        default = 'relationshipmanagementAPI:company_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    # company
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

    supplier = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lieferanten',
        name = 'supplier',
        verbose_name = 'Lieferant',
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
        field_string += "companycontact_count," if self.contact else ""
        field_string += "companyitem_count," if self.item else ""
        field_string += "supplier," if self.supplier else ""
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
        field_string += "url_detail,url_update,url_delete,url_block," if self.url_block else ""
        return reverse(
            self.api
        )+f"?values={field_string}"

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'relationshipmanagementcompanytableusersetting_user',
        to = get_user_model(),
        verbose_name = 'Benutzer',
    )

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        """
        Meta Data from Model
        """
        app_label = 'relationshipmanagement'
        default_permissions = ()
        ordering = ['user']
        permissions = (
            (
                'relationshipmanagement_company_table_setting',
                'Relationshipmanagement Company Table can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Firmen Tabelle"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Firmen Tabelle"

#--------------------------------------------------------------------------------
class RelationshipManagementCompanyContactListUserSetting(
    CreateData,
    UpdateData
):
    """
    RelationshipManagementCompanyContactListUserSetting
    """

    # api
    api = models.CharField(
        default = 'relationshipmanagementAPI:companycontact_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    # company
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

    company = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Firma',
        name = 'company',
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
        field_string += "company_name," if self.company else ""
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
        field_string += "url_detail,url_update,url_delete,url_block," if self.url_block else ""
        return reverse(
            self.api
        )+f"?values={field_string}"

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'relationshipmanagementcompanycontactlistusersetting_user',
        to = get_user_model(),
        verbose_name = 'Benutzer',
    )

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        """
        Meta Data from Model
        """
        app_label = 'relationshipmanagement'
        default_permissions = ()
        ordering = ['user']
        permissions = (
            (
                'relationshipmanagement_companyontact_list_setting',
                'Relationshipmanagement Company Contact List can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Kontakt Liste"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Kontakt Liste"

#--------------------------------------------------------------------------------
class RelationshipManagementCompanyContactTableUserSetting(
    CreateData,
    UpdateData
):
    """
    RelationshipManagementCompanyContactTableUserSetting
    """

    # api
    api = models.CharField(
        default = 'relationshipmanagementAPI:companycontact_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    # company
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

    company = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Firma',
        name = 'company',
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
        field_string += "company_name," if self.company else ""
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
        field_string += "url_detail,url_update,url_delete,url_block," if self.url_block else ""
        return reverse(
            self.api
        )+f"?values={field_string}"

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'relationshipmanagementcompanycontacttableusersetting_user',
        to = get_user_model(),
        verbose_name = 'Benutzer',
    )

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        """
        Meta Data from Model
        """
        app_label = 'relationshipmanagement'
        default_permissions = ()
        ordering = ['user']
        permissions = (
            (
                'relationshipmanagement_companycontact_table_setting',
                'Relationshipmanagement Company Contact Table can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Kontakt Tabelle"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Kontakt Tabelle"

#--------------------------------------------------------------------------------
class RelationshipManagementCompanyItemListUserSetting(
    CreateData,
    UpdateData
):
    """
    RelationshipManagementCompanyItemListUserSetting
    """

    # api
    api = models.CharField(
        default = 'relationshipmanagementAPI:companyitem_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    # company
    reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Referenz Nummer',
        name = 'reference_number',
        verbose_name = 'Referenznummer',
    )

    name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Artikels',
        name = 'name',
        verbose_name = 'Artikel',
    )

    company = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Firma',
        name = 'company',
        verbose_name = 'Firma',
    )

    item_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikelnummer',
        name = 'item_number',
        verbose_name = 'Artikelnummer',
    )

    price = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Preises',
        name = 'price',
        verbose_name = 'Preis',
    )

    unit = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Einheit',
        name = 'unit',
        verbose_name = 'Einheit',
    )

    image = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Bildes',
        name = 'image',
        verbose_name = 'Bild',
    )

    storageitem = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lagerartikel',
        name = 'storageitem',
        verbose_name = 'Lagerartikel',
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

    url_request_create = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links für eine Preisanfrage',
        name = 'url_request_create',
        verbose_name = 'Preisanfrage',
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
        field_string += "company_name," if self.company else ""
        field_string += "item_number," if self.item_number else ""
        field_string += "price," if self.price else ""
        field_string += "unit," if self.unit else ""
        field_string += "image," if self.image else ""
        field_string += "storageitem," if self.storageitem else ""
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "update_date," if self.update_date else ""
        field_string += "update_time," if self.update_time else ""
        field_string += "update_username," if self.update_user else ""
        field_string += "url_request_create," if self.url_request_create else ""
        field_string += "url_detail," if self.url_detail else ""
        field_string += "url_update," if self.url_update else ""
        field_string += "url_delete," if self.url_delete else ""
        field_string += "url_detail,url_update,url_delete,url_block," if self.url_block else ""
        return reverse(
            self.api
        )+f"?values={field_string}"

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'relationshipmanagementcompanyitemlistusersetting_user',
        to = get_user_model(),
        verbose_name = 'Benutzer',
    )

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        """
        Meta Data from Model
        """
        app_label = 'relationshipmanagement'
        default_permissions = ()
        ordering = ['user']
        permissions = (
            (
                'relationshipmanagement_companyitem_list_setting',
                'Relationshipmanagement Company Item List can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Item Liste"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Item Liste"

#--------------------------------------------------------------------------------
class RelationshipManagementCompanyItemTableUserSetting(
    CreateData,
    UpdateData
):
    """
    RelationshipManagementCompanyItemTableUserSetting
    """

    # api
    api = models.CharField(
        default = 'relationshipmanagementAPI:companyitem_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    # company
    reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Referenz Nummer',
        name = 'reference_number',
        verbose_name = 'Referenznummer',
    )

    name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Artikels',
        name = 'name',
        verbose_name = 'Artikel',
    )

    company = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Firma',
        name = 'company',
        verbose_name = 'Firma',
    )

    item_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikelnummer',
        name = 'item_number',
        verbose_name = 'Artikelnummer',
    )

    price = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Preises',
        name = 'price',
        verbose_name = 'Preis',
    )

    unit = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Einheit',
        name = 'unit',
        verbose_name = 'Einheit',
    )

    image = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Bildes',
        name = 'image',
        verbose_name = 'Bild',
    )

    storageitem = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lagerartikel',
        name = 'storageitem',
        verbose_name = 'Lagerartikel',
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

    url_request_create = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links für eine Preisanfrage',
        name = 'url_request_create',
        verbose_name = 'Preisanfrage',
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
        field_string += "company_name," if self.company else ""
        field_string += "item_number," if self.item_number else ""
        field_string += "price," if self.price else ""
        field_string += "unit," if self.unit else ""
        field_string += "image," if self.image else ""
        field_string += "storageitem," if self.storageitem else ""
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "update_date," if self.update_date else ""
        field_string += "update_time," if self.update_time else ""
        field_string += "update_username," if self.update_user else ""
        field_string += "url_request_create," if self.url_request_create else ""
        field_string += "url_detail," if self.url_detail else ""
        field_string += "url_update," if self.url_update else ""
        field_string += "url_delete," if self.url_delete else ""
        field_string += "url_detail,url_update,url_delete,url_block," if self.url_block else ""
        return reverse(
            self.api
        )+f"?values={field_string}"

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'relationshipmanagementcompanyitemtableusersetting_user',
        to = get_user_model(),
        verbose_name = 'Benutzer',
    )

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        """
        Meta Data from Model
        """
        app_label = 'relationshipmanagement'
        default_permissions = ()
        ordering = ['user']
        permissions = (
            (
                'relationshipmanagement_companyitem_table_setting',
                'Relationshipmanagement Company Item Table can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Item Tabelle"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Item Tabelle"

#--------------------------------------------------------------------------------
