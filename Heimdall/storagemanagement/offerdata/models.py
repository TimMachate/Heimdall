"""
#--------------------------------------------------------------------------------
# Models File from Model Offer Data
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
from tools.createdata.models import CreateData
from tools.referencenumber.models import ReferenceNumber
from tools.slug.models import Slug
from tools.updatedata.models import UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class OfferDataBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):
    """
    OfferDataBaseModel

    Args:
        CreateData (_type_): _description_
        ReferenceNumber (_type_): _description_
        Slug (_type_): _description_
        UpdateData (_type_): _description_
    """

    # Variables
    short_name = "STOFDA"

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

    # Fields/Methodes for the supplieritem
    supplieritem = models.ForeignKey(
        blank = True,
        name = 'supplieritem',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'offerdata_supplieritem',
        to = 'storagemanagement.SupplierItem',
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
        """
        Meta Data from Model
        """
        app_label = 'storagemanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class OfferData(OfferDataBaseModel):
    """
    OfferData

    Args:
        OfferDataBaseModel (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Authorized
    def authorized_date(self):
        """
        authorized_date

        Returns:
            string: authorize date from the offer item
        """
        obj = self.authorized_datetime
        return self.authorized_datetime_formated().split(" ")[0] if obj else None

    def authorized_datetime_formated(self):
        """
        authorized_datetime_formated

        Returns:
            string: authorize date time formated from the offer item
        """
        obj = self.authorized_datetime
        return obj.strftime("%d.%m.%Y %H:%M:%S") if obj else None

    def authorized_time(self):
        """
        authorized_time

        Returns:
            string: authorize time from the offer item
        """
        obj = self.authorized_datetime
        return self.authorized_datetime_formated().split(" ")[1] if obj else None

    def authorized_username(self):
        """
        authorized_username

        Returns:
            string: authorize username from the offer item
        """
        return str(self.authorized_user_id.username) if self.authorized_user_id else None

    # Supplier
    def get_supplier_object(self):
        """
        get_supplier_object

        Returns:
            query: contains supplier object from offer item
        """
        if self.supplieritem:
            result = self.supplieritem.company if self.supplieritem.company else None
        else:
            result = None
        return result

    def supplier_id(self):
        """
        supplier_id

        Returns:
            int: supplier id from offer item
        """
        result = self.get_supplier_object().id if self.get_supplier_object() else None
        return result

    def supplier_name(self):
        """
        supplier_name

        Returns:
            string: supplier name from the offer item
        """
        result = self.get_supplier_object().name if self.get_supplier_object() else None
        return result

    def supplier_reference_number(self):
        """
        supplier_reference_number

        Returns:
            string: supplier reference number from the offer item
        """
        result = self.get_supplier_object().reference_number if self.get_supplier_object() else None
        return result

    def supplier_slug(self):
        """
        supplier_slug

        Returns:
            string: supplier slug from the offer item
        """
        result = self.get_supplier_object().slug if self.get_supplier_object() else None
        return result

    def supplier_url_detail(self):
        """
        supplier_url_detail

        Returns:
            string: url to supplier detail page from the offer item
        """
        result = self.get_supplier_object().url_detail() if self.get_supplier_object() else None
        return result

    # Supplier Item
    def get_supplieritem_object(self):
        """
        get_supplieritem_object

        Returns:
            string: supplieritem from the offer item
        """
        result = self.supplieritem if self.supplieritem else None
        return result

    def supplieritem_id(self):
        """
        supplieritem_id

        Returns:
            int: supplieritem id from the offer item
        """
        result = self.get_supplieritem_object().id if self.get_supplieritem_object() else None
        return result

    def supplieritem_name(self):
        """
        supplieritem_name

        Returns:
            string: supplieritem name from the offer item
        """
        result = self.get_supplieritem_object().name if self.get_supplieritem_object() else None
        return result

    def supplieritem_item_number(self):
        """
        supplieritem_item_number

        Returns:
            string: supplieritem item number from the offer item
        """
        obj = self.get_supplieritem_object()
        result = obj.item_number if obj else None
        return result

    def supplieritem_reference_number(self):
        """
        supplieritem_reference_number

        Returns:
            string: supplieritem reference number from the offer item
        """
        obj = self.get_supplieritem_object()
        result = obj.reference_number if obj else None
        return result

    def supplieritem_slug(self):
        """
        supplieritem_slug

        Returns:
            string: supplieritem slug from the offer item
        """
        obj = self.get_supplieritem_object()
        result = obj.slug if obj else None
        return result

    def supplieritem_url_detail(self):
        """
        supplieritem_url_detail

        Returns:
            string: url to supplieritem detail page from the offer item
        """
        obj = self.get_supplieritem_object()
        result = obj.url_detail() if obj else None
        return result

    # Offer
    def get_offer_object(self):
        """
        get_offer_object

        Returns:
            query: contains the offer object
        """
        result = self.offer if self.offer else None
        return result

    def offer_id(self):
        """
        offer_id

        Returns:
            int: offer from the the offer item
        """
        obj = self.get_offer_object()
        result = obj.id if obj else None
        return result

    def offer_reference_number(self):
        """
        offer_reference_number

        Returns:
            string: offer reference number from the offer item
        """
        obj = self.get_offer_object()
        result = obj.reference_number if obj else None
        return result

    def offer_slug(self):
        """
        offer_slug

        Returns:
            string: offer slug from the offer item
        """
        obj = self.get_offer_object()
        result = obj.slug if obj else None
        return result

    def offer_url_detail(self):
        """
        offer_url_detail

        Returns:
            string: offer url detail from the offer item
        """
        obj = self.get_offer_object()
        result = obj.url_detail() if obj else None
        return result

    # Storage Item
    def get_storageitem_object(self):
        """
        get_storageitem_object

        Returns:
            query: contains storage item object
        """
        result = self.storageitem if self.storageitem else None
        return result

    def storageitem_id(self):
        """
        storageitem_id

        Returns:
            int: storage item id from offer item
        """
        obj = self.get_storageitem_object()
        return obj.id if obj else None

    def storageitem_name(self):
        """
        storageitem_name

        Returns:
            string: storage item name from offer item
        """
        obj = self.get_storageitem_object()
        return obj.name if obj else None

    def storageitem_reference_number(self):
        """
        storageitem_reference_number

        Returns:
            string: storage item reference number from the offer item
        """
        obj = self.get_storageitem_object()
        return obj.reference_number if obj else None

    def storageitem_slug(self):
        """
        storageitem_slug

        Returns:
            string: storage item slug from the offer item
        """
        obj = self.get_storageitem_object()
        return obj.slug if obj else None

    def storageitem_url_detail(self):
        """
        storageitem_url_detail

        Returns:
            string: url to storage item detail page
        """
        obj = self.get_storageitem_object()
        return obj.url_detail() if obj else None

    # Unit
    def unit(self):
        """
        unit

        Returns:
            string: unit from the supplier item
        """
        obj = self.get_supplieritem_object()
        result = obj.unit if obj else None
        return result

    # Urls
    def url_authorize_true(self):
        """
        url_authorize_true

        Returns:
            string: url to set authorization to true
        """
        return reverse('storagemanagement:offerdata_authorize_true',kwargs={'offerdata':self.slug})

    def url_authorize_false(self):
        """
        url_authorize_false

        Returns:
            string: url to set authorization to false
        """
        return reverse('storagemanagement:offerdata_authorize_false',kwargs={'offerdata':self.slug})

    def url_delete(self):
        """
        url_delete

        Returns:
            string: url to delete page
        """
        return reverse('storagemanagement:offerdata_delete',kwargs={'offerdata':self.slug})

    def url_detail(self):
        """
        url_detail

        Returns:
            string: url to detail page
        """
        return reverse('storagemanagement:offerdata_detail',kwargs={'offerdata':self.slug})

    def url_qrcode(self):
        """
        url_qrcode

        Returns:
            string: url to qrcode page
        """
        return 'http://'+settings.HOST+self.url_detail()

    def url_recived(self):
        """
        url_recived

        Returns:
            string: url to set recived to true
        """
        return reverse('storagemanagement:offerdata_recived',kwargs={'offerdata':self.slug})

    def url_sent(self):
        """
        url_sent

        Returns:
            string: url to set sent to true
        """
        return reverse('storagemanagement:offerdata_sent',kwargs={'offerdata':self.slug})

    def url_update(self):
        """
        url_update

        Returns:
            string: url to update page
        """
        return reverse('storagemanagement:offerdata_update',kwargs={'offerdata':self.slug})

    def __str__(self):
        return "{}{}{}_{}".format(
            self.create_datetime.year,
            self.create_datetime.month,
            self.create_datetime.day,
            self.reference_number
        )

    def value(self):
        """
        value

        Returns:
            float: value of the offer item
        """
        result = self.price*self.amount
        return result

    class Meta:
        """
        Meta Data from Model
        """
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
#--------------------------------------------------------------------------------
