#--------------------------------------------------------------------------------
# Models File from Model Booking
# 05.11.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

from tinymce import models as tinymce_models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.models import CreateData
from storagemanagement.models import ReferenceNumber
from storagemanagement.models import Slug
from storagemanagement.models import UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class BookingBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):

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

    # Fields/Methodes for the companyitem
    companyitem = models.ForeignKey(
        blank = True,
        name = 'companyitem',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'booking_companyitem',
        to = 'storagemanagement.companyitem',
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
        app_label = 'storagemanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class Booking(BookingBaseModel):

    # Company
    def company_id(self):
        if self.companyitem:
            result = self.companyitem.company.id if self.companyitem.company else None
        else:
            result = None
        return result

    def company_name(self):
        if self.companyitem:
            result = self.companyitem.company.name if self.companyitem.company else None
        else:
            result = None
        return result
        
    def company_reference_number(self):
        if self.companyitem:
            result = self.companyitem.company.reference_number if self.companyitem.company else None
        else:
            result = None
        return result
        
    def company_slug(self):
        if self.companyitem:
            result = self.companyitem.company.slug if self.companyitem.company else None
        else:
            result = None
        return result
        
    def company_url_detail(self):
        if self.companyitem:
            result = self.companyitem.company.url_detail() if self.companyitem.company else None
        else:
            result = None
        return result
        
    # Company Item
    def companyitem_id(self):
        result = self.companyitem.id if self.companyitem else None
        return result
        
    def companyitem_name(self):
        result = self.companyitem.name if self.companyitem else None
        return result
        
    def companyitem_item_number(self):
        result = self.companyitem.item_number if self.companyitem else None
        return result
        
    def companyitem_reference_number(self):
        result = self.companyitem.reference_number if self.companyitem else None
        return result
        
    def companyitem_slug(self):
        result = self.companyitem.slug if self.companyitem else None
        return result
        
    def companyitem_url_detail(self):
        result = self.companyitem.url_detail() if self.companyitem else None
        return result

    # Company
    def storageitem_id(self):
        if self.companyitem:
            result = self.companyitem.storageitem.id if self.companyitem.storageitem else None
        else:
            result = None
        return result

    def storageitem_name(self):
        if self.companyitem:
            result = self.companyitem.storageitem.name if self.companyitem.storageitem else None
        else:
            result = None
        return result
        
    def storageitem_reference_number(self):
        if self.companyitem:
            result = self.companyitem.storageitem.reference_number if self.companyitem.storageitem else None
        else:
            result = None
        return result
        
    def storageitem_slug(self):
        if self.companyitem:
            result = self.companyitem.storageitem.slug if self.companyitem.storageitem else None
        else:
            result = None
        return result
        
    def storageitem_url_detail(self):
        if self.companyitem:
            result = self.companyitem.storageitem.url_detail() if self.companyitem.storageitem else None
        else:
            result = None
        return result

    # Unit
    def unit(self):
        if self.companyitem:
            result = self.companyitem.unit
        else:
            result = None
        return result

    # Urls
    def url_delete(self):
        return reverse('storagemanagement:booking_delete',kwargs={'booking':self.slug})

    def url_detail(self):
        return reverse('storagemanagement:booking_detail',kwargs={'booking':self.slug})

    def url_qrcode(self):
        return 'http://'+settings.HOST+self.url_detail()

    def url_update(self):
        return reverse('storagemanagement:booking_update',kwargs={'booking':self.slug})

    def value(self):
        return self.price * self.amount

    def __str__(self):
        return "{}{:02d}{:02d}_{}".format(self.create_datetime.year,self.create_datetime.month,self.create_datetime.day,self.reference_number)

    
    class Meta:
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
        verbose_name = "Buchung"
        verbose_name_plural = "Buchungen"