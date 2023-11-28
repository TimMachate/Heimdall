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
from personalmanagement.processtable.models import ProcessTable
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
class ProcessTableAdminInline(admin.StackedInline):
    model = ProcessTable
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
            ('referenceNumber_show'),
            ('name_show'),
            ('duration_theoretical_show'),
            ('duration_average_show'),
            ('count_total_show'),
            ('count_average_show'),
            ('utilization_show'),
            ('create_datetime_show'),
            ('create_datetime_formated_show'),
            ('create_time_show'),
            ('create_date_show'),
            ('create_username_show'),
            ('update_datetime_show'),
            ('update_datetime_formated_show'),
            ('update_time_show'),
            ('update_date_show'),
            ('update_username_show'),
            )}),
    )
    filter_horizontal = []
#--------------------------------------------------------------------------------