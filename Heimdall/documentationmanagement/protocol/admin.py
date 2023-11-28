#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import admin
from django.utils import timezone
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.protocol.models import Protocol, ProtocolStep, ProtocolData, Variable
from documentationmanagement.file.models import File, ProtocolProxy
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Admins
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
class ProtocolStepInline(admin.StackedInline):
    model = ProtocolStep
    extra = 1
    ordering = ['order',]
    fieldsets = (
        (None, {'fields':(
            'name',
            'order',
            'text',
            'variables',
            )}),
    )
    filter_horizontal = ['variables',]

class ProtocolInlineAdmin(admin.StackedInline):
    model = Protocol
    max_num = 1
    fieldsets = (
        ('Protokoll Daten', {'fields':(
            'topic',
            'procedure',
            'protocol',   
            )}),
    )
    inlines = [ProtocolStepInline]


@admin.register(ProtocolProxy)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ['reference_number','name','version_prefix','version_suffix']
    search_fields = ['name']
    list_filter = []
    list_editable = []
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            'version_prefix',
            )}),
        (None, {'fields':(
            'file',
            )}),
        ('Beschreibung', {'fields':(
            'keywords',
        )}),
    )

    inlines = [ProtocolInlineAdmin]
    filter_horizontal = []
    radio_fields = {}
    def save_model(self, request, instance, form, change):
        user = request.user
        instance.type=instance.Types.PROTOCOL
        instance = form.save(commit=False)
        if not change or not instance.create_user_id:
            instance.create_user_id = user
        instance.update_user_id = user
        instance.update_datetime = timezone.now()
        instance.save()
        form.save_m2m()
        return instance
#--------------------------------------------------------------------------------
@admin.register(ProtocolData)
class ProtocolDataAdmin(admin.ModelAdmin):
    list_display = ['reference_number','version','update_datetime','update_user_id']
    search_fields = ['update_user_id']
    list_filter = []
    list_editable = []
    ordering = ['-update_datetime']
    fieldsets = (
        (None, {'fields':(
            'protocol_id',
            'json',
            'file'
            )}),
    )

    inlines = []
    filter_horizontal = []
    radio_fields = {}
    def save_model(self, request, instance, form, change):
        user = request.user
        if not change or not instance.create_user_id:
            instance.create_user_id = user
        instance.update_user_id = user
        instance.update_datetime = timezone.now()
        instance.save()
        form.save_m2m()
        return instance
#--------------------------------------------------------------------------------
@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    list_display = ['name','symbol','unit','update_datetime','update_user_id',]
    search_fields = ['name']
    list_filter = []
    list_editable = []
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            'input_type',
            'symbol',
            'unit',
            )}),
    )

    inlines = []
    filter_horizontal = []
    radio_fields = {}
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.create_user_id:
            instance.create_user_id = user
        instance.update_user_id = user
        instance.update_datetime = timezone.now()
        instance.save()
        form.save_m2m()
        return instance
#--------------------------------------------------------------------------------