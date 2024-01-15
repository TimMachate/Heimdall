"""
#--------------------------------------------------------------------------------
# Models File from Model Offer
# 15.10.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from tinymce import models as tinymce_models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.offerdata.models import OfferData
from tools.createdata.models import CreateData
from tools.referencenumber.models import ReferenceNumber
from tools.slug.models import Slug
from tools.updatedata.models import UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class OfferBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):
    """
    OfferBaseModel

    Args:
        CreateData (_type_): _description_
        ReferenceNumber (_type_): _description_
        Slug (_type_): _description_
        UpdateData (_type_): _description_
    """

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
        """
        Meta Data from Model
        """
        app_label = 'storagemanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class Offer(OfferBaseModel):
    """
    Offer

    Args:
        OfferBaseModel (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Authorized
    def authorized(self):
        """
        authorized

        Returns:
            boolean: is authorized (true) or rejected (false)
        """
        queryset = self.offerdata()
        result = False
        if queryset.exists():
            if queryset.exclude(authorized=False).count() == queryset.filter(authorized=True).count():
                result = True
        return result

    # Company
    def get_supplier_object(self):
        """
        supplier

        Returns:
            query: contains supplier object
        """
        queryset = self.offerdata()
        if queryset:
            result = queryset.first().supplieritem.company
        else:
            result = None
        return result

    def supplier_id(self):
        """
        supplier_id

        Returns:
            int: id from supplier
        """
        return self.get_supplier_object().id if self.get_supplier_object() else None

    def supplier_name(self):
        """
        supplier_name

        Returns:
            string: name from supplier
        """
        return self.get_supplier_object().name if self.get_supplier_object() else None

    def supplier_reference_number(self):
        """
        supplier_reference_number

        Returns:
            string: reference_number from supplier
        """
        return self.get_supplier_object().reference_number if self.get_supplier_object() else None

    def supplier_slug(self):
        """
        supplier_slug

        Returns:
            string: slug from supplier
        """
        return self.get_supplier_object().slug if self.get_supplier_object() else None

    def supplier_url_detail(self):
        """
        supplier_url_detail

        Returns:
            string: url to detail page from supplier
        """
        return self.get_supplier_object().url_detail() if self.get_supplier_object() else None

    # Offer Data
    def offerdata(self):
        """
        offerdata

        Returns:
            queryset: contains all offerdata objects
        """
        result = OfferData.objects.filter(offer=self)
        return result if result.exists() else None

    def offerdata_count(self):
        """
        offerdata_count

        Returns:
            int: count from the offerdata
        """
        return self.offerdata().count() if self.offerdata() else 0

    # Offer File
    def offer_file_name(self):
        """
        offer_file_name

        Returns:
            string: name of offer file
        """
        result = None
        if self.offer_file:
            result = self.offer_file.name.split('/')[-1]
        return result

    def offer_file_url(self):
        """
        offer_file_url

        Returns:
            string: url to offer file
        """
        result = None
        if self.offer_file:
            result = self.offer_file.url
        return result

    # Ordered
    def ordered_date(self):
        """
        ordered_date

        Returns:
            string: date of the order
        """
        return self.ordered_datetime_formated().split(" ")[0] if self.ordered_datetime else None

    def ordered_datetime_formated(self):
        """
        ordered_datetime_formated

        Returns:
            string: date and time formated from order
        """
        obj = self.ordered_datetime
        return obj.strftime("%d.%m.%Y %H:%M:%S") if obj else None

    def ordered_time(self):
        """
        ordered_time

        Returns:
            string: time from order
        """
        return self.ordered_datetime_formated().split(" ")[1] if self.ordered_datetime else None

    def ordered_username(self):
        """
        ordered_username

        Returns:
            string: username from the person who ordered
        """
        return str(self.ordered_user_id.username) if self.ordered_user_id else None

    # Recived
    def recived_date(self):
        """
        recived_date

        Returns:
            string: recive date of the offer
        """
        return self.recived_datetime_formated().split(" ")[0] if self.recived_datetime else None

    def recived_datetime_formated(self):
        """
        recived_datetime_formated

        Returns:
            string: recive date time formated of the offer
        """
        obj = self.recived_datetime
        return obj.strftime("%d.%m.%Y %H:%M:%S") if obj else None

    def recived_time(self):
        """
        recived_time

        Returns:
            string: recived time of the offer
        """
        return self.recived_datetime_formated().split(" ")[1] if self.recived_datetime else None

    def recived_username(self):
        """
        recived_username

        Returns:
            string: recive username of the offer
        """
        return str(self.recived_user_id.username) if self.recived_user_id else None

    # Sent
    def sent_date(self):
        """
        sent_date

        Returns:
            string: sent date of the offer
        """
        return self.sent_datetime_formated().split(" ")[0] if self.sent_datetime else None

    def sent_datetime_formated(self):
        """
        sent_datetime_formated

        Returns:
            string: sent date time formated of the offer
        """
        obj = self.sent_datetime
        return obj.strftime("%d.%m.%Y %H:%M:%S") if obj else None

    def sent_time(self):
        """
        sent_time

        Returns:
            string: sent time of the offer
        """
        return self.sent_datetime_formated().split(" ")[1] if self.sent_datetime else None

    def sent_username(self):
        """
        sent_username

        Returns:
            string: sent username of the offer
        """
        return str(self.sent_user_id.username) if self.sent_user_id else None

    # Urls
    def url_authorize_true(self):
        """
        url_authorize_true

        Returns:
            string: url to set authorization to true
        """
        return reverse('storagemanagement:offer_authorize_true',kwargs={'offer':self.slug})

    def url_authorize_false(self):
        """
        url_authorize_false

        Returns:
            string: url to set authorization to false
        """
        return reverse('storagemanagement:offer_authorize_false',kwargs={'offer':self.slug})

    def url_delete(self):
        """
        url_delete

        Returns:
            string: url to delete page
        """
        return reverse('storagemanagement:offer_delete',kwargs={'offer':self.slug})

    def url_detail(self):
        """
        url_detail

        Returns:
            string: url to detail page
        """
        return reverse('storagemanagement:offer_detail',kwargs={'offer':self.slug})

    def url_order_true(self):
        """
        url_order_true

        Returns:
            string: url to set the order to true
        """
        return reverse('storagemanagement:offer_order_true',kwargs={'offer':self.slug})

    def url_order_false(self):
        """
        url_order_false

        Returns:
            string: url to set the order to false
        """
        return reverse('storagemanagement:offer_order_false',kwargs={'offer':self.slug})

    def url_qrcode(self):
        """
        url_qrcode

        Returns:
            string: url to qrcode page
        """
        return 'http://'+settings.HOST+self.url_detail()

    def url_recived(self):
        """
        url recived

        Returns:
            string: url to set recive to true
        """
        return reverse('storagemanagement:offer_recived',kwargs={'offer':self.slug})

    def url_sent(self):
        """
        url_sent

        Returns:
            string: url to set sent to true
        """
        return reverse('storagemanagement:offer_sent',kwargs={'offer':self.slug})

    def url_update(self):
        """
        url_update

        Returns:
            string: url to the update page
        """
        return reverse('storagemanagement:offer_update',kwargs={'offer':self.slug})

    def value(self):
        """
        value

        Returns:
            float: contains the summary value of the offer
        """
        queryset=self.offerdata()
        result = 0
        for query in queryset:
            result += query.value()
        return result

    def __str__(self):
        return "{}{}{}_{}".format(
            self.create_datetime.year,
            self.create_datetime.month,
            self.create_datetime.day,
            self.supplier_name()
        )

    class Meta:
        """
        Meta Data from Model
        """
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
#--------------------------------------------------------------------------------
