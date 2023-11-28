#--------------------------------------------------------------------------------
# Models File from Model StorageItem
# 05.11.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.apps import apps
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.models import CreateData,ReferenceNumber,Slug,UpdateData
from storagemanagement.booking.models import Booking
from storagemanagement.companyitem.models import CompanyItem
from storagemanagement.storage.models import Storage
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class StorageItemBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):

    short_name = "STIT"

    # Fields/Methodes for the booking
    companyitem = models.ForeignKey(
        blank = True,
        help_text = 'Artikel des Standardlieferanten',
        name = 'companyitem',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'storageitem_companyitem',
        to = 'storagemanagement.companyitem',
        verbose_name = 'Standardartikel',
    )
        
    # Fields/Methodes for the maximum
    maximum = models.PositiveIntegerField(
        blank = True,
        default = 0,
        help_text = "Maximale Lagermenge.",
        name = 'maximum',
        null = True,
        verbose_name = 'Maximum',
        )

    # Fields/Methodes for the minimum
    minimum = models.PositiveIntegerField(
        blank = True,
        default = 0,
        help_text = "Minimale Lagermenge.",
        name = 'minimum',
        null = True,
        verbose_name = 'Minimum',
        )

    # Fields/Methodes for the minimum
    name = models.CharField(
        blank = True,
        help_text = "Name des Artikels.",
        max_length = 200,
        name = 'name',
        null = True,
        verbose_name = 'Name',
        )

    # Fields/Methodes for the warning
    warning = models.PositiveIntegerField(
        blank = True,
        default = 0,
        help_text = "Warnung Lagermenge.",
        name = 'warning',
        null = True,
        verbose_name = 'warning',
        )

    class Meta:
        app_label = 'storagemanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class StorageItem(StorageItemBaseModel):

    # Fields/Methodes for the booking
    def booking(self):
        result = Booking.objects.filter(companyitem__in=self.suppliers())
        if result == []:
            result = None
        return result

    def booking_count(self):
        objects = self.booking()
        result = objects.count() if objects else 0
        return result
    
    def booking_last(self):
        objects = self.booking()
        result = objects.last() if objects else None
        return result

    # Fields/Methodes for the company
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

    # Fields/Methodes for the company
    def companyitem_id(self):
        result = self.companyitem.id if self.companyitem else None
        return result

    def companyitem_item_number(self):
        result = self.companyitem.item_number if self.companyitem else None
        return result
        
    def companyitem_name(self):
        result = self.companyitem.name if self.companyitem else None
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

    # Fields/Methodes for the status
    def status(self):
        count = self.stock_count()
        if count > self.maximum or self.maximum == 0:
            result = 'overload'
        elif count > self.warning:
            result = 'ok'
        elif count > self.minimum:
            result = 'warning'
        else:
            result = 'alarm'
        return result

    # Fields/Methodes for the stock
    def stock(self):
        result = Storage.objects.filter(companyitem__in=self.suppliers(),unload_datetime=None)
        if result == []:
            result = None
        return result

    def stock_count(self):
        queryset = self.stock()
        result = queryset.count() if queryset else 0
        return result

    def stock_percentage(self):
        count = self.stock_count()
        maximum = self.maximum
        result = int(count/maximum*100) if count > 0 and maximum > 0 else int(0)
        return result

    def stock_value(self):
        objects = self.stock()
        if objects:
            result = 0
            for obj in objects:
                result += obj.value()
        else:
            result = 0
        return result

    # Fields/Methodes for the suppliers
    def suppliers(self):
        result = CompanyItem.objects.filter(storageitem=self)
        if result == []:
            result = None
        return result

    def supplier_count(self):
        queryset = self.suppliers()
        result = queryset.count() if queryset else 0
        return result

    # Fields/Methodes for the urls
    def url_booking(self):
        return reverse('storagemanagement:storageitem_booking_overview',kwargs={'storageitem':self.slug})

    def url_booking_list(self):
        return reverse('storagemanagement:storageitem_booking_list',kwargs={'storageitem':self.slug})

    def url_booking_table(self):
        return reverse('storagemanagement:storageitem_booking_table',kwargs={'storageitem':self.slug})

    def url_booking_add(self):
        return reverse('storagemanagement:storageitem_booking_add',kwargs={'storageitem':self.slug})

    def url_booking_create(self):
        return reverse('storagemanagement:storageitem_booking_create',kwargs={'storageitem':self.slug})

    def url_booking_remove(self):
        return reverse('storagemanagement:storageitem_booking_remove',kwargs={'storageitem':self.slug})
    
    def url_booking_create_add_remove(self):
        return reverse('storagemanagement:storageitem_booking_create_add_remove',kwargs={'storageitem':self.slug})

    def url_delete(self):
        return reverse('storagemanagement:storageitem_delete',kwargs={'storageitem':self.slug})

    def url_detail(self):
        return reverse('storagemanagement:storageitem_detail',kwargs={'storageitem':self.slug})

    def url_qrcode(self):
        return 'http://'+settings.HOST+self.url_detail()

    def url_qrcode_booking_add(self):
        return 'http://'+settings.HOST+self.url_booking_add()

    def url_qrcode_booking_remove(self):
        return 'http://'+settings.HOST+self.url_booking_remove()
    
    def url_qrcode_request(self):
        return 'http://'+settings.HOST+self.url_request_create()
    
    def url_request_create(self):
        return reverse('storagemanagement:storageitem_request_create',kwargs={'storageitem':self.slug})

    def url_storage(self):
        return reverse('storagemanagement:storageitem_storage_overview',kwargs={'storageitem':self.slug})

    def url_storage_list(self):
        return reverse('storagemanagement:storageitem_storage_list',kwargs={'storageitem':self.slug})

    def url_storage_table(self):
        return reverse('storagemanagement:storageitem_storage_table',kwargs={'storageitem':self.slug})

    def url_storage_create(self):
        return reverse('storagemanagement:storageitem_storage_create',kwargs={'storageitem':self.slug})

    def url_update(self):
        return reverse('storagemanagement:storageitem_update',kwargs={'storageitem':self.slug})
    
    def __str__(self):
        return "{} ({})".format(str(self.name),str(self.reference_number))

    class Meta:
        app_label = 'storagemanagement'
        ordering = []
        default_permissions = ()
        permissions = (
            ('add_storageitem','StorageItem can view create'),
            ('change_storageitem','StorageItem can view change'),
            ('delete_storageitem','StorageItem can view delete'),
            ('detail_storageitem','StorageItem can view detail'),
            ('list_storageitem','StorageItem can view list'),
            ('table_storageitem','StorageItem can view table'),
            ('view_storageitem','StorageItem can view overview'),
        )
        proxy = True
        verbose_name = 'Lagerartikel'
        verbose_name_plural = 'Lagerartikel'