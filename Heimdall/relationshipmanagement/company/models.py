"""
#--------------------------------------------------------------------------------
# Models File from Model Company
# 16.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
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
from relationshipmanagement.models import CreateData,ReferenceNumber,Slug,UpdateData
from relationshipmanagement.companycontact.models import CompanyContact
from relationshipmanagement.companyitem.models import CompanyItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class CompanyBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):
    """
    CompanyBaseModel

    Args:
        CreateData (_type_): _description_
        ReferenceNumber (_type_): _description_
        Slug (_type_): _description_
        UpdateData (_type_): _description_

    Returns:
        _type_: _description_
    """
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
            related_name = 'company_logo',
            to = 'documentationmanagement.PictureProxy',
            verbose_name = 'Bild',
        )
    else:
        logo = models.FileField(
            blank = True,
            help_text = "Logo der Firma.",
            name = "logo",
            null = True,
            upload_to = 'relationshipmanagement/company/',
            verbose_name = "Logo",
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

    # Fields/Methodes for Company
    supplier = models.BooleanField(
        default = False,
        help_text = 'Ist die Firma ein Lieferant',
        name = 'supplier',
        verbose_name = 'Lieferant',
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

    def __str__(self):
        return f"{self.name} ({self.reference_number})"

    class Meta:
        """
        Meta Data from CompanyBaseModel
        """
        app_label = 'relationshipmanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class Company(CompanyBaseModel):
    """
    Company

    Args:
        CompanyBaseModel (_type_): _description_
    """

    def companycontacts(self):
        """
        companycontacts

        Returns:
            queryset: contains all contacts from company
        """
        result = CompanyContact.objects.filter(company = self.id)
        if result == []:
            result = None
        return result

    def companycontact_count(self):
        """
        companycontact_count

        Returns:
            int: count contacts from company
        """
        queryset = self.companycontacts().count()
        result = queryset if queryset else 0
        return result

    def companyitems(self):
        """
        companyitems

        Returns:
            queryset: contains all items from company
        """
        result = CompanyItem.objects.filter(company = self.id)
        if result == []:
            result = None
        return result

    def companyitem_count(self):
        """
        companyitem_count

        Returns:
            int: count items from company
        """
        queryset = self.companyitems().count()
        result = queryset if queryset else 0
        return result

    # Logo
    def logo_name(self):
        """
        logo_url

        Returns:
            string: url from picture logo
        """
        result = self.logo.name.split("/")[-1] if self.logo else None
        return result

    def logo_url(self):
        """
        logo_url

        Returns:
            string: url from picture logo
        """
        result = self.logo.url if self.logo else None
        return result

    # Urls
    def url_companycontact(self):
        """
        url_companycontact

        Returns:
            string: url to company contact page
        """
        return reverse(
            'relationshipmanagement:company_companycontact_overview',
            kwargs={"company":self.slug}
        )

    def url_companycontact_create(self):
        """
        url_companycontact_create

        Returns:
            string: url to contact create page
        """
        return reverse(
            'relationshipmanagement:company_companycontact_create',
            kwargs={"company":self.slug}
        )

    def url_companycontact_list(self):
        """
        url_companycontact_list

        Returns:
            string: url to contact list page
        """
        return reverse(
            'relationshipmanagement:company_companycontact_list',
            kwargs={"company":self.slug}
        )

    def url_companycontact_table(self):
        """
        url_companycontact_table

        Returns:
            string: url to contact table page
        """
        return reverse(
            'relationshipmanagement:company_companycontact_table',
            kwargs={"company":self.slug}
        )

    def url_companyitem(self):
        """
        url_companyitem

        Returns:
            string: url to item page
        """
        return reverse(
            'relationshipmanagement:company_companyitem_overview',
            kwargs={"company":self.slug}
        )

    def url_companyitem_create(self):
        """
        url_companyitem_create

        Returns:
            string: url to company item create page
        """
        return reverse(
            'relationshipmanagement:company_companyitem_create',
            kwargs={"company":self.slug}
        )

    def url_companyitem_list(self):
        """
        url_companyitem_list

        Returns:
            string: url to company item list page
        """
        return reverse(
            'relationshipmanagement:company_companyitem_list',
            kwargs={"company":self.slug}
        )

    def url_companyitem_table(self):
        """
        url_companyitem_table

        Returns:
            string: url to company item table page
        """
        return reverse(
            'relationshipmanagement:company_companyitem_table',
            kwargs={"company":self.slug}
        )

    def url_detail(self):
        """
        url_detail

        Returns:
            string: url to company detail page
        """
        return reverse(
            'relationshipmanagement:company_detail',
            kwargs={"company":self.slug}
        )

    def url_delete(self):
        """
        url_delete

        Returns:
            string: url to company delete page
        """
        return reverse(
            'relationshipmanagement:company_delete',
            kwargs={"company":self.slug}
        )

    def url_qrcode(self):
        """
        url qrcode

        Returns:
            string: url to qrcode page
        """
        return 'http://'+settings.HOST+self.url_detail()

    def url_update(self):
        """
        url_update

        Returns:
            string: url to company update page
        """
        return reverse(
            'relationshipmanagement:company_update',
            kwargs={"company":self.slug}
        )

    def __str__(self):
        return f"{self.name} ({self.reference_number})"

    class Meta:
        """
        Meta Data from Model
        """
        app_label = 'relationshipmanagement'
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
#--------------------------------------------------------------------------------
