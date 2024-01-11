"""
#--------------------------------------------------------------------------------
# Model File from Model Ware
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.companyitem.models import CompanyItemBaseModel
from storagemanagement.booking.models import Booking
from storagemanagement.storage.models import Storage
from storagemanagement.storageitem.models import StorageItem
from tools.createdata.models import CreateData
from tools.referencenumber.models import ReferenceNumber
from tools.slug.models import Slug
from tools.updatedata.models import UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class SupplierItemBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):
    """
    SupplierItemBaseModel

    Args:
        CreateData (_type_): _description_
        ReferenceNumber (_type_): _description_
        Slug (_type_): _description_
        UpdateData (_type_): _description_
    """

    short_name = "STSI"

    supplieritem = models.OneToOneField(
        blank = True,
        name = "supplieritem",
        null = True,
        on_delete = models.CASCADE,
        related_name = "supplieritem_supplieritem",
        to = "storagemanagement.supplieritem",
        verbose_name = "Artikel",
    )

    class Meta:
        """
        Meta Data from SupplierItemBaseModel
        """
        app_label = 'storagemanagement'
        default_permissions = ()

class SupplierItem(CompanyItemBaseModel):
    """
    SupplierItem

    Args:
        CompanyItemBaseModel (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Fields/Methodes for the booking
    def booking(self):
        """
        booking

        Returns:
            queryset: contains all bookings from supplieritem
        """
        result = Booking.objects.filter(supplieritem=self)
        if result == []:
            result = None
        return result

    def booking_count(self):
        """
        booking_count

        Returns:
            int: booking count from supplieritem
        """
        objects = self.booking()
        result = objects.count() if objects else 0
        return result

    def booking_last(self):
        """
        booking_last

        Returns:
            queryset: contains last booking
        """
        objects = self.booking()
        result = objects.last() if objects else None
        return result

    # Fields/Methodes for the stock
    def stock(self):
        """
        stock

        Returns:
            queryset: contains all supplieritems in stock
        """
        result = Storage.objects.filter(supplieritem=self,unload_datetime=None)
        if result == []:
            result = None
        return result

    def stock_count(self):
        """
        stock_count

        Returns:
            int: stock count from supplieritems in stock
        """
        queryset = self.stock()
        result = queryset.count() if queryset else 0
        return result

    def stock_value(self):
        """
        stock_value

        Returns:
            float: value of all supplieritems in stock
        """
        objects = self.stock()
        if objects:
            result = 0
            for obj in objects:
                result += obj.booking.price
        else:
            result = 0
        return result

    # Storage Item
    def storageitem(self):
        """
        storageitem

        Returns:
            query: storage item object
        """
        result=StorageItem.objects.filter(supplieritem_data=self).first()
        return result

    def storageitem_id(self):
        """
        storageitem_id

        Returns:
            string: id from storageitem
        """
        result = self.storageitem().id if self.storageitem() else None
        return result

    def storageitem_name(self):
        """
        storageitem_name

        Returns:
            string: name from storageitem
        """
        result = self.storageitem().name if self.storageitem() else None
        return result

    def storageitem_reference_number(self):
        """
        storageitem_reference_number

        Returns:
            string: reference number from storageitem
        """
        result = self.storageitem().reference_number if self.storageitem() else None
        return result

    def storageitem_slug(self):
        """
        storageitem_slug

        Returns:
            string: slug from storageitem
        """
        result = self.storageitem().slug if self.storageitem() else None
        return result

    def storageitem_url_detail(self):
        """
        storageitem_url_detail

        Returns:
            string: url to storageitem detail page
        """
        result = self.storageitem().url_detail() if self.storageitem() else None
        return result

    # Company
    def supplier_id(self):
        """
        supplier_id

        Returns:
            int: id from supplier
        """
        result = self.company.id if self.company else None
        return result

    def supplier_name(self):
        """
        supplier_name

        Returns:
            string: name from supplier
        """
        result = self.company.name if self.company else None
        return result

    def supplier_reference_number(self):
        """
        supplier_reference_number

        Returns:
            string: reference number from supplier
        """
        result = self.company.reference_number if self.company else None
        return result

    def supplier_slug(self):
        """
        supplier_slug

        Returns:
            string: slug from supplier
        """
        result = self.company.slug if self.company else None
        return result

    def supplier_url_detail(self):
        """
        supplier_url_detail

        Returns:
            string: url to supplier detail page
        """
        return reverse(
            'storagemanagement:supplier_detail',
            kwargs={'supplier':self.supplier_slug()}
        )

    # Fields/Methodes for the urls
    def url_booking(self):
        """
        url_booking

        Returns:
            string: url to booking page
        """
        return reverse(
            'storagemanagement:supplieritem_booking_overview',
            kwargs={'supplieritem':self.slug}
        )

    def url_booking_list(self):
        """
        url_booking_list

        Returns:
            string: url to booking list page
        """
        return reverse(
            'storagemanagement:supplieritem_booking_list',
            kwargs={'supplieritem':self.slug}
        )

    def url_booking_table(self):
        """
        url_booking_table

        Returns:
            string: url to booking table page
        """
        return reverse(
            'storagemanagement:supplieritem_booking_table',
            kwargs={'supplieritem':self.slug}
        )

    def url_booking_add(self):
        """
        url_booking_add

        Returns:
            string: url to booking add page
        """
        return reverse(
            'storagemanagement:supplieritem_booking_add',
            kwargs={'supplieritem':self.slug}
        )

    def url_booking_create(self):
        """
        url_booking_create

        Returns:
            string: url to booking create page
        """
        return reverse(
            'storagemanagement:supplieritem_booking_create',
            kwargs={'supplieritem':self.slug}
        )

    def url_booking_remove(self):
        """
        url_booking_remove

        Returns:
            string: url to booking remove page
        """
        return reverse(
            'storagemanagement:supplieritem_booking_remove',
            kwargs={'supplieritem':self.slug}
        )

    def url_delete(self):
        """
        url_delete

        Returns:
            string: url to delete page
        """
        return reverse(
            'storagemanagement:supplieritem_delete',
            kwargs={'supplieritem':self.slug}
        )

    def url_detail(self):
        """
        url_detail

        Returns:
            string: url to detail page
        """
        return reverse(
            'storagemanagement:supplieritem_detail',
            kwargs={'supplieritem':self.slug}
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
            string: url to qrcode booking add page
        """
        return 'http://'+settings.HOST+self.url_booking_add()

    def url_qrcode_booking_create(self):
        """
        url_qrcode_booking_create

        Returns:
            string: url to qrcode booking create page
        """
        return 'http://'+settings.HOST+self.url_booking_create()

    def url_qrcode_booking_remove(self):
        """
        url_qrcode_booking_remove

        Returns:
            string: url to qrcode booking remove page
        """
        return 'http://'+settings.HOST+self.url_booking_remove()

    def url_qrcode_request(self):
        """
        url_qrcode_request

        Returns:
            string: url to qrcode request page
        """
        return 'http://'+settings.HOST+self.url_request_create()

    def url_request_create(self):
        """
        url_request_create

        Returns:
            string: url to request create page
        """
        return reverse(
            'storagemanagement:supplieritem_request_create',
            kwargs={'supplieritem':self.slug}
        )

    def url_storage(self):
        """
        url_storage

        Returns:
            string: url to storage page
        """
        return reverse(
            'storagemanagement:supplieritem_storage_overview',
            kwargs={'supplieritem':self.slug}
        )

    def url_storage_create(self):
        """
        url_storage_create

        Returns:
            string: url to storage create page
        """
        return reverse(
            'storagemanagement:supplieritem_storage_create',
            kwargs={'supplieritem':self.slug}
        )

    def url_storage_list(self):
        """
        url_storage_list

        Returns:
            string: url to storage list page
        """
        return reverse(
            'storagemanagement:supplieritem_storage_list',
            kwargs={'supplieritem':self.slug}
        )

    def url_storage_table(self):
        """
        url_storage_table

        Returns:
            string: url to storage table page
        """
        return reverse(
            'storagemanagement:supplieritem_storage_table',
            kwargs={'supplieritem':self.slug}
        )

    def url_update(self):
        """
        url_update

        Returns:
            string: url to update page
        """
        return reverse(
            'storagemanagement:supplieritem_update',
            kwargs={'supplieritem':self.slug}
        )

    def __str__(self):
        return f"{str(self.name)} ({str(self.item_number)})"

    class Meta:
        """
        contains all Meta data of the model
        """
        app_label = 'storagemanagement'
        default_permissions = ()
        ordering = []
        permissions = (
            ('add_supplieritem','SupplierItem can view create'),
            ('change_supplieritem','SupplierItem can view change'),
            ('delete_supplieritem','SupplierItem can view delete'),
            ('detail_supplieritem','SupplierItem can view detail'),
            ('list_supplieritem','SupplierItem can view list'),
            ('table_supplieritem','SupplierItem can view table'),
            ('view_supplieritem','SupplierItem can view overview'),
        )
        proxy = True
        verbose_name = "Lieferantenartikel"
        verbose_name_plural = "Lieferantenartikel"
#--------------------------------------------------------------------------------
