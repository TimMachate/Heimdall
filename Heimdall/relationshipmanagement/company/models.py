#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from tinymce import models as tinymce_models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from main.referencenumber.models import ReferenceNumber
from main.createdata.models import CreateData
from main.slug.models import Slug
from main.updatedata.models import UpdateData
from relationshipmanagement.customer.models import Customer
from relationshipmanagement.general.models import General
from relationshipmanagement.person.models import Person
from relationshipmanagement.supplier.models import Supplier
from relationshipmanagement.ware.models import Ware
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model Manager
#--------------------------------------------------------------------------------
class CustomerManager(models.Manager):
    def get_queryset(self):
        return super(CustomerManager,self).get_queryset().filter(customer=True)
#--------------------------------------------------------------------------------
class GeneralManager(models.Manager):
    def get_queryset(self):
        return super(GeneralManager,self).get_queryset().filter(customer=False,supplier=False)
#--------------------------------------------------------------------------------
class SupplierManager(models.Manager):
    def get_queryset(self):
        return super(SupplierManager,self).get_queryset().filter(supplier=True)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class Company(CreateData, ReferenceNumber, Slug, UpdateData):

    # Variables
    short_name = "RECO"

    # Fields/Methodes for the city
    city = models.CharField(
        blank = True,
        help_text = "Stadt",
        max_length = 200,
        name = 'city',
        null = True,
        verbose_name = 'Stadt',
    )

    # Fields/Methodes for the country
    country = models.CharField(
        blank = True,
        help_text = "Land",
        max_length = 200,
        name = 'country',
        null = True,
        verbose_name = 'Land',
    )

    # Fields/Methodes for the customer
    customer = models.BooleanField(
        blank = True,
        default = False,
        help_text = "Handelt es sich bei der Firma um einen Kunden?",
        name = 'customer',
        null = False,
        verbose_name = 'Kunde',
    )

    def customer_information(self):
        if Customer.objects.filter(company_id=self.id).exists():
            result = Customer.objects.get(company_id = self.id)
        else:
            result=None
        return result

    # Fields/Methodes for the email
    def emails(self):
        return Email.objects.filter(company_id = self)

    # Fields/Methodes for the house number
    house_number = models.CharField(
        blank = True,
        help_text = "Hausnummer",
        max_length = 200,
        name = 'house_number',
        null = True,
        verbose_name = 'Hausnummer',
    )

    # Fields/Methodes for the name
    name = models.CharField(
        blank = True,
        help_text = "Name der Firma.",
        max_length = 200,
        name = 'name',
        null = True,
        verbose_name = 'Name',
    )

    # Fields/Methodes for the notice
    notice = tinymce_models.HTMLField(
        blank = True,
        help_text = "Nützliche Informationen über die Firma.",
        name = 'notice',
        null = True,
        verbose_name = 'Bemerkung',
    )

    def persons(self):
        return Person.objects.filter(company_id = self.id)

    # Fields/Methodes for the post code
    post_code = models.CharField(
        blank = True,
        help_text = "Postleitzahl",
        max_length = 200,
        name = 'post_code',
        null = True,
        verbose_name = 'Postleitzahl',
    )

    # Fields/Methodes for the street
    street = models.CharField(
        blank = True,
        help_text = "Straße ohne Hausnummer",
        max_length = 200,
        name = 'street',
        null = True,
        verbose_name = 'Straße',
    )

    # Fields/Methodes for the supplier
    supplier = models.BooleanField(
        blank = True,
        default = False,
        help_text = "Handelt es sich bei der Firma um einen Lieferanten?",
        name = 'supplier',
        null = False,
        verbose_name = 'Lieferant',
    )

    def supplier_information(self):
        if SupplierProxy.objects.get(id=self.id):
            result = SupplierProxy.objects.get(id=self.id)
        else:
            result=None
        return result

    # Fields/Methodes for the telephone numbers
    def telephones(self):
        return Telephone.objects.filter(company_id = self)

    def url_detail(self):
        return reverse('relationshipmanagement:company_detail',kwargs={"company":self.slug})

    def url_delete(self):
        return reverse('relationshipmanagement:company_delete',kwargs={"company":self.slug})
    
    def url_update(self):
        return reverse('relationshipmanagement:company_update',kwargs={"company":self.slug})

    def __str__(self):
        return str(self.name) + " (" + str(self.reference_number) + ")"
    
    class Meta:
        app_label = 'relationshipmanagement'
        ordering = ['name']
        permissions = (
            ('list_company','Can view List Unternehmen'),
            ('table_company','Can view Table Unternehmen'),
            ('detail_company','Can view Detail Unternehmen')
        )
        verbose_name = "Unternehmen"
        verbose_name_plural = "Unternehmen"
