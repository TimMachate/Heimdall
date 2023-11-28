#--------------------------------------------------------------------------------
# Models File from Model Storage
# 03.11.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
from django.contrib.auth import get_user_model
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
class StorageBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STST"

    # Fields/Methodes for the companyitem
    companyitem = models.ForeignKey(
        blank = True,
        name = 'companyitem',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'storage_companyitem',
        to = 'storagemanagement.companyitem',
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
        app_label = 'storagemanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class Storage(StorageBaseModel):

    # Booking
    def booking_id(self):
        result = self.booking.id if self.booking else None
        return result
        
    def booking_reference_number(self):
        result = self.booking.reference_number if self.booking else None
        return result
        
    def booking_slug(self):
        result = self.booking.slug if self.booking else None
        return result
        
    def booking_url_detail(self):
        result = self.booking.url_detail() if self.booking else None
        return result

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
        result = self.companyitem.unit if self.companyitem else None
        return result

    # fields/methodes for the unloading of a object
    def unload_date(self):
        return self.unload_datetime_formated().split(" ")[0] if self.unload_datetime else None

    def unload_datetime_formated(self):
        return self.unload_datetime.strftime("%d.%m.%Y %H:%M:%S") if self.unload_datetime else None

    def unload_time(self):
        return self.unload_datetime_formated().split(" ")[1] if self.unload_datetime else None

    def unload_username(self):
        return str(self.unload_user_id.username) if self.unload_user_id else None

    # fields/methodes for the urls
    def url_delete(self):
        return reverse('storagemanagement:storage_delete',kwargs={'storage':self.slug})

    def url_detail(self):
        return reverse('storagemanagement:storage_detail',kwargs={'storage':self.slug})

    def url_qrcode(self):
        return 'http://'+settings.HOST+self.url_detail()

    def url_unload(self):
        return reverse('storagemanagement:storage_unload',kwargs={'storage':self.slug})

    def url_update(self):
        return reverse('storagemanagement:storage_update',kwargs={'storage':self.slug})

    # fields/methodes for the value
    def value(self):
        return self.booking.price if self.booking else 0

    def __str__(self):
        return "{}-{}".format(self.short_name,self.id)
    
    class Meta:
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
        verbose_name = "Lager"
        verbose_name_plural = "Lager"