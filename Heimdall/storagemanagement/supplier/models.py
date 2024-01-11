"""
#--------------------------------------------------------------------------------
# Models File from Model Supplier
# 25.10.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
from django.db import models
from django.urls import reverse

from tinymce import models as tinymce_models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.company.models import CompanyBaseModel
from storagemanagement.booking.models import Booking
from storagemanagement.storage.models import Storage
from tools.createdata.models import CreateData
from tools.referencenumber.models import ReferenceNumber
from tools.slug.models import Slug
from tools.updatedata.models import UpdateData
from storagemanagement.suppliercontact.models import SupplierContact
from storagemanagement.supplieritem.models import SupplierItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model Manager
#--------------------------------------------------------------------------------
class SupplierManager(models.Manager):
    """
    SupplierManager

    Args:
        models (_type_): _description_
    """
    def get_queryset(self):
        """
        get_queryset

        Returns:
            queryset: contains all company objects witch are suppliers
        """
        return super(SupplierManager,self).get_queryset().filter(supplier=True)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class SupplierBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):
    """
    SupplierBaseModel

    Args:
        CreateData (_type_): _description_
        ReferenceNumber (_type_): _description_
        Slug (_type_): _description_
        UpdateData (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Variables
    short_name = "STSU"

    # Fields/Methodes for company
    company = models.OneToOneField(
        blank = False,
        help_text = "Firma ",
        name = "company",
        null = False,
        on_delete = models.CASCADE,
        related_name = "company_supplier",
        to = "relationshipmanagement.companybasemodel",
        verbose_name = "Firma",
    )

    # Fields/Methodes for email contacts
    email_address_offer = models.EmailField(
        blank = True,
        help_text = "Email bei der ein Angebot angefragt wird",
        name = "email_address_offer",
        null = True,
        verbose_name = "Email Angebot"
    )

    email_address_cc_offer = models.CharField(
        blank = True,
        help_text= """
CC Email bei der ein Angebot angefragt wird.
Mehrere Emails werden durch ein Simikolon getrennt.""",
        max_length = 200,
        name = "email_address_cc_offer",
        null = True,
        verbose_name = "CC Email Angebot"
    )

    email_address_order = models.EmailField(
        blank = True,
        help_text= "Email bei der eine Bestellung aufgegeben wird",
        name = "email_address_order",
        null = True,
        verbose_name = "Email Bestellung"
    )

    email_address_cc_order = models.CharField(
        blank = True,
        help_text= """
CC Email bei der eine Bestellung aufgegeben wird.
Mehrere Emails werden durch ein Simikolon getrennt.""",
        max_length = 200,
        name = "email_address_cc_order",
        null = True,
        verbose_name = "CC Email Bestellung"
    )

    email_body_offer = tinymce_models.HTMLField(
        default = """
Sehr geehrte Damen und Herren,

bitte schicken sie mir ein Angebot für die nachfolgend aufgelisteten Dinge.

Stückzahl [Einheit] - Artikel (Artikelnummer)
        """,
        help_text = "Anschreiben für ein Angebote.",
        name = 'email_body_offer',
        verbose_name = 'Anschreiben Angebot',
    )

    email_body_order = tinymce_models.HTMLField(
        default = """
Sehr geehrte Damen und Herren,

hiermit erhalten sie unsere Bestellung für die unten aufgelisteten Artikel. Im Anhang befindet sich der Auftrag.

Stückzahl [Einheit] - Artikel (Artikelnummer)
        """,
        help_text = "Anschreiben für eine Bestellung.",
        name = 'email_body_order',
        verbose_name = 'Anschreiben Bestellung',
    )

    email_subject_offer = models.CharField(
        default = "Angebot",
        help_text = "Inhalt der Betreffzeile bei der Anfrage eines Angebotes",
        max_length = 200,
        name = 'email_subject_offer',
        verbose_name = 'Betreff Angebot',
    )

    email_subject_order = models.CharField(
        default = "Bestellung",
        help_text = "Inhalt der Betreffzeile bei der Bestellung",
        max_length = 200,
        name = 'email_subject_order',
        verbose_name = 'Betreff Bestellung',
    )

    class Meta:
        """
        Meta Data from SupplierBaseModel
        """
        app_label = 'storagemanagement'
        default_permissions = ()

#--------------------------------------------------------------------------------
class Supplier(CompanyBaseModel):
    """
    Supplier

    Args:
        SupplierBaseModel (_type_): _description_
    """

    objects = SupplierManager()

    def booking_data(self):
        """
        bookings
        collect all bookings from supplier

        Returns:
            queryset: contains all bookings from supplier
        """
        result = Booking.objects.filter(supplieritem__company = self)
        if result == []:
            result = None
        return result

    def booking_count(self):
        """
        booking_count

        Returns:
            int: count bookings from supplier
        """
        queryset = self.booking_data().count()
        result = queryset if queryset else 0
        return result

    def suppliercontact_data(self):
        """
        suppliercontacts

        Returns:
            queryset: contains all contacts from supplier
        """
        result = SupplierContact.objects.filter(company = self)
        if result == []:
            result = None
        return result

    def suppliercontact_count(self):
        """
        suppliercontact_count

        Returns:
            int: count contacts from supplier
        """
        queryset = self.suppliercontact_data().count()
        result = queryset if queryset else 0
        return result

    def supplieritem_data(self):
        """
        supplieritems

        Returns:
            queryset: contains all items from supplier
        """
        result = SupplierItem.objects.filter(company = self)
        if result == []:
            result = None
        return result

    def supplieritem_count(self):
        """
        supplieritem_count

        Returns:
            int: count items from supplier
        """
        queryset = self.supplieritem_data().count()
        result = queryset if queryset else 0
        return result

    def stock_data(self):
        """
        stock

        Returns:
            queryset: contains all items in stock from supplier
        """
        result = Storage.objects.filter(supplieritem__company = self,unload_datetime=None)
        if result == []:
            result = None
        return result

    def stock_count(self):
        """
        stock_count

        Returns:
            int: count item in stock from supplier
        """
        queryset = self.stock_data().count()
        result = queryset if queryset else 0
        return result

    def stock_value(self):
        """
        stock_value

        Returns:
            float: value of all items in stock from supplier
        """
        objects = self.stock_data()
        if objects:
            result = 0
            for obj in objects:
                result += obj.booking.price
        else:
            result = 0
        return result

    def storageitems(self):
        """
        storageitems

        Returns:
            queryset: contains al storage items from supplier
        """
        if self.stock():
            items = list(set(self.stock().values_list('supplieritem_id',flat=True)))
            result = SupplierItem.objects.filter(
                id__in = items).values_list('storageitem',flat=True)
            if result == []:
                result = None
        else:
            result = None
        return result

    def storageitem_count(self):
        """
        storageitem_count

        Returns:
            int: count storage item from supplier
        """
        queryset = self.storageitems()
        result = queryset.count() if queryset else 0
        return result

    # Fields/Methodes Supplier Informations
    def supplier_info(self):
        """
        supplier_info

        Returns:
            query: Contains SupplierBaseModel Object
        """
        query = SupplierBaseModel.objects.filter(company=self)
        if query.exists():
            return query.first()
        else:
            query = SupplierBaseModel(
                company = self,
                email_address_offer = self.email,
                email_address_order = self.email
            )
            query.save()
            return query

    # Urls
    def url_booking(self):
        """
        url_booking

        Returns:
            string: url to booking page
        """
        return reverse(
            'storagemanagement:supplier_booking_overview',
            kwargs={"supplier":self.slug}
        )

    def url_booking_create(self):
        """
        url_booking_create

        Returns:
            string: url to booking create page
        """
        return reverse(
            'storagemanagement:supplier_booking_create',
            kwargs={"supplier":self.slug}
        )

    def url_booking_list(self):
        """
        url_booking_list

        Returns:
            string: url to booking list page
        """
        return reverse(
            'storagemanagement:supplier_booking_list',
            kwargs={"supplier":self.slug}
        )

    def url_booking_table(self):
        """
        url_booking_table

        Returns:
            string: url to booking table page
        """
        return reverse(
            'storagemanagement:supplier_booking_table',
            kwargs={"supplier":self.slug}
        )

    def url_suppliercontact(self):
        """
        url_suppliercontact

        Returns:
            string: url to supplier contact page
        """
        return reverse(
            'storagemanagement:supplier_suppliercontact_overview',
            kwargs={"supplier":self.slug}
        )

    def url_suppliercontact_create(self):
        """
        url_suppliercontact_create

        Returns:
            string: url to contact create page
        """
        return reverse(
            'storagemanagement:supplier_suppliercontact_create',
            kwargs={"supplier":self.slug}
        )

    def url_suppliercontact_list(self):
        """
        url_suppliercontact_list

        Returns:
            string: url to contact list page
        """
        return reverse(
            'storagemanagement:supplier_suppliercontact_list',
            kwargs={"supplier":self.slug}
        )

    def url_suppliercontact_table(self):
        """
        url_suppliercontact_table

        Returns:
            string: url to contact table page
        """
        return reverse(
            'storagemanagement:supplier_suppliercontact_table',
            kwargs={"supplier":self.slug}
        )

    def url_supplieritem(self):
        """
        url_supplieritem

        Returns:
            string: url to item page
        """
        return reverse(
            'storagemanagement:supplier_supplieritem_overview',
            kwargs={"supplier":self.slug}
        )

    def url_supplieritem_create(self):
        """
        url_supplieritem_create

        Returns:
            string: url to supplier item create page
        """
        return reverse(
            'storagemanagement:supplier_supplieritem_create',
            kwargs={"supplier":self.slug}
        )

    def url_supplieritem_list(self):
        """
        url_supplieritem_list

        Returns:
            string: url to supplier item list page
        """
        return reverse(
            'storagemanagement:supplier_supplieritem_list',
            kwargs={"supplier":self.slug}
        )

    def url_supplieritem_table(self):
        """
        url_supplieritem_table

        Returns:
            string: url to supplier item table page
        """
        return reverse(
            'storagemanagement:supplier_supplieritem_table',
            kwargs={"supplier":self.slug}
        )

    def url_detail(self):
        """
        url_detail

        Returns:
            string: url to supplier detail page
        """
        return reverse(
            'storagemanagement:supplier_detail',
            kwargs={"supplier":self.slug}
        )

    def url_delete(self):
        """
        url_delete

        Returns:
            string: url to supplier delete page
        """
        return reverse(
            'storagemanagement:supplier_delete',
            kwargs={"supplier":self.slug}
        )

    def url_qrcode(self):
        """
        url qrcode

        Returns:
            string: url to qrcode page
        """
        return 'http://'+settings.HOST+self.url_detail()

    def url_storage(self):
        """
        url_storage

        Returns:
            string: url to storage page
        """
        return reverse(
            'storagemanagement:supplier_storage_overview',
            kwargs={"supplier":self.slug}
        )

    def url_storage_create(self):
        """
        url_storage_create

        Returns:
            string: url to storage create page
        """
        return reverse('storagemanagement:supplier_storage_create',kwargs={"supplier":self.slug})

    def url_storage_list(self):
        """
        url_storage_list

        Returns:
            string: url to storage list page
        """
        return reverse(
            'storagemanagement:supplier_storage_list',
            kwargs={"supplier":self.slug}
        )

    def url_storage_table(self):
        """
        url_storage_table

        Returns:
            string: url to storage table page
        """
        return reverse(
            'storagemanagement:supplier_storage_table',
            kwargs={"supplier":self.slug}
        )

    def url_update(self):
        """
        url_update

        Returns:
            string: url to supplier update page
        """
        return reverse(
            'storagemanagement:supplier_update',
            kwargs={"supplier":self.slug}
        )

    def __str__(self):
        if self.supplier_info():
            return f"{self.name} ({self.supplier_info().reference_number})"
        else:
            return f"{self.reference_number}"

    class Meta:
        """
        Meta Data from Model
        """
        app_label = 'storagemanagement'
        default_permissions = ()
        ordering = []
        permissions = (
            ('add_supplier','Supplier can view create'),
            ('change_supplier','Supplier can view change'),
            ('delete_supplier','Supplier can view delete'),
            ('detail_supplier','Supplier can view detail'),
            ('list_supplier','Supplier can view list'),
            ('table_supplier','Supplier can view table'),
            ('view_supplier','Supplier can view overview'),
        )
        proxy = True
        verbose_name = "Lieferant"
        verbose_name_plural = "Lieferanten"
#--------------------------------------------------------------------------------
