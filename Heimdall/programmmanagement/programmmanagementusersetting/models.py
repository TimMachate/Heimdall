"""
#--------------------------------------------------------------------------------
# Models File from Model Programm
# 18.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
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
from programmmanagement.models import CreateData,UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class ProgrammManagementProgrammListUserSetting(
    CreateData,
    UpdateData
):
    """
    ProgrammManagementProgrammListUserSetting
    """
    # api
    api = models.CharField(
        default = 'programmmanagementAPI:programm_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    # programm
    reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Referenz Nummer',
        name = 'reference_number',
        verbose_name = 'Referenznummer',
    )

    name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Firmennamen',
        name = 'name',
        verbose_name = 'Firmenname',
    )

    description = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Beschreibung',
        name = 'description',
        verbose_name = 'Beschreibung',
    )

    htmlfile_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des HTML Datei Namen',
        name = 'htmlfile_name',
        verbose_name = 'HTML Datei Name',
    )

    htmlfile_url = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links der HTML Datei',
        name = 'htmlfile_url',
        verbose_name = 'Link HTML Datei',
    )

    users = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Benutzer',
        name = 'users',
        verbose_name = 'Benutzer',
    )

    users_count = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Benutzeranzahl',
        name = 'users_count',
        verbose_name = 'Benutzeranzahl',
    )

    create_date = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Erstellerdatums',
        name = 'create_date',
        verbose_name = 'Erstellerdatum',
    )

    create_time = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Erstellerzeit',
        name = 'create_time',
        verbose_name = 'Erstellerzeit',
    )

    create_user = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Erstellers',
        name = 'create_user',
        verbose_name = 'Ersteller',
    )

    update_date = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Update-Datum',
        name = 'update_date',
        verbose_name = 'Update-Datum',
    )

    update_time = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Update-Zeit',
        name = 'update_time',
        verbose_name = 'Update-Zeit',
    )

    update_user = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Update-Benutzer',
        name = 'update_user',
        verbose_name = 'Update-Benutzer',
    )

    url_detail = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Detail-Links',
        name = 'url_detail',
        verbose_name = 'Detail-Link',
    )

    url_update = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Update-links',
        name = 'url_update',
        verbose_name = 'Update-Link',
    )

    url_delete = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Löschen-Links',
        name = 'url_delete',
        verbose_name = 'Löschen-Link',
    )

    url_block = models.BooleanField(
        default = True,
        help_text = 'Darstellung aller Links in einem Block',
        name = 'url_block',
        verbose_name = 'Links',
    )

    # urls
    def fields(self):
        """
        url_api

        Returns:
            string: url to api
        """
        field_string = "id,"
        field_string += "reference_number," if self.reference_number else ""
        field_string += "name," if self.name else ""
        field_string += "description," if self.description else ""
        field_string += "htmlfile_name," if self.htmlfile_name else ""
        field_string += "htmlfile_url," if self.htmlfile_url else ""
        field_string += "users," if self.users else ""
        field_string += "users_count," if self.users_count else ""
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "update_date," if self.update_date else ""
        field_string += "update_time," if self.update_time else ""
        field_string += "update_username," if self.update_user else ""
        field_string += "url_detail," if self.url_detail else ""
        field_string += "url_update," if self.url_update else ""
        field_string += "url_delete," if self.url_delete else ""
        field_string += "url_detail,url_update,url_delete,url_block," if self.url_block else ""
        return reverse(
            self.api
        )+f"?values={field_string}"

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'programmmanagementprogrammlistusersetting_user',
        to = get_user_model(),
        verbose_name = 'Benutzer',
    )

    def __str__(self):
        """
        __str__

        Returns:
            string: _description_
        """
        return f"{self.user.username}"

    class Meta:
        """
        Meta Data from Model
        """
        app_label = 'programmmanagement'
        default_permissions = ()
        ordering = ['user']
        permissions = (
            (
                'programmmanagement_programm_list_setting',
                'Programmmanagement Programm List can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Firmen Liste"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Firmen Liste"

#--------------------------------------------------------------------------------
class ProgrammManagementProgrammTableUserSetting(
    CreateData,
    UpdateData
):
    """
    ProgrammManagementProgrammTableUserSetting
    """

    # api
    api = models.CharField(
        default = 'programmmanagementAPI:programm_list',
        help_text = 'Url Adresse der API',
        max_length = 200,
        name = 'api',
        verbose_name = 'API Url',
    )

    # programm
    reference_number = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Referenz Nummer',
        name = 'reference_number',
        verbose_name = 'Referenznummer',
    )

    name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Firmennamen',
        name = 'name',
        verbose_name = 'Firmenname',
    )

    description = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Beschreibung',
        name = 'description',
        verbose_name = 'Beschreibung',
    )

    htmlfile_name = models.BooleanField(
        default = True,
        help_text = 'Darstellung des HTML Datei Namen',
        name = 'htmlfile_name',
        verbose_name = 'HTML Datei Name',
    )

    htmlfile_url = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Links der HTML Datei',
        name = 'htmlfile_url',
        verbose_name = 'Link HTML Datei',
    )

    users = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Benutzer',
        name = 'users',
        verbose_name = 'Benutzer',
    )

    users_count = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Benutzeranzahl',
        name = 'users_count',
        verbose_name = 'Benutzeranzahl',
    )

    create_date = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Erstellerdatums',
        name = 'create_date',
        verbose_name = 'Erstellerdatum',
    )

    create_time = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Erstellerzeit',
        name = 'create_time',
        verbose_name = 'Erstellerzeit',
    )

    create_user = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Erstellers',
        name = 'create_user',
        verbose_name = 'Ersteller',
    )

    update_date = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Update-Datum',
        name = 'update_date',
        verbose_name = 'Update-Datum',
    )

    update_time = models.BooleanField(
        default = True,
        help_text = 'Darstellung der Update-Zeit',
        name = 'update_time',
        verbose_name = 'Update-Zeit',
    )

    update_user = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Update-Benutzer',
        name = 'update_user',
        verbose_name = 'Update-Benutzer',
    )

    url_detail = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Detail-Links',
        name = 'url_detail',
        verbose_name = 'Detail-Link',
    )

    url_update = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Update-links',
        name = 'url_update',
        verbose_name = 'Update-Link',
    )

    url_delete = models.BooleanField(
        default = True,
        help_text = 'Darstellung des Löschen-Links',
        name = 'url_delete',
        verbose_name = 'Löschen-Link',
    )

    url_block = models.BooleanField(
        default = True,
        help_text = 'Darstellung aller Links in einem Block',
        name = 'url_block',
        verbose_name = 'Links',
    )

    # urls
    def fields(self):
        """
        url_api

        Returns:
            string: url to api
        """
        field_string = "id,"
        field_string += "reference_number," if self.reference_number else ""
        field_string += "name," if self.name else ""
        field_string += "description," if self.description else ""
        field_string += "htmlfile_name," if self.htmlfile_name else ""
        field_string += "htmlfile_url," if self.htmlfile_url else ""
        field_string += "users," if self.users else ""
        field_string += "users_count," if self.users_count else ""
        field_string += "create_date," if self.create_date else ""
        field_string += "create_time," if self.create_time else ""
        field_string += "create_username," if self.create_user else ""
        field_string += "update_date," if self.update_date else ""
        field_string += "update_time," if self.update_time else ""
        field_string += "update_username," if self.update_user else ""
        field_string += "url_detail," if self.url_detail else ""
        field_string += "url_update," if self.url_update else ""
        field_string += "url_delete," if self.url_delete else ""
        field_string += "url_detail,url_update,url_delete,url_block," if self.url_block else ""
        return reverse(
            self.api
        )+f"?values={field_string}"

    # user
    user = models.OneToOneField(
        blank = False,
        name = 'user',
        null = False,
        on_delete = models.CASCADE,
        related_name = 'programmmanagementprogrammtableusersetting_user',
        to = get_user_model(),
        verbose_name = 'Benutzer',
    )

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        """
        Meta Data from Model
        """
        app_label = 'programmmanagement'
        default_permissions = ()
        ordering = ['user']
        permissions = (
            (
                'programmmanagement_programm_table_setting',
                'Programmmanagement Programm Table can view Setting'
            ),
        )
        verbose_name = "Einstellung Beziehungsmanagement Firmen Tabelle"
        verbose_name_plural = "Einstellungen Beziehungsmanagement Firmen Tabelle"

#--------------------------------------------------------------------------------
