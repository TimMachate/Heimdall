#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.text import slugify

import os
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class Program(models.Model):
    def rename(self,filename):
        return os.path.join('Program/{}'.format(slugify(self.name)),filename)
    
    name = models.CharField(
        name = 'name',
        verbose_name = 'Name',
        max_length = 200,
        blank = False,
        null = False,
    )

    createUser = models.ForeignKey(
        name = 'createUser',
        verbose_name = 'Ersteller',
        related_name = "{}_createUser".format("%(app_label)s_%(class)ss"),
        related_query_name="%(app_label)s_%(class)ss",
        to = get_user_model(),
        on_delete = models.PROTECT,
        default = None,
        editable = False,
        blank = False,
        null = True,
    )

    createTime = models.DateTimeField(
        name = 'createTime',
        verbose_name = 'Zeitpunkt der Erstellung',
        default = timezone.now,
        editable = False,
        blank = False,
        null = False,
    )

    updateUser = models.ForeignKey(
        name = 'updateUser',
        verbose_name = 'Updater',
        related_name = "%(app_label)s_%(class)s_updateUser",
        related_query_name="%(app_label)s_%(class)ss",
        to = get_user_model(),
        on_delete = models.PROTECT,
        default = None,
        editable = False,
        blank = False,
        null = True,
    )

    updateTime = models.DateTimeField(
        name = 'updateTime',
        verbose_name = 'Zeitpunkt des Updates',
        default = timezone.now,
        editable = False,
        blank = False,
        null = False,
    )

    htmlfile = models.FileField(
        name = 'htmlfile',
        verbose_name = 'HTML Datei',
        upload_to = rename,
        blank = True,
        null = True,
    )

    json = models.JSONField(
        name = 'json',
        verbose_name = 'Daten',
        blank = True,
        null = True,
    )

    def get_absolute_url(self):
        return reverse('programs:program_detail',args=[self.id])

    def htmlFileName(self):
        return os.path.basename(self.htmlfile.name)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not os.path.exists(os.path.join(os.path.dirname(self.htmlfile.path),"script.py")):
            old = os.path.join(os.path.dirname(os.path.dirname(self.htmlfile.path)),"script.py")
            new = os.path.join(os.path.dirname(self.htmlfile.path),"script.py")
            os.system("copy {} {}".format(old,new))

    class Meta:
        permissions = (
            ('list_programs','Can view List Unternehmen'),
            ('table_programs','Can view Table Unternehmen'),
            ('detail_programs','Can view Detail Unternehmen')
        )
        verbose_name = 'Programm'
        verbose_name_plural = 'Programme'
#--------------------------------------------------------------------------------