#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models
from django.urls import reverse
from django.utils import timezone

from tinymce import models as tinymce_models
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
class Error(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STER"

    # Fields/Methodes for the description of the error
    description = tinymce_models.HTMLField(
        blank = True,
        help_text = "Beschreibung des Fehler.",
        name = 'description',
        null = True,
        verbose_name = 'Beschreibung',
    )

    # Fields/Methodes for the error data of the error
    def errors(self):
        return ErrorData.objects.filter(error_id = self.id)

    def errors_count(self):
        return self.errors().count()

    def error_last(self):
        if self.errors_count() > 0:
            result = self.errors().order_by('-create_datetime')[0]
        else:
            result = None
        return result

    # Fields/Methodes for the name of the error
    name = models.CharField(
        blank = False,
        help_text = "Name des Fehler.",
        max_length = 200,
        name = 'name',
        null = False,
        verbose_name = 'Fehler',
    )

    def url_data_create(self):
        return reverse('structuremanagement:error_errordata_create',kwargs={'error':self.slug})
    
    def url_data_list(self):
        return reverse('structuremanagement:error_errordata_list',kwargs={'error':self.slug})
    
    def url_data_table(self):
        return reverse('structuremanagement:error_errordata_table',kwargs={'error':self.slug})

    def url_delete(self):
        return reverse('structuremanagement:error_delete',kwargs={'error':self.slug})

    def url_detail(self):
        return reverse('structuremanagement:error_detail',kwargs={'error':self.slug})

    def url_update(self):
        return reverse('structuremanagement:error_update',kwargs={'error':self.slug})
    
    def __str__(self):
        return "{} ({})".format(self.name,self.reference_number)

    class Meta:
        app_label = 'structuremanagement'
        ordering = ['name']
        permissions = (
            ('list_error','Can view List Fehler'),
            ('table_error','Can view Table Fehler'),
            ('detail_error','Can view Detail Fehler'),
            ('pdf_error','Can view PDF Fehler')
        )
        verbose_name = "Fehler"
        verbose_name_plural = "Fehler"
#--------------------------------------------------------------------------------
class ErrorData(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STERDA"

    # Fields/Methodes for the device of the error data
    device_id = models.ForeignKey(
        name = 'device_id',
        verbose_name = 'Maschine',
        related_name = 'error_data_device_id',
        to = 'structuremanagement.Device',
        on_delete = models.CASCADE,
        blank = False,
        null = False,
    )

    # Fields/Methodes for the error of the error data
    error = models.ForeignKey(
        name = 'error_id',
        verbose_name = 'Fehlermeldung',
        related_name = 'error_data_error_id',
        to = 'structuremanagement.Error',
        on_delete = models.PROTECT,
        blank = False,
        null = False,
    )
    
    # Fields/Methodes for the notice of the error data
    notice = tinymce_models.HTMLField(
        name = 'notice',
        verbose_name = 'Bemerkungen',
        blank = True,
        null = True,
    )
    
    def url_delete(self):
        return reverse('structuremanagement:errordata_delete',kwargs={'errordata':self.slug})
    
    def url_detail(self):
        return reverse('structuremanagement:errordata_detail',kwargs={'errordata':self.slug})
    
    def url_update(self):
        return reverse('structuremanagement:errordata_update',kwargs={'errordata':self.slug})

    def __str__(self):
        return str(self.create_datetime.strftime("%d.%m.%Y,%H:%M:%S"))+'-'+str(self.device_id.reference_number)+'-'+str(self.error_id.reference_number)

    class Meta:
        app_label = 'structuremanagement'
        ordering = ['-create_datetime']
        permissions = (
            ('list_errordata','Can view List Fehler Daten'),
            ('table_errordata','Can view Table Fehler Daten'),
            ('detail_errordata','Can view Detail Fehler Daten')
        )
        verbose_name = "Fehler Daten"
        verbose_name_plural = "Fehler Daten"
#--------------------------------------------------------------------------------