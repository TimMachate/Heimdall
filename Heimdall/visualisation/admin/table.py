from django.contrib import admin
from django.utils import timezone

from visualisation.models import Table, TableItem

class TableItemAdmin(admin.TabularInline):
    model = TableItem
    extra = 0
    ordering = ['order']
    fieldsets = (
        (None, {'fields':(
            ('name','order'),
            ('itemData','col_width',),
            ('hAlign','vAlign'),
            )}),
    )

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['id','get_user','get_tab','name','create_user','create_time','update_user','update_time','order',]
    search_fields = ['name','tab__name','tab__user__username',]
    list_filter = ['tab__user__username']
    list_editable = ['order',]
    ordering = ['tab','order','name',]
    fieldsets = (
        (None, {'fields':(
            'tab',
            )}),
        ('Tabelle', {'fields':(
            ('name','order'),
            )}),
        ('Daten', {'fields':(
            'dataURL',
            'time',
            )}),
        ('Layout', {'fields':(
            ('col_xs','col_sm','col_md','col_lg','col_xl',),
            )}),
    )
    inlines = [
        TableItemAdmin,
    ]
    filter_horizontal = []
    radio_fields = {}
    def get_user(self, obj):
        return obj.tab.user.username
    get_user.admin_order_field  = 'tab'
    get_user.short_description = 'Benutzer'
    def get_tab(self, obj):
        return obj.tab.name
    get_tab.short_description = 'Tab'
    def get_column(self,obj):
        return 'xs-'+str(obj.col_xs)+' '+'sm-'+str(obj.col_sm)+' '+'md-'+str(obj.col_md)+' '+'lg-'+str(obj.col_lg)+' '+'xl-'+str(obj.col_xl)
    get_column.short_description = 'Column'

    def save_model(self, request, instance, form, change):
        if not instance.create_user:
            instance.create_user = request.user
        if not instance.create_time:
            instance.create_time = timezone.now()
        instance.update_user = request.user
        instance.update_time = timezone.now()
        return super().save_model(request, instance, form, change = True)