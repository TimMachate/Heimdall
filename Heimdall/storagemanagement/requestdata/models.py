#--------------------------------------------------------------------------------
# Models File from Model Request Data
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
class RequestDataBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STRE"

    # Fields/Methodes for the amount
    amount = models.PositiveIntegerField(
        blank = True,
        name = "amount",
        null = True,
        verbose_name = "Menge",
    )

    # Fields/Methodes for the deny
    authorized = models.BooleanField(
        blank = True,
        default = None,
        help_text = 'Anfrage wurde autorisiert.',
        name = "authorized",
        null = True,
        verbose_name = "Autorisiert",
    )

    authorized_datetime = models.DateTimeField(
        blank = True,
        default = None,
        editable = False,
        help_text = "Zeitpunkt der Autorisierung.",
        name = 'authorized_datetime',
        null = True,
        verbose_name = 'Zeitpunkt der Autorisierung.',
    )

    authorized_username = models.ForeignKey(
        blank = True,
        default = None,
        editable = False,
        help_text = "Person der Autorisierung.",
        name = 'authorized_user_id',
        null = True,
        on_delete = models.PROTECT,
        related_name = "requestdata_authorized_user_id",
        to = get_user_model(),
        verbose_name = 'Autorisierer',
    )

    # Fields/Methodes for the ware
    companyitem = models.ForeignKey(
        blank = True,
        name = 'companyitem',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'requestdata_companyitem',
        to = 'storagemanagement.companyitem',
        verbose_name = 'Item',
    )

    # Fields/Methodes for the done
    done = models.BooleanField(
        default = False,
        help_text = 'Bearbeitung der Anfrage Ja/Nein',
        name="done",
        null = False,
        verbose_name = "Bearbeitet",
    )

    # Fields/Methodes for the notice
    notice = tinymce_models.HTMLField(
        blank = True,
        help_text = "Nützliche Informationen zur Anfrage.",
        name = 'notice',
        null = True,
        verbose_name = 'Bemerkung',
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
        related_name = 'requestdata_storageitem',
        to = 'storagemanagement.storageitem',
        verbose_name = 'Item',
    )

    class Meta:
        app_label = 'storagemanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class RequestData(RequestDataBaseModel):

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

    def status(self):
        if self.orderprocess:
            result = self.orderprocess.Status(self.orderprocess.status).label
        else:
            result = None
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
        return reverse('storagemanagement:requestdata_authorize_true',kwargs={'requestdata':self.slug})

    def url_authorize_false(self):
        return reverse('storagemanagement:requestdata_authorize_false',kwargs={'requestdata':self.slug})

    def url_delete(self):
        return reverse('storagemanagement:requestdata_delete',kwargs={'requestdata':self.slug})

    def url_detail(self):
        return reverse('storagemanagement:requestdata_detail',kwargs={'requestdata':self.slug})

    def url_qrcode(self):
        return 'http://'+settings.HOST+self.url_detail()

    def url_update(self):
        return reverse('storagemanagement:requestdata_update',kwargs={'requestdata':self.slug})
    
    # Value
    def value(self):
        result = self.amount * self.price
        return result
    
    def __str__(self):
        return "{}{}{}_{}".format(self.create_datetime.year,self.create_datetime.month,self.create_datetime.day,self.companyitem.slug)

    class Meta:
        app_label = 'storagemanagement'
        default_permissions = ()
        ordering = []
        permissions = (
            ('add_requestdata','RequestData can view create'),
            ('authorize_true_requestdata','RequestData can authorize true'),
            ('authorize_false_requestdata','RequestData can authorize false'),
            ('change_requestdata','RequestData can view change'),
            ('delete_requestdata','RequestData can view delete'),
            ('detail_requestdata','RequestData can view detail'),
            ('list_requestdata','RequestData can view list'),
            ('table_requestdata','RequestData can view table'),
            ('view_requestdata','RequestData can view overview'),
        )
        verbose_name = "Anfrage"
        verbose_name_plural = "Anfragen"