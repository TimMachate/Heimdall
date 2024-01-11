"""
#--------------------------------------------------------------------------------
# Model File from Model Ware
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

from django.utils.translation import gettext_lazy as _
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
class CompanyItemBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):
    """
    CompanyItemBaseModel

    Args:
        CreateData (_type_): _description_
        ReferenceNumber (_type_): _description_
        Slug (_type_): _description_
        UpdateData (_type_): _description_
    """

    # Variables
    short_name = "STCI"

    class Units(models.TextChoices):
        """
        Units

        Args:
            models (_type_): _description_
        """
        PIECE = "Stk",_("Stk")
        MILLIMETER = "mm",_("mm")
        METER = "m",_("m")
        KILOMETER = "km",_("km")
        MILLIGRAMM = "mg",_("mg")
        GRAMM = "g",_("g")
        KILOGRAMM = "kg",_("kg")
        TONNES = "t",_("t")
        MILLILITER = "ml",_("ml")
        LITER = "l",_("l")

    # Fields/Methodes for the company
    company = models.ForeignKey(
        blank = True,
        name = 'company',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'companyitem_company',
        to = 'relationshipmanagement.Company',
        verbose_name = 'Firma',
    )

    # Fields/Methodes for the image
    if 'documentationmanagement' in [app.name for app in apps.get_app_configs()]:
        image = models.ForeignKey(
            blank = True,
            help_text = "Bild des Artikels.",
            name = 'image',
            null = True,
            on_delete = models.CASCADE,
            related_name = 'companyitem_image',
            to = 'documentationmanagement.PictureProxy',
            verbose_name = 'Bild',
        )
    else:
        image = models.FileField(
            blank = True,
            help_text = "Bild des Artikels.",
            name = "image",
            null = True,
            upload_to = 'relationshipmanagement/companyitem/',
            verbose_name = "Bild",
        )

    # Fields/Methodes for the name
    name = models.CharField(
        blank = True,
        help_text = "Name der Ware.",
        max_length = 200,
        name = 'name',
        null = True,
        verbose_name = 'Name',
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

    # Fields/Methodes for the unit
    unit = models.CharField(
        blank = True,
        choices = Units.choices,
        default = Units.PIECE,
        help_text = "Einheit der Ware.",
        max_length = 3,
        name = 'unit',
        null = True,
        verbose_name = 'Einheit',
    )

    # Fields/Methodes for the name
    item_number = models.CharField(
        blank = True,
        help_text = "Warennummer der Ware.",
        max_length = 200,
        name = 'item_number',
        null = True,
        verbose_name = 'Artikelnummer',
    )

    def __str__(self):
        return f"{str(self.name)} ({str(self.item_number)})"

    class Meta:
        """
        contains all Meta data of the model
        """
        app_label = 'relationshipmanagement'
        #db_table = 'relationshipmanagement_db'
        default_permissions = ()
#--------------------------------------------------------------------------------
class CompanyItem(CompanyItemBaseModel):
    """
    CompanyItem

    Args:
        CompanyItemBaseModel (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Fields/Methodes for the booking
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
            string: name from company
        """
        result = self.company.name if self.company else None
        return result

    def company_reference_number(self):
        """
        company_reference_number

        Returns:
            string: reference number from company
        """
        result = self.company.reference_number if self.company else None
        return result

    def company_slug(self):
        """
        company_slug

        Returns:
            string: slug from company
        """
        result = self.company.slug if self.company else None
        return result

    def company_url_detail(self):
        """
        company_url_detail

        Returns:
            string: url to company detail page
        """
        return reverse(
            'relationshipmanagement:company_detail',
            kwargs={'company':self.company_slug()}
        )

    # Image
    def image_name(self):
        """
        image_url

        Returns:
            string: url from picture image
        """
        result = self.image.name.split("/")[-1] if self.image else None
        return result

    def image_url(self):
        """
        image_url

        Returns:
            string: url from picture image
        """
        result = self.image.url if self.image else None
        return result

    # Fields/Methodes for the urls
    def url_delete(self):
        """
        url_delete

        Returns:
            string: url to delete page
        """
        return reverse(
            'relationshipmanagement:companyitem_delete',
            kwargs={'companyitem':self.slug}
        )

    def url_detail(self):
        """
        url_detail

        Returns:
            string: url to detail page
        """
        return reverse(
            'relationshipmanagement:companyitem_detail',
            kwargs={'companyitem':self.slug}
        )

    def url_qrcode(self):
        """
        url_qrcode

        Returns:
            string: url to qrcode page
        """
        return 'http://'+settings.HOST+self.url_detail()

    def url_request_create(self):
        """
        url_update

        Returns:
            string: url to update page
        """
        mail = self.company.email
        cc = ""
        subject = "Preisanfrage"
        body = f"""
Sehr geehrte Damen und Herren,%0D%0A
%0D%0A
bitte schicken sie mir ein Angebot für die folgenden Artikel.%0D%0A
%0D%0A
-----------------------------------------------------------------------------------------%0D%0A
Menge       | Einheit | Artikelnummer             | Artikel%0D%0A
-----------------------------------------------------------------------------------------%0D%0A
1           | {self.unit}   | {self.item_number}        | {self.name}%0D%0A
-----------------------------------------------------------------------------------------%0D%0A
%0D%0A
Mit freundlichen Grüßen%0D%0A
%0D%0A
%0D%0A
"""
        url = f"mailto:{mail}?subject={subject}&cc={cc}&body={body}"
        return url

    def url_update(self):
        """
        url_update

        Returns:
            string: url to update page
        """
        return reverse(
            'relationshipmanagement:companyitem_update',
            kwargs={'companyitem':self.slug}
        )

    def __str__(self):
        return f"{str(self.name)} ({str(self.item_number)})"

    class Meta:
        """
        contains all Meta data of the model
        """
        app_label = 'relationshipmanagement'
        default_permissions = ()
        ordering = []
        permissions = (
            ('add_companyitem','CompanyItem can view create'),
            ('change_companyitem','CompanyItem can view change'),
            ('delete_companyitem','CompanyItem can view delete'),
            ('detail_companyitem','CompanyItem can view detail'),
            ('list_companyitem','CompanyItem can view list'),
            ('table_companyitem','CompanyItem can view table'),
            ('view_companyitem','CompanyItem can view overview'),
        )
        proxy = True
        verbose_name = "Firmenartikel"
        verbose_name_plural = "Firmenartikel"
#--------------------------------------------------------------------------------
