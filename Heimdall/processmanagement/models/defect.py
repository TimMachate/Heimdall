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
class Defect(CreateData,UpdateData,Slug):
    def rename(self,filename):
        return os.path.join('ProcessManagement/Defect',filename)
    
    name = models.CharField(
        max_length = 200,
        name = 'name',
        verbose_name = 'Defekt',
        blank = False,
        null = False,
    )

    description = models.TextField(
        name = 'description',
        verbose_name = 'Beschreibung',
        blank = True,
        null = True,
    )

    file = models.FileField(
        name = 'file',
        verbose_name = 'Beispiel',
        upload_to = rename,
        blank = True,
        null = True,
    )

    def countToday(self):
        return Data.objects.filter(defect=self.id,createTime__gte=timezone.now().date())

    def countMonth(self):
        time = timezone.now().date()
        result = {}
        for i in range(0,30,1):
            result[time-timezone.timedelta(days=i)] = Data.objects.filter(
                defect=self.id,
                createTime__gte=time-timezone.timedelta(days=i),
                createTime__lte=time-timezone.timedelta(days=i-1),
                ).count()
        return result

    def get_absolute_url(self):
        return reverse('processmanagement:defect_detail',args=[self.id])

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Defekt'
        verbose_name_plural = 'Defekte'
#--------------------------------------------------------------------------------