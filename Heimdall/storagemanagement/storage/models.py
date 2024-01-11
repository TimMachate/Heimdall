"""
#--------------------------------------------------------------------------------
# Models File from Model Storage
# 03.11.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from tinymce import models as tinymce_models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from tools.createdata.models import CreateData
from tools.referencenumber.models import ReferenceNumber
from tools.slug.models import Slug
from tools.updatedata.models import UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class StorageBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):
    """
    StorageBaseModel

    Args:
        CreateData (_type_): _description_
        ReferenceNumber (_type_): _description_
        Slug (_type_): _description_
        UpdateData (_type_): _description_
    """

    # Variables
    short_name = "STST"

    # Fields/Methodes for the supplieritem
    supplieritem = models.ForeignKey(
        blank = True,
        name = 'supplieritem',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'storage_supplieritem',
        to = 'storagemanagement.SupplierItem',
        verbose_name = 'Artikel',
    )

    # Fields/Methodes for the booking
    booking = models.ForeignKey(
        blank = True,
        name = 'booking',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'storage_booking',
        to = 'storagemanagement.booking',
        verbose_name = 'Buchung',
    )

    # Fields/Methodes for the notice
    notice = tinymce_models.HTMLField(
        blank = True,
        help_text = "Bemerkungen zum Prozess",
        name = 'notice',
        null = True,
        verbose_name = 'Bemerkung',
    )

    unload_datetime = models.DateTimeField(
        blank = True,
        default = None,
        help_text = "Zeitpunkt der Entnahme.",
        name = 'unload_datetime',
        null = True,
        verbose_name = 'Zeitpunkt der Entnahme',
    )

    unload_user_id = models.ForeignKey(
        blank = True,
        default = None,
        help_text = "Person der Entnahme.",
        name = 'unload_user_id',
        null = True,
        on_delete = models.PROTECT,
        related_name = "storage_unload_user_id",
        to = get_user_model(),
        verbose_name = 'Entnehmer',
    )

    class Meta:
        """
        Meta Data for model
        """
        app_label = 'storagemanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class Storage(StorageBaseModel):
    """
    Storage

    Args:
        StorageBaseModel (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Booking
    def booking_id(self):
        """
        booking_id

        Returns:
            int: id from the booking object
        """
        result = self.booking.id if self.booking else None
        return result

    def booking_reference_number(self):
        """
        booking_reference_number

        Returns:
            string: reference number from the booking object
        """
        result = self.booking.reference_number if self.booking else None
        return result

    def booking_slug(self):
        """
        booking_slug

        Returns:
            string: slug from the booking object
        """
        result = self.booking.slug if self.booking else None
        return result

    def booking_url_detail(self):
        """
        booking_url_detail

        Returns:
            string: url to booking detail page
        """
        result = self.booking.url_detail() if self.booking else None
        return result

    # Supplier
    def supplier_id(self):
        """
        supplier_id

        Returns:
            int: id from supplier
        """
        if self.supplieritem:
            result = self.supplieritem.supplier_id()
        else:
            result = None
        return result

    def supplier_name(self):
        """
        supplier_name

        Returns:
            string: name of supplier
        """
        if self.supplieritem:
            result = self.supplieritem.supplier_name()
        else:
            result = None
        return result

    def supplier_reference_number(self):
        """
        supplier_reference_number

        Returns:
            string: reference number from supplier
        """
        if self.supplieritem:
            result = self.supplieritem.supplier_reference_number()
        else:
            result = None
        return result

    def supplier_slug(self):
        """
        supplier_slug

        Returns:
            string: slug from supplier
        """
        if self.supplieritem:
            result = self.supplieritem.supplier_slug()
        else:
            result = None
        return result

    def supplier_url_detail(self):
        """
        supplier_url_detail

        Returns:
            string: url to supplier detail page
        """
        if self.supplieritem:
            result = self.supplieritem.supplier_url_detail()
        else:
            result = None
        return result

    # Supplier Item
    def supplieritem_id(self):
        """
        supplieritem_id

        Returns:
            string: id from supplieritem
        """
        result = self.supplieritem.id if self.supplieritem else None
        return result

    def supplieritem_name(self):
        """
        supplieritem_name

        Returns:
            string: name from supplier item
        """
        result = self.supplieritem.name if self.supplieritem else None
        return result

    def supplieritem_item_number(self):
        """
        supplieritem_item_number

        Returns:
            string: item number from supplier item
        """
        result = self.supplieritem.item_number if self.supplieritem else None
        return result

    def supplieritem_reference_number(self):
        """
        supplieritem_reference_number

        Returns:
            string: reference number from supplier item
        """
        result = self.supplieritem.reference_number if self.supplieritem else None
        return result

    def supplieritem_slug(self):
        """
        supplieritem_slug

        Returns:
            _type_: slug from supplier item
        """
        result = self.supplieritem.slug if self.supplieritem else None
        return result

    def supplieritem_url_detail(self):
        """
        supplieritem_url_detail

        Returns:
            string: url from supplier item detail page
        """
        result = self.supplieritem.url_detail() if self.supplieritem else None
        return result

    # Storage Item
    def storageitem_id(self):
        """
        storageitem_id

        Returns:
            int: id from storage item
        """
        if self.supplieritem:
            result = self.supplieritem.storageitem_id()
        else:
            result = None
        return result

    def storageitem_name(self):
        """
        storageitem_name

        Returns:
            string: name from storage item
        """
        if self.supplieritem:
            result = self.supplieritem.storageitem_name()
        else:
            result = None
        return result

    def storageitem_reference_number(self):
        """
        storageitem_reference_number

        Returns:
            string: reference number from storage item
        """
        if self.supplieritem:
            result = self.supplieritem.storageitem_reference_number()
        else:
            result = None
        return result

    def storageitem_slug(self):
        """
        storageitem_slug

        Returns:
            string: slug from storage item
        """
        if self.supplieritem:
            result = self.supplieritem.storageitem_slug()
        else:
            result = None
        return result

    def storageitem_url_detail(self):
        """
        storageitem_url_detail

        Returns:
            string: url to storage item detail page
        """
        if self.supplieritem:
            result = self.supplieritem.storageitem_url_detail()
        else:
            result = None
        return result

    # Unit
    def unit(self):
        """
        unit

        Returns:
            string: unit from the supplier item
        """
        result = self.supplieritem.unit if self.supplieritem else None
        return result

    # fields/methodes for the unloading of a object
    def unload_date(self):
        """
        unload_date

        Returns:
            string: date from the unload
        """
        return self.unload_datetime_formated().split(" ")[0] if self.unload_datetime else None

    def unload_datetime_formated(self):
        """
        unload_datetime_formated

        Returns:
            string: datetime from the unload
        """
        return self.unload_datetime.strftime("%d.%m.%Y %H:%M:%S") if self.unload_datetime else None

    def unload_time(self):
        """
        unload_time

        Returns:
            string: time from the unloading point
        """
        return self.unload_datetime_formated().split(" ")[1] if self.unload_datetime else None

    def unload_username(self):
        """
        unload_username

        Returns:
            string: user name from who unloads
        """
        return str(self.unload_user_id.username) if self.unload_user_id else None

    # fields/methodes for the urls
    def url_delete(self):
        """
        url_delete

        Returns:
            string: url to delete page
        """
        return reverse('storagemanagement:storage_delete',kwargs={'storage':self.slug})

    def url_detail(self):
        """
        url_detail

        Returns:
            string: url to detail page
        """
        return reverse('storagemanagement:storage_detail',kwargs={'storage':self.slug})

    def url_qrcode(self):
        """
        url_qrcode

        Returns:
            string: url to qrcode page
        """
        return 'http://'+settings.HOST+self.url_detail()

    def url_unload(self):
        """
        url_unload

        Returns:
            string: url to unload page
        """
        return reverse('storagemanagement:storage_unload',kwargs={'storage':self.slug})

    def url_update(self):
        """
        url_update

        Returns:
            string: url to update page
        """
        return reverse('storagemanagement:storage_update',kwargs={'storage':self.slug})

    # fields/methodes for the value
    def value(self):
        """
        value

        Returns:
            float: price
        """
        return self.booking.price if self.booking else 0

    def __str__(self):
        return "{}-{}".format(self.short_name,self.id)

    class Meta:
        """
        Meta Data for model
        """
        app_label = 'storagemanagement'
        default_permissions = ()
        ordering = []
        permissions = (
            ('add_storage','Storage can view create'),
            ('change_storage','Storage can view change'),
            ('delete_storage','Storage can view delete'),
            ('detail_storage','Storage can view detail'),
            ('list_storage','Storage can view list'),
            ('table_storage','Storage can view table'),
            ('unload_storage','Storage can unload a Storage Item'),
            ('view_storage','Storage can view overview'),
        )
        proxy = True
        verbose_name = "Lager"
        verbose_name_plural = "Lager"
#--------------------------------------------------------------------------------
