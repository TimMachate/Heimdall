#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

import os
from pathlib import Path
import qrcode
import shutil
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
# Model Manager
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class Picture(ReferenceNumber,Slug):

    # Variables
    short_name = "DOPI"

    file_id = models.OneToOneField(
        blank = True,
        name = 'file_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'picture_file_id',
        to = 'documentationmanagement.File',
        verbose_name = 'Datei',  
    )

    content = HTMLField(
        name = 'content',
        verbose_name = 'Inhalt',
        blank = True,
        null = True,
    )
#--------------------------------------------------------------------------------