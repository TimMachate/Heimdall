"""
#--------------------------------------------------------------------------------
# Models File from Model CompanyContact
# 16.12.2023
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

from tinymce import models as tinymce_models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.models import (
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
class CompanyContactBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):
    """
    CompanyContactBaseModel

    Args:
        CreateData (_type_): _description_
        ReferenceNumber (_type_): _description_
        Slug (_type_): _description_
        UpdateData (_type_): _description_
    """

    # Variables
    short_name = "STCC"

    company = models.ForeignKey(
        name = 'company',
        verbose_name = 'Firma',
        related_name = 'companycontact_company',
        to = 'relationshipmanagement.Company',
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
        """
        contains all Meta data of the model
        """
        app_label = 'relationshipmanagement'
        #db_table = 'relationshipmanagement_db'
        default_permissions = ()

#----------------------------------------------------------------------------
class CompanyContactEmailBaseModel(models.Model):
    """
    CompanyContactEmailBaseModel

    Args:
        models (_type_): _description_
    """

    companycontact = models.ForeignKey(
        blank = True,
        help_text = "Kontakt der zur Email gehört.",
        name = 'companycontact',
        null = True,
        on_delete = models.CASCADE,
        related_name = "companycontactbasemodel_companycontact",
        to = "relationshipmanagement.CompanyContactBaseModel",
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
        """
        contains all Meta data of the model
        """
        app_label = 'relationshipmanagement'
        #db_table = 'relationshipmanagement_db'
        default_permissions = ()
        verbose_name = "Email"
        verbose_name_plural = "Emails"

#----------------------------------------------------------------------------
class CompanyContactTelephoneBaseModel(models.Model):
    """
    CompanyContactTelephoneBaseModel

    Args:
        models (_type_): _description_
    """

    class Types(models.IntegerChoices):
        """
        Types

        Args:
            models (_type_): _description_
        """
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
        to = "relationshipmanagement.CompanyContactBaseModel",
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
        """
        contains all Meta data of the model
        """
        app_label = 'relationshipmanagement'
        #db_table = 'relationshipmanagement_db'
        default_permissions = ()
        verbose_name = "Telefonnummer"
        verbose_name_plural = "Telefonnummern"

#--------------------------------------------------------------------------------
class CompanyContact(CompanyContactBaseModel):
    """
    CompanyContact

    Args:
        CompanyContactBaseModel (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Company
    def company_id(self):
        """
        company_id

        Returns:
            int: id from company
        """
        result = self.company.id if self.company else None
        return result

    def company_name(self):
        """
        company_name

        Returns:
            string: name of company
        """
        result = self.company.name if self.company else None
        return result

    def company_reference_number(self):
        """
        company_reference_number

        Returns:
            string: reference number of company
        """
        result = self.company.reference_number if self.company else None
        return result

    def company_slug(self):
        """
        company_slug

        Returns:
            string: slug of company
        """
        result = self.company.slug if self.company else None
        return result

    def company_url_detail(self):
        """
        company_url_detail

        Returns:
            string: url of company detail page
        """
        return reverse(
                'relationshipmanagement:company_detail',
                kwargs={'company':self.company_slug()}
            )

    # Fields/Methodes for the email
    def emails(self):
        """
        emails

        Returns:
            queryset: contains all emails of contact
        """
        result = CompanyContactEmail.objects.filter(companycontact = self)
        if result == []:
            result = None
        return result

    def email_count(self):
        """
        email_count

        Returns:
            int: email count of contact
        """
        queryset = self.emails()
        result = queryset.count() if queryset else 0
        return result

    # Fields/Methodes for the name
    def name(self):
        """
        name

        Returns:
            string: name of the contact
        """
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
        """
        telephones

        Returns:
            queryset: contains all telephone numbers of contact
        """
        result = CompanyContactTelephone.objects.filter(companycontact = self)
        if result == []:
            result = None
        return result

    def telephone_count(self):
        """
        telephone_count

        Returns:
            int: count of the telephone numbers
        """
        queryset = self.telephones()
        result = queryset.count() if queryset else 0
        return result

    # Fields/Methodes for the urls
    def url_detail(self):
        """
        url_detail

        Returns:
            string: url to detail page
        """
        return reverse(
            'relationshipmanagement:companycontact_detail',
            kwargs={"companycontact":self.slug}
        )

    def url_delete(self):
        """
        url_delete

        Returns:
            string: url to delete page
        """
        return reverse(
            'relationshipmanagement:companycontact_delete',
            kwargs={"companycontact":self.slug}
        )

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
        return reverse(
            'relationshipmanagement:companycontact_update',
            kwargs={"companycontact":self.slug}
        )

    def __str__(self):
        return f"{str(self.name())} ({str(self.reference_number)})"

    class Meta:
        """
        contains all Meta data of the model
        """
        app_label = 'relationshipmanagement'
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
        proxy = True
        verbose_name = "Firmenkontakt"
        verbose_name_plural = "Firmenkontakte"
#--------------------------------------------------------------------------------
class CompanyContactEmail(CompanyContactEmailBaseModel):
    """
    CompanyContactEmail

    Args:
        CompanyContactEmailBaseModel (_type_): _description_
    """
    class Meta:
        """
        contains all Meta data of the model
        """
        app_label = 'relationshipmanagement'
        default_permissions = ()
        proxy = True
        verbose_name = "Email"
        verbose_name_plural = "Emails"
#--------------------------------------------------------------------------------
class CompanyContactTelephone(CompanyContactTelephoneBaseModel):
    """
    CompanyContactTelephone

    Args:
        CompanyContactTelephoneBaseModel (_type_): _description_
    """
    class Meta:
        """
        contains all Meta data of the model
        """
        app_label = 'relationshipmanagement'
        default_permissions = ()
        proxy = True
        verbose_name = "Telefonnummer"
        verbose_name_plural = "Telefonnummern"
#--------------------------------------------------------------------------------
