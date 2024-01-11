"""
#--------------------------------------------------------------------------------
# Models File from Model Storage Item User Setting
# 04.01.2024
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
class StorageManagementStorageItemOverviewUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementStorageItemOverviewUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:storageitem_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    def api_url(self):
        """
        api_url

        Returns:
            string: url to api page
        """
        return reverse(self.api)+f"?values={self.fields()}"

    # supplier
    image = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Bildes',
        name = 'image',
        verbose_name = 'Bild',
    )

    status = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Status',
        name = 'status',
        verbose_name = 'Status',
    )

    name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lagerartikel',
        name = 'name',
        verbose_name = 'Lagerartikel',
    )

    stock_count = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Bestands',
        name = 'stock_count',
        verbose_name = 'Bestand',
    )

    stock_percentage = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Stands',
        name = 'stock_percentage',
        verbose_name = 'Stand',
    )

    url_booking_add = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links für eine Zubuchung',
        name = 'url_booking_add',
        verbose_name = 'Zubuchung',
    )

    url_booking_create = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links für eine Buchung',
        name = 'url_booking_create',
        verbose_name = 'Erstellung einer Buchung',
    )

    url_booking_remove = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links für eine Abbuchung',
        name = 'url_booking_remove',
        verbose_name = 'Abbuchung',
    )

    url_detail = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Detail-Links',
        name = 'url_detail',
        verbose_name = 'Detail-Link',
    )

    url_offer = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Angebots-Links',
        name = 'url_offer',
        verbose_name = 'Angebot-Link',
    )

    offer_count = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Anzahl der offenen Angebote',
        name = 'offer_count',
        verbose_name = 'Offene Angebote',
    )

    url_order = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Bestellung-Links',
        name = 'url_order',
        verbose_name = 'Bestellung-Link',
    )

    order_count = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Anzahl der offenen Bestellungen',
        name = 'order_count',
        verbose_name = 'Offene Bestellungen',
    )

    # urls
    def fields(self):
        """
        url_api

        Returns:
            string: url to api
        """
        field_string = "id,"
        field_string += "image," if self.image else ""
        field_string += "status," if self.status else ""
        field_string += "name," if self.name else ""
        field_string += "stock_count," if self.stock_count else ""
        field_string += "stock_percentage," if self.stock_percentage else ""
        field_string += "url_booking_add," if self.url_booking_add else ""
        field_string += "url_booking_create," if self.url_booking_create else ""
        field_string += "url_booking_remove," if self.url_booking_remove else ""
        field_string += "url_detail," if self.url_detail else ""
        return str(field_string)

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'storagemanagementstorageitemoverviewusersetting_user',
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
                'storagemanagement_storageitem_overview_setting',
                'Storagemanagement Storage Item Overview can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Lagerartikel Übersicht"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Lagerartikel Übersicht"
#--------------------------------------------------------------------------------
class StorageManagementStorageItemListUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementStorageItemListUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:storageitem_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    def api_url(self):
        """
        api_url

        Returns:
            string: url to api page
        """
        return reverse(self.api)+f"?values={self.fields()}"

    # supplier
    status = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Status',
        name = 'status',
        verbose_name = 'Status',
    )

    name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lagerartikel',
        name = 'name',
        verbose_name = 'Lagerartikel',
    )

    reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lagerartikel Referenz',
        name = 'reference_number',
        verbose_name = 'Lagerartikel Referenz',
    )

    supplier_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lieferanten',
        name = 'supplier_name',
        verbose_name = 'Lieferant',
    )

    supplieritem_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Artikels',
        name = 'supplieritem_name',
        verbose_name = 'Artikel',
    )

    supplieritem_item_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lagerartikel Artikelnummer',
        name = 'supplieritem_item_number',
        verbose_name = 'Artikelnummer',
    )

    stock_count = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Bestands',
        name = 'stock_count',
        verbose_name = 'Bestand',
    )

    stock_percentage = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Stands',
        name = 'stock_percentage',
        verbose_name = 'Stand',
    )

    minimum = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Minimums',
        name = 'minimum',
        verbose_name = 'Minimum',
    )

    warning = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Warnung',
        name = 'warning',
        verbose_name = 'Warnung',
    )

    maximum = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Maximums',
        name = 'maximum',
        verbose_name = 'Maximum',
    )

    booking_count = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Anzahl der Buchungen',
        name = 'booking_count',
        verbose_name = 'Anzahl der Buchungen',
    )

    booking_last = models.BooleanField(
        default = True,
        help_text = 'Darstellung der letzten Buchung',
        name = 'booking_last',
        verbose_name = 'Letzte Buchung',
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

    url_booking_add = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links für eine Preisanfrage',
        name = 'url_booking_add',
        verbose_name = 'Zubuchung',
    )

    url_booking = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links für eine Preisanfrage',
        name = 'url_booking',
        verbose_name = 'Erstellung einer Buchung',
    )

    url_booking_remove = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links für eine Preisanfrage',
        name = 'url_booking_remove',
        verbose_name = 'Abbuchung',
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
        field_string += "status," if self.status else ""
        field_string += "name," if self.name else ""
        field_string += "reference_number," if self.reference_number else ""
        field_string += "supplier_name," if self.supplier_name else ""
        field_string += "supplieritem_name," if self.supplieritem_name else ""
        field_string += "supplieritem_item_number," if self.supplieritem_item_number else ""
        field_string += "stock_count," if self.stock_count else ""
        field_string += "stock_percentage," if self.stock_percentage else ""
        field_string += "minimum," if self.minimum else ""
        field_string += "warning," if self.warning else ""
        field_string += "maximum," if self.maximum else ""
        field_string += "booking_count," if self.booking_count else ""
        field_string += "booking_last," if self.booking_last else ""
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "update_date," if self.update_date else ""
        field_string += "update_time," if self.update_time else ""
        field_string += "update_username," if self.update_user else ""
        field_string += "url_request_create," if self.url_request_create else ""
        field_string += "url_booking_add," if self.url_booking_add else ""
        field_string += "url_booking," if self.url_booking else ""
        field_string += "url_booking_remove," if self.url_booking_remove else ""
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
        related_name = 'storagemanagementstorageitemlistusersetting_user',
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
                'storagemanagement_storageitem_list_setting',
                'Storagemanagement Storage Item List can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Lagerartikel Liste"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Lagerartikel Liste"
#--------------------------------------------------------------------------------
class StorageManagementStorageItemTableUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementStorageItemTableUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:storageitem_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    def api_url(self):
        """
        api_url

        Returns:
            string: url to api page
        """
        return reverse(self.api)+f"?values={self.fields()}"

    # supplier
    status = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Status',
        name = 'status',
        verbose_name = 'Status',
    )

    name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lagerartikel',
        name = 'name',
        verbose_name = 'Lagerartikel',
    )

    reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lagerartikel Referenz',
        name = 'reference_number',
        verbose_name = 'Lagerartikel Referenz',
    )

    supplier_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lieferanten',
        name = 'supplier_name',
        verbose_name = 'Lieferant',
    )

    supplieritem_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Artikels',
        name = 'supplieritem_name',
        verbose_name = 'Artikel',
    )

    supplieritem_item_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lagerartikel Referenz',
        name = 'supplieritem_item_number',
        verbose_name = 'Artikel Referenz',
    )

    stock_count = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Bestands',
        name = 'stock_count',
        verbose_name = 'Bestand',
    )

    stock_percentage = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Stands',
        name = 'stock_percentage',
        verbose_name = 'Stand',
    )

    minimum = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Minimums',
        name = 'minimum',
        verbose_name = 'Minimum',
    )

    warning = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Warnung',
        name = 'warning',
        verbose_name = 'Warnung',
    )

    maximum = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Maximums',
        name = 'maximum',
        verbose_name = 'Maximum',
    )

    booking_count = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Anzahl der Buchungen',
        name = 'booking_count',
        verbose_name = 'Anzahl der Buchungen',
    )

    booking_last = models.BooleanField(
        default = True,
        help_text = 'Darstellung der letzten Buchung',
        name = 'booking_last',
        verbose_name = 'Letzte Buchung',
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

    url_booking_add = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links für eine Zubuchung',
        name = 'url_booking_add',
        verbose_name = 'Zubuchung',
    )

    url_booking = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links für eine Buchung',
        name = 'url_booking',
        verbose_name = 'Erstellung einer Buchung',
    )

    url_booking_remove = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links für eine Abbuchung',
        name = 'url_booking_remove',
        verbose_name = 'Abbuchung',
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
        field_string += "status," if self.status else ""
        field_string += "name," if self.name else ""
        field_string += "reference_number," if self.reference_number else ""
        field_string += "supplier_name," if self.supplier_name else ""
        field_string += "supplieritem_name," if self.supplieritem_name else ""
        field_string += "supplieritem_item_number," if self.supplieritem_item_number else ""
        field_string += "stock_count," if self.stock_count else ""
        field_string += "stock_percentage," if self.stock_percentage else ""
        field_string += "minimum," if self.minimum else ""
        field_string += "warning," if self.warning else ""
        field_string += "maximum," if self.maximum else ""
        field_string += "booking_count," if self.booking_count else ""
        field_string += "booking_last," if self.booking_last else ""
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "update_date," if self.update_date else ""
        field_string += "update_time," if self.update_time else ""
        field_string += "update_username," if self.update_user else ""
        field_string += "url_request_create," if self.url_request_create else ""
        field_string += "url_booking_add," if self.url_booking_add else ""
        field_string += "url_booking," if self.url_booking else ""
        field_string += "url_booking_remove," if self.url_booking_remove else ""
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
        related_name = 'storagemanagementstorageitemtableusersetting_user',
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
                'storagemanagement_storageitem_table_setting',
                'Storagemanagement Storage Item Table can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Lagerartikel Tabelle"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Lagerartikel Tabelle"
#--------------------------------------------------------------------------------
