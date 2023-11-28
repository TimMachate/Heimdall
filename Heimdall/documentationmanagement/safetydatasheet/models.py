#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
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
class SafetyDataSheet(ReferenceNumber,Slug):

    # Variables
    short_name = "DOSA"

    file_id = models.OneToOneField(
        blank = True,
        name = 'file_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'safetydatasheet_file_id',
        to = 'documentationmanagement.File',
        verbose_name = 'Datei',  
    )

    actualization = models.PositiveIntegerField(
        blank = True,
        default = 730,
        help_text = 'Nächste Aktualisierung in Tagen.',
        name = 'actualization',
        null = True,
        verbose_name = 'Aktualisierung',
    )

    def status(self):
        if timezone.now() >= self.file_id.update_datetime + timezone.timedelta(days=self.actualization):
            result = 'alarm'
        elif timezone.now() >= self.file_id.update_datetime + timezone.timedelta(days=self.warning):
            result = 'warning'
        else:
            result = None
        return result
    
    def termination(self):
        result = self.file_id.update_datetime + timezone.timedelta(days=self.actualization)
        return result.strftime('%d.%m.%Y')+' '+result.strftime('%H:%M')

    warning = models.PositiveIntegerField(
        blank = True,
        default = 700,
        help_text = 'Warnung für die nächste Aktualisierung in Tagen.',
        name = 'warning',
        null = True,
        verbose_name = 'Warnung',
    )
#--------------------------------------------------------------------------------