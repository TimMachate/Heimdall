"""
#--------------------------------------------------------------------------------
# Models File from Model Booking
# 05.11.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
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
class BookingBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):
    """
    BookingBaseModel
    contains all model fields for the base booking obj
    """
    # Variables
    short_name = "STBO"

    # Fields/Methodes for the amount
    amount = models.IntegerField(
        blank = True,
        default = 0,
        help_text = 'Menge der Buchung',
        name = 'amount',
        null = True,
        verbose_name = 'Menge',
    )

    # Fields/Methodes for the supplieritem
    storageitem = models.ForeignKey(
        blank = True,
        name = 'storageitem',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'booking_storageitem',
        to = 'storagemanagement.storageitem',
        verbose_name = 'Artikel',
    )

    # Fields/Methodes for the supplieritem
    supplieritem = models.ForeignKey(
        blank = True,
        name = 'supplieritem',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'booking_supplieritem',
        to = 'storagemanagement.SupplierItem',
        verbose_name = 'Artikel',
    )

    # Fields/Methodes for the price
    price = models.DecimalField(
        blank = True,
        decimal_places = 2,
        default = 0,
        help_text = "Preis des Artikels.",
        max_digits = 12,
        name = 'price',
        null = True,
        verbose_name = 'Preis',
    )

    # Fields/Methodes for the stock
    stock = models.PositiveIntegerField(
        blank = True,
        default = 0,
        editable = False,
        help_text = "Der aktuelle Bestand im Lager.",
        name = 'stock',
        null = True,
        verbose_name = 'Bestand',
    )

    # Fields/Methodes for the notice
    notice = tinymce_models.HTMLField(
        blank = True,
        help_text = "Bemerkungen zum Prozess",
        name = 'notice',
        null = True,
        verbose_name = 'Bemerkung',
    )

    class Meta:
        """ Meta Data for the Model """
        app_label = 'storagemanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class Booking(BookingBaseModel):
    """
    Booking
    contains all model fields for the booking obj
    """

    # Supplier
    def supplier_id(self):
        """
        supplier_id
        returns id from supplier
        """
        if self.supplieritem:
            result = self.supplieritem.company.id if self.supplieritem.company else None
        else:
            result = None
        return result

    def supplier_name(self):
        """
        supplier_name
        returns name from supplier
        """
        if self.supplieritem:
            result = self.supplieritem.company.name if self.supplieritem.company else None
        else:
            result = None
        return result

    def supplier_reference_number(self):
        """
        supplier_reference_number
        returns reference number from supplier
        """
        if self.supplieritem:
            result = self.supplieritem.company.reference_number if self.supplieritem.company else None
        else:
            result = None
        return result

    def supplier_slug(self):
        """
        supplier_slug
        returns slug from supplier
        """
        if self.supplieritem:
            result = self.supplieritem.company.slug if self.supplieritem.company else None
        else:
            result = None
        return result

    def supplier_url_detail(self):
        """
        supplier_url_detail
        returns url from supplier
        """
        if self.supplieritem:
            result = self.supplieritem.company.url_detail() if self.supplieritem.company else None
        else:
            result = None
        return result

    # Supplier Item
    def supplieritem_id(self):
        """
        supplieritem_id
        returns id from supplier item
        """
        result = self.supplieritem.id if self.supplieritem else None
        return result

    def supplieritem_name(self):
        """
        supplieritem_name
        returns name from supplier item
        """
        result = self.supplieritem.name if self.supplieritem else None
        return result

    def supplieritem_item_number(self):
        """
        supplieritem_item_number
        returns item number from supplier item
        """
        result = self.supplieritem.item_number if self.supplieritem else None
        return result

    def supplieritem_reference_number(self):
        """
        supplieritem_reference_number
        returns supplier from supplier item
        """
        result = self.supplieritem.reference_number if self.supplieritem else None
        return result

    def supplieritem_slug(self):
        """
        supplieritem_slug
        returns slug from supplier item
        """
        result = self.supplieritem.slug if self.supplieritem else None
        return result

    def supplieritem_url_detail(self):
        """
        supplieritem_url_detail
        returns url from supplier item
        """
        result = self.supplieritem.url_detail() if self.supplieritem else None
        return result

    # Storage Item
    def storageitem_id(self):
        """
        storageitem_id
        returns id from storage item
        """
        if self.supplieritem:
            result = self.storageitem.id if self.storageitem else None
        else:
            result = None
        return result

    def storageitem_name(self):
        """
        storageitem_name
        returns name from storage item
        """
        if self.supplieritem:
            result = self.storageitem.name if self.storageitem else None
        else:
            result = None
        return result

    def storageitem_reference_number(self):
        """
        storageitem_reference_number
        returns reference number from storage item
        """
        if self.supplieritem:
            result = self.storageitem.reference_number if self.storageitem else None
        else:
            result = None
        return result

    def storageitem_slug(self):
        """
        storageitem_slug
        returns slug from storage item
        """
        if self.supplieritem:
            result = self.storageitem.slug if self.storageitem else None
        else:
            result = None
        return result

    def storageitem_url_detail(self):
        """
        storageitem_url_detail
        returns url from storage item
        """
        if self.supplieritem:
            result = self.storageitem.url_detail() if self.storageitem else None
        else:
            result = None
        return result

    # Unit
    def unit(self):
        """
        unit
        returns the unit from the booking
        """
        if self.supplieritem:
            result = self.supplieritem.unit
        else:
            result = None
        return result

    # Urls
    def url_delete(self):
        """
        url_delete
        returns url from delete page
        """
        return reverse('storagemanagement:booking_delete',kwargs={'booking':self.slug})

    def url_detail(self):
        """
        url_detail
        returns url from detail page
        """
        return reverse('storagemanagement:booking_detail',kwargs={'booking':self.slug})

    def url_qrcode(self):
        """
        url_qrcode
        returns url from qrcode page
        """
        return 'http://'+settings.HOST+self.url_detail()

    def url_update(self):
        """
        url_update
        returns url from update page
        """
        return reverse('storagemanagement:booking_update',kwargs={'booking':self.slug})

    def value(self):
        """
        value
        returns the value of the whole booking
        """
        return self.price * self.amount

    def __str__(self):
        return f"""{self.create_datetime.year}{self.create_datetime.month:02d}
        {self.create_datetime.day:02d}_{self.reference_number}"""

    class Meta:
        """ Meta Data for the Model """
        app_label = 'storagemanagement'
        default_permissions = ()
        ordering = []
        permissions = (
            ('add_booking','Booking can view create'),
            ('change_booking','Booking can view change'),
            ('delete_booking','Booking can view delete'),
            ('detail_booking','Booking can view detail'),
            ('list_booking','Booking can view list'),
            ('table_booking','Booking can view table'),
            ('view_booking','Booking can view overview'),
        )
        proxy = True
        verbose_name = "Buchung"
        verbose_name_plural = "Buchungen"
#--------------------------------------------------------------------------------
        