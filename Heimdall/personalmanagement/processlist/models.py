#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from main.absolute.createdata import CreateData
from main.absolute.updatedata import UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class ProcessList(CreateData,UpdateData):
    user = models.OneToOneField(
        name = "user",
        verbose_name = "Benutzername",
        related_name = "processListUser",
        to = get_user_model(),
        on_delete = models.CASCADE,
        blank = False,
        null = False,
        )

    begin = models.DateTimeField(
        name = 'begin',
        verbose_name = 'Begin',
        help_text= "Zeitpunkt des Beginns der Datenabfrage.",
        default = None,
        blank = True,
        null = True,
    )

    end = models.DateTimeField(
        name = 'end',
        verbose_name = 'Ende',
        help_text= "Zeitpunkt des Endes der Datenabfrage.",
        default = None,
        blank = True,
        null = True,
    )

    day = models.PositiveIntegerField(
        name = 'day',
        verbose_name = 'Tage',
        help_text= "Die letzten Tage der Datenabfrage.",
        default = None,
        blank = True,
        null = True,
    )

    url = models.CharField(
        max_length = 200,
        name = 'url',
        verbose_name = 'URL',
        help_text= "Basis-Url der API Schnittstelle für die Datenabfrage.",
        default = "structuremanagementAPI:process_list",
        blank = True,
        null = True,
    )

    id_show = models.BooleanField(
        name = 'id_show',
        verbose_name = 'ID',
        help_text= "Anzeige der ID in der Tabelle.",
        default = False,
    )

    referenceNumber_show = models.BooleanField(
        name = 'referenceNumber_show',
        verbose_name = 'Referenznummer',
        help_text= "Anzeige der Referenznummer in der Tabelle.",
        default = True,
    )

    name_show = models.BooleanField(
        name = 'name_show',
        verbose_name = 'Name',
        help_text= "Anzeige des Namens in der Tabelle.",
        default = True,
    )

    theoretical_show = models.BooleanField(
        name = 'theoretical_show',
        verbose_name = 'Theoretische Dauer',
        help_text= "Anzeige der theoretischen Dauer in der Tabelle.",
        default = True,
    )

    days_show = models.BooleanField(
        name = 'days_show',
        verbose_name = 'Tage',
        help_text= "Anzeige der Dauer der Tage in der Tabelle.",
        default = False,
    )

    hours_show = models.BooleanField(
        name = 'hours_show',
        verbose_name = 'Stunden',
        help_text= "Anzeige der Dauer der Stunden in der Tabelle.",
        default = False,
    )

    minutes_show = models.BooleanField(
        name = 'minutes_show',
        verbose_name = 'Minuten',
        help_text= "Anzeige der Dauer der Minuten in der Tabelle.",
        default = False,
    )

    seconds_show = models.BooleanField(
        name = 'seconds_show',
        verbose_name = 'Sekunden',
        help_text= "Anzeige der Dauer der Sekunden in der Tabelle.",
        default = False,
    )

    picture_show = models.BooleanField(
        name = 'picture_show',
        verbose_name = 'Bild',
        help_text= "Anzeige des Links vom Bild in der Tabelle.",
        default = True,
    )

    technicalDataSheet_show = models.BooleanField(
        name = 'technicalDataSheet_show',
        verbose_name = 'TDS',
        help_text= "Anzeige des Links vom technischen Datenblatts in der Tabelle.",
        default = True,
    )

    update_show = models.BooleanField(
        name = 'update_show',
        verbose_name = 'Update',
        help_text= "Anzeige des Links zum Bearbeiten des Prozesses in der Tabelle.",
        default = True,
    )

    delete_show = models.BooleanField(
        name = 'delete_show',
        verbose_name = 'Löschen',
        help_text= "Anzeige des Links zum Löschen des Prozesses in der Tabelle.",
        default = True,
    )

    add_data_show = models.BooleanField(
        name = 'add_data_show',
        verbose_name = 'Hinzufügen',
        help_text= "Anzeige des Links zum Hinzufügen eines neuen Prozesses in der Tabelle.",
        default = True,
    )

    def __str__(self):
        return self.user.username

    def field_string(self):
        result = ""
        result += "id," if self.id_show else ""
        result += "referenceNumber," if self.referenceNumber_show else ""
        result += "name," if self.name_show else ""
        result += "duration," if (
            self.theoretical_show or
            self.days_show or
            self.hours_show or
            self.minutes_show or
            self.seconds_show
            ) else ""
        result += "technicalDataSheet," if self.technicalDataSheet_show else ""
        result += "picture," if self.picture_show else ""
        result += "url_update," if self.update_show else ""
        result += "url_add_data," if self.add_data_show else ""
        result += "url_delete," if self.delete_show else ""
        return result
        
    #def url_delete(self):
    #    return reverse('personalmanagement:employee_delete',kwargs={'employee':self.id})

    #def url_detail(self):
    #    return reverse('personalmanagement:employee_detail',kwargs={'employee':self.id})
    
    #def url_update(self):
    #    return reverse('personalmanagement:employee_update',kwargs={'employee':self.id})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'personalmanagement'
        ordering = []
        permissions = ()
        verbose_name = "Prozess List API Url"
        verbose_name_plural = "Prozess List API Urls"
#--------------------------------------------------------------------------------