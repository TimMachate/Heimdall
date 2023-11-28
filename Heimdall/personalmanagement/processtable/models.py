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
class ProcessTable(CreateData,UpdateData):
    user = models.OneToOneField(
        name = "user",
        verbose_name = "Benutzername",
        related_name = "processTableUser",
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

    duration_theoretical_show = models.BooleanField(
        name = 'duration_theoretical_show',
        verbose_name = 'Theoretische Dauer',
        help_text= "Anzeige der theoretischen Dauer in der Tabelle.",
        default = True,
    )

    duration_average_show = models.BooleanField(
        name = 'duration_average_show',
        verbose_name = 'Durschnittliche Dauer',
        help_text= "Anzeige der durchschnittlichen Dauer in der Tabelle.",
        default = True,
    )

    count_total_show = models.BooleanField(
        name = 'count_total_show',
        verbose_name = 'Totale Anzahl',
        help_text= "Anzeige der totalen Anzahl in der Tabelle.",
        default = True,
    )

    count_average_show = models.BooleanField(
        name = 'count_average_show',
        verbose_name = 'Durschnittliche Anzahl',
        help_text= "Anzeige der durchschnittlichen Anzahl in der Tabelle.",
        default = True,
    )

    utilization_show = models.BooleanField(
        name = 'utilization_show',
        verbose_name = 'Auslastung',
        help_text= "Anzeige der Auslastung in der Tabelle.",
        default = True,
    )

    last_process_process_data_show = models.BooleanField(
        name = 'last_process_process_data_show',
        verbose_name = 'Letzter Prozess',
        help_text= "Anzeige des letzten Prozesses in der Tabelle.",
        default = True,
    )

    last_process_process_data_datetime_show = models.BooleanField(
        name = 'last_process_process_data_datetime_show',
        verbose_name = 'Zeitpunkt des letzten Prozess',
        help_text= "Anzeige des Zeitpunktes des letzten Prozesses in der Tabelle.",
        default = False,
    )

    last_process_process_data_datetime_formated_show = models.BooleanField(
        name = 'last_process_process_data_datetime_formated_show',
        verbose_name = 'Formatierter Zeitpunkt des letzten Prozess',
        help_text= "Anzeige des formatierten Zeitpunktes des letzten Prozesses in der Tabelle.",
        default = False,
    )

    last_process_process_data_time_show = models.BooleanField(
        name = 'last_process_process_data_time_show',
        verbose_name = 'Uhrzeit des letzten Prozess',
        help_text= "Anzeige der Uhrzeit des letzten Prozesses in der Tabelle.",
        default = True,
    )

    last_process_process_data_date_show = models.BooleanField(
        name = 'last_process_process_data_date_show',
        verbose_name = 'Datum des letzten Prozess',
        help_text= "Anzeige des Datums des letzten Prozesses in der Tabelle.",
        default = True,
    )

    last_process_process_data_machine_show = models.BooleanField(
        name = 'last_process_process_data_machine_show',
        verbose_name = 'Maschine des letzten Prozess',
        help_text= "Anzeige der Maschine des letzten Prozesses in der Tabelle.",
        default = True,
    )

    create_datetime_show = models.BooleanField(
        name = 'create_datetime_show',
        verbose_name = 'Zeitpunkt der Erstellung',
        help_text= "Anzeige des Zeitpunktes der Erstellung in der Tabelle.",
        default = False,
    )

    create_datetime_formated_show = models.BooleanField(
        name = 'create_datetime_formated_show',
        verbose_name = 'Formatierter Zeitpunkt der Erstellung',
        help_text= "Anzeige des formatierten Zeitpunktes der Erstellung in der Tabelle.",
        default = False,
    )

    create_time_show = models.BooleanField(
        name = 'create_time_show',
        verbose_name = 'Uhrzeit der Erstellung',
        help_text= "Anzeige der Uhrzeit der Erstellung in der Tabelle.",
        default = True,
    )

    create_date_show = models.BooleanField(
        name = 'create_date_show',
        verbose_name = 'Datum der Erstellung',
        help_text= "Anzeige des Datums der Erstellung in der Tabelle.",
        default = True,
    )

    create_username_show = models.BooleanField(
        name = 'create_username_show',
        verbose_name = 'Name des Erstellers',
        help_text= "Anzeige des Namens der Erstellung in der Tabelle.",
        default = True,
    )

    update_datetime_show = models.BooleanField(
        name = 'update_datetime_show',
        verbose_name = 'Zeitpunkt des letzten Updates',
        help_text= "Anzeige des Zeitpunktes des letzten Updates in der Tabelle.",
        default = False,
    )

    update_datetime_formated_show = models.BooleanField(
        name = 'update_datetime_formated_show',
        verbose_name = 'Formatierter Zeitpunkt des letzten Updates',
        help_text= "Anzeige des formatierten Zeitpunktes des letzten Updates in der Tabelle.",
        default = False,
    )

    update_time_show = models.BooleanField(
        name = 'update_time_show',
        verbose_name = 'Uhrzeit des letzten Updates',
        help_text= "Anzeige der Uhrzeit des letzten Updates in der Tabelle.",
        default = True,
    )

    update_date_show = models.BooleanField(
        name = 'update_date_show',
        verbose_name = 'Datum des letzten Updates',
        help_text= "Anzeige des Datums des letzten Updates in der Tabelle.",
        default = True,
    )

    update_username_show = models.BooleanField(
        name = 'update_username_show',
        verbose_name = 'Name des letzten Updates',
        help_text= "Anzeige des Namens des letzten Updates in der Tabelle.",
        default = True,
    )

    def __str__(self):
        return self.user.username

    def field_string(self):
        result = ""
        result += "id," if self.id_show else ""
        result += "referenceNumber," if self.referenceNumber_show else ""
        result += "name," if self.name_show else ""
        result += "duration," if self.duration_theoretical_show or self.duration_average_show else ""
        result += "count," if self.count_total_show or self.count_average_show else ""
        result += "utilization," if self.utilization_show else ""
        result += "lastProcess," if (
            self.last_process_process_data_show or 
            self.last_process_process_data_datetime_show or
            self.last_process_process_data_datetime_formated_show or
            self.last_process_process_data_time_show or
            self.last_process_process_data_date_show or
            self.last_process_process_data_machine_show
            ) else ""
        result += "create," if (
            self.create_username_show or 
            self.create_datetime_show or
            self.create_datetime_formated_show or
            self.create_time_show or
            self.create_date_show
            ) else ""
        result += "update," if (
            self.update_username_show or 
            self.update_datetime_show or
            self.update_datetime_formated_show or
            self.update_time_show or
            self.update_date_show
            ) else ""
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
        verbose_name = "Prozess Tabelle API Url"
        verbose_name_plural = "Prozess Tabelle API Urls"
#--------------------------------------------------------------------------------