"""
#--------------------------------------------------------------------------------
# Models File from Model storagemanagementrequestdatausersetting
# 05.01.2024
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
class StorageManagementRequestDataOverviewUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementRequestDataOverviewUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:requestdata_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
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

    # supplier
    reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Referenz Nummer',
        name = 'reference_number',
        verbose_name = 'Referenznummer',
    )

    storageitem_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lagerartikel',
        name = 'storageitem_name',
        verbose_name = 'Lagerartikel',
    )

    storageitem_reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Lagerartikelreferenz',
        name = 'storageitem_reference_number',
        verbose_name = 'Lagerartikelreferenz',
    )

    supplieritem_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Artikels',
        name = 'supplieritem_name',
        verbose_name = 'Artikels',
    )

    supplieritem_reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikelreferenz',
        name = 'supplieritem_reference_number',
        verbose_name = 'Artikelreferenz',
    )

    supplieritem_item_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikelnummer',
        name = 'supplieritem_item_number',
        verbose_name = 'Artikelnummer',
    )

    supplier_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Firma',
        name = 'supplier_name',
        verbose_name = 'Firma',
    )

    amount = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Menge',
        name = 'amount',
        verbose_name = 'Menge',
    )

    unit = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Einheit',
        name = 'unit',
        verbose_name = 'Einheit',
    )

    price = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Preises',
        name = 'price',
        verbose_name = 'Preis',
    )

    value = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Wertes',
        name = 'value',
        verbose_name = 'Wert',
    )

    notice = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Bemerkung',
        name = 'notice',
        verbose_name = 'Bemerkung',
    )

    url_authorize_true = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Zustimmen-Links',
        name = 'url_authorize_true',
        verbose_name = 'Zustimmen-Link',
    )

    url_authorize_false = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Ablehnen-Links',
        name = 'url_authorize_false',
        verbose_name = 'Ablehnen-Link',
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

    # urls
    def fields(self):
        """
        url_api

        Returns:
            string: url to api
        """
        field_string = "id,"
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "reference_number," if self.reference_number else ""
        field_string += "storageitem_name," if self.storageitem_name else ""
        field_string += "storageitem_reference_number," if self.storageitem_reference_number else ""
        field_string += "supplieritem_name," if self.supplieritem_name else ""
        field_string += "supplieritem_reference_number," if self.supplieritem_reference_number else ""
        field_string += "supplieritem_item_number," if self.supplieritem_item_number else ""
        field_string += "supplier_name," if self.supplier_name else ""
        field_string += "amount," if self.amount else ""
        field_string += "unit," if self.unit else ""
        field_string += "price," if self.price else ""
        field_string += "value," if self.value else ""
        field_string += "notice," if self.notice else ""
        field_string += "url_authorize_true," if self.url_authorize_true else ""
        field_string += "url_authorize_false," if self.url_authorize_false else ""
        field_string += "url_detail," if self.url_detail else ""
        field_string += "url_update," if self.url_update else ""
        field_string += "url_delete," if self.url_delete else ""
        return reverse(
            self.api
        )+f"?values={field_string}"

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'storagemanagementrequestdataoverviewusersetting_user',
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
                'storagemanagement_requestdata_overview_setting',
                'Storagemanagement Request Data overview can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Anfrage Übersicht"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Anfragen Übersicht"
#--------------------------------------------------------------------------------
class StorageManagementRequestDataListUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementRequestDataListUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:requestdata_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    authorized = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Autorisierung',
        name = 'authorized',
        verbose_name = 'Autorisierung',
    )

    authorized_date = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Autorisierungsdatums',
        name = 'authorized_date',
        verbose_name = 'Autorisierungsdatum',
    )

    authorized_time = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Autorisierungszeit',
        name = 'authorized_time',
        verbose_name = 'Autorisierungszeit',
    )

    authorized_username = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Autorisierers',
        name = 'authorized_username',
        verbose_name = 'Autorisierer',
    )

    done = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Status',
        name = 'done',
        verbose_name = 'Status',
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

    # supplier
    reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Referenz Nummer',
        name = 'reference_number',
        verbose_name = 'Referenznummer',
    )

    storageitem_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lagerartikel',
        name = 'storageitem_name',
        verbose_name = 'Lagerartikel',
    )

    storageitem_reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Lagerartikelreferenz',
        name = 'storageitem_reference_number',
        verbose_name = 'Lagerartikelreferenz',
    )

    supplieritem_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Artikels',
        name = 'supplieritem_name',
        verbose_name = 'Artikels',
    )

    supplieritem_reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikelreferenz',
        name = 'supplieritem_reference_number',
        verbose_name = 'Artikelreferenz',
    )

    supplieritem_item_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikelnummer',
        name = 'supplieritem_item_number',
        verbose_name = 'Artikelnummer',
    )

    supplier_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Firma',
        name = 'supplier_name',
        verbose_name = 'Firma',
    )

    amount = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Menge',
        name = 'amount',
        verbose_name = 'Menge',
    )

    unit = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Einheit',
        name = 'unit',
        verbose_name = 'Einheit',
    )

    price = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Preises',
        name = 'price',
        verbose_name = 'Preis',
    )

    value = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Wertes',
        name = 'value',
        verbose_name = 'Wert',
    )

    notice = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Bemerkung',
        name = 'notice',
        verbose_name = 'Bemerkung',
    )

    url_authorize_true = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Zustimmen-Links',
        name = 'url_authorize_true',
        verbose_name = 'Zustimmen-Link',
    )

    url_authorize_false = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Ablehnen-Links',
        name = 'url_authorize_false',
        verbose_name = 'Ablehnen-Link',
    )

    url_authorize = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Autorisieren-Links',
        name = 'url_authorize',
        verbose_name = 'Autorisieren-Link',
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
        field_string += "authorized," if self.authorized else ""
        field_string += "authorized_date," if self.authorized_date else ""
        field_string += "authorized_time," if self.authorized_time else ""
        field_string += "authorized_username," if self.authorized_username else ""
        field_string += "done," if self.done else ""
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "update_date," if self.update_date else ""
        field_string += "update_time," if self.update_time else ""
        field_string += "update_username," if self.update_user else ""
        field_string += "reference_number," if self.reference_number else ""
        field_string += "storageitem_name," if self.storageitem_name else ""
        field_string += "storageitem_reference_number," if self.storageitem_reference_number else ""
        field_string += "supplieritem_name," if self.supplieritem_name else ""
        field_string += "supplieritem_reference_number," if self.supplieritem_reference_number else ""
        field_string += "supplieritem_item_number," if self.supplieritem_item_number else ""
        field_string += "supplier_name," if self.supplier_name else ""
        field_string += "amount," if self.amount else ""
        field_string += "unit," if self.unit else ""
        field_string += "price," if self.price else ""
        field_string += "value," if self.value else ""
        field_string += "notice," if self.notice else ""
        field_string += "url_authorize_true," if self.url_authorize_true else ""
        field_string += "url_authorize_false," if self.url_authorize_false else ""
        field_string += "url_authorize," if self.url_authorize else ""
        field_string += "url_detail," if self.url_detail else ""
        field_string += "url_update," if self.url_update else ""
        field_string += "url_delete," if self.url_delete else ""
        field_string += "url_block," if self.url_block else ""
        return reverse(
            self.api
        )+f"?values={field_string}"

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'storagemanagementrequestdatalistusersetting_user',
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
                'storagemanagement_requestdata_list_setting',
                'Storagemanagement Request Data List can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Anfrage Liste"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Anfragen Liste"
#--------------------------------------------------------------------------------
class StorageManagementRequestDataTableUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementRequestDataTableUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:requestdata_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    authorized = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Autorisierung',
        name = 'authorized',
        verbose_name = 'Autorisierung',
    )

    authorized_date = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Autorisierungsdatums',
        name = 'authorized_date',
        verbose_name = 'Autorisierungsdatum',
    )

    authorized_time = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Autorisierungszeit',
        name = 'authorized_time',
        verbose_name = 'Autorisierungszeit',
    )

    authorized_username = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Autorisierers',
        name = 'authorized_username',
        verbose_name = 'Autorisierer',
    )

    done = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Status',
        name = 'done',
        verbose_name = 'Status',
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

    # supplier
    reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Referenz Nummer',
        name = 'reference_number',
        verbose_name = 'Referenznummer',
    )

    storageitem_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lagerartikel',
        name = 'storageitem_name',
        verbose_name = 'Lagerartikel',
    )

    storageitem_reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Lagerartikelreferenz',
        name = 'storageitem_reference_number',
        verbose_name = 'Lagerartikelreferenz',
    )

    supplieritem_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Artikels',
        name = 'supplieritem_name',
        verbose_name = 'Artikels',
    )

    supplieritem_reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikelreferenz',
        name = 'supplieritem_reference_number',
        verbose_name = 'Artikelreferenz',
    )

    supplieritem_item_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikelnummer',
        name = 'supplieritem_item_number',
        verbose_name = 'Artikelnummer',
    )

    supplier_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Firma',
        name = 'supplier_name',
        verbose_name = 'Firma',
    )

    amount = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Menge',
        name = 'amount',
        verbose_name = 'Menge',
    )

    unit = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Einheit',
        name = 'unit',
        verbose_name = 'Einheit',
    )

    price = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Preises',
        name = 'price',
        verbose_name = 'Preis',
    )

    value = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Wertes',
        name = 'value',
        verbose_name = 'Wert',
    )

    notice = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Bemerkung',
        name = 'notice',
        verbose_name = 'Bemerkung',
    )

    url_authorize_true = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Zustimmen-Links',
        name = 'url_authorize_true',
        verbose_name = 'Zustimmen-Link',
    )

    url_authorize_false = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Ablehnen-Links',
        name = 'url_authorize_false',
        verbose_name = 'Ablehnen-Link',
    )

    url_authorize = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Autorisieren-Links',
        name = 'url_authorize',
        verbose_name = 'Autorisieren-Link',
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
        field_string += "authorized," if self.authorized else ""
        field_string += "authorized_date," if self.authorized_date else ""
        field_string += "authorized_time," if self.authorized_time else ""
        field_string += "authorized_username," if self.authorized_username else ""
        field_string += "done," if self.done else ""
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "update_date," if self.update_date else ""
        field_string += "update_time," if self.update_time else ""
        field_string += "update_username," if self.update_user else ""
        field_string += "reference_number," if self.reference_number else ""
        field_string += "storageitem_name," if self.storageitem_name else ""
        field_string += "storageitem_reference_number," if self.storageitem_reference_number else ""
        field_string += "supplieritem_name," if self.supplieritem_name else ""
        field_string += "supplieritem_reference_number," if self.supplieritem_reference_number else ""
        field_string += "supplieritem_item_number," if self.supplieritem_item_number else ""
        field_string += "supplier_name," if self.supplier_name else ""
        field_string += "amount," if self.amount else ""
        field_string += "unit," if self.unit else ""
        field_string += "price," if self.price else ""
        field_string += "value," if self.value else ""
        field_string += "notice," if self.notice else ""
        field_string += "url_authorize_true," if self.url_authorize_true else ""
        field_string += "url_authorize_false," if self.url_authorize_false else ""
        field_string += "url_authorize," if self.url_authorize else ""
        field_string += "url_detail," if self.url_detail else ""
        field_string += "url_update," if self.url_update else ""
        field_string += "url_delete," if self.url_delete else ""
        field_string += "url_block," if self.url_block else ""
        return reverse(
            self.api
        )+f"?values={field_string}"

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'storagemanagementrequestdatatableusersetting_user',
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
                'storagemanagement_requestdata_table_setting',
                'Storagemanagement Request Data Table can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Anfrage Tabelle"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Anfragen Tabelle"
#--------------------------------------------------------------------------------
