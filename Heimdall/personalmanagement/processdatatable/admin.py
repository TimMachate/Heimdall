#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import admin
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from personalmanagement.processdatatable.models import ProcessDataTable
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
class ProcessDataTableAdminInline(admin.StackedInline):
    model = ProcessDataTable
    fk_name = 'user'
    fieldsets = (
        (None, {'fields':(
            ('user'),
            )}),
        ('Datum', {'fields':(
            ('begin','end'),
            )}),
        ('Tages', {'fields':(
            'day',
            )}),
        ('Url', {'fields':(
            'url',
            )}),
        ('Anzeigen', {'fields':(
            ('id_show'),
            ('url_detail_show'),
            ('url_update_show'),
            ('reference_number_show'),
            ('slug_show'),
            ('create_datetime_show'),
            ('create_datetime_formated_show'),
            ('create_time_show'),
            ('create_date_show'),
            ('create_username_show'),
            ('begin_datetime_show'),
            ('begin_datetime_formated_show'),
            ('begin_time_show'),
            ('begin_date_show'),
            ('begin_username_show'),
            ('duration_show'),
            ('duration_formated_show'),
            ('end_datetime_show'),
            ('end_datetime_formated_show'),
            ('end_time_show'),
            ('end_date_show'),
            ('end_username_show'),
            ('update_datetime_show'),
            ('update_datetime_formated_show'),
            ('update_time_show'),
            ('update_date_show'),
            ('update_username_show'),
            ('machine_show'),
            ('process_show'),
            ('count_show'),
            ('utilization_show'),
            ('utilization_percentage_show'),
            ('utilization_percentage_formated_show'),
            ('protocol_show'),
            ('url_delete_show'),
            )}),
    )
    filter_horizontal = []
#--------------------------------------------------------------------------------