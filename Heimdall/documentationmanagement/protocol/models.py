#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
from django.db import models
from django.http import HttpRequest
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

import json
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
# Model
#--------------------------------------------------------------------------------
class Protocol(ReferenceNumber,Slug):

    # Variables
    short_name = "DOPO"

    def data(self):
        return ProtocolData.objects.filter(protocol_id=self).order_by('-create_datetime')

    def data_last(self):
        if self.data().count() != 0:
            result = self.data().latest('create_datetime')
        else:
            result = None
        return result

    file_id = models.OneToOneField(
        blank = False,
        name = 'file_id',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'protocol_file_id',
        to = 'documentationmanagement.ProtocolProxy',
        verbose_name = 'Datei',
    )

    def name(self):
        return self.file_id.name

    procedure = HTMLField(
        blank = True,
        help_text= 'Ablauf des Protokolls.',
        name = 'procedure',
        null = True,
        verbose_name = 'Ablauf',
    )

    protocol = models.BooleanField(
        default = False,
        help_text= '',
        name = 'protocol',
        verbose_name = 'Protokoll',
    )

    def steps(self):
        if self.file_id:
            result = ProtocolStep.objects.filter(protocol_id=self).order_by('order')
        else:
            result = None
        return result

    def steps_count(self):
        return self.steps().count() if self.steps() else None

    topic = HTMLField(
        blank = True,
        help_text= 'Ziel und Thema des Protokolls.',
        name = 'topic',
        null = True,
        verbose_name = 'Thema',
    )

    def type(self):
        return self.file_id.Types(self.file_id.type).label if self.file_id else None

    def url_data_create(self):
        url = reverse('documentationmanagement:protocol_protocoldata_create',kwargs={'protocol':self.slug})
        return url

    def url_delete(self):
        url = reverse('documentationmanagement:protocol_delete',kwargs={'protocol':self.slug})
        return url
        
    def url_detail(self):
        url = reverse('documentationmanagement:protocol_detail',kwargs={'protocol':self.slug})
        return url
    
    def url_file(self):
        if self.file_id.file:
            result = self.file_id.file.url
        else:
            result = reverse('documentationmanagement:protocol_detail',kwargs={'protocol':self.slug})
        return result
    
    def url_qrcode(self):
        url = reverse('documentationmanagement:protocol_detail',kwargs={'protocol':self.slug})
        return url

    def url_update(self):
        url = reverse('documentationmanagement:protocol_update',kwargs={'protocol':self.slug})
        return url

    def version(self):
        return self.file_id.version() if self.file_id else None

    def __str__(self):
        return '{} ({})'.format(self.name(),self.reference_number)
