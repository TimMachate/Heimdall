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
class Customer(models.Model):

    company_id = models.OneToOneField(
        blank = True,
        name = 'company_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'customer_company_id',
        to = "relationshipmanagement.Company",
        verbose_name = 'Firma',
    )

    status = models.CharField(
        blank = True,
        default = "Banned",
        help_text = "Status des Kunden Banned/Basic/Premium",
        max_length = 200,
        name = 'status',
        null = True,
        verbose_name = 'Status',
    )

    def url_detail(self):
        return reverse('relationshipmanagement:customer_detail',kwargs={"customer":self.slug})

    def url_delete(self):
        return reverse('relationshipmanagement:customer_delete',kwargs={"customer":self.slug})
    
    def url_update(self):
        return reverse('relationshipmanagement:customer_update',kwargs={"customer":self.slug})

    class Meta:
        app_label = 'relationshipmanagement'
        ordering = []
        permissions = (
            ('list_customer','Can view List Kunde'),
            ('table_customer','Can view Table Kunde'),
            ('detail_customer','Can view Detail Kunde')
        )
        verbose_name = "Kundeninformation"
        verbose_name_plural = "Kundeninformationen"
#--------------------------------------------------------------------------------