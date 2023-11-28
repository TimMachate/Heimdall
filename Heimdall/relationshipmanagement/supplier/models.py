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
from relationshipmanagement.ware.models import Ware
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class Supplier(models.Model):

    company_id = models.OneToOneField(
        name = 'company_id',
        verbose_name = 'Firma',
        related_name= 'supplier_company_id',
        to = 'relationshipmanagement.Company',
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )

    def wares(self):
        return Ware.objects.filter(company_id = self.company_id)

    class Meta:
        app_label = 'relationshipmanagement'
        ordering = []
        permissions = (
            ('list_supplier','Can view List Lieferant'),
            ('table_supplier','Can view Table Lieferant'),
            ('detail_supplier','Can view Detail Lieferant')
        )
        verbose_name = "Lieferanteninformation"
        verbose_name_plural = "Lieferanteninformationen"
#--------------------------------------------------------------------------------