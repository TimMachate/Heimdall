#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models
from django.utils import timezone
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class ReferenceNumber(models.Model):

    # Fields/Methodes for the reference number
    reference_number = models.CharField(
        blank = True,
        default = None,
        editable = False,
        help_text = "Referenznummer, mit der eine eindeutige Identifizierung ermöglicht wird.",
        max_length = 200,
        name = 'reference_number',
        null = True,
        verbose_name = 'Aktenzeichen',
    )

    # save methode 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #------------------------------------------------------------------------
        # create a reference number
        #------------------------------------------------------------------------
        sn = self.short_name if self.short_name else "OBJ"
        self.reference_number = '{}-{}'.format(sn,self.id).upper()
        #------------------------------------------------------------------------
        super().save(*args, **kwargs)

    class Meta:
        abstract = True