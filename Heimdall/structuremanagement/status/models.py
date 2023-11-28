#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.core.validators import MaxValueValidator, MinValueValidator
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
class Status(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STST"

    # Fields/Methodes for the description of the status
    description = tinymce_models.HTMLField(
        blank = True,
        help_text = "Beschreibung des Status.",
        name = 'description',
        null = True,
        verbose_name = 'Beschreibung',
    )

    # Fields/Methodes for the name of the status
    name = models.CharField(
        blank = False,
        help_text = "Name des Status.",
        max_length = 200,
        name = 'name',
        null = False,
        verbose_name = 'Status',
    )

    # Fields/Methodes for the color of the status
    rgba_alpha = models.DecimalField(
        decimal_places = 2,
        default = 1,
        help_text = "Sichtbarkeit des Hintergrundes zwischen 0 und 1. 1 = 0% transparent. 0 = 100% transparent",
        max_digits = 3,
        name = 'rgba_alpha',
        validators=[MaxValueValidator(1),MinValueValidator(0)],
        verbose_name = 'Sichtbarkeit',
    )

    rgba_blue = models.PositiveSmallIntegerField(
        default = 0,
        help_text = "Blau-Wert der Hintergrundfarbe",
        name = 'rgba_blue',
        validators=[MaxValueValidator(255),MinValueValidator(0)],
        verbose_name = 'Blau-Anteil',
    )

    rgba_green = models.PositiveSmallIntegerField(
        default = 0,
        help_text = "Grün-Wert der Hintergrundfarbe",
        name = 'rgba_green',
        validators=[MaxValueValidator(255),MinValueValidator(0)],
        verbose_name = 'Grün-Anteil',
    )

    rgba_red = models.PositiveSmallIntegerField(
        default = 0,
        help_text = "Rot-Wert der Hintergrundfarbe",
        name = 'rgba_red',
        validators=[MaxValueValidator(255),MinValueValidator(0)],
        verbose_name = 'Rot-Anteil',
    )

    def rgba_style(self):
        return "style=background-color:rgba("+str(self.rgba_red)+","+str(self.rgba_green)+","+str(self.rgba_blue)+","+str(self.rgba_alpha)+")"

    def rgba_value(self):
        return "{},{},{},{}".format(str(self.rgba_red),str(self.rgba_green),str(self.rgba_blue),str(self.rgba_alpha))

    # Fields/Methodes for the stati of the status
    def stati(self):
        result = StatusData.objects.filter(status_id=self.id)
        return result

    def stati_count(self):
        return self.stati().count()

    def stati_last(self):
        if self.stati_count() > 0:
            result = self.stati().order_by('-create_datetime')[0]
        else:
            result = None
        return result

    # Fields/Methodes for the url of the status
    def url_data_create(self):
        return reverse('structuremanagement:status_statusdata_create',kwargs={'status':self.slug})
    
    def url_data_list(self):
        return reverse('structuremanagement:status_statusdata_list',kwargs={'status':self.slug})
    
    def url_data_table(self):
        return reverse('structuremanagement:status_statusdata_table',kwargs={'status':self.slug})

    def url_delete(self):
        return reverse('structuremanagement:status_delete',kwargs={'status':self.slug})

    def url_detail(self):
        return reverse('structuremanagement:status_detail',kwargs={'status':self.slug})

    def url_update(self):
        return reverse('structuremanagement:status_update',kwargs={'status':self.slug})
    
    def __str__(self):
        return str(self.name)

    class Meta:
        app_label = 'structuremanagement'
        ordering = ['name']
        permissions = (
            ('list_status','Can view List Status'),
            ('table_status','Can view Table Status'),
            ('detail_status','Can view Detail Status'),
            ('pdf_status','Can view PDF Status')
        )
        verbose_name = "Status"
        verbose_name_plural = "Stati"
#--------------------------------------------------------------------------------
class StatusData(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STSTDA"

    # Fields/Methodes for the device of the status data
    device_id = models.ForeignKey(
        name = 'device_id',
        verbose_name = 'Gerät',
        related_name = 'statusdata_device_id',
        to = 'structuremanagement.Device',
        on_delete = models.CASCADE,
        blank = False,
        null = False,
    )

    # Fields/Methodes for the status of the status data
    status_id = models.ForeignKey(
        name = 'status_id',
        verbose_name = 'Status',
        related_name = 'statusdata_status_id',
        to = 'structuremanagement.Status',
        on_delete = models.CASCADE,
        blank = False,
        null = False,
    )
    
    def url_delete(self):
        return reverse('structuremanagement:statusdata_delete',kwargs={'statusdata':self.slug})
    
    def url_detail(self):
        return reverse('structuremanagement:statusdata_detail',kwargs={'statusdata':self.slug})
    
    def url_update(self):
        return reverse('structuremanagement:statusdata_update',kwargs={'statusdata':self.slug})
    
    def __str__(self):
        return str(self.create_datetime.strftime("%d.%m.%Y,%H:%M:%S"))+'-'+str(self.device_id.name)+'-'+str(self.status_id.name)

    class Meta:
        app_label = 'structuremanagement'
        ordering = ['-create_datetime']
        permissions = (
            ('list_statusdata','Can view List Status Daten'),
            ('table_statusdata','Can view Table Status Daten'),
            ('detail_statusdata','Can view Detail Status Daten')
        )
        verbose_name = "Status Daten"
        verbose_name_plural = "Status Daten"
#--------------------------------------------------------------------------------