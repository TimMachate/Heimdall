#--------------------------------------------------------------------------------
# Models File from Model Slug
# 15.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class Slug(models.Model):

    # save methode 
    def save(self, *args, **kwargs):
        #------------------------------------------------------------------------
        # create a slug
        #------------------------------------------------------------------------
        sn = self.short_name if self.short_name else "OBJ"
        self.slug = slugify('{}-{}'.format(sn,self.id))
        #------------------------------------------------------------------------
        super().save(*args, **kwargs)

    # Fields/Methodes for the slug
    slug = models.SlugField(
        blank = False,
        default = None,
        editable = False,
        help_text = "Slug, mit der eine eindeutige Identifizierung ermöglicht wird.",
        name = 'slug',
        null = True,
        unique = True,
        verbose_name = 'Slug',
    )

    class Meta:
        abstract = True