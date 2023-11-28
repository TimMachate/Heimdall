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
from documentationmanagement.protocol.models import ProtocolData

from main.createdata.models import CreateData
from main.referencenumber.models import ReferenceNumber
from main.slug.models import Slug
from main.updatedata.models import UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class Maintenance(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STMA"

    # Fields/Methodes for the alarm of the maintenance
    def alarm(self):
        if self.maintenance_next():
            if timezone.now()>self.maintenance_next():
                result = True
            else:
                result = False
        else:
            result = False
        return result

    # Fields/Methodes for the device of the maintenance
    device_id = models.ForeignKey(
        blank = True,
        help_text = "Gerät zu dem diese Wartung gehört.",
        name = 'device_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'maintenance_device_id',
        to = 'structuremanagement.device', 
        verbose_name = 'Maschine',
        )

    # Fields/Methodes for the maintenance
    def maintenance_count(self):
        result = self.maintenance_data().count()
        return result

    def maintenance_data(self):
        result = ProtocolData.objects.filter(protocol_id=self.protocol_id)
        return result

    def maintenance_last(self):
        if self.maintenance_data():
            result = self.maintenance_data().latest('create_datetime')
        else:
            result = None
        return result

    def maintenance_next(self):
        if self.maintenance_last():
            result = self.maintenance_last().create_datetime + timezone.timedelta(days=self.repetition_days,hours=self.repetition_hours,minutes=self.repetition_minutes,seconds=self.repetition_seconds)
        else:
            result = None
        return result

    # Fields/Methodes for the name of the maintenance
    name = models.CharField(
        blank = False,
        help_text = "Name der Wartung.",
        max_length = 200,
        name = 'name',
        null = False,
        verbose_name = 'Wartung',
    )

    # Fields/Methodes for the protocol of the maintenance
    protocol_id = models.ForeignKey(
        blank = True,
        help_text = "Protokoll der Wartung.",
        name = 'protocol_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'maintenance_protocol_id',
        to = 'documentationmanagement.Protocol',
        verbose_name = 'Protokoll',
        )
    
    # Fields/Methodes for the repetition of the maintenance
    repetition_days = models.IntegerField(
        blank = True,
        default = 0,
        help_text = "Tage nach dem die Wartung wiederholt werden soll.",
        name = 'repetition_days',
        null = True,
        verbose_name = 'Tage',
    )

    def repetition_formated(self):
        return "{}d {}h {}min {}s".format(str(self.repetition_days),str(self.repetition_hours),str(self.repetition_minutes),str(self.repetition_seconds))

    repetition_hours = models.IntegerField(
        blank = True,
        default = 0,
        help_text = "Stunden nach dem die Wartung wiederholt werden soll.",
        name = 'repetition_hours',
        null = True,
        verbose_name = 'Stunden',
    )

    repetition_minutes = models.IntegerField(
        blank = True,
        default = 0,
        help_text = "Minuten nach dem die Wartung wiederholt werden soll.",
        name = 'repetition_minutes',
        null = True,
        verbose_name = 'Minuten',
    )

    repetition_seconds = models.IntegerField(
        blank = True,
        default = 0,
        help_text = "Sekunden nach dem die Wartung wiederholt werden soll.",
        name = 'repetition_seconds',
        null = True,
        verbose_name = 'Sekunden',
    )

    def status(self):
        if self.alarm():
            result = "alarm"
        elif self.warning_status():
            result = "warning"
        elif self.maintenance_count()>0:
            result = "OK"
        else:
            result = None
        return result

    # Fields/Methodes for the url from the maintenance
    def url_delete(self):
        url = reverse('structuremanagement:maintenance_delete',kwargs={'maintenance':self.slug})
        return url

    def url_detail(self):
        url = reverse('structuremanagement:maintenance_detail',kwargs={'maintenance':self.slug})
        return url

    def url_data_create(self):
        if self.protocol_id:
            result = reverse('documentationmanagement:protocol_protocoldata_create',kwargs={'protocol':self.protocol_id.slug})
        else:
            result = None
        return result

    def url_update(self):
        url = reverse('structuremanagement:maintenance_update',kwargs={'maintenance':self.slug})
        return url

    # Fields/Methodes for the warning of the maintenance
    warning_days = models.IntegerField(
        blank = True,
        default = 0,
        help_text = "Tage nach dem die Wartung als Warnung angezeigt werden soll.",
        name = 'warning_days',
        null = True,
        verbose_name = 'Tage',
    )

    def warning_formated(self):
        return "{}d {}h {}min {}s".format(str(self.warning_days),str(self.warning_hours),str(self.warning_minutes),str(self.warning_seconds))

    warning_hours = models.IntegerField(
        blank = True,
        default = 0,
        help_text = "Stunden nach dem die Wartung als Warnung angezeigt werden soll.",
        name = 'warning_hours',
        null = True,
        verbose_name = 'Stunden',
    )

    warning_minutes = models.IntegerField(
        blank = True,
        default = 0,
        help_text = "Minuten nach dem die Wartung als Warnung angezeigt werden soll.",
        name = 'warning_minutes',
        null = True,
        verbose_name = 'Minuten',
    )

    warning_seconds = models.IntegerField(
        blank = True,
        default = 0,
        help_text = "Sekunden nach dem die Wartung als Warnung angezeigt werden soll.",
        name = 'warning_seconds',
        null = True,
        verbose_name = 'Sekunden',
    )

    def warning_status(self):
        if self.maintenance_next():
            warning_time = self.maintenance_next() - timezone.timedelta(days=self.warning_days,hours=self.warning_hours,minutes=self.warning_minutes,seconds=self.warning_seconds)
            if not self.alarm() and timezone.now()>warning_time:
                result = True
            else:
                result = False
        else:
            result = False
        return result
    
    def __str__(self):
        return str(self.name)

    class Meta:
        app_label = 'structuremanagement'
        ordering = ['device_id','name']
        permissions = (
            ('list_maintenance','Can view List Wartung'),
            ('table_maintenance','Can view Table Wartung'),
            ('detail_maintenance','Can view Detail Wartung')
        )
        verbose_name = "Wartung"
        verbose_name_plural = "Wartungen"
#--------------------------------------------------------------------------------