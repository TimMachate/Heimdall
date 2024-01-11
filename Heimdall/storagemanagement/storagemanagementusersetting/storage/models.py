"""
#--------------------------------------------------------------------------------
# Models File from Model storagemanagementstorageusersetting
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
class StorageManagementStorageOverviewUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementStorageOverviewUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:storage_list',
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

    image = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Bildes',
        name = 'image',
        verbose_name = 'Bild',
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
        help_text = 'Darstellung der Lagerartikelnummer',
        name = 'storageitem_reference_number',
        verbose_name = 'Lagerartikelnummer',
    )

    supplieritem_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lagerartikel',
        name = 'supplieritem_name',
        verbose_name = 'Lagerartikel',
    )

    supplieritem_reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Lagerartikelnummer',
        name = 'supplieritem_reference_number',
        verbose_name = 'Lagerartikelnummer',
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

    url_unload = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links für eine Entnahme',
        name = 'url_unload',
        verbose_name = 'Entnahme',
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
        field_string += "image," if self.image else ""
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
        field_string += "unit," if self.unit else ""
        field_string += "price," if self.price else ""
        field_string += "url_unload," if self.url_unload else ""
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
        related_name = 'storagemanagementstorageoverviewusersetting_user',
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
                'storagemanagement_storage_overview_setting',
                'Storagemanagement Storage Overview can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Lager Übersicht"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Lager Übersicht"
#--------------------------------------------------------------------------------
class StorageManagementStorageListUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementSupplierItemListUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:storage_list',
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

    image = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Bildes',
        name = 'image',
        verbose_name = 'Bild',
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

    unload_date = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Entnahme-Datum',
        name = 'unload_date',
        verbose_name = 'Entnahme-Datum',
    )

    unload_time = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Entnahme-Zeit',
        name = 'unload_time',
        verbose_name = 'Entnahme-Zeit',
    )

    unload_user = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Entnahme-Benutzer',
        name = 'unload_user',
        verbose_name = 'Entnahme-Benutzer',
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
        help_text = 'Darstellung der Lagerartikelnummer',
        name = 'storageitem_reference_number',
        verbose_name = 'Lagerartikelnummer',
    )

    supplieritem_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Lagerartikel',
        name = 'supplieritem_name',
        verbose_name = 'Artikel',
    )

    supplieritem_reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikel Referenz',
        name = 'supplieritem_reference_number',
        verbose_name = 'Artikel Referenz',
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

    unit = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Einheit',
        name = 'unit',
        verbose_name = 'Einheit',
    )

    value = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Wertes',
        name = 'value',
        verbose_name = 'Wert',
    )

    url_unload = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links für eine Entnahme',
        name = 'url_unload',
        verbose_name = 'Entnahme',
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
        field_string += "image," if self.image else ""
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "update_date," if self.update_date else ""
        field_string += "update_time," if self.update_time else ""
        field_string += "update_username," if self.update_user else ""
        field_string += "unload_date," if self.unload_date else ""
        field_string += "unload_time," if self.unload_time else ""
        field_string += "unload_username," if self.unload_user else ""
        field_string += "reference_number," if self.reference_number else ""
        field_string += "storageitem_name," if self.storageitem_name else ""
        field_string += "storageitem_reference_number," if self.storageitem_reference_number else ""
        field_string += "supplieritem_name," if self.supplieritem_name else ""
        field_string += "supplieritem_reference_number," if self.supplieritem_reference_number else ""
        field_string += "supplieritem_item_number," if self.supplieritem_item_number else ""
        field_string += "supplier_name," if self.supplier_name else ""
        field_string += "unit," if self.unit else ""
        field_string += "value," if self.value else ""
        field_string += "url_unload," if self.url_unload else ""
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
        related_name = 'storagemanagementstoragelistusersetting_user',
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
                'storagemanagement_storage_list_setting',
                'Storagemanagement Storage List can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Lager Liste"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Lager Liste"
#--------------------------------------------------------------------------------
class StorageManagementStorageTableUserSetting(
    CreateData,
    UpdateData
):
    """
    StorageManagementSupplierItemTableUserSetting
    """

    # api
    api = models.CharField(
        default = 'storagemanagementAPI:storage_list',
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

    image = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Bildes',
        name = 'image',
        verbose_name = 'Bild',
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

    unload_date = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Entnahme-Datum',
        name = 'unload_date',
        verbose_name = 'Entnahme-Datum',
    )

    unload_time = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Entnahme-Zeit',
        name = 'unload_time',
        verbose_name = 'Entnahme-Zeit',
    )

    unload_user = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Entnahme-Benutzer',
        name = 'unload_user',
        verbose_name = 'Entnahme-Benutzer',
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
        help_text = 'Darstellung der Lagerartikelnummer',
        name = 'storageitem_reference_number',
        verbose_name = 'Lagerartikelnummer',
    )

    supplieritem_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Artikel',
        name = 'supplieritem_name',
        verbose_name = 'Artikel',
    )

    supplieritem_reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikel Referenz',
        name = 'supplieritem_reference_number',
        verbose_name = 'Artikel Referenz',
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

    unit = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Einheit',
        name = 'unit',
        verbose_name = 'Einheit',
    )

    value = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Wertes',
        name = 'value',
        verbose_name = 'Wertes',
    )

    url_unload = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links für eine Entnahme',
        name = 'url_unload',
        verbose_name = 'Entnahme',
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
        field_string += "image," if self.image else ""
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "update_date," if self.update_date else ""
        field_string += "update_time," if self.update_time else ""
        field_string += "update_username," if self.update_user else ""
        field_string += "unload_date," if self.unload_date else ""
        field_string += "unload_time," if self.unload_time else ""
        field_string += "unload_username," if self.unload_user else ""
        field_string += "reference_number," if self.reference_number else ""
        field_string += "storageitem_name," if self.storageitem_name else ""
        field_string += "storageitem_reference_number," if self.storageitem_reference_number else ""
        field_string += "supplieritem_name," if self.supplieritem_name else ""
        field_string += "supplieritem_reference_number," if self.supplieritem_reference_number else ""
        field_string += "supplieritem_item_number," if self.supplieritem_item_number else ""
        field_string += "supplier_name," if self.supplier_name else ""
        field_string += "unit," if self.unit else ""
        field_string += "value," if self.value else ""
        field_string += "url_unload," if self.url_unload else ""
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
        related_name = 'storagemanagementstoragetableusersetting_user',
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
                'storagemanagement_storage_table_setting',
                'Storagemanagement Storage Table can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Lager Tabelle"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Lager Tabelle"
#--------------------------------------------------------------------------------
