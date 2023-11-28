#--------------------------------------------------------------------------------
# Model File from Model Ware
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.apps import apps
from django.conf import settings
from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.booking.models import Booking
from storagemanagement.storage.models import Storage
if 'relationshipmanagement' in [app.name for app in apps.get_app_configs()]:
    from relationshipmanagement.companyitem.model import CompanyItem
else:
    from storagemanagement.models import (
        CreateData,
        ReferenceNumber,
        Slug,
        UpdateData
        )
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
if not 'relationshipmanagement' in [app.name for app in apps.get_app_configs()]:
    class CompanyItemBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):

        # Variables
        short_name = "STCI"

        class Units(models.TextChoices):
            PIECE = "Stk",_("Stk")
            MILLIMETER = "mm",_("mm")
            METER = "m",_("m")
            KILOMETER = "km",_("km")
            MILLIGRAMM = "mg",_("mg")
            GRAMM = "g",_("g")
            KILOGRAMM = "kg",_("kg")
            TONNES = "t",_("t")
            MILLILITER = "ml",_("ml")
            LITER = "l",_("l")

        # Fields/Methodes for the company
        company = models.ForeignKey(
            blank = True,
            name = 'company',
            null = True,
            on_delete = models.CASCADE,
            related_name = 'companyitem_company',
            to = 'storagemanagement.Company',
            verbose_name = 'Firma',
        )

        # Fields/Methodes for the image
        if 'documentationmanagement' in [app.name for app in apps.get_app_configs()]:
            image = models.ForeignKey(
                blank = True,
                help_text = "Bild des Artikels.",
                name = 'image',
                null = True,
                on_delete = models.CASCADE,
                related_name = 'companyitem_image',
                to = 'documentationmanagement.PictureProxy',
                verbose_name = 'Bild',
            )
        else:
            image = models.FileField(
                blank = True,
                help_text = "Bild des Artikels.",
                name = "image",
                null = True,
                upload_to = 'storagemanagement/companyitem/',
                verbose_name = "Bild",
            )

        # Fields/Methodes for the name
        name = models.CharField(
            blank = True,
            help_text = "Name der Ware.",
            max_length = 200,
            name = 'name',
            null = True,
            verbose_name = 'Name',
        )

        # Fields/Methodes for the price
        price = models.DecimalField(
            blank = True,
            decimal_places = 2,
            default = 0.00,
            help_text = "Preis der Ware.",
            max_digits = 12,
            name = 'price',
            null = True,
            verbose_name = 'Preis',
        )

        # Fields/Methodes for the storageitem
        storageitem = models.ForeignKey(
            blank = True,
            help_text = "Artikel im eigenen Lager.",
            name = 'storageitem',
            null = True,
            on_delete = models.CASCADE,
            related_name = 'companyitem_storageitem',
            to = 'storagemanagement.storageitem',
            verbose_name = 'Lagerartikel',
        )

        # Fields/Methodes for the unit
        unit = models.CharField(
            blank = True,
            choices = Units.choices,
            default = Units.PIECE,
            help_text = "Einheit der Ware.",
            max_length = 3,
            name = 'unit',
            null = True,
            verbose_name = 'Einheit',
        )

        # Fields/Methodes for the name
        item_number = models.CharField(
            blank = True,
            help_text = "Warennummer der Ware.",
            max_length = 200,
            name = 'item_number',
            null = True,
            verbose_name = 'Artikelnummer',
        )

        class Meta:
            app_label = 'storagemanagement'
            default_permissions = ()
#--------------------------------------------------------------------------------
class CompanyItem(CompanyItemBaseModel):

    # Fields/Methodes for the booking
    def booking(self):
        result = Booking.objects.filter(companyitem=self)
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

    # Company
    def company_id(self):
        result = self.company.id if self.company else None
        return result
        
    def company_name(self):
        result = self.company.name if self.company else None
        return result
        
    def company_reference_number(self):
        result = self.company.reference_number if self.company else None
        return result
        
    def company_slug(self):
        result = self.company.slug if self.company else None
        return result
        
    def company_url_detail(self):
        result = self.company.url_detail() if self.company else None
        return result

    # Fields/Methodes for the stock
    def stock(self):
        result = Storage.objects.filter(companyitem=self,unload_datetime=None)
        if result == []:
            result = None
        return result

    def stock_count(self):
        queryset = self.stock()
        result = queryset.count() if queryset else 0
        return result

    def stock_value(self):
        objects = self.stock()
        if objects:
            result = 0
            for obj in objects:
                result += obj.booking.price
        else:
            result = 0
        return result

    # Storage Item
    def storageitem_id(self):
        result = self.storageitem.id if self.storageitem else None
        return result
        
    def storageitem_name(self):
        result = self.storageitem.name if self.storageitem else None
        return result
        
    def storageitem_reference_number(self):
        result = self.storageitem.reference_number if self.storageitem else None
        return result
        
    def storageitem_slug(self):
        result = self.storageitem.slug if self.storageitem else None
        return result
        
    def storageitem_url_detail(self):
        result = self.storageitem.url_detail() if self.storageitem else None
        return result

    # Fields/Methodes for the urls
    def url_booking(self):
        return reverse('storagemanagement:companyitem_booking_overview',kwargs={'companyitem':self.slug})
    
    def url_booking_list(self):
        return reverse('storagemanagement:companyitem_booking_list',kwargs={'companyitem':self.slug})
    
    def url_booking_table(self):
        return reverse('storagemanagement:companyitem_booking_table',kwargs={'companyitem':self.slug})

    def url_booking_add(self):
        return reverse('storagemanagement:companyitem_booking_add',kwargs={'companyitem':self.slug})

    def url_booking_create(self):
        return reverse('storagemanagement:companyitem_booking_create',kwargs={'companyitem':self.slug})

    def url_booking_remove(self):
        return reverse('storagemanagement:companyitem_booking_remove',kwargs={'companyitem':self.slug})

    def url_delete(self):
        return reverse('storagemanagement:companyitem_delete',kwargs={'companyitem':self.slug})

    def url_detail(self):
        return reverse('storagemanagement:companyitem_detail',kwargs={'companyitem':self.slug})

    def url_qrcode(self):
        return 'http://'+settings.HOST+self.url_detail()

    def url_qrcode_booking_add(self):
        return 'http://'+settings.HOST+self.url_booking_add()
    
    def url_qrcode_booking_create(self):
        return 'http://'+settings.HOST+self.url_booking_create()

    def url_qrcode_booking_remove(self):
        return 'http://'+settings.HOST+self.url_booking_remove()
    
    def url_qrcode_request(self):
        return 'http://'+settings.HOST+self.url_request_create()
    
    def url_request_create(self):
        return reverse('storagemanagement:companyitem_request_create',kwargs={'companyitem':self.slug})

    def url_storage(self):
        return reverse('storagemanagement:companyitem_storage_overview',kwargs={'companyitem':self.slug})

    def url_storage_create(self):
        return reverse('storagemanagement:companyitem_storage_create',kwargs={'companyitem':self.slug})
    
    def url_storage_list(self):
        return reverse('storagemanagement:companyitem_storage_list',kwargs={'companyitem':self.slug})
    
    def url_storage_table(self):
        return reverse('storagemanagement:companyitem_storage_table',kwargs={'companyitem':self.slug})

    def url_update(self):
        return reverse('storagemanagement:companyitem_update',kwargs={'companyitem':self.slug})
    
    def __str__(self):
        return "{} ({})".format(str(self.name),str(self.item_number))
        
    class Meta:
        app_label = 'storagemanagement'
        default_permissions = ()
        ordering = []
        permissions = (
            ('add_companyitem','CompanyItem can view create'),
            ('change_companyitem','CompanyItem can view change'),
            ('delete_companyitem','CompanyItem can view delete'),
            ('detail_companyitem','CompanyItem can view detail'),
            ('list_companyitem','CompanyItem can view list'),
            ('table_companyitem','CompanyItem can view table'),
            ('view_companyitem','CompanyItem can view overview'),
        )
        proxy = True
        verbose_name = "Firmenartikel"
        verbose_name_plural = "Firmenartikel"