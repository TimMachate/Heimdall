#--------------------------------------------------------------------------------
# Models File from Model Offer Data
# 15.10.2023
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
class OfferDataBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STOD"
    
    # Fields/Methodes for the amount
    amount = models.PositiveIntegerField(
        blank = True,
        default = 0,
        name = "amount",
        null = True,
        verbose_name = "Menge",
    )

    # Fields/Methodes for the done
    authorized = models.BooleanField(
        blank = True,
        default = None,
        help_text = 'Angebot wurde autorisiert.',
        name = "authorized",
        null = True,
        verbose_name = "Autorisiert",
    )

    authorized_datetime = models.DateTimeField(
        blank = True,
        default = None,
        editable = True,
        help_text = "Zeitpunkt der Autorisierung.",
        name = 'authorized_datetime',
        null = True,
        verbose_name = 'Zeitpunkt der Autorisierung.',
    )

    authorized_user_id = models.ForeignKey(
        blank = True,
        default = None,
        editable = True,
        help_text = "Person der Autorisierung.",
        name = 'authorized_user_id',
        null = True,
        on_delete = models.PROTECT,
        related_name = "offerdata_authorized_user_id",
        to = get_user_model(),
        verbose_name = 'Autorisierer',
    )

    # Fields/Methodes for the companyitem
    companyitem = models.ForeignKey(
        blank = True,
        name = 'companyitem',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'offerdata_companyitem',
        to = 'storagemanagement.companyitem',
        verbose_name = 'Firmenartikel',
    )

    # Fields/Methodes for the done
    done = models.BooleanField(
        blank = True,
        default = False,
        help_text = 'Artikel des Angebotes wurde bearbeitet.',
        name = "done",
        null = True,
        verbose_name = "Erledigt",
    )

    # Fields/Methodes for the notice
    notice = tinymce_models.HTMLField(
        blank = True,
        help_text = "Nützliche Informationen für das Angebot.",
        name = 'notice',
        null = True,
        verbose_name = 'Bemerkung',
    )

    # Fields/Methodes for the offer
    offer = models.ForeignKey(
        blank = True,
        name = 'offer',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'offerdata_offer',
        to = 'storagemanagement.offer',
        verbose_name = 'Angebot',
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

    # Fields/Methodes for the ware
    storageitem = models.ForeignKey(
        blank = True,
        name = 'storageitem',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'offerdata_storageitem',
        to = 'storagemanagement.storageitem',
        verbose_name = 'Lagerartikel',
    )

    class Meta:
        app_label = 'storagemanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class OfferData(OfferDataBaseModel):

    # Authorized
    def authorized_date(self):
        return self.authorized_datetime_formated().split(" ")[0] if self.authorized_datetime else None

    def authorized_datetime_formated(self):
        return self.authorized_datetime.strftime("%d.%m.%Y %H:%M:%S") if self.authorized_datetime else None

    def authorized_time(self):
        return self.authorized_datetime_formated().split(" ")[1] if self.authorized_datetime else None

    def authorized_username(self):
        return str(self.authorized_user_id.username) if self.authorized_user_id else None

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

    # Offer
    def offer_id(self):
        result = self.offer.id if self.offer else None
        return result
        
    def offer_reference_number(self):
        result = self.offer.reference_number if self.offer else None
        return result
        
    def offer_slug(self):
        result = self.offer.slug if self.offer else None
        return result
        
    def offer_url_detail(self):
        result = self.offer.url_detail() if self.offer else None
        return result

    # Storage Item
    def storageitem_id(self):
        return self.storageitem.id if self.storageitem else None

    def storageitem_name(self):
        return self.storageitem.name if self.storageitem else None
        
    def storageitem_reference_number(self):
        return self.storageitem.reference_number if self.storageitem else None
        
    def storageitem_slug(self):
        return self.storageitem.slug if self.storageitem else None
        
    def storageitem_url_detail(self):
        return self.storageitem.url_detail() if self.storageitem else None
    
    # Unit
    def unit(self):
        result = self.companyitem.unit if self.companyitem else None
        return result

    # Urls
    def url_authorize_true(self):
        return reverse('storagemanagement:offerdata_authorize_true',kwargs={'offerdata':self.slug})

    def url_authorize_false(self):
        return reverse('storagemanagement:offerdata_authorize_false',kwargs={'offerdata':self.slug})

    def url_delete(self):
        return reverse('storagemanagement:offerdata_delete',kwargs={'offerdata':self.slug})

    def url_detail(self):
        return reverse('storagemanagement:offerdata_detail',kwargs={'offerdata':self.slug})

    def url_qrcode(self):
        return 'http://'+settings.HOST+self.url_detail()

    def url_recived(self):
        return reverse('storagemanagement:offerdata_recived',kwargs={'offerdata':self.slug})

    def url_sent(self):
        return reverse('storagemanagement:offerdata_sent',kwargs={'offerdata':self.slug})

    def url_update(self):
        return reverse('storagemanagement:offerdata_update',kwargs={'offerdata':self.slug})
    
    def __str__(self):
        return "{}{}{}_{}".format(self.create_datetime.year,self.create_datetime.month,self.create_datetime.day,self.reference_number)

    def value(self):
        result = self.price*self.amount
        return result

    class Meta:
        app_label = 'storagemanagement'
        default_permissions = ()
        ordering = []
        permissions = (
            ('add_offerdata','OfferData can view create'),
            ('authorize_true_offerdata','OfferData can authorize true'),
            ('authorize_false_offerdata','OfferData can authorize false'),
            ('change_offerdata','OfferData can view change'),
            ('delete_offerdata','OfferData can view delete'),
            ('detail_offerdata','OfferData can view detail'),
            ('list_offerdata','OfferData can view list'),
            ('send_offerdata','OfferData can send offerdata'),
            ('table_offerdata','OfferData can view table'),
            ('view_offerdata','OfferData can view overview'),
        )
        verbose_name = "Angebot Artikel"
        verbose_name_plural = "Angebote Artikel"