#--------------------------------------------------------------------------------
# Models File from Model Company
# 25.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.apps import apps
from django.conf import settings
from django.db import models
from django.urls import reverse

from tinymce import models as tinymce_models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.booking.models import Booking
from storagemanagement.storage.models import Storage
if 'relationshipmanagement' in [app.name for app in apps.get_app_configs()]:
    from relationshipmanagement.company.model import CompanyBaseModel
else:
    from storagemanagement.models import CreateData,ReferenceNumber,Slug,UpdateData
    from storagemanagement.companycontact.models import CompanyContact
    from storagemanagement.companyitem.models import CompanyItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
if not 'relationshipmanagement' in [app.name for app in apps.get_app_configs()]:
    class CompanyBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):

        # Variables
        short_name = "STCO"

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

        # Fields/Methodes for the email
        email = models.EmailField(
            blank = True,
            help_text = "Email Adresse der Firma.",
            name = 'email',
            null = True,
            verbose_name = 'Email',
        )

        # Fields/Methodes for the house number
        house_number = models.CharField(
            blank = True,
            help_text = "Hausnummer",
            max_length = 200,
            name = 'house_number',
            null = True,
            verbose_name = 'Hausnummer',
        )

        # Fields/Methodes for the logo
        if 'documentationmanagement' in [app.name for app in apps.get_app_configs()]:
            logo = models.ForeignKey(
                blank = True,
                help_text = "Bild der Ware",
                name = 'logo',
                null = True,
                on_delete = models.CASCADE,
                related_name = 'companyitem_logo',
                to = 'documentationmanagement.PictureProxy',
                verbose_name = 'Bild',
            )
        else:
            logo = models.FileField(
                blank = True,
                help_text = "Logo der Firma.",
                name = "logo",
                null = True,
                upload_to = 'storagemanagement/company/',
                verbose_name = "Logo",
            )
        def logo_url(self):
            result = self.logo.url if self.logo else None
            return result


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

        # Fields/Methodes for the telephone
        telephone = models.CharField(
            blank = True,
            help_text = "Telefonnummer der Firma",
            max_length = 200,
            name = 'telephone',
            null = True,
            verbose_name = 'Telefon',
        )

        class Meta:
            app_label = 'storagemanagement'
            default_permissions = ()
            
#--------------------------------------------------------------------------------
class Company(CompanyBaseModel):

    def bookings(self):
        result = Booking.objects.filter(companyitem__company = self)
        if result == []:
            result = None
        return result

    def booking_count(self):
        queryset = self.bookings().count()
        result = queryset if queryset else 0
        return result

    def companycontacts(self):
        result = CompanyContact.objects.filter(company = self.id)
        if result == []:
            result = None
        return result

    def companycontact_count(self):
        queryset = self.companycontacts().count()
        result = queryset if queryset else 0
        return result

    def companyitems(self):
        result = CompanyItem.objects.filter(company = self.id)
        if result == []:
            result = None
        return result

    def companyitem_count(self):
        queryset = self.companyitems().count()
        result = queryset if queryset else 0
        return result

    def stock(self):
        result = Storage.objects.filter(companyitem__company = self,unload_datetime=None)
        if result == []:
            result = None
        return result

    def stock_count(self):
        queryset = self.stock().count()
        result = queryset if queryset else 0
        return result

    def stock_value(self):
        objects = self.stock()
        if objects:
            result = 0
            for obj in objects:
                result += obj.booking.price
        else:
            result = 0
        return result

    def storageitems(self):
        if self.stock():
            items = list(set(self.stock().values_list('companyitem_id',flat=True)))
            result = CompanyItem.objects.filter(id__in = items).values_list('storageitem',flat=True)
            if result == []:
                result = None
        else:
            result = None
        return result

    def storageitem_count(self):
        queryset = self.storageitems()
        result = queryset.count() if queryset else 0
        return result

    # Urls
    def url_booking(self):
        return reverse('storagemanagement:company_booking_overview',kwargs={"company":self.slug})
    
    def url_booking_create(self):
        return reverse('storagemanagement:company_booking_create',kwargs={"company":self.slug})
    
    def url_booking_list(self):
        return reverse('storagemanagement:company_booking_list',kwargs={"company":self.slug})
    
    def url_booking_table(self):
        return reverse('storagemanagement:company_booking_table',kwargs={"company":self.slug})

    def url_companycontact(self):
        return reverse('storagemanagement:company_companycontact_overview',kwargs={"company":self.slug})
    
    def url_companycontact_create(self):
        return reverse('storagemanagement:company_companycontact_create',kwargs={"company":self.slug})
    
    def url_companycontact_list(self):
        return reverse('storagemanagement:company_companycontact_list',kwargs={"company":self.slug})
    
    def url_companycontact_table(self):
        return reverse('storagemanagement:company_companycontact_table',kwargs={"company":self.slug})

    def url_companyitem(self):
        return reverse('storagemanagement:company_companyitem_overview',kwargs={"company":self.slug})
    
    def url_companyitem_create(self):
        return reverse('storagemanagement:company_companyitem_create',kwargs={"company":self.slug})
    
    def url_companyitem_list(self):
        return reverse('storagemanagement:company_companyitem_list',kwargs={"company":self.slug})
    
    def url_companyitem_table(self):
        return reverse('storagemanagement:company_companyitem_table',kwargs={"company":self.slug})

    def url_detail(self):
        return reverse('storagemanagement:company_detail',kwargs={"company":self.slug})

    def url_delete(self):
        return reverse('storagemanagement:company_delete',kwargs={"company":self.slug})

    def url_qrcode(self):
        return 'http://'+settings.HOST+self.url_detail()

    def url_storage(self):
        return reverse('storagemanagement:company_storage_overview',kwargs={"company":self.slug})
    
    def url_storage_create(self):
        return reverse('storagemanagement:company_storage_create',kwargs={"company":self.slug})
    
    def url_storage_list(self):
        return reverse('storagemanagement:company_storage_list',kwargs={"company":self.slug})
    
    def url_storage_table(self):
        return reverse('storagemanagement:company_storage_table',kwargs={"company":self.slug})

    def url_update(self):
        return reverse('storagemanagement:company_update',kwargs={"company":self.slug})

    def __str__(self):
            return "{} ({})".format(str(self.name),str(self.reference_number))
        
    class Meta:
        app_label = 'storagemanagement'
        default_permissions = ()
        ordering = []
        permissions = (
            ('add_company','Company can view create'),
            ('change_company','Company can view change'),
            ('delete_company','Company can view delete'),
            ('detail_company','Company can view detail'),
            ('list_company','Company can view list'),
            ('table_company','Company can view table'),
            ('view_company','Company can view overview'),
        )
        proxy = True
        verbose_name = "Firma"
        verbose_name_plural = "Firmen"