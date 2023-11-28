#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models
from django.urls import reverse
from django.utils import timezone
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from main.createdata.models import CreateData
from main.referencenumber.models import ReferenceNumber
from main.slug.models import Slug
from main.updatedata.models import UpdateData
from structuremanagement.error.models import ErrorData
from structuremanagement.maintenance.models import Maintenance
from structuremanagement.process.models import ProcessData
from structuremanagement.status.models import StatusData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class Device(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STDE"

    # Fields/Methodes for the count of the device
    count = models.IntegerField(
        blank = True,
        name = 'count',
        null = True,
        verbose_name= 'Stückzahl',
    )

    # Fields/Methodes for the documents of the device
    documents = models.ManyToManyField(
        blank = True,
        name = 'documents',
        related_name = 'device_documents',
        to = 'documentationmanagement.DocumentProxy',
        verbose_name = 'Dokumente',
    )

    def documents_count(self):
        return self.documents.all().count()

    # Fields/Methodes for the errors of the device
    errors = models.ManyToManyField(
        blank = True,
        name = 'errors',
        related_name = 'device_errors',
        to = 'structuremanagement.Error',
        verbose_name = 'Fehler',
    )

    def errors_count(self):
        return self.errors.all().count()

    # Fields/Methodes for the errordata of the device
    def errordata(self, error_slug = None, begin_datetime=None ,end_datetime=None):
        tb = timezone.datetime.strptime(begin_datetime,"%Y-%m-%d %H:%S") if begin_datetime else timezone.datetime(2000,1,1)
        te = timezone.datetime.strptime(end_datetime,"%Y-%m-%d %H:%S") if end_datetime else timezone.now()
        if error_slug:
            result = ErrorData.objects.filter(error_id__slug = error_slug, device_id = self.id, create_datetime__gte=tb, create_datetime__lte=te)
        else:
            result = ErrorData.objects.filter(device_id = self.id, create_datetime__gte=tb, create_datetime__lte=te)
        return result.order_by('-create_datetime')

    def errordata_count(self,er=None, tb=None, te=None):
        return self.errordata(error_slug = er, begin_datetime = tb, end_datetime = te).count()

    def errordata_last(self,er=None, tb=None, te=None):
        if self.errordata_count(er=er, tb=tb, te=te) > 0:
            result = self.errordata(error_slug = er, begin_datetime = tb, end_datetime = te).order_by('-create_datetime')[0]
        else:
            result = None
        return result

    # Fields/Methodes for the fabricator of the device
    fabricator_id = models.ForeignKey(
        blank = True,
        name = 'fabricator_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = "device_fabricator_id",
        to = 'relationshipmanagement.company',
        verbose_name = 'Hersteller',
    )

    # Fields/Methodes for the fabricator label of the device
    fabricator_label = models.CharField(
        blank = True,
        max_length = 200,
        name = 'fabricator_label',
        null = True,
        verbose_name = 'Herstellerbezeichnung',
    )

    # Fields/Methodes for the maintenance of the device
    def maintenances(self):
        return Maintenance.objects.filter(device_id=self.id).order_by('-create_datetime')

    def maintenances_count(self):
        return self.maintenances().count()

    def maintenances_open(self):
        queryset=self.maintenances()
        result = 0
        for maintenance in queryset:
            if maintenance.maintenance_next():
                if maintenance.maintenance_next() < timezone.now():
                    result = result + 1
            else:
                result = result + 1
        return result

    # Fields/Methodes for the manuals of the device
    manuals = models.ManyToManyField(
        blank = True,
        name = 'manuals',
        related_name = 'device_manuals',
        to = 'documentationmanagement.ManualProxy',
        verbose_name = 'Handbücher',
    )

    def manuals_count(self):
        return self.manuals.all().count()

    # Fields/Methodes for the name of the device
    name = models.CharField(
        blank = False,
        help_text = "Name des Gerätes.",
        max_length = 200,
        name = 'name',
        null = False,
        verbose_name = 'Gerät',
    )

    # Fields/Methodes for the picture of the device
    picture_id = models.ForeignKey(
        blank=True,
        name = "picture_id",
        null=True,
        on_delete= models.PROTECT,
        related_name= "device_picture_id" ,
        to = "documentationmanagement.PictureProxy",
        verbose_name = "Bild",
    )

    # Fields/Methodes for the power of the device
    power = models.IntegerField(
        blank = True,
        name = 'power',
        null = True,
        verbose_name= 'Leistung',
    )

    # Fields/Methodes for the processes of the device
    processes = models.ManyToManyField(
        blank = True,
        name = 'processes',
        related_name = 'device_processes',
        to = 'structuremanagement.Process',
        verbose_name = 'Prozesse',
    )

    def processes_count(self):
        return self.processes.all().count()

    # Fields/Methodes for processdata of the Process
    def processdata(self, process_slug = None, begin_datetime=None ,end_datetime=None):
        tb = timezone.datetime.strptime(begin_datetime,"%Y-%m-%d %H:%S") if begin_datetime else timezone.datetime(2000,1,1)
        te = timezone.datetime.strptime(end_datetime,"%Y-%m-%d %H:%S") if end_datetime else timezone.now()
        if process_slug:
            result = ProcessData.objects.filter(process_id__slug = process_slug, device_id = self.id, begin_datetime__gte=tb, end_datetime__lte=te)
        else:
            result = ProcessData.objects.filter(device_id = self.id, begin_datetime__gte=tb, end_datetime__lte=te)
        return result.order_by('-begin_datetime')

    def processdata_count(self,pr=None, tb=None, te=None):
        return self.processdata(process_slug=pr, begin_datetime=tb, end_datetime=te).count()

    def processdata_last(self,pr=None, tb=None, te=None):
        result = self.processdata(process_slug=pr, begin_datetime=tb, end_datetime=te).filter(device_id=self.id,end_datetime__lte=timezone.now())
        result = result.order_by('begin_datetime').last() if result else None
        return result

    def processdata_next(self):
        result = ProcessData.objects.filter(device_id=self.id,end_datetime=None)
        result = result.exclude(begin_datetime__lte = timezone.now())
        result = result.order_by('begin_datetime').first() if result else None
        return result

    def processdata_running(self):
        result = ProcessData.objects.filter(device_id=self.id,begin_datetime__lte=timezone.now(),end_datetime=None)
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

    # Fields/Methodes for the serial number of the device
    serial_number = models.CharField(
        blank = True,
        max_length = 200,
        name = 'serial_number',
        null = True,
        verbose_name = 'Seriennummer',
    )

    # Fields/Methodes for the status of the device
    status = models.ManyToManyField(
        blank = True,
        name = 'status',
        related_name = 'device_status',
        to = 'structuremanagement.Status',
        verbose_name = 'Status',
    )

    def status_count(self):
        return self.status.all().count()

    # Fields/Methodes for the statusdata of the device
    def statusdata(self, status_slug = None, begin_datetime = None, end_datetime = None):
        tb = timezone.datetime.strptime(begin_datetime,"%Y-%m-%d %H:%S") if begin_datetime else timezone.datetime(2000,1,1)
        te = timezone.datetime.strptime(end_datetime,"%Y-%m-%d %H:%S") if end_datetime else timezone.now()
        if status_slug:
            result = StatusData.objects.filter(status_id__slug = status_slug, device_id = self.id, create_datetime__gte=tb, create_datetime__lte=te)
        else:
            result = StatusData.objects.filter(device_id = self.id, create_datetime__gte=tb, create_datetime__lte=te)
        return result.order_by('-create_datetime')

    def statusdata_count(self,st=None, tb=None, te=None):
        return self.statusdata(status_slug = st, begin_datetime = tb, end_datetime = te).count()

    def statusdata_last(self,st=None, tb=None, te=None):
        if self.statusdata_count() > 0:
            result = self.statusdata(status_slug = st, begin_datetime = tb, end_datetime = te).order_by('-create_datetime')[0]
        else:
            result = None
        return result
    
    # Fields/Methodes for the url of the device
    def url_delete(self):
        return reverse('structuremanagement:device_delete',kwargs={'device':self.slug})

    def url_detail(self):
        return reverse('structuremanagement:device_detail',kwargs={'device':self.slug})
    
    def url_errordata_create(self):
        return reverse('structuremanagement:device_errordata_create',kwargs={'device':self.slug})
    
    def url_errordata_overview(self):
        return reverse('structuremanagement:device_errordata_overview',kwargs={'device':self.slug})

    def url_errordata_list(self):
        return reverse('structuremanagement:device_errordata_list',kwargs={'device':self.slug})
    
    def url_errordata_table(self):
        return reverse('structuremanagement:device_errordata_table',kwargs={'device':self.slug})

    def url_maintenancedata_create(self):
        return reverse('structuremanagement:device_maintenancedata_create',kwargs={'device':self.slug})
    
    def url_maintenancedata_overview(self):
        return reverse('structuremanagement:device_maintenancedata_overview',kwargs={'device':self.slug})

    def url_maintenancedata_list(self):
        return reverse('structuremanagement:device_maintenancedata_list',kwargs={'device':self.slug})
    
    def url_maintenancedata_table(self):
        return reverse('structuremanagement:device_maintenancedata_table',kwargs={'device':self.slug})

    def url_processdata_create(self):
        return reverse('structuremanagement:device_processdata_create',kwargs={'device':self.slug})

    def url_processdata_overview(self):
        return reverse('structuremanagement:device_processdata_overview',kwargs={'device':self.slug})
    
    def url_processdata_list(self):
        return reverse('structuremanagement:device_processdata_list',kwargs={'device':self.slug})

    def url_processdata_table(self):
        return reverse('structuremanagement:device_processdata_table',kwargs={'device':self.slug})

    def url_statusdata_create(self):
        return reverse('structuremanagement:device_statusdata_create',kwargs={'device':self.slug})
    
    def url_statusdata_overview(self):
        return reverse('structuremanagement:device_statusdata_overview',kwargs={'device':self.slug})

    def url_statusdata_list(self):
        return reverse('structuremanagement:device_statusdata_list',kwargs={'device':self.slug})
    
    def url_statusdata_table(self):
        return reverse('structuremanagement:device_statusdata_table',kwargs={'device':self.slug})

    def url_update(self):
        return reverse('structuremanagement:device_update',kwargs={'device':self.slug})

    # Fields/Methodes for the voltage of the device
    voltage = models.IntegerField(
        blank = True,
        name = 'voltage',
        null = True,
        verbose_name= 'Spannung',
    )

    # Fields/Methodes for the working_instructions of the device
    working_instructions = models.ManyToManyField(
        blank = True,
        name = 'working_instructions',
        related_name = 'device_working_instructions',
        to = 'documentationmanagement.WorkingInstructionProxy',
        verbose_name = 'Arbeitsanweisungen',
    )

    def working_instructions_count(self):
        return self.working_instructions.all().count()

    # Fields/Methodes for the year of manufacture of the device
    year_of_manufacture = models.DateField(
        blank = True,
        name = 'year_of_manufacture',
        null = True,
        verbose_name= 'Herstellungsjahr',
    )
    
    def __str__(self):
        return "{} ({})".format(str(self.name),str(self.reference_number))

    class Meta:
        app_label = 'structuremanagement'
        ordering = ['name']
        permissions = (
            ('list_device','Can view List Gerät'),
            ('table_device','Can view Table Gerät'),
            ('detail_device','Can view Detail Gerät')
        )
        verbose_name = "Gerät"
        verbose_name_plural = "Geräte"
#--------------------------------------------------------------------------------