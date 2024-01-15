"""
#--------------------------------------------------------------------------------
# Models File from Model StorageItem
# 05.11.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
from django.db import models
from django.urls import reverse
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.booking.models import Booking
from storagemanagement.storage.models import Storage
from tools.createdata.models import CreateData
from tools.referencenumber.models import ReferenceNumber
from tools.slug.models import Slug
from tools.updatedata.models import UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class StorageItemBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):
    """
    StorageItemBaseModel

    Args:
        CreateData (_type_): _description_
        ReferenceNumber (_type_): _description_
        Slug (_type_): _description_
        UpdateData (_type_): _description_
    """

    short_name = "STIT"

    # Fields/Methodes for the booking
    supplieritem = models.ForeignKey(
        blank = True,
        help_text = 'Artikel des Standardlieferanten',
        name = 'supplieritem',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'storageitem_supplieritem',
        to = 'storagemanagement.SupplierItem',
        verbose_name = 'Standardartikel',
    )

    supplieritem_data = models.ManyToManyField(
        blank=True,
        help_text = 'Artikel anderer Lieferanten',
        name = 'supplieritem_data',
        related_name = 'storageitem_supplieritem_data',
        to = 'storagemanagement.SupplierItem',
        verbose_name = 'Artikel anderer Lieferanten',
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
        """
        Meta Data from Model
        """
        app_label = 'storagemanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class StorageItem(StorageItemBaseModel):
    """
    StorageItem

    Args:
        StorageItemBaseModel (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Fields/Methodes for the booking
    def booking_data(self):
        """
        booking

        Returns:
            queryset: contains all booking objects of the storageitem
        """
        result = Booking.objects.filter(
            supplieritem__in=self.supplieritem_data.values_list("booking_supplieritem")
        )
        return result

    def booking_count(self):
        """
        booking_count

        Returns:
            int: count of all bookings objects
        """
        objects = self.booking_data()
        result = objects.count() if objects else 0
        return result

    def booking_last(self):
        """
        booking_last

        Returns:
            query: last booking object
        """
        objects = self.booking_data()
        result = objects.last() if objects else None
        return result

    # Fields/Methodes for the supplier
    def get_supplier_object(self):
        """
        supplier

        Returns:
            query: supplier object
        """
        result = self.supplieritem.company if self.supplieritem else None
        return result

    def supplier_data(self):
        """
        suppliers

        Returns:
            queryset: contains all supplieritems
        """
        result = self.supplieritem_data.values('company')
        #result = Supplier.objects.filter(id__in = id_list)
        return result

    def supplier_count(self):
        """
        supplier_count

        Returns:
            int: count of suppliers
        """
        queryset = self.supplier_data()
        result = queryset.all().count() if queryset else 0
        return result

    def supplier_id(self):
        """
        supplier_id

        Returns:
            int: id from the supplier
        """
        result = self.get_supplier_object().id if self.get_supplier_object() else None
        return result

    def supplier_name(self):
        """
        supplier_name

        Returns:
            string: name from the supplier
        """
        result = self.get_supplier_object().name if self.get_supplier_object() else None
        return result

    def supplier_reference_number(self):
        """
        supplier_reference_number

        Returns:
            string: reference number from the supplier
        """
        result = self.get_supplier_object().reference_number if self.get_supplier_object() else None
        return result

    def supplier_slug(self):
        """
        supplier_slug

        Returns:
            string: slug from the supplier
        """
        result = self.get_supplier_object().slug if self.get_supplier_object() else None
        return result

    def supplier_url_detail(self):
        """
        supplier_url_detail

        Returns:
            string: url to the supplier detail page
        """
        return reverse(
            "storagemanagement:supplier_detail",
            kwargs={'supplier':self.supplier_slug()}
        )

    # Fields/Methodes for the supplier item
    def supplieritem_count(self):
        """
        supplieritem_count

        Returns:
            int: count of supplier items
        """
        queryset = self.supplieritem_data.values_list('id')
        result = queryset.count() if queryset else 0
        return result

    def get_supplieritem_object(self):
        """
        supplieritem

        Returns:
            query: supplieritem object
        """
        result = self.supplieritem
        return result

    def supplieritem_id(self):
        """
        supplieritem_id

        Returns:
            int: id from the supplieritem
        """
        result = self.get_supplieritem_object().id if self.get_supplieritem_object() else None
        return result

    def supplieritem_item_number(self):
        """
        supplieritem_item_number

        Returns:
            string: item number from the supplieritem
        """
        result = self.get_supplieritem_object().item_number if self.get_supplieritem_object() else None
        return result

    def supplieritem_name(self):
        """
        supplieritem_name

        Returns:
            string: name from the supplieritem
        """
        result = self.get_supplieritem_object().name if self.get_supplieritem_object() else None
        return result

    def supplieritem_reference_number(self):
        """
        supplieritem_reference_number

        Returns:
            string: reference number from the supplieritem
        """
        result = self.get_supplieritem_object().reference_number if self.get_supplieritem_object() else None
        return result

    def supplieritem_slug(self):
        """
        supplieritem_slug

        Returns:
            string: slug from supplieritem
        """
        result = self.get_supplieritem_object().slug if self.get_supplieritem_object() else None
        return result

    def supplieritem_url_detail(self):
        """
        supplieritem_url_detail

        Returns:
            string: url to detail page of supplieritem
        """
        return reverse(
            "storagemanagement:supplieritem_detail",
            kwargs={"supplieritem":self.supplieritem_slug()}
        )

    # Fields/Methodes for the status
    def status(self):
        """
        status

        Returns:
            string: status of the storage
        """
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
    def stock_data(self):
        """
        stock

        Returns:
            queryset: contains all supplieritems in the stock
        """
        result = Storage.objects.filter(
            supplieritem__in=self.supplieritem_data.all(),
            unload_datetime=None
        )
        if result == []:
            result = None
        return result

    def stock_count(self):
        """
        stock_count

        Returns:
            int: count of items in the stock
        """
        queryset = self.stock_data()
        result = queryset.count() if queryset else 0
        return result

    def stock_percentage(self):
        """
        stock_percentage

        Returns:
            float: load of the stock in procentage
        """
        count = self.stock_count()
        maximum = self.maximum
        result = int(count/maximum*100) if count > 0 and maximum > 0 else int(0)
        return result

    def stock_value(self):
        """
        stock_value

        Returns:
            float: whole value of supplieritem in the stock
        """
        objects = self.stock_data()
        if objects:
            result = 0
            for obj in objects:
                result += obj.value()
        else:
            result = 0
        return result

    # Fields/Methodes for the urls
    def url_booking(self):
        """
        url_booking

        Returns:
            string: url to booking page
        """
        return reverse(
            'storagemanagement:storageitem_booking_overview',
            kwargs={'storageitem':self.slug}
        )

    def url_booking_list(self):
        """
        url_booking_list

        Returns:
            string: url to booking list page
        """
        return reverse(
            'storagemanagement:storageitem_booking_list',
            kwargs={'storageitem':self.slug}
        )

    def url_booking_table(self):
        """
        url_booking_table

        Returns:
            string: url to booking table page
        """
        return reverse(
            'storagemanagement:storageitem_booking_table',
            kwargs={'storageitem':self.slug}
        )

    def url_booking_add(self):
        """
        url_booking_add

        Returns:
            string: url to booking add page
        """
        return reverse(
            'storagemanagement:storageitem_booking_add',
            kwargs={'storageitem':self.slug}
        )

    def url_booking_create(self):
        """
        url_booking_create

        Returns:
            string: url to booking create page
        """
        return reverse(
            'storagemanagement:storageitem_booking_create',
            kwargs={'storageitem':self.slug}
        )

    def url_booking_remove(self):
        """
        url_booking_remove

        Returns:
            string: url to booking remove page
        """
        return reverse(
            'storagemanagement:storageitem_booking_remove',
            kwargs={'storageitem':self.slug}
        )

    def url_delete(self):
        """
        url_delete

        Returns:
            string: url to delete page
        """
        return reverse(
            'storagemanagement:storageitem_delete',
            kwargs={'storageitem':self.slug}
        )

    def url_detail(self):
        """
        url_detail

        Returns:
            string: url to detail page
        """
        return reverse(
            'storagemanagement:storageitem_detail',
            kwargs={'storageitem':self.slug}
        )

    def url_qrcode(self):
        """
        url_qrcode

        Returns:
            string: url to qrcode page
        """
        return 'http://'+settings.HOST+self.url_detail()

    def url_qrcode_booking_add(self):
        """
        url_qrcode_booking_add

        Returns:
            string: url to qrcode booking add link
        """
        return 'http://'+settings.HOST+self.url_booking_add()

    def url_qrcode_booking_remove(self):
        """
        url_qrcode_booking_remove

        Returns:
            string: url to qrcode booking remove link
        """
        return 'http://'+settings.HOST+self.url_booking_remove()

    def url_qrcode_request(self):
        """
        url_qrcode_request

        Returns:
            string: url to qrcode request link
        """
        return 'http://'+settings.HOST+self.url_request_create()

    def url_request_create(self):
        """
        url_request_create

        Returns:
            string: url to request create link
        """
        return reverse(
            'storagemanagement:storageitem_request_create',
            kwargs={'storageitem':self.slug}
        )

    def url_storage(self):
        """
        url_storage

        Returns:
            string: url to storage page
        """
        return reverse(
            'storagemanagement:storageitem_storage_overview',
            kwargs={'storageitem':self.slug}
        )

    def url_storage_list(self):
        """
        url_storage_list

        Returns:
            string: url to storage list page
        """
        return reverse(
            'storagemanagement:storageitem_storage_list',
            kwargs={'storageitem':self.slug}
        )

    def url_storage_table(self):
        """
        url_storage_table

        Returns:
            string: url to storage table page
        """
        return reverse(
            'storagemanagement:storageitem_storage_table',
            kwargs={'storageitem':self.slug}
        )

    def url_storage_create(self):
        """
        url_storage_create

        Returns:
            string: url to storage create page
        """
        return reverse(
            'storagemanagement:storageitem_storage_create',
            kwargs={'storageitem':self.slug}
        )

    def url_update(self):
        """
        url_update

        Returns:
            string: url to storage detail page
        """
        return reverse(
            'storagemanagement:storageitem_update',
            kwargs={'storageitem':self.slug}
        )

    def __str__(self):
        return "{} ({})".format(str(self.name),str(self.reference_number))

    class Meta:
        """
        Meta Data from Model
        """
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
#--------------------------------------------------------------------------------
