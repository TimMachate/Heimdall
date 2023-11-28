#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models
from django.urls import reverse
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class General(models.Model):

    company_id = models.OneToOneField(
        name = 'company_id',
        verbose_name = 'Firma',
        related_name= 'general_company_id',
        to = 'relationshipmanagement.Company',
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )

    class Meta:
        app_label = 'relationshipmanagement'
        ordering = []
        permissions = (
            ('list_general','Can view List Sonstige Firmen'),
            ('table_general','Can view Table Sonstige Firmen'),
            ('detail_general','Can view Detail Sonstige Firmen')
        )
        verbose_name = "Sonstigeinformation"
        verbose_name_plural = "Sonstigeinformationen"
#--------------------------------------------------------------------------------