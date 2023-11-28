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
class Group(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STGR"

    # Fields/Methodes for the description of the group
    description = tinymce_models.HTMLField(
        blank = True,
        help_text = "Beschreibung der Gruppe.",
        name = 'description',
        null = True,
        verbose_name = 'Beschreibung',
    )

    # Fields/Methodes for the devices of the group
    devices = models.ManyToManyField(
        blank = True,
        name = 'devices',
        related_name = 'group_devices',
        to = 'structuremanagement.Device',
        verbose_name = 'Geräte',
    )
    
    def devices_count(self):
        return self.devices.all().count()

    # Fields/Methodes for the name of the group
    name = models.CharField(
        blank = False,
        help_text = "Name der Gruppe.",
        max_length = 200,
        name = 'name',
        null = False,
        verbose_name = 'Gruppe',
    )

    def url_delete(self):
        return reverse('structuremanagement:group_delete',kwargs={'group':self.slug})

    def url_detail(self):
        return reverse('structuremanagement:group_detail',kwargs={'group':self.slug})

    def url_update(self):
        return reverse('structuremanagement:group_update',kwargs={'group':self.slug})
    
    def __str__(self):
        return "{} ({})".format(self.name,self.reference_number)

    class Meta:
        app_label = 'structuremanagement'
        ordering = ['name']
        permissions = (
            ('list_group','Can view List Gruppe'),
            ('table_group','Can view Table Gruppe'),
            ('detail_group','Can view Detail Gruppe'),
        )
        verbose_name = "Gruppe"
        verbose_name_plural = "Gruppen"
#--------------------------------------------------------------------------------