#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models
from django.utils import timezone
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class Slug(models.Model):

    slug = models.SlugField(
        name = 'slug',
        verbose_name = 'Slug',
        default = None,
        editable = False,
        blank = False,
        null = True,
    )

    class Meta:
        abstract = True