#--------------------------------------------------------------------------------
class ProtocolStep(models.Model):
    protocol_id = models.ForeignKey(
        blank = True,
        name = 'protocol_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'protocolstep_protocol_id',
        to = 'documentationmanagement.Protocol',
        verbose_name = 'Protokoll',
    )

    name = models.CharField(
        max_length = 200,
        name = 'name',
        verbose_name = 'Titel',
        blank = True,
        null = True,
    )

    order = models.IntegerField(
        name = 'order',
        verbose_name = 'Reihenfolge',
        default = 0,
        blank = True,
        null = True,
    )

    text = HTMLField(
        name = 'text',
        verbose_name = 'Text',
        blank = True,
        null = True,
    )

    variables = models.ManyToManyField(
        name = 'variables',
        verbose_name = 'Variablen',
        related_name = 'protocolstep_variables',
        to = 'documentationmanagement.Variable',
        blank = True,
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        app_label = 'documentationmanagement'
        ordering = ['protocol_id','order']
        permissions = (
            ('list_protocolstep','Can view List Protocol Step'),
            ('table_protocolstep','Can view Table Protocol Step'),
            ('detail_protocolstep','Can view Detail Protocol Step')
        )
        verbose_name = 'Protokollschritt'
        verbose_name_plural = 'Protokollschritte'
#--------------------------------------------------------------------------------
class ProtocolData(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "DOPODA"

    protocol_id = models.ForeignKey(
        blank = True,
        name = 'protocol_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'protocoldata_protocol_id',
        to = 'documentationmanagement.Protocol',
        verbose_name = 'Protokoll',
    )

    json = models.JSONField(
        name = 'json',
        verbose_name = 'Json Daten',
        blank = True,
        null = True,
    )

    file = models.FileField(
        name = "file",
        verbose_name = "Datei",
        upload_to = '',
        blank = True,
        null = True,
    )

    def results(self):
        if self.json:
            result = json.loads(self.json)
        else:
            result = None
        return result

    def url_delete(self):
        return reverse('documentationmanagement:protocoldata_delete',kwargs={'protocoldata':self.slug})

    def url_detail(self):
        return reverse('documentationmanagement:protocoldata_detail',kwargs={'protocoldata':self.slug})

    def url_qrcode(self):
        return reverse('documentationmanagement:protocoldata_detail',kwargs={'protocoldata':self.slug})
    
    def url_update(self):
        return reverse('documentationmanagement:protocoldata_update',kwargs={'protocoldata':self.slug})

    version = models.CharField(
        max_length = 200,
        name = 'version',
        verbose_name = 'Version',
        editable = False,
        blank = True,
        null = True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #------------------------------------------------------------------------
        # safe version from the protocol
        #------------------------------------------------------------------------
        self.version = self.protocol_id.version()
        #------------------------------------------------------------------------

        #------------------------------------------------------------------------
        # safe file to correct location and rename it
        #------------------------------------------------------------------------
        if self.file:
            absolut_media_path = Path(settings.MEDIA_ROOT)
            path_to_protocols = os.path.join(absolut_media_path,self.protocol_id._meta.app_label,self.protocol_id.file_id.type,self.protocol_id.file_id.reference_number,'protocols')
            # create path if not exists
            if not os.path.exists(path_to_protocols):
                    os.makedirs(path_to_protocols)
            extend = self.file.name.split('.')[-1]
            file_path = self.file.path
            new_name = timezone.now().strftime("%Y%m%d%H%M%S_")+self.reference_number+'.'+extend
            os.rename(file_path,os.path.join(path_to_protocols,new_name))
            self.file = os.path.join(self.protocol_id._meta.app_label,self.protocol_id.file_id.type,self.protocol_id.file_id.reference_number,'protocols',new_name)
        #------------------------------------------------------------------------

        return super().save(*args, **kwargs)


    class Meta:
        app_label = 'documentationmanagement'
        ordering = ['-update_datetime']
        permissions = (
            ('list_protocoldata','Can view List Protocol Data'),
            ('table_protocoldata','Can view Table Protocol Data'),
            ('detail_protocoldata','Can view Detail Protocol Data')
        )
        verbose_name = 'Protokoll Daten'
        verbose_name_plural = 'Protokoll Daten'
#--------------------------------------------------------------------------------
class Variable(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "DOPOVA"

    class InputTypes(models.TextChoices):
        CHECKBOX = 'BO',_("Checkbox")
        NUMBER = 'NU',_("Zahl")
        TEXT = 'TE',_("Text")

    name = models.CharField(
        max_length = 200,
        name = 'name',
        verbose_name = 'Name',
        blank = True,
        null = True,
    )

    input_type = models.CharField(
        max_length = 2,
        name="input_type",
        verbose_name="Eingabe Typ",
        choices = InputTypes.choices,
        default = InputTypes.TEXT,
    )

    symbol = models.CharField(
        max_length = 10,
        name = 'symbol',
        verbose_name = 'Formelzeichen',
        blank = True,
        null = True,
    )

    unit = models.CharField(
        max_length = 20,
        name = 'unit',
        verbose_name = 'Einheit',
        blank = True,
        null = True,
    )
    
    def url_delete(self):
        return reverse('documentationmanagement:variable_delete',kwargs={'variable':self.slug})

    def url_detail(self):
        return reverse('documentationmanagement:variable_detail',kwargs={'variable':self.slug})
    
    def url_update(self):
        return reverse('documentationmanagement:variable_update',kwargs={'variable':self.slug})

    def __str__(self):
        return str(self.name) + ' [' + str(self.symbol) + ' in ' + str(self.unit) + ']'

    class Meta:
        app_label = 'documentationmanagement'
        ordering = []
        permissions = (
            ('list_variable','Can view List Variable'),
            ('table_variable','Can view Table Variable'),
            ('detail_variable','Can view Detail Variable')
        )
        verbose_name = 'Protokoll Variable'
        verbose_name_plural = 'Protokoll Variablen'
#--------------------------------------------------------------------------------