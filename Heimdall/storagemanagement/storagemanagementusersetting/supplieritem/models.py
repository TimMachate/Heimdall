"""
#--------------------------------------------------------------------------------
# Models File from Model Supplier
# 06.01.2024
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
class StorageManagementSupplierItemOverviewUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementSupplierItemOverviewUserSetting

    Args:
        CreateData (_type_): _description_
        UpdateData (_type_): _description_

    Returns:
        _type_: _description_
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:supplieritem_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    def api_url(self):
        """
        api_url

        Returns:
            string: url to api supplier item list page
        """
        return reverse(self.api)+f"?values={self.fields()}"

    # supplier
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

    supplier_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Firmen Namens',
        name = 'supplier_name',
        verbose_name = 'Firma',
    )

    supplier_url_detail = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Firmen Links',
        name = 'supplier_url_detail',
        verbose_name = 'Firmen Link',
    )

    item_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikelnummer',
        name = 'item_number',
        verbose_name = 'Artikelnummer',
    )

    image = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Bildes',
        name = 'image',
        verbose_name = 'Bild',
    )

    stock_count = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Anzahl der Artikel auf Lager',
        name = 'stock_count',
        verbose_name = 'Stand',
    )

    stock_value = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Wertes',
        name = 'stock_value',
        verbose_name = 'Wert',
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
        field_string += "reference_number," if self.reference_number else ""
        field_string += "name," if self.name else ""
        field_string += "supplier_name," if self.supplier_name else ""
        field_string += "supplier_url_detail," if self.supplier_url_detail else ""
        field_string += "item_number," if self.item_number else ""
        field_string += "image," if self.image else ""
        field_string += "stock_count," if self.stock_count else ""
        field_string += "stock_value," if self.stock_value else ""
        field_string += "url_detail," if self.url_detail else ""
        return str(field_string)

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'storagemanagementsupplieritemoverviewusersetting_user',
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
                'storagemanagement_supplieritem_overview_setting',
                'Storagemanagement Supplier Item Overview can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Item Übersicht"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Item Übersicht"
#--------------------------------------------------------------------------------
class StorageManagementSupplierItemListUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementSupplierItemListUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:supplieritem_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    def api_url(self):
        """
        api_url

        Returns:
            string: url to api supplier item list page
        """
        return reverse(self.api)+f"?values={self.fields()}"

    # supplier
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

    supplier = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Firma',
        name = 'supplier',
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

    stock_count = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Anzahl der Artikel auf Lager',
        name = 'stock_count',
        verbose_name = 'Stand',
    )

    booking_count = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Anzahl der Buchungen',
        name = 'booking_count',
        verbose_name = 'Buchungsanzahl',
    )

    booking_last = models.BooleanField(
        default = True,
        help_text = 'Darstellung der letzten Buchungen',
        name = 'booking_last',
        verbose_name = 'Letzte Buchungen',
    )

    stock_value = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Wertes',
        name = 'stock_value',
        verbose_name = 'Wert',
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
        field_string += "supplier_name," if self.supplier else ""
        field_string += "item_number," if self.item_number else ""
        field_string += "price," if self.price else ""
        field_string += "unit," if self.unit else ""
        field_string += "image," if self.image else ""
        field_string += "storageitem," if self.storageitem else ""
        field_string += "booking_count," if self.booking_count else ""
        field_string += "booking_last," if self.booking_last else ""
        field_string += "stock_count," if self.stock_count else ""
        field_string += "stock_value," if self.stock_value else ""
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
        field_string += "url_block," if self.url_block else ""
        return str(field_string)

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'storagemanagementsupplieritemlistusersetting_user',
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
                'storagemanagement_supplieritem_list_setting',
                'Storagemanagement Supplier Item List can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Item Liste"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Item Liste"
#--------------------------------------------------------------------------------
class StorageManagementSupplierItemTableUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementSupplierItemTableUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:supplieritem_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    def api_url(self):
        """
        api_url

        Returns:
            string: url to api supplier item list page
        """
        return reverse(self.api)+f"?values={self.fields()}"

    # supplier
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

    supplier = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Firma',
        name = 'supplier',
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

    stock_count = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Anzahl der Artikel auf Lager',
        name = 'stock_count',
        verbose_name = 'Stand',
    )

    stock_value = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Wertes',
        name = 'stock_value',
        verbose_name = 'Wert',
    )

    booking_count = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Anzahl der Buchungen',
        name = 'booking_count',
        verbose_name = 'Buchungsanzahl',
    )

    booking_last = models.BooleanField(
        default = True,
        help_text = 'Darstellung der letzten Buchungen',
        name = 'booking_last',
        verbose_name = 'Letzte Buchungen',
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
        field_string += "supplier_name," if self.supplier else ""
        field_string += "item_number," if self.item_number else ""
        field_string += "price," if self.price else ""
        field_string += "unit," if self.unit else ""
        field_string += "image," if self.image else ""
        field_string += "storageitem," if self.storageitem else ""
        field_string += "booking_last," if self.booking_last else ""
        field_string += "booking_count," if self.booking_count else ""
        field_string += "stock_count," if self.stock_count else ""
        field_string += "stock_value," if self.stock_value else ""
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
        field_string += "url_block," if self.url_block else ""
        return str(field_string)

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'storagemanagementsupplieritemtableusersetting_user',
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
                'storagemanagement_supplieritem_table_setting',
                'Storagemanagement Supplier Item Table can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Item Tabelle"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Item Tabelle"
#--------------------------------------------------------------------------------
