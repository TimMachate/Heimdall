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
        name = 'storageitem',
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
        name = 'supplieritem',
        verbose_name = 'Lagerartikelnummer',
    )

    item_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikelnummer',
        name = 'item_number',
        verbose_name = 'Artikelnummer',
    )

    supplier = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Firma',
        name = 'supplier',
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
        field_string += "item_number," if self.item_number else ""
        field_string += "supplier_name," if self.supplier else ""
        field_string += "unit," if self.unit else ""
        field_string += "price," if self.price else ""
        field_string += "url_unload," if self.url_unload else ""
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
        name = 'storageitem',
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
        name = 'supplieritem',
        verbose_name = 'Lagerartikelnummer',
    )

    item_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Artikelnummer',
        name = 'item_number',
        verbose_name = 'Artikelnummer',
    )

    supplier = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Firma',
        name = 'supplier',
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
        field_string += "item_number," if self.item_number else ""
        field_string += "supplier_name," if self.supplier else ""
        field_string += "unit," if self.unit else ""
        field_string += "price," if self.price else ""
        field_string += "url_unload," if self.url_unload else ""
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
