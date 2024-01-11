"""
#--------------------------------------------------------------------------------
# Models File from Model Request Data
# 10.11.2023
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
class RequestDataBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):
    """
    RequestDataBaseModel

    Args:
        CreateData (_type_): _description_
        ReferenceNumber (_type_): _description_
        Slug (_type_): _description_
        UpdateData (_type_): _description_
    """

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
    supplieritem = models.ForeignKey(
        blank = True,
        name = 'supplieritem',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'requestdata_supplieritem',
        to = 'storagemanagement.supplierItemBaseModel',
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
        """
        Meta Data from Model
        """
        app_label = 'storagemanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class RequestData(RequestDataBaseModel):
    """
    RequestData

    Args:
        RequestDataBaseModel (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Authorized
    def authorized_date(self):
        """
        authorized_date

        Returns:
            string: date from authorization
        """
        return self.authorized_datetime_formated().split(" ")[0] if self.authorized_datetime else None

    def authorized_datetime_formated(self):
        """
        authorized_datetime_formated

        Returns:
            string: datetime from authorization
        """
        return self.authorized_datetime.strftime("%d.%m.%Y %H:%M:%S") if self.authorized_datetime else None

    def authorized_time(self):
        """
        authorized_time

        Returns:
            string: time from authorization
        """
        return self.authorized_datetime_formated().split(" ")[1] if self.authorized_datetime else None

    def authorized_username(self):
        """
        authorized_username

        Returns:
            string: username from authorization
        """
        return str(self.authorized_user_id.username) if self.authorized_user_id else None

    # Supplier
    def supplier_id(self):
        """
        supplier_id

        Returns:
            int: id from supplier
        """
        if self.supplieritem:
            result = self.supplieritem.supplier_id()
        else:
            result = None
        return result

    def supplier_name(self):
        """
        supplier_name

        Returns:
            string: name from supplier
        """
        if self.supplieritem:
            result = self.supplieritem.supplier_name()
        else:
            result = None
        return result

    def supplier_reference_number(self):
        """
        supplier_reference_number

        Returns:
            string: reference number from supplier
        """
        if self.supplieritem:
            result = self.supplieritem.supplier_reference_number()
        else:
            result = None
        return result

    def supplier_slug(self):
        """
        supplier_slug

        Returns:
            string: slug from supplier
        """
        if self.supplieritem:
            result = self.supplieritem.supplier_slug()
        else:
            result = None
        return result

    def supplier_url_detail(self):
        """
        supplier_url_detail

        Returns:
            string: url to supplier detail page
        """
        if self.supplieritem:
            result = self.supplieritem.supplier_url_detail()
        else:
            result = None
        return result

    # Supplier Item
    def supplieritem_id(self):
        """
        supplieritem_id

        Returns:
            int: id from supplier item
        """
        result = self.supplieritem.id if self.supplieritem else None
        return result

    def supplieritem_name(self):
        """
        supplieritem_name

        Returns:
            string: name from supplier item
        """
        result = self.supplieritem.name if self.supplieritem else None
        return result

    def supplieritem_item_number(self):
        """
        supplieritem_item_number

        Returns:
            string: item number from supplier item
        """
        result = self.supplieritem.item_number if self.supplieritem else None
        return result

    def supplieritem_reference_number(self):
        """
        supplieritem_reference_number

        Returns:
            string: reference number from supplier item
        """
        result = self.supplieritem.reference_number if self.supplieritem else None
        return result

    def supplieritem_slug(self):
        """
        supplieritem_slug

        Returns:
            string: slug from supplieritem
        """
        result = self.supplieritem.slug if self.supplieritem else None
        return result

    def supplieritem_url_detail(self):
        """
        supplieritem_url_detail

        Returns:
            string: url to supplieritem detail page
        """
        result = self.supplieritem.url_detail() if self.supplieritem else None
        return result

    def status(self):
        """
        status

        Returns:
            string: status from request
        """
        if self.orderprocess:
            result = self.orderprocess.Status(self.orderprocess.status).label
        else:
            result = None
        return result

    # Storage Item
    def storageitem_id(self):
        """
        storageitem_id

        Returns:
            int: url to storageitem id
        """
        return self.storageitem.id if self.storageitem else None

    def storageitem_name(self):
        """
        storageitem_name

        Returns:
            string: url to storageitem name
        """
        return self.storageitem.name if self.storageitem else None

    def storageitem_reference_number(self):
        """
        storageitem_reference_number

        Returns:
            string: url to storageitem reference number
        """
        return self.storageitem.reference_number if self.storageitem else None

    def storageitem_slug(self):
        """
        storageitem_slug

        Returns:
            string: url to storageitem slug
        """
        return self.storageitem.slug if self.storageitem else None

    def storageitem_url_detail(self):
        """
        storageitem_url_detail

        Returns:
            string: url to storageitem detail page
        """
        return self.storageitem.url_detail() if self.storageitem else None

    # Unit
    def unit(self):
        """
        unit

        Returns:
            string: unit from supplieritem
        """
        result = self.supplieritem.unit if self.supplieritem else None
        return result

    # Urls
    def url_authorize_true(self):
        """
        url_authorize_true

        Returns:
            string: url to authorize true page
        """
        return reverse(
            'storagemanagement:requestdata_authorize_true',
            kwargs={'requestdata':self.slug}
        )

    def url_authorize_false(self):
        """
        url_authorize_false

        Returns:
            string: url to authorize false page
        """
        return reverse(
            'storagemanagement:requestdata_authorize_false',
            kwargs={'requestdata':self.slug}
        )

    def url_delete(self):
        """
        url_delete

        Returns:
            string: url to delete page
        """
        return reverse('storagemanagement:requestdata_delete',kwargs={'requestdata':self.slug})

    def url_detail(self):
        """
        url_detail

        Returns:
            string: url to detail page
        """
        return reverse('storagemanagement:requestdata_detail',kwargs={'requestdata':self.slug})

    def url_qrcode(self):
        """
        url_qrcode

        Returns:
            string: url to qrcode page
        """
        return 'http://'+settings.HOST+self.url_detail()

    def url_update(self):
        """
        url_update

        Returns:
            string: url to update page
        """
        return reverse('storagemanagement:requestdata_update',kwargs={'requestdata':self.slug})

    # Value
    def value(self):
        """
        value

        Returns:
            float: whole value of all items in request
        """
        result = self.amount * self.price
        return result

    def __str__(self):
        return "{}{}{}_{}".format(
            self.create_datetime.year,
            self.create_datetime.month,
            self.create_datetime.day,
            self.supplieritem.slug
        )

    class Meta:
        """
        Meta Data from Model
        """
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
#--------------------------------------------------------------------------------