#--------------------------------------------------------------------------------
class CustomerProxy(Company):
    objects = CustomerManager()

    def url_detail(self):
        return reverse('relationshipmanagement:customer_detail',kwargs={"customer":self.slug})

    def url_delete(self):
        return reverse('relationshipmanagement:customer_delete',kwargs={"customer":self.slug})
    
    def url_update(self):
        return reverse('relationshipmanagement:customer_update',kwargs={"customer":self.slug})

    class Meta:
        proxy = True
        verbose_name = 'Kunde'
        verbose_name_plural = 'Kunden'
#--------------------------------------------------------------------------------
class Email(models.Model):

    company_id = models.ForeignKey(
        blank = True,
        help_text = "Firma die zur Email gehört.",
        name = 'company_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = "email_company_id",
        to = "relationshipmanagement.Company",
        verbose_name = 'Firma',
    )

    email = models.EmailField(
        blank = True,
        help_text = "Email-Adresse.",
        name = 'email',
        null = True,
        verbose_name = 'Email',
    )

    target = models.CharField(
        blank = True,
        help_text = "Ziel in der Firma.",
        max_length = 200,
        name = 'target',
        null = True,
        verbose_name = 'Ziel',
    )

    class Meta:
        app_label = 'relationshipmanagement'
        verbose_name = "Email"
        verbose_name_plural = "Emails"
#--------------------------------------------------------------------------------
class GeneralProxy(Company):
    objects = GeneralManager()

    def url_detail(self):
        return reverse('relationshipmanagement:general_detail',kwargs={"general":self.slug})

    def url_delete(self):
        return reverse('relationshipmanagement:general_delete',kwargs={"general":self.slug})
    
    def url_update(self):
        return reverse('relationshipmanagement:general_update',kwargs={"general":self.slug})

    class Meta:
        proxy = True
        verbose_name = 'Sonstige Firma'
        verbose_name_plural = 'Sonstige Firmen'
#--------------------------------------------------------------------------------
class SupplierProxy(Company):
    objects = SupplierManager()

    def wares(self):
        return Ware.objects.filter(company_id = self.id)

    def url_detail(self):
        return reverse('relationshipmanagement:supplier_detail',kwargs={"supplier":self.slug})

    def url_delete(self):
        return reverse('relationshipmanagement:supplier_delete',kwargs={"supplier":self.slug})
    
    def url_update(self):
        return reverse('relationshipmanagement:supplier_update',kwargs={"supplier":self.slug})

    class Meta:
        proxy = True
        verbose_name = 'Lieferant'
        verbose_name_plural = 'Lieferanten'
#--------------------------------------------------------------------------------
class Telephone(models.Model):

    class Types(models.IntegerChoices):
        TELEPHONE = 1,_("Telefon")
        MOBILEPHONE = 2,_("Handy")
        FAX = 3,_("Fax")

    company_id = models.ForeignKey(
        blank = True,
        help_text = "Firma die zur Telefonnummer gehört.",
        name = 'company_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = "telephone_company_id",
        to = "relationshipmanagement.Company",
        verbose_name = 'Firma',
    )

    number = models.CharField(
        blank = True,
        help_text = "Telefonnummer.",
        max_length = 200,
        name = 'number',
        null = True,
        verbose_name = 'Telefonnummer',
    )

    target = models.CharField(
        blank = True,
        help_text = "Ziel in der Firma.",
        max_length = 200,
        name = 'target',
        null = True,
        verbose_name = 'Ziel',
    )

    # Fields/Methodes for the type
    type = models.IntegerField(
        choices = Types.choices,
        default = Types.TELEPHONE,
        name="type",
        verbose_name="Typ",
    )

    class Meta:
        app_label = 'relationshipmanagement'
        verbose_name = "Telefonnummer"
        verbose_name_plural = "Telefonnummern"
#--------------------------------------------------------------------------------