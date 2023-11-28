#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib.auth import get_user_model
from django.core import serializers
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
import json
from statistics import mean

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
#from structuremanagement.device.models import Device
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class Process(CreateData,ReferenceNumber,UpdateData,Slug):

    # Variables
    short_name = "STPR"

    # Fields/Methodes for count of the Process
    def count_average(self, de=None, tb=None ,te=None):
        if de:
            l = [i.count for i in self.processdata(device_slug=ma, begin_datetime=tb, end_datetime=te)]
            result = mean(l) if len(l)>0 else 0
        else:
            l = [i.count for i in self.processdata(begin_datetime=tb, end_datetime=te)]
            result = mean(l) if len(l)>0 else 0
        return round(result,2)

    def count_data(self, de=None, tb=None ,te=None):
        result = {"value":[],"time":[]}
        for v in self.processdata(device_slug=de ,begin_datetime=tb,end_datetime=te).order_by('-begin_datetime'):
            result["value"].append(v.count)
            result["time"].append(v.begin_datetime)
        return result

    def count_total(self, de=None, tb=None ,te=None):
        if de:
            result = sum([i.count for i in self.processdata(device_slug=de, begin_datetime=tb, end_datetime=te)])
        else:
            result = sum([i.count for i in self.processdata(begin_datetime=tb, end_datetime=te)])
        return result

    # Fields/Methodes for duration of the Process
    def duration_theoretical(self):
        result = "{} d : {} h : {} min : {} s".format(str(self.duration_days),str(self.duration_hours),str(self.duration_minutes),str(self.duration_seconds))
        return result

    def duration_average(self,de=None,tb=None,te=None):
        time = [i.duration().total_seconds() for i in self.processdata(device_slug=de,begin_datetime=tb,end_datetime=te)]
        if len(time)>0:
            time = timezone.timedelta(seconds=sum(time)/len(time))
            result = "{} d : {:02d} h : {:02d} min : {:02d} s".format(time.days,int(time.seconds/60/60),int((time.seconds/60) - int(time.seconds/60/60)*60),int(time.seconds) - int(time.seconds/60)*60)
        else:
            result  = "0 d : 00 h : 00 min : 00 s"
        return result

    def duration_data(self,de=None,tb=None,te=None):
        result = {"value":[],"time":[]}
        for v in self.processdata(device_slug=de ,begin_datetime=tb,end_datetime=te).order_by('-begin_datetime'):
            result["value"].append(v.duration().total_seconds())
            result["time"].append(v.begin_datetime)
        return result

    duration_days = models.IntegerField(
        name = 'duration_days',
        verbose_name = 'Tage',
        default = 0,
        blank = True,
        null = True,
    )

    duration_hours = models.IntegerField(
        name = 'duration_hours',
        verbose_name = 'Stunden',
        default = 0,
        blank = True,
        null = True,
    )

    duration_minutes = models.IntegerField(
        name = 'duration_minutes',
        verbose_name = 'Minuten',
        default = 0,
        blank = True,
        null = True,
    )

    duration_seconds = models.IntegerField(
        name = 'duration_seconds',
        verbose_name = 'Sekunden',
        default = 0,
        blank = True,
        null = True,
    )

    # Fields/Methodes for devices of the Process
    #def devices(self,tb=None,te=None):
    #    result = Device.objects.filter(id__in=self.processdata(begin_datetime=tb ,end_datetime=te).values('device_id'))
    #    return result

    #def devices_distribution(self,de=None, tb=None, te=None):
    #    return round(self.count_total(de=de, tb=tb, te=te)/self.count_total(tb=tb, te=te)*100,2)

    # Fields/Methodes for name of the Process
    name = models.CharField(
        max_length = 200,
        name = "name",
        verbose_name = "Name",
        blank = True,
        null = True,
        )

    # Fields/Methodes for picture of the Process
    picture_id =  models.ForeignKey(
        name = 'picture_id',
        verbose_name = 'Bild',
        related_name = 'process_picture_id',
        to = 'documentationmanagement.PictureProxy',
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    # Fields/Methodes for processdata of the Process
    def processdata(self, device_slug = None, begin_datetime=None ,end_datetime=None):
        tb = timezone.datetime.strptime(begin_datetime,"%Y-%m-%d %H:%S") if begin_datetime else timezone.datetime(2000,1,1)
        te = timezone.datetime.strptime(end_datetime,"%Y-%m-%d %H:%S") if end_datetime else timezone.now()
        if device_slug:
            result = ProcessData.objects.filter(device_id__slug = device_slug, process_id = self.id, begin_datetime__gte=tb, end_datetime__lte=te)
        else:
            result = ProcessData.objects.filter(process_id = self.id, begin_datetime__gte=tb, end_datetime__lte=te)
        return result.order_by('-begin_datetime')

    def processdata_count(self,de=None, tb=None, te=None):
        return self.processdata(device_slug=de, begin_datetime=tb, end_datetime=te).count()

    def processdata_last(self,de=None, tb=None, te=None):
        result = self.processdata(device_slug=de, begin_datetime=tb, end_datetime=te).filter(process_id = self.id,end_datetime__lte=timezone.now())
        result = result.order_by('begin_datetime').first() if result else None
        return result

    def processdata_next(self):
        result = ProcessData.objects.filter(process_id = self.id,end_datetime=None)
        result = result.exclude(begin_datetime__lte = timezone.now())
        result = result.order_by('begin_datetime').first() if result else None
        return result

    def processdata_running(self):
        result = ProcessData.objects.filter(process_id = self.id,begin_datetime__lte=timezone.now(),end_datetime=None)
        result = result.order_by('begin_datetime').first() if result else None
        return result

    def processdata_status(self):
        if self.processdata_running():
            result = "running"
        elif self.processdata_next():
            result = "open"
        elif self.processdata_last():
            result = "closed"
        else:
            result = None
        return result

    # Fields/Methodes for technical data sheet of the Process
    technical_data_sheet_id = models.ForeignKey(
        name = 'technical_data_sheet_id',
        verbose_name = 'Technisches Datenblatt',
        related_name = 'process_technical_data_sheet_id',
        to = 'documentationmanagement.TechnicalDataSheetProxy',
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    # Fields/Methodes for urls of the Process
    def url_delete(self):
        return reverse('structuremanagement:process_delete',kwargs={'process':self.slug})

    def url_detail(self):
        return reverse('structuremanagement:process_detail',kwargs={'process':self.slug})

    def url_data_create(self):
        return reverse('structuremanagement:process_processdata_create',kwargs={'process':self.slug})
    
    def url_data_list(self):
        return reverse('structuremanagement:process_processdata_list',kwargs={'process':self.slug})

    def url_data_overview(self):
        return reverse('structuremanagement:process_processdata_overview',kwargs={'process':self.slug})

    def url_data_table(self):
        return reverse('structuremanagement:process_processdata_table',kwargs={'process':self.slug})

    def url_update(self):
        return reverse('structuremanagement:process_update',kwargs={'process':self.slug})

    # Fields/Methodes for utilization of the Process
    def utilization_average(self, de=None, tb=None ,te=None):
        l = [i.utilization_percentage() for i in self.processdata(device_slug=de, begin_datetime=tb, end_datetime=te)]
        result = mean(l) if len(l)>0 else 0
        return round(result,2)
    
    def utilization_data(self, de=None, tb=None ,te=None):
        result = {"value":[],"time":[]}
        for v in self.processdata(device_slug=de ,begin_datetime=tb,end_datetime=te).order_by('-begin_datetime'):
            result["value"].append(v.utilization_percentage())
            result["time"].append(v.begin_datetime)
        return result

    def __str__(self):
        return "{} ({})".format(str(self.name),str(self.reference_number))

    class Meta:
        app_label = 'structuremanagement'
        ordering = ['name']
        permissions = (
            ('list_process','Can view List Prozess'),
            ('table_process','Can view Table Prozess'),
            ('detail_process','Can view Detail Prozess')
        )
        verbose_name = "Prozess"
        verbose_name_plural = "Prozesse"
#--------------------------------------------------------------------------------
class ProcessData(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STPRDA"

    # fields/methodes for the begin of the process
    begin_datetime = models.DateTimeField(
        name = 'begin_datetime',
        verbose_name = 'Zeitpunkt des Begins',
        default = None,
        editable = True,
        help_text = "Zeitpunkt bei dem der Prozess gestartet wird.",
        blank = True,
        null = True,
    )

    begin_user_id = models.ForeignKey(
        name = 'begin_user_id',
        verbose_name = 'Person Zeitpunkt des Begins',
        related_name = 'processdata_begin_user_id',
        help_text = "Person die den Prozess gestartet wird.",
        to = get_user_model(),
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    # fields/methodes for the count in the process
    count = models.IntegerField(
        default = 0,
        name = "count",
        verbose_name = "Anzahl",
        help_text = "Anzahl der Aufträge die dem Prozess unterliegen.",
        blank = True,
        null = True,
    )

    # Fields/Methodes for the device in the process
    device_id = models.ForeignKey(
        name = 'device_id',
        verbose_name = 'Gerät',
        related_name = 'processdata_device_id',
        to = 'structuremanagement.Device', 
        on_delete = models.CASCADE,
        help_text = "Maschine in der der Prozess abläuft.",
        blank = True,
        null = True,
    )

    # fields/methodes for the duration of the process
    def duration(self):
        if self.begin_datetime and self.end_datetime:
            result = self.end_datetime-self.begin_datetime
        elif self.begin_datetime and self.end_theoretical_datetime():
            result = self.end_theoretical_datetime()-self.begin_datetime
        else:
            result = None
        return result
    
    def duration_formated(self):
        if self.duration():
            time = self.duration()
            result = "{} Tage, {:02d}:{:02d}:{:02d}".format(time.days,int(time.seconds/60/60),int((time.seconds/60) - int(time.seconds/60/60)*60),int(time.seconds) - int(time.seconds/60)*60)
        else:
            result = None
        return result

    # fields/methodes for the end of the process

    end_datetime = models.DateTimeField(
        name = 'end_datetime',
        verbose_name = 'Zeitpunkt des Endes',
        default = None,
        editable = True,
        help_text = "Zeitpunkt bei dem der Prozess beendet ist.",
        blank = True,
        null = True,
    )

    def end_theoretical_datetime(self):
        if self.begin_datetime and self.process_id:
            result = self.begin_datetime+timezone.timedelta(days=self.process_id.duration_days,hours=self.process_id.duration_hours,minutes=self.process_id.duration_minutes,seconds=self.process_id.duration_seconds)
        else:
            result = None
        return result

    end_user_id = models.ForeignKey(
        name = 'end_user_id',
        verbose_name = 'Person Zeitpunkt des Endes',
        related_name = 'processdata_end_user_id',
        help_text = "Person die den Prozess beendet hat.",
        to = get_user_model(),
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    # Fields/Methodes for the notice in the process
    notice = tinymce_models.HTMLField(
        blank = True,
        help_text = "Bemerkungen zum Prozess",
        name = 'notice',
        null = True,
        verbose_name = 'Bemerkung',
    )

    # Fields/Methodes for the process in the process
    process_id = models.ForeignKey(
        name = 'process_id',
        verbose_name = 'Prozess',
        related_name = 'processdata_process_id',
        to = 'structuremanagement.Process', 
        on_delete = models.CASCADE,
        help_text = "Der eingestellte Prozess in der Maschine wird hier eingestellt.",
        blank = True,
        null = True,
    )

    # Fields/Methodes for the protocol in the process
    protocol_id = models.ForeignKey(
        name = 'protocol_id',
        verbose_name = 'Protokoll',
        related_name = 'processdata_protocol_id',
        to = 'documentationmanagement.ProtocolData',
        on_delete = models.CASCADE,
        help_text = "Protokol in dem das Ergenis festgehalten wird.",
        blank = True,
        null = True,
        )

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    # Fields/Methodes for the urls of the process
    def url_delete(self):
        return reverse('structuremanagement:processdata_delete',kwargs={'processdata':self.slug})

    def url_detail(self):
        return reverse('structuremanagement:processdata_detail',kwargs={'processdata':self.slug})

    def url_update(self):
        return reverse('structuremanagement:processdata_update',kwargs={'processdata':self.slug})

    # Fields/Methodes for the utilization in the process
    def utilization(self):
        if self.device_id and self.count:
            return round(self.count / self.device_id.count,4) if self.device_id.count else None
        else:
            return None

    def utilization_percentage(self):
        return round(self.utilization() * 100,4) if self.utilization() else None
    
    def utilization_percentage_formated(self):
        return "{:5}%".format(str(self.utilization_percentage()).replace('.', ',')) if self.utilization() else None

    # methode for the return string of the process    
    def __str__(self):
        return "{}-{}-{}".format(str(self.reference_number),str(self.device_id.name),str(self.process_id.name))
    
    # define meta data
    class Meta:
        app_label = 'structuremanagement'
        ordering = ['-begin_datetime']
        permissions = (
            ('list_processdata','Can view List Prozess Daten'),
            ('list_setting_processdata','Can view the setting of the list'),
            ('table_processdata','Can view Table Prozess Daten'),
            ('detail_processdata','Can view Detail Prozess Daten')
        )
        verbose_name = "Prozess Daten"
        verbose_name_plural = "Prozesse Daten"
#--------------------------------------------------------------------------------