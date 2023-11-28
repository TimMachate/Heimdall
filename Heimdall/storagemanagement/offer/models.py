#--------------------------------------------------------------------------------
# Models File from Model Offer
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

from storagemanagement.offerdata.models import OfferData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class OfferBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STOF"

    # Fields/Methodes for the done
    done = models.BooleanField(
        blank = True,
        default = False,
        help_text = 'Angebot wurde bearbeitet.',
        name = "done",
        null = False,
        verbose_name = "Bearbeitet",
    )

    # Fields/Methodes for the notice
    notice = tinymce_models.HTMLField(
        blank = True,
        help_text = "Nützliche Informationen zum Angebot.",
        name = 'notice',
        null = True,
        verbose_name = 'Bemerkung',
    )

    offer_file = models.FileField(
        blank = True,
        help_text = "Erhaltenes Angebot",
        name = "offer_file",
        null = True,
        upload_to = 'storagemanagement/offer/',
        verbose_name = "Angebot",
    )

    # Fields/Methodes for the ordered
    ordered = models.BooleanField(
        blank = True,
        default = False,
        help_text = 'Bestellung wurde aufgegeben.',
        name = "ordered",
        null = False,
        verbose_name = "Bestellung",
    )

    ordered_datetime = models.DateTimeField(
        blank = True,
        default = None,
        editable = True,
        help_text = "Zeitpunkt der Erstellung der Bestellung.",
        name = 'ordered_datetime',
        null = True,
        verbose_name = 'Erstellung der Bestellung.',
    )

    ordered_user_id = models.ForeignKey(
        blank = True,
        default = None,
        editable = True,
        help_text = "Person die die Bestellung erstellt hat.",
        name = 'ordered_user_id',
        null = True,
        on_delete = models.PROTECT,
        related_name = "offer_ordered_user_id",
        to = get_user_model(),
        verbose_name = 'Person der Erstellung der Bestellung',
    )

    # Fields/Methodes for the offerdata_recived
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
        name = 'recived_datetime',
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
        related_name = "offer_recived_user_id",
        to = get_user_model(),
        verbose_name = 'Person des Erhalten der Bestellung',
    )

    # Fields/Methodes for the offerdata_request
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
        name = 'sent_datetime',
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
        related_name = "offer_sent_user_id",
        to = get_user_model(),
        verbose_name = 'Besteller',
    )

    class Meta:
        app_label = 'storagemanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class Offer(OfferBaseModel):

    # Authorized
    def authorized(self):
        queryset = self.offerdata()
        result = False
        if queryset.exists():
            if queryset.exclude(authorized=False).count() == queryset.filter(authorized=True).count():
                result = True
        return result

    # Company
    def company(self):
        queryset = self.offerdata()
        if queryset:
            result = queryset.first().companyitem.company
        else:
            result = None
        return result

    def company_id(self):
        return self.company().id if self.company() else None

    def company_name(self):
        return self.company().name if self.company() else None
        
    def company_reference_number(self):
        return self.company().reference_number if self.company() else None
        
    def company_slug(self):
        return self.company().slug if self.company() else None
        
    def company_url_detail(self):
        return self.company().url_detail() if self.company() else None

    # Offer Data
    def offerdata(self):
        result = OfferData.objects.filter(offer=self)
        return result if result.exists() else None

    def offerdata_count(self):
        return self.offerdata().count() if self.offerdata() else 0

    # Offer File
    def offer_file_name(self):
        result = None
        if self.offer_file:
            result = self.offer_file.name.split('/')[-1]
        return result

    def offer_file_url(self):
        result = None
        if self.offer_file:
            result = self.offer_file.url
        return result

    # Ordered
    def ordered_date(self):
        return self.ordered_datetime_formated().split(" ")[0] if self.ordered_datetime else None

    def ordered_datetime_formated(self):
        return self.ordered_datetime.strftime("%d.%m.%Y %H:%M:%S") if self.ordered_datetime else None

    def ordered_time(self):
        return self.ordered_datetime_formated().split(" ")[1] if self.ordered_datetime else None

    def ordered_username(self):
        return str(self.ordered_user_id.username) if self.ordered_user_id else None

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
        return reverse('storagemanagement:offer_authorize_true',kwargs={'offer':self.slug})

    def url_authorize_false(self):
        return reverse('storagemanagement:offer_authorize_false',kwargs={'offer':self.slug})

    def url_delete(self):
        return reverse('storagemanagement:offer_delete',kwargs={'offer':self.slug})

    def url_detail(self):
        return reverse('storagemanagement:offer_detail',kwargs={'offer':self.slug})

    def url_order_true(self):
        return reverse('storagemanagement:offer_order_true',kwargs={'offer':self.slug})

    def url_order_false(self):
        return reverse('storagemanagement:offer_order_false',kwargs={'offer':self.slug})

    def url_qrcode(self):
        return 'http://'+settings.HOST+self.url_detail()

    def url_recived(self):
        return reverse('storagemanagement:offer_recived',kwargs={'offer':self.slug})

    def url_sent(self):
        return reverse('storagemanagement:offer_sent',kwargs={'offer':self.slug})

    def url_update(self):
        return reverse('storagemanagement:offer_update',kwargs={'offer':self.slug})
    
    def value(self):
        queryset=self.offerdata()
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
            ('add_offer','Offer can view create'),
            ('authorize_true_offer','Offer can authorize false offer'),
            ('authorize_false_offer','Offer can authorize false offer'),
            ('change_offer','Offer can view change'),
            ('delete_offer','Offer can view delete'),
            ('detail_offer','Offer can view detail'),
            ('list_offer','Offer can view list'),
            ('recived_offer','Offer can recived offer'),
            ('sent_offer','Offer can sent offer'),
            ('order_true_offer','Offer can order true'),
            ('order_false_offer','Offer can order false'),
            ('table_offer','Offer can view table'),
            ('view_offer','Offer can view overview'),
        )
        verbose_name = "Angebot"
        verbose_name_plural = "Angebote"