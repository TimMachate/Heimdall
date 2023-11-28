#--------------------------------------------------------------------------------
# Models File from Model Order Data
# 10.11.2023
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
class OrderDataBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STDA"

    # Fields/Methodes for the amount
    amount = models.PositiveIntegerField(
        blank = True,
        default = 0,
        name = "amount",
        null = True,
        verbose_name = "Menge",
    )

    amount_recived = models.PositiveIntegerField(
        blank = True,
        name = "amount_recived",
        null = True,
        verbose_name = "Erhaltene Menge",
    )

    # Fields/Methodes for the authorized
    authorized = models.BooleanField(
        blank = True,
        default = None,
        help_text = 'Bestellung wurde autorisiert.',
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
        related_name = "orderdata_authorized_user_id",
        to = get_user_model(),
        verbose_name = 'Autorisierer',
    )

    # Fields/Methodes for the booking
    booking = models.BooleanField(
        blank = True,
        default = None,
        help_text = 'Bestellung wurde gebucht.',
        name = "booking",
        null = True,
        verbose_name = "Gebucht",
    )

    booking_datetime = models.DateTimeField(
        blank = True,
        default = None,
        editable = True,
        help_text = "Zeitpunkt der Buchung.",
        name = 'booking_datetime',
        null = True,
        verbose_name = 'Zeitpunkt der Buchung.',
    )

    booking_user_id = models.ForeignKey(
        blank = True,
        default = None,
        editable = True,
        help_text = "Person der Buchung.",
        name = 'booking_user_id',
        null = True,
        on_delete = models.PROTECT,
        related_name = "orderdata_booking_user_id",
        to = get_user_model(),
        verbose_name = 'Bucher',
    )

    # Fields/Methodes for the companyitem
    companyitem = models.ForeignKey(
        blank = True,
        name = 'companyitem',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'orderdata_companyitem',
        to = 'storagemanagement.companyitem',
        verbose_name = 'Firmenartikel',
    )

    # Fields/Methodes for the done
    done = models.BooleanField(
        blank = True,
        default = False,
        help_text = 'Angebot wurde erledigt.',
        name = "done",
        null = False,
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
        blank=True,
        name='offer',
        null=True,
        on_delete=models.CASCADE,
        related_name='order_offer',
        to='storagemanagement.offer',
        verbose_name='Angebot',
    )

    # Fields/Methodes for the order
    order = models.ForeignKey(
        blank = True,
        name = 'order',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'orderdata_order',
        to = 'storagemanagement.order',
        verbose_name = 'Bestellung',
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

    class Meta:
        app_label = 'storagemanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class OrderData(OrderDataBaseModel):

    # Authorized
    def authorized_date(self):
        return self.authorized_datetime_formated().split(" ")[0] if self.authorized_datetime else None

    def authorized_datetime_formated(self):
        return self.authorized_datetime.strftime("%d.%m.%Y %H:%M:%S") if self.authorized_datetime else None

    def authorized_time(self):
        return self.authorized_datetime_formated().split(" ")[1] if self.authorized_datetime else None

    def authorized_username(self):
        return str(self.authorized_user_id.username) if self.authorized_user_id else None

    # Booking
    def booking_date(self):
        return self.booking_datetime_formated().split(" ")[0] if self.booking_datetime else None

    def booking_datetime_formated(self):
        return self.booking_datetime.strftime("%d.%m.%Y %H:%M:%S") if self.booking_datetime else None

    def booking_time(self):
        return self.booking_datetime_formated().split(" ")[1] if self.booking_datetime else None

    def booking_username(self):
        return str(self.booking_user_id.username) if self.booking_user_id else None

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

    def offer_file_name(self):
        result = None
        if self.offer:
            result = self.offer.offer_file.name if self.offer.offer_file else None
        return result

    def offer_file_url(self):
        result = None
        if self.offer:
            result = self.offer.offer_file.url if self.offer.offer_file else None
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
    
    # Order
    def order_id(self):
        result = self.order.id if self.order else None
        return result
        
    def order_reference_number(self):
        result = self.order.reference_number if self.order else None
        return result
        
    def order_slug(self):
        result = self.order.slug if self.order else None
        return result
        
    def order_url_detail(self):
        result = self.order.url_detail() if self.order else None
        return result

    # Storage Item
    def storageitem_id(self):
        result = None
        if self.companyitem:
            result = self.companyitem.storageitem.id if self.companyitem.storageitem else None
        return result
        
    def storageitem_name(self):
        result = None
        if self.companyitem:
            result = self.companyitem.storageitem.name if self.companyitem.storageitem else None
        return result
        
    def storageitem_reference_number(self):
        result = None
        if self.companyitem:
            result = self.companyitem.storageitem.reference_number if self.companyitem.storageitem else None
        return result
        
    def storageitem_slug(self):
        result = None
        if self.companyitem:
            result = self.companyitem.storageitem.slug if self.companyitem.storageitem else None
        return result
        
    def storageitem_url_detail(self):
        result = None
        if self.companyitem:
            result = self.companyitem.storageitem.url_detail() if self.companyitem.storageitem else None
        return result

    # Unit
    def unit(self):
        result = self.companyitem.unit if self.companyitem else None
        return result

    # Urls
    def url_authorize_true(self):
        return reverse('storagemanagement:orderdata_authorize_true',kwargs={'orderdata':self.slug})

    def url_authorize_false(self):
        return reverse('storagemanagement:orderdata_authorize_false',kwargs={'orderdata':self.slug})

    def url_booking_true(self):
        return reverse('storagemanagement:orderdata_booking_true',kwargs={'orderdata':self.slug})

    def url_booking_false(self):
        return reverse('storagemanagement:orderdata_booking_false',kwargs={'orderdata':self.slug})

    def url_delete(self):
        return reverse('storagemanagement:orderdata_delete',kwargs={'orderdata':self.slug})

    def url_detail(self):
        return reverse('storagemanagement:orderdata_detail',kwargs={'orderdata':self.slug})

    def url_qrcode(self):
        return 'http://'+settings.HOST+self.url_detail()

    def url_recived(self):
        return reverse('storagemanagement:orderdata_recived',kwargs={'orderdata':self.slug})

    def url_sent(self):
        return reverse('storagemanagement:orderdata_sent',kwargs={'orderdata':self.slug})

    def url_update(self):
        return reverse('storagemanagement:orderdata_update',kwargs={'orderdata':self.slug})
    
    def __str__(self):
        return "{}{}{}_{}".format(self.create_datetime.year,self.create_datetime.month,self.create_datetime.day,self.companyitem.slug)

    def value(self):
        return self.price * self.amount

    class Meta:
        app_label = 'storagemanagement'
        default_permissions = ()
        ordering = []
        permissions = (
            ('add_orderdata','OrderData can view create'),
            ('authorize_true_orderdata','OrderData can authorize true'),
            ('authorize_false_orderdata','OrderData can authorize false'),
            ('booking_true_orderdata','OrderData can booking true'),
            ('booking_false_orderdata','OrderData can booking false'),
            ('change_orderdata','OrderData can view change'),
            ('delete_orderdata','OrderData can view delete'),
            ('detail_orderdata','OrderData can view detail'),
            ('list_orderdata','OrderData can view list'),
            ('table_orderdata','OrderData can view table'),
            ('view_orderdata','OrderData can view overview'),
        )
        verbose_name = "Bestellung Artikel"
        verbose_name_plural = "Bestellungen Artikel"