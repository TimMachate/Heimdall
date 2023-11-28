#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.file.models import ProtocolProxy
from documentationmanagement.protocol.models import ProtocolData
from structuremanagement.device.models import Device
from structuremanagement.maintenance.models import Maintenance
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id','name', 'reference_number','url_detail']

class ProtocolSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProtocolProxy
        fields = ['id','name','reference_number','url_detail']

class ProtocolDataSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime.strftime("%d.%m.%Y %H:%M:%S")
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
        return result

    def get_url(self,obj):
        result = {}
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    class Meta:
        model = ProtocolData
        fields = ['id','create','file','reference_number','version','url','results']

class MaintenanceListSerializer(serializers.ModelSerializer):

    alarm = serializers.ReadOnlyField()

    create = serializers.SerializerMethodField()

    device = DeviceSerializer(source='device_id',many=False,read_only=True)

    maintenance_count = serializers.ReadOnlyField()

    maintenance_next = serializers.SerializerMethodField()

    maintenance_last = ProtocolDataSerializer(many=False,read_only=True)

    protocol = ProtocolSerializer(source='protocol_id',many=False,read_only=True)

    repetition = serializers.SerializerMethodField()

    status = serializers.ReadOnlyField()

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    warning = serializers.SerializerMethodField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
        return result
    
    def get_maintenance_next(self,obj):
        if obj.maintenance_next():
            result = {}
            result["date"] = obj.maintenance_next().date().strftime("%d.%m.%Y")
            result["datetime"] = obj.maintenance_next()
            result["datetime_formated"] = obj.maintenance_next().strftime("%d.%m.%Y %H:%M:%S")
            result["time"] = obj.maintenance_next().time().strftime("%H:%M:%S")
        else:
            result = None
        return result

    def get_repetition(self,obj):
        result = {}
        result["days"] = obj.repetition_days
        result["hours"] = obj.repetition_hours
        result["minutes"] = obj.repetition_minutes
        result["seconds"] = obj.repetition_seconds
        result["formated"] = obj.repetition_formated()
        return result
    
    def get_update(self,obj):
        result = {}
        result["id"] = obj.update_user_id.id
        result["date"] = obj.update_date()
        result["datetime"] = obj.update_datetime
        result["datetime_formated"] = obj.update_datetime_formated()
        result["time"] = obj.update_time()
        result["username"] = obj.update_username()
        return result
    
    def get_url(self,obj):
        result = {}
        result["data_create"] = obj.url_data_create()
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    def get_warning(self,obj):
        result = {}
        result["days"] = obj.warning_days
        result["hours"] = obj.warning_hours
        result["minutes"] = obj.warning_minutes
        result["seconds"] = obj.warning_seconds
        result["formated"] = obj.warning_formated()
        result["status"] = obj.warning_status()
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(MaintenanceListSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Maintenance
        exclude = [
            'create_user_id',
            'create_datetime',
            'device_id',
            'protocol_id',
            'repetition_days',
            'repetition_hours',
            'repetition_minutes',
            'repetition_seconds',
            'update_user_id',
            'update_datetime',
            'warning_days',
            'warning_hours',
            'warning_minutes',
            'warning_seconds',
            ]
#--------------------------------------------------------------------------------
class MaintenanceDetailSerializer(serializers.ModelSerializer):

    alarm = serializers.ReadOnlyField()

    create = serializers.SerializerMethodField()

    device = DeviceSerializer(source='device_id',many=False,read_only=True)

    maintenance_count = serializers.ReadOnlyField()

    maintenance_data = ProtocolDataSerializer(many=True,read_only=True)

    maintenance_next = serializers.SerializerMethodField()

    maintenance_last = ProtocolSerializer(many=False,read_only=True)

    protocol = ProtocolSerializer(source='protocol_id',many=False,read_only=True)

    repetition = serializers.SerializerMethodField()

    status = serializers.ReadOnlyField()

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    warning = serializers.SerializerMethodField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
        return result
    
    def get_maintenance_next(self,obj):
        if obj.maintenance_next():
            result = {}
            result["date"] = obj.maintenance_next().date().strftime("%d.%m.%Y")
            result["datetime"] = obj.maintenance_next()
            result["datetime_formated"] = obj.maintenance_next().strftime("%d.%m.%Y %H:%M:%S")
            result["time"] = obj.maintenance_next().time().strftime("%H:%M:%S")
        else:
            result = None
        return result

    def get_repetition(self,obj):
        result = {}
        result["days"] = obj.repetition_days
        result["hours"] = obj.repetition_hours
        result["minutes"] = obj.repetition_minutes
        result["seconds"] = obj.repetition_seconds
        result["formated"] = obj.repetition_formated()
        return result
    
    def get_update(self,obj):
        result = {}
        result["id"] = obj.update_user_id.id
        result["date"] = obj.update_date()
        result["datetime"] = obj.update_datetime
        result["datetime_formated"] = obj.update_datetime_formated()
        result["time"] = obj.update_time()
        result["username"] = obj.update_username()
        return result
    
    def get_url(self,obj):
        result = {}
        result["data_create"] = obj.url_data_create()
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    def get_warning(self,obj):
        result = {}
        result["days"] = obj.warning_days
        result["hours"] = obj.warning_hours
        result["minutes"] = obj.warning_minutes
        result["seconds"] = obj.warning_seconds
        result["formated"] = obj.warning_formated()
        result["status"] = obj.warning_status()
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(MaintenanceDetailSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Maintenance
        exclude = [
            'create_user_id',
            'create_datetime',
            'device_id',
            'protocol_id',
            'repetition_days',
            'repetition_hours',
            'repetition_minutes',
            'repetition_seconds',
            'update_user_id',
            'update_datetime',
            'warning_days',
            'warning_hours',
            'warning_minutes',
            'warning_seconds',
            ]
#--------------------------------------------------------------------------------