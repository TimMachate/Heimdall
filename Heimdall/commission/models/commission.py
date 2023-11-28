#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models
from django.urls import reverse
from django.utils import timezone
import random
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from .abstract import CreateData,UpdateData,Slug
from processmanagement.models.data import Data
from processmanagement.models.statusreport import StatusReport
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class Commission(CreateData,UpdateData,Slug):
    name = models.CharField(
        max_length = 200,
        name = 'name',
        verbose_name = 'Auftrag',
        blank = False,
        null = False,
    )

    sos = models.BooleanField(
        name = 'sos',
        verbose_name = 'SOS',
        default = False,
    )

    ticket = models.BooleanField(
        name = 'ticket',
        verbose_name = 'Ticket',
        default = False,
    )

    done = models.BooleanField(
        name = 'done',
        verbose_name = 'Erledigt',
        default = False,
    )

    def getAge(self):
        obj = Data.objects.filter(commission=self.id).first()
        if obj:
            entry_date = obj.createTime
            now = timezone.now()
            age = now - entry_date
            result = age.days + 1
        else:
            result = None
        return result

    def get_absolute_url(self):
        return reverse('commission:commission_detail',args=[self.id])

    def getFirstStatusReport(self):
        return Data.objects.filter(commission=self.id).earliest('createTime')

    def getLastStatusReport(self):
        return Data.objects.filter(commission=self.id).latest('createTime')
    
    def getStatusReport(self):
        return Data.objects.filter(commission=self.id).order_by('createTime')

    def getProcress(self):
        return random.randint(0,100)
    
    def getRemake(self):
        start_run_through = StatusReport.objects.get(startRunThrough=True)
        if start_run_through:
            data = Data.objects.filter(commission=self.id, statusreport=start_run_through.id)
            result = data.count()
        else:
            result = '-'
        return result

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Auftrag'
        verbose_name_plural = 'Auftraege'
        ordering=['-id']
#--------------------------------------------------------------------------------