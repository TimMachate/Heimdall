#--------------------------------------------------------------------------------
# Models File from Model Order
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
from storagemanagement.orderdata.models import OrderData
from tools.createdata.models import CreateData
from tools.referencenumber.models import ReferenceNumber
from tools.slug.models import Slug
from tools.updatedata.models import UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class OrderBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "PROR"


    order_file = models.FileField(
        blank = True,
        help_text = "Verschickte Bestellung",
        name = "order_file",
        null = True,
        upload_to = 'storagemanagement/order/order',
        verbose_name = "Bestellung",
    )

    # Fields/Methodes for the done
    done = models.BooleanField(
        blank = True,
        default = False,
        help_text = 'Angebot wurde bearbeitet.',
        name = "done",
        null = False,
        verbose_name = "Bearbeitet",
    ) 

    delivery_note = models.FileField(
        blank = True,
        help_text = "Erhaltener Lieferschein",
        name = "delivery_note",
        null = True,
        upload_to = 'storagemanagement/offer/deliverynote/',
        verbose_name = "Lieferschein",
    )

    # Fields/Methodes for the notice
    notice = tinymce_models.HTMLField(
        blank = True,
        help_text = "Nützliche Informationen zum Angebot.",
        name = 'notice',
        null = True,
        verbose_name = 'Bemerkung',
    )

    # Fields/Methodes for the orderdata_recived
    recived = models.BooleanField(
        blank = True,
        default = False,
        help_text = 'Bestellung angekommen.',
        name = "recived",
        null = False,
        verbose_name = "Erhalten.",
    )

    recived_datetime = models.DateTimeField(
        blank = True,
        default = None,
        editable = True,
        help_text = "Zeitpunkt des Erhalten der Bestellung.",
        name = 'sent_datetime',
        null = True,
        verbose_name = 'Ankunft der Bestellung.',
    )

    recived_user_id = models.ForeignKey(
        blank = True,
        default = None,
        editable = True,
        help_text = "Person die die Bestellung erhalten hat.",
        name = 'recived_user_id',
        null = True,
        on_delete = models.PROTECT,
        related_name = "order_recived_user_id",
        to = get_user_model(),
        verbose_name = 'Person des Erhalten der Bestellung',
    )

    # Fields/Methodes for the orderdata_request
    sent = models.BooleanField(
        blank = True,
        default = False,
        help_text = 'Bestellung wurde rausgeschickt.',
        name = "sent",
        null = False,
        verbose_name = "Bestellt.",
    )

    sent_datetime = models.DateTimeField(
        blank = True,
        default = None,
        editable = True,
        help_text = "Zeitpunkt der Bestellung.",
        name = 'recived_datetime',
        null = True,
        verbose_name = 'Zeitpunkt der Bestellung.',
    )

    sent_user_id = models.ForeignKey(
        blank = True,
        default = None,
        editable = True,
        help_text = "Person die bestellt hat.",
        name = 'sent_user_id',
        null = True,
        on_delete = models.PROTECT,
        related_name = "order_sent_user_id",
        to = get_user_model(),
        verbose_name = 'Besteller',
    )

    class Meta:
        app_label = 'storagemanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class Order(OrderBaseModel):

    # Authorized
    def authorized(self):
        queryset = self.orderdata()
        result = None
        if queryset.exists():
            if queryset.filter(authorized=None).count() == 0:
                result = True
        return result

    # Booked
    def booked(self):
        queryset = self.orderdata()
        result = None
        if queryset.exists():
            if queryset.filter(booking=None).count() == 0:
                result = True
        return result

    # Company
    def company(self):
        result = None
        if self.orderdata():
            if self.orderdata().exists():
                result = self.orderdata().first().companyitem.company
        return result

    def company_id(self):
        if self.company():
            result = self.company().id if self.company() else None
        else:
            result = None
        return result

    def company_name(self):
        if self.company():
            result = self.company().name if self.company() else None
        else:
            result = None
        return result
        
    def company_reference_number(self):
        if self.company():
            result = self.company().reference_number if self.company() else None
        else:
            result = None
        return result
        
    def company_slug(self):
        if self.company():
            result = self.company().slug if self.company() else None
        else:
            result = None
        return result
        
    def company_url_detail(self):
        if self.company():
            result = self.company().url_detail() if self.company() else None
        else:
            result = None
        return result

    # Delivery Note
    def delivery_note_name(self):
        result = None
        if self.delivery_note:
            result = self.delivery_note.name.split('/')[-1]
        return result

    def delivery_note_url(self):
        result = None
        if self.delivery_note:
            result = self.delivery_note.url
        return result

    # Order Data
    def orderdata(self):
        result = OrderData.objects.filter(order=self)
        return result if result.exists() else None

    def orderdata_count(self):
        return self.orderdata().count() if self.orderdata() else 0

    # Order File
    def order_file_name(self):
        result = None
        if self.order_file:
            result = self.order_file.name.split('/')[-1]
        return result

    def order_file_url(self):
        result = None
        if self.order_file:
            result = self.order_file.url
        return result

    # Recived
    def recived_date(self):
        return self.recived_datetime_formated().split(" ")[0] if self.recived_datetime else None

    def recived_datetime_formated(self):
        return self.recived_datetime.strftime("%d.%m.%Y %H:%M:%S") if self.recived_datetime else None

    def recived_time(self):
        return self.recived_datetime_formated().split(" ")[1] if self.recived_datetime else None

    def recived_username(self):
        return str(self.recived_user_id.username) if self.recived_user_id else None

    # Sent
    def sent_date(self):
        return self.sent_datetime_formated().split(" ")[0] if self.sent_datetime else None

    def sent_datetime_formated(self):
        return self.sent_datetime.strftime("%d.%m.%Y %H:%M:%S") if self.sent_datetime else None

    def sent_time(self):
        return self.sent_datetime_formated().split(" ")[1] if self.sent_datetime else None

    def sent_username(self):
        return str(self.sent_user_id.username) if self.sent_user_id else None

    # Urls
    def url_authorize_true(self):
        return reverse('storagemanagement:order_authorize_true',kwargs={'order':self.slug})

    def url_authorize_false(self):
        return reverse('storagemanagement:order_authorize_false',kwargs={'order':self.slug})

    def url_booking_true(self):
        return reverse('storagemanagement:order_booking_true',kwargs={'order':self.slug})

    def url_booking_false(self):
        return reverse('storagemanagement:order_booking_false',kwargs={'order':self.slug})

    def url_delete(self):
        return reverse('storagemanagement:order_delete',kwargs={'order':self.slug})

    def url_detail(self):
        return reverse('storagemanagement:order_detail',kwargs={'order':self.slug})

    def url_qrcode(self):
        return 'http://'+settings.HOST+self.url_detail()

    def url_recived(self):
        return reverse('storagemanagement:order_recived',kwargs={'order':self.slug})

    def url_sent(self):
        return reverse('storagemanagement:order_sent',kwargs={'order':self.slug})

    def url_update(self):
        return reverse('storagemanagement:order_update',kwargs={'order':self.slug})

    def value(self):
        queryset=self.orderdata()
        result = 0
        for query in queryset:
            result += query.value()
        return result
    
    def __str__(self):
        return "{}{}{}_{}".format(self.create_datetime.year,self.create_datetime.month,self.create_datetime.day,self.company_name())

    class Meta:
        app_label = 'storagemanagement'
        default_permissions = ()
        ordering = []
        permissions = (
            ('add_order','Order can view create'),
            ('change_order','Order can view change'),
            ('delete_order','Order can view delete'),
            ('detail_order','Order can view detail'),
            ('list_order','Order can view list'),
            ('table_order','Order can view table'),
            ('view_order','Order can view overview'),
        )
        verbose_name = "Bestellung"
        verbose_name_plural = "Bestellungen"