#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models
from django.urls import reverse
from django.utils import timezone

import os
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from .abstract import CreateData,UpdateData,Slug
from .data import Data
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class StatusReport(CreateData,UpdateData,Slug):
    name = models.CharField(
        max_length = 200,
        name = 'name',
        verbose_name = 'Statusmeldung',
        blank = False,
        null = False,
    )

    defects = models.ManyToManyField(
        name = "defects",
        verbose_name = 'Defekte',
        to = 'processmanagement.Defect',
        blank = True,
    )

    start_run_through = models.BooleanField(
        name = "startRunThrough",
        default = False,
        blank = False,
        null = False,
    )

    def countToday(self):
        return Data.objects.filter(defect=self.id,createTime__gte=timezone.now().date())

    def countMonth(self):
        time = timezone.now().date()
        result = {}
        for i in range(0,30,1):
            result[time-timezone.timedelta(days=i)] = Data.objects.filter(
                statusreport=self.id,
                createTime__gte=time-timezone.timedelta(days=i),
                createTime__lte=time-timezone.timedelta(days=i-1),
                ).count()
        return result

    def get_absolute_url(self):
        return reverse('processmanagement:statusreport_detail',args=[self.id])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.startRunThrough == True:
            for obj in StatusReport.objects.exclude(id=self.id):
                obj.startRunThrough = False
                obj.save()
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Statusmeldung'
        verbose_name_plural = 'Statusmeldungen'
#--------------------------------------------------------------------------------