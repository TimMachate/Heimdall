#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from main.createdata.models import CreateData
from main.referencenumber.models import ReferenceNumber
from main.slug.models import Slug
from main.updatedata.models import UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class Ware(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "REWA"

    class Units(models.TextChoices):
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
    company_id = models.ForeignKey(
        blank = True,
        name = 'company_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'ware_company_id',
        to = 'relationshipmanagement.SupplierProxy',
        verbose_name = 'Firma',
    )

    # Fields/Methodes for the image
    image_id = models.ForeignKey(
        blank = True,
        name = 'image_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'ware_image_id',
        to = 'documentationmanagement.PictureProxy',
        verbose_name = 'Bild',
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
        help_text = "Preis der Ware.",
        max_digits = 12,
        name = 'price',
        null = True,
        verbose_name = 'Preis',
    )

    # Fields/Methodes for the name
    ware_number = models.CharField(
        blank = True,
        help_text = "Warennummer der Ware.",
        max_length = 200,
        name = 'ware_number',
        null = True,
        verbose_name = 'Warennummer',
    )

    # Fields/Methodes for the package unit
    unit_package = models.PositiveIntegerField(
        blank = True,
        help_text = "Verpackungseinheit der Ware.",
        name = 'unit_package',
        null = True,
        verbose_name = 'Verpackungseinheit',
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

    def url_detail(self):
        return reverse('relationshipmanagement:ware_detail',kwargs={"ware":self.slug})

    def url_delete(self):
        return reverse('relationshipmanagement:ware_delete',kwargs={"ware":self.slug})

    def url_request_add(self):
        return reverse('relationshipmanagement:ware_request_add',kwargs={"ware":self.slug})
    
    def url_update(self):
        return reverse('relationshipmanagement:ware_update',kwargs={"ware":self.slug})

    def __str__(self):
        return "{} ({})".format(str(self.name),str(self.ware_number))

    class Meta:
        app_label = 'relationshipmanagement'
        ordering = []
        permissions = (
            ('list_ware','Can view List Waren'),
            ('table_ware','Can view Table Waren'),
            ('detail_ware','Can view Detail Waren')
        )
        verbose_name = "Ware"
        verbose_name_plural = "Waren"
#--------------------------------------------------------------------------------