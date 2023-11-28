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
class ProcessDataTable(CreateData,UpdateData):
    user = models.OneToOneField(
        name = "user",
        verbose_name = "Benutzername",
        related_name = "processDataTableUser",
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
        default = "structuremanagementAPI:processdata_list",
        blank = True,
        null = True,
    )

    id_show = models.BooleanField(
        name = 'id_show',
        verbose_name = 'ID',
        help_text= "Anzeige der ID in der Tabelle.",
        default = False,
    )

    url_detail_show = models.BooleanField(
        name = 'url_detail_show',
        verbose_name = 'Detail',
        help_text= "Anzeige des Links zum Detail des Prozesses in der Tabelle.",
        default = False,
    )

    url_update_show = models.BooleanField(
        name = 'url_update_show',
        verbose_name = 'Update',
        help_text= "Anzeige des Links zum Bearbeiten des Prozesses in der Tabelle.",
        default = False,
    )

    referenceNumber_show = models.BooleanField(
        name = 'reference_number_show',
        verbose_name = 'Referenznummer',
        help_text= "Anzeige der Referenznummer in der Tabelle.",
        default = True,
    )

    slug_show = models.BooleanField(
        name = 'slug_show',
        verbose_name = 'Slug',
        help_text= "Anzeige des Slugs in der Tabelle.",
        default = False,
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
        default = False,
    )

    create_date_show = models.BooleanField(
        name = 'create_date_show',
        verbose_name = 'Datum der Erstellung',
        help_text= "Anzeige des Datums der Erstellung in der Tabelle.",
        default = False,
    )

    create_username_show = models.BooleanField(
        name = 'create_username_show',
        verbose_name = 'Name des Erstellers',
        help_text= "Anzeige des Namens der Erstellung in der Tabelle.",
        default = False,
    )

    begin_datetime_show = models.BooleanField(
        name = 'begin_datetime_show',
        verbose_name = 'Zeitpunkt des Begins',
        help_text= "Anzeige des Zeitpunktes des Begins in der Tabelle.",
        default = False,
    )

    begin_datetime_formated_show = models.BooleanField(
        name = 'begin_datetime_formated_show',
        verbose_name = 'Formatierter Zeitpunkt des Begins',
        help_text= "Anzeige des formatierten Zeitpunktes des Begins in der Tabelle.",
        default = False,
    )

    begin_time_show = models.BooleanField(
        name = 'begin_time_show',
        verbose_name = 'Uhrzeit des Begins',
        help_text= "Anzeige der Uhrzeit des Begins in der Tabelle.",
        default = True,
    )

    begin_date_show = models.BooleanField(
        name = 'begin_date_show',
        verbose_name = 'Datum des Begins',
        help_text= "Anzeige des Datums des Begins in der Tabelle.",
        default = True,
    )

    begin_username_show = models.BooleanField(
        name = 'begin_username_show',
        verbose_name = 'Person des Begins',
        help_text= "Anzeige der Person des Begins in der Tabelle.",
        default = True,
    )

    duration_show = models.BooleanField(
        name = 'duration_show',
        verbose_name = 'Dauer in Sekunden',
        help_text= "Anzeige der Dauer in Sekunden in der Tabelle.",
        default = False,
    )

    duration_formated_show = models.BooleanField(
        name = 'duration_formated_show',
        verbose_name = 'Formatierte Dauer',
        help_text= "Anzeige der formatierte Dauer in der Tabelle.",
        default = True,
    )

    end_datetime_show = models.BooleanField(
        name = 'end_datetime_show',
        verbose_name = 'Zeitpunkt des Endes',
        help_text= "Anzeige des Zeitpunktes des Endes in der Tabelle.",
        default = False,
    )

    end_datetime_formated_show = models.BooleanField(
        name = 'end_datetime_formated_show',
        verbose_name = 'Formatierter Zeitpunkt des Endes',
        help_text= "Anzeige des formatierten Zeitpunktes des Endes in der Tabelle.",
        default = False,
    )

    end_time_show = models.BooleanField(
        name = 'end_time_show',
        verbose_name = 'Uhrzeit des Endes',
        help_text= "Anzeige der Uhrzeit des Endes in der Tabelle.",
        default = True,
    )

    end_date_show = models.BooleanField(
        name = 'end_date_show',
        verbose_name = 'Datum des Endes',
        help_text= "Anzeige des Datums des Endes in der Tabelle.",
        default = True,
    )

    end_username_show = models.BooleanField(
        name = 'end_username_show',
        verbose_name = 'Person des Endes',
        help_text= "Anzeige der Person des Endes in der Tabelle.",
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
        default = False,
    )

    update_date_show = models.BooleanField(
        name = 'update_date_show',
        verbose_name = 'Datum des letzten Updates',
        help_text= "Anzeige des Datums des letzten Updates in der Tabelle.",
        default = False,
    )

    update_username_show = models.BooleanField(
        name = 'update_username_show',
        verbose_name = 'Name des letzten Updates',
        help_text= "Anzeige des Namens des letzten Updates in der Tabelle.",
        default = False,
    )

    machine_show = models.BooleanField(
        name = 'machine_show',
        verbose_name = 'Maschine',
        help_text= "Anzeige der Maschine in der Tabelle.",
        default = True,
    )

    process_show = models.BooleanField(
        name = 'process_show',
        verbose_name = 'Prozess',
        help_text= "Anzeige des Prozesses in der Tabelle.",
        default = True,
    )

    count_show = models.BooleanField(
        name = 'count_show',
        verbose_name = 'Anzahl',
        help_text= "Anzeige der Anzahl in der Tabelle.",
        default = True,
    )

    utilization_show = models.BooleanField(
        name = 'utilization_show',
        verbose_name = 'Auslastung',
        help_text= "Anzeige der Auslastung in der Tabelle.",
        default = False,
    )

    utilization_percentage_show = models.BooleanField(
        name = 'utilization_percentage_show',
        verbose_name = 'Auslastung',
        help_text= "Anzeige der Auslastung in Prozent in der Tabelle.",
        default = False,
    )  

    utilization_percentage_formated = models.BooleanField(
        name = 'utilization_percentage_formated_show',
        verbose_name = 'Auslastung',
        help_text= "Anzeige der Auslastung in Prozent mit Einheit in der Tabelle.",
        default = True,
    )

    protocol_show = models.BooleanField(
        name = 'protocol_show',
        verbose_name = 'Protocol',
        help_text= "Anzeige des Protocols in der Tabelle.",
        default = True,
    )  

    url_delete_show = models.BooleanField(
        name = 'url_delete_show',
        verbose_name = 'Löschen',
        help_text= "Anzeige des Links zum Löschen des Prozesses in der Tabelle.",
        default = False,
    )

    def __str__(self):
        return self.user.username

    def field_string(self):
        result = ""
        result += "id," if self.id_show else ""
        result += "url_detail," if self.url_detail_show else ""
        result += "url_update," if self.url_update_show else ""
        result += "reference_number," if self.reference_number_show else ""
        result += "slug," if self.slug_show else ""
        result += "create_datetime," if self.create_datetime_show else ""
        result += "create_datetime_formated," if self.create_datetime_formated_show else ""
        result += "create_time," if self.create_datetime_show else ""
        result += "create_date," if self.create_datetime_show else ""
        result += "create_username," if self.create_username_show else ""
        result += "begin_datetime," if self.begin_datetime_show else ""
        result += "begin_datetime_formated," if self.begin_datetime_formated_show else ""
        result += "begin_time," if self.begin_time_show else ""
        result += "begin_date," if self.begin_date_show else ""
        result += "begin_username," if self.begin_username_show else ""
        result += "duration," if self.duration_show else ""
        result += "duration_formated," if self.duration_formated_show else ""
        result += "end_datetime," if self.end_datetime_show else ""
        result += "end_datetime_formated," if self.end_datetime_formated_show else ""
        result += "end_time," if self.end_time_show else ""
        result += "end_date," if self.end_date_show else ""
        result += "end_username," if self.end_username_show else ""
        result += "update_datetime," if self.update_datetime_show else ""
        result += "update_datetime_formated," if self.update_datetime_formated_show else ""
        result += "update_time," if self.update_time_show else ""
        result += "update_date," if self.update_date_show else ""
        result += "update_username," if self.update_username_show else ""
        result += "process_id," if self.process_show else ""
        result += "process_name," if self.process_show else ""
        result += "process_reference_number," if self.process_show else ""
        result += "process_url_detail," if self.process_show else ""
        result += "machine_id," if self.machine_show else ""
        result += "machine_name," if self.machine_show else ""
        result += "machine_reference_number," if self.machine_show else ""
        result += "machine_url_detail," if self.machine_show else ""
        result += "count," if self.count_show else ""
        result += "utilization," if self.utilization_show else ""
        result += "utilization_percentage," if self.utilization_percentage_show else ""
        result += "utilization_percentage_formated," if self.utilization_percentage_formated_show else ""
        result += "protocol_id," if self.protocol_show else ""
        result += "protocol_name," if self.protocol_show else ""
        result += "protocol_reference_number," if self.protocol_show else ""
        result += "protocol_url_detail," if self.protocol_show else ""
        result += "url_delete," if self.url_delete_show else ""
        return result
        
    #def url_delete(self):
    #    return reverse('personalmanagement:employee_delete',kwargs={'employee':self.id})

    #def url_detail(self):
    #    return reverse('personalmanagement:employee_detail',kwargs={'employee':self.id})
    
    #def url_update(self):
    #    return reverse('personalmanagement:employee_update',kwargs={'employee':self.id})

    class Meta:
        app_label = 'personalmanagement'
        ordering = []
        permissions = ()
        verbose_name = "Prozess Daten API Url"
        verbose_name_plural = "Prozess Daten API Urls"
#--------------------------------------------------------------------------------