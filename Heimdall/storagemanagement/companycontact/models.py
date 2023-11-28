#--------------------------------------------------------------------------------
# Models File from Model CompanyContact
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
from django.utils.translation import gettext_lazy as _

from tinymce import models as tinymce_models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
if 'relationshipmanagement' in [app.name for app in apps.get_app_configs()]:
    from relationshipmanagement.companycontact.model import CompanyContact,CompanyContactEmail,CompanyContactTelephone
else:
    from storagemanagement.models import (
        CreateData,
        ReferenceNumber,
        Slug,
        UpdateData
        )
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
if not 'relationshipmanagement' in [app.name for app in apps.get_app_configs()]:
    class CompanyContactBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):

        # Variables
        short_name = "STCC"

        company = models.ForeignKey(
            name = 'company',
            verbose_name = 'Firma',
            related_name = 'companycontact_company',
            to = 'storagemanagement.Company',
            on_delete = models.CASCADE,
            blank = True,
            null = True,
        )

        first_name = models.CharField(
            max_length = 200,
            name = 'first_name',
            verbose_name = 'Vorname',
            blank = True,
            null = True,
        )

        last_name = models.CharField(
            max_length = 200,
            name = 'last_name',
            verbose_name = 'Nachname',
            blank = True,
            null = True,
        )

        notice = tinymce_models.HTMLField(
            name = 'notice',
            verbose_name = 'Bemerkung',
            blank = True,
            null = True,
        )

        class Meta:
            app_label = 'storagemanagement'
            default_permissions = ()
            
    #----------------------------------------------------------------------------
    class CompanyContactEmailBaseModel(models.Model):

        companycontact = models.ForeignKey(
            blank = True,
            help_text = "Kontakt der zur Email gehört.",
            name = 'companycontact',
            null = True,
            on_delete = models.CASCADE,
            related_name = "companycontactbasemodel_companycontact",
            to = "storagemanagement.CompanyContactBaseModel",
            verbose_name = 'Kontakt',
        )

        email = models.EmailField(
            blank = True,
            help_text = "Email-Adresse.",
            name = 'email',
            null = True,
            verbose_name = 'Email',
        )

        class Meta:
            app_label = 'storagemanagement'
            default_permissions = ()
            verbose_name = "Email"
            verbose_name_plural = "Emails"

    #----------------------------------------------------------------------------  
    class CompanyContactTelephoneBaseModel(models.Model):

        class Types(models.IntegerChoices):
            TELEPHONE = 1,_("Telefon")
            MOBILEPHONE = 2,_("Handy")
            FAX = 3,_("Fax")

        companycontact = models.ForeignKey(
            blank = True,
            help_text = "Kontakt der zur Telefonnummer gehört.",
            name = 'companycontact',
            null = True,
            on_delete = models.CASCADE,
            related_name = "companycontacttelephonebasemodel_companycontact",
            to = "storagemanagement.CompanyContactBaseModel",
            verbose_name = 'Kontakt',
        )

        number = models.CharField(
            blank = True,
            help_text = "Telefonnummer.",
            max_length = 200,
            name = 'number',
            null = True,
            verbose_name = 'Telefonnummer',
        )

        # Fields/Methodes for the type
        types = models.IntegerField(
            choices = Types.choices,
            default = Types.TELEPHONE,
            name="types",
            verbose_name="Typ",
        )

        class Meta:
            app_label = 'storagemanagement'
            default_permissions = ()
            verbose_name = "Telefonnummer"
            verbose_name_plural = "Telefonnummern"

    #----------------------------------------------------------------------------
#--------------------------------------------------------------------------------
class CompanyContact(CompanyContactBaseModel):

    # Company
    def company_id(self):
        result = self.company.id if self.company else None
        return result

    def company_name(self):
        result = self.company.name if self.company else None
        return result
        
    def company_reference_number(self):
        result = self.company.reference_number if self.company else None
        return result
        
    def company_slug(self):
        result = self.company.slug if self.company else None
        return result
        
    def company_url_detail(self):
        result = self.company.url_detail() if self.company else None
        return result

    # Fields/Methodes for the email
    def emails(self):
        result = CompanyContactEmail.objects.filter(companycontact = self)
        if result == []:
            result = None
        return result

    def email_count(self):
        queryset = self.emails()
        result = queryset.count() if queryset else 0
        return result

    # Fields/Methodes for the name
    def name(self):
        if self.last_name and self.first_name:
            result = str(self.last_name) + ', ' + str(self.first_name)
        elif self.last_name and not self.first_name:
            result = str(self.last_name)
        elif not self.last_name and self.first_name:
            result = str(self.first_name)
        else:
            result = self.reference_number
        return result

    # Fields/Methodes for the telephone numbers
    def telephones(self):
        result = CompanyContactTelephone.objects.filter(companycontact = self)
        if result == []:
            result = None
        return result

    def telephone_count(self):
        queryset = self.telephones()
        result = queryset.count() if queryset else 0
        return result

    # Fields/Methodes for the urls
    def url_detail(self):
        return reverse('storagemanagement:companycontact_detail',kwargs={"companycontact":self.slug})

    def url_delete(self):
        return reverse('storagemanagement:companycontact_delete',kwargs={"companycontact":self.slug})

    def url_qrcode(self):
        return 'http://'+settings.HOST+self.url_detail()
    
    def url_update(self):
        return reverse('storagemanagement:companycontact_update',kwargs={"companycontact":self.slug})

    def __str__(self):
            return "{} ({})".format(str(self.name()),str(self.reference_number))

    class Meta:
        app_label = 'storagemanagement'
        ordering = []
        default_permissions = ()
        permissions = (
            ('add_companycontact','CompanyContact can view create'),
            ('change_companycontact','CompanyContact can view change'),
            ('delete_companycontact','CompanyContact can view delete'),
            ('detail_companycontact','CompanyContact can view detail'),
            ('list_companycontact','CompanyContact can view list'),
            ('table_companycontact','CompanyContact can view table'),
            ('view_companycontact','CompanyContact can view overview'),
        )
        verbose_name = "Firmenkontakt"
        verbose_name_plural = "Firmenkontakte"
#--------------------------------------------------------------------------------
class CompanyContactEmail(CompanyContactEmailBaseModel):
    class Meta:
        app_label = 'storagemanagement'
        default_permissions = ()
        verbose_name = "Email"
        verbose_name_plural = "Emails"
#--------------------------------------------------------------------------------
class CompanyContactTelephone(CompanyContactTelephoneBaseModel):
    class Meta:
        app_label = 'storagemanagement'
        default_permissions = ()
        verbose_name = "Telefonnummer"
        verbose_name_plural = "Telefonnummern"
#--------------------------------------------------------------------------------