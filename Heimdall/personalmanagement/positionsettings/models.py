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
from main.createdata.models import CreateData
from main.updatedata.models import UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class PositionSettings(CreateData,UpdateData):
    user_id = models.OneToOneField(
        name = "user_id",
        verbose_name = "Benutzername",
        related_name = "position_settings_user_id",
        to = get_user_model(),
        on_delete = models.CASCADE,
        blank = False,
        null = False,
        )

    api_url_overview_view = models.TextField(
        name = 'api_url_overview_view',
        verbose_name = 'API Overview View Url',
        help_text= """
        Von der hier eingegebenen URL werden die angezeigten Daten bezogen. Mit dem Zusatz ?values= können spezielle Werte eingegeben werden. Es werden ausschließlich diese Werte angezeigt. Wird der Zusatz weggelassen, so werden alle Werte angezeigt.<br>
        <br>
        Mögliche Werte: <br>
        id <br>
        create_datetime <br>
        create_datetime_formated <br>
        create_date <br>
        create_time <br>
        create_username <br>
        update_datetime <br>
        update_datetime_formated <br>
        update_date <br>
        update_time <br>
        update_username <br>
        name <br>
        section_count <br>
        position_count <br>
        employee_count <br>
        process_instruction_file_url <br>
        process_instruction_url_detail <br>
        image_file_url <br>
        image_url_detail <br>
        reference_number <br>
        responsible_reference_number <br>
        responsible_name <br>
        responsible_url_detail <br>
        responsible_email <br>
        responsible_telephone <br>
        substitute_reference_number <br>
        substitute_name <br>
        substitute_url_detail <br>
        substitute_email <br>
        substitute_telephone <br>
        rgba_value <br>
        rgba_style <br>
        rgba_red <br>
        rgba_green <br>
        rgba_blue <br>
        rgba_alpha <br>
        url_detail <br>
        url_update <br>
        url_delete <br>
        <br>
        Beispiel: <br>
        /api/structuremanagement/position/list/?values=name,reference_number <br>
        Es wird ausschließlich der Name und die Referenznummer angzeigt. <br>
        """,
        default = "/api/structuremanagement/position/list/?values=id,name,url_detail,position_count,section_count,reference_number,employee_count,responsible_name,responsible_url_detail,responsible_telephone,responsible_email,substitute_name,substitute_url_detail,substitute_telephone,substitute_email,image_file_url",
        blank = True,
        null = True,
    )

    api_url_list_view = models.TextField(
        name = 'api_url_list_view',
        verbose_name = 'API List View Url',
        help_text= """
        Von der hier eingegebenen URL werden die angezeigten Daten bezogen. Mit dem Zusatz ?values= können spezielle Werte eingegeben werden. Es werden ausschließlich diese Werte angezeigt. Wird der Zusatz weggelassen, so werden alle Werte angezeigt.<br>
        <br>
        Mögliche Werte: <br>
        id <br>
        create_datetime <br>
        create_datetime_formated <br>
        create_date <br>
        create_time <br>
        create_username <br>
        update_datetime <br>
        update_datetime_formated <br>
        update_date <br>
        update_time <br>
        update_username <br>
        name <br>
        section_count <br>
        position_count <br>
        employee_count <br>
        process_instruction_file_url <br>
        process_instruction_url_detail <br>
        image_file_url <br>
        image_url_detail <br>
        reference_number <br>
        responsible_reference_number <br>
        responsible_name <br>
        responsible_url_detail <br>
        responsible_email <br>
        responsible_telephone <br>
        substitute_reference_number <br>
        substitute_name <br>
        substitute_url_detail <br>
        substitute_email <br>
        substitute_telephone <br>
        rgba_value <br>
        rgba_style <br>
        rgba_red <br>
        rgba_green <br>
        rgba_blue <br>
        rgba_alpha <br>
        url_detail <br>
        url_update <br>
        url_delete <br>
        <br>
        Beispiel: <br>
        /api/structuremanagement/position/list/?values=name,reference_number <br>
        Es wird ausschließlich der Name und die Referenznummer angzeigt. <br>
        """,
        default = "/api/structuremanagement/position/list/?values=url_detail,url_update,url_delete,reference_number,name,rgba_value,rgba_style",
        blank = True,
        null = True,
    )

    api_url_table_view = models.TextField(
        name = 'api_url_table_view',
        verbose_name = 'API Table View Url',
        help_text= """
        Von der hier eingegebenen URL werden die angezeigten Daten bezogen. Mit dem Zusatz ?values= können spezielle Werte eingegeben werden. Es werden ausschließlich diese Werte angezeigt. Wird der Zusatz weggelassen, so werden alle Werte angezeigt.<br>
        <br>
        Mögliche Werte: <br>
        id <br>
        create_datetime <br>
        create_datetime_formated <br>
        create_date <br>
        create_time <br>
        create_username <br>
        update_datetime <br>
        update_datetime_formated <br>
        update_date <br>
        update_time <br>
        update_username <br>
        name <br>
        section_count <br>
        position_count <br>
        employee_count <br>
        process_instruction_file_url <br>
        process_instruction_url_detail <br>
        image_file_url <br>
        image_url_detail <br>
        reference_number <br>
        responsible_reference_number <br>
        responsible_name <br>
        responsible_url_detail <br>
        responsible_email <br>
        responsible_telephone <br>
        substitute_reference_number <br>
        substitute_name <br>
        substitute_url_detail <br>
        substitute_email <br>
        substitute_telephone <br>
        rgba_value <br>
        rgba_style <br>
        rgba_red <br>
        rgba_green <br>
        rgba_blue <br>
        rgba_alpha <br>
        url_detail <br>
        url_update <br>
        url_delete <br>
        <br>
        Beispiel: <br>
        /api/structuremanagement/position/list/?values=name,reference_number <br>
        Es wird ausschließlich der Name und die Referenznummer angzeigt. <br>
        """,
        default = "/api/structuremanagement/position/list/?values=url_detail,reference_number,name,rgba_value,rgba_style,responsible_name,substitute_name,section_count,position_count,employee_count,process_instruction_file_url,update_date,update_time,update_username",
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.user_id.username

    class Meta:
        app_label = 'personalmanagement'
        ordering = []
        permissions = ()
        verbose_name = "Einstellung für die Position"
        verbose_name_plural = "Einstellungen für die Position"
#--------------------------------------------------------------------------------