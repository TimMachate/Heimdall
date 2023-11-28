#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.file.models import TechnicalDataSheetProxy,PictureProxy,ProtocolProxy
from structuremanagement.device.models import Device
from personalmanagement.employee.models import Employee
from structuremanagement.process.models import Process,ProcessData
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id','name','reference_number','url_detail']
#--------------------------------------------------------------------------------
class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PictureProxy
        fields = ['id','reference_number','name','url_detail','url_file']
#--------------------------------------------------------------------------------
class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ['id','name','reference_number','url_detail']
#--------------------------------------------------------------------------------
class ProcessDataSerializer(serializers.ModelSerializer):

    begin = serializers.SerializerMethodField()

    device = DeviceSerializer(source='device_id',many=False,read_only=True)

    duration_formated = serializers.ReadOnlyField()

    end = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    utilization_percentage_formated = serializers.ReadOnlyField()

    def get_begin(self,obj):
        result = {}
        result["id"] = obj.begin_user_id.id if obj.begin_user_id else None
        result["date"] = obj.begin_datetime.date().strftime("%d.%m.%Y") if obj.begin_datetime else None
        result["datetime"] = obj.begin_datetime if obj.begin_datetime else None
        result["datetime_formated"] = obj.begin_datetime.strftime("%d.%m.%Y %H:%M:%S") if obj.begin_datetime else None
        result["time"] = obj.begin_datetime.time().strftime("%H:%M:%S") if obj.begin_datetime else None
        result["username"] = obj.begin_user_id.username if obj.begin_user_id else None
        return result

    def get_end(self,obj):
        result = {}
        result["id"] = obj.end_user_id.id if obj.end_user_id else None
        result["date"] = obj.end_datetime.date().strftime("%d.%m.%Y") if obj.end_datetime else None
        result["datetime"] = obj.end_datetime if obj.end_datetime else None
        result["datetime_formated"] = obj.end_datetime.strftime("%d.%m.%Y %H:%M:%S") if obj.end_datetime else None
        result["time"] = obj.end_datetime.time().strftime("%H:%M:%S") if obj.end_datetime else None
        result["username"] = obj.end_user_id.username if obj.end_user_id else None
        return result

    def get_url(self,obj):
        result = {}
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    class Meta:
        model = ProcessData
        fields = ['id','reference_number','device','duration_formated','url', 'begin', 'end', 'count', 'utilization_percentage_formated']
#--------------------------------------------------------------------------------
class ProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtocolProxy
        fields = ['id','name','reference_number','url_detail','url_file']
#--------------------------------------------------------------------------------
class TechnicalDataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalDataSheetProxy
        fields = ['id','reference_number','name','url_detail','url_file']
#--------------------------------------------------------------------------------
class ProcessListSerializer(serializers.ModelSerializer):

    count = serializers.SerializerMethodField()

    create = serializers.SerializerMethodField()

    duration = serializers.SerializerMethodField()

    picture = PictureSerializer(source="picture_id",many=False,read_only=True)

    processes = serializers.SerializerMethodField()

    technical_data_sheet = TechnicalDataSheetSerializer(source="technical_data_sheet_id",many=False,read_only=True)

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    utilization = serializers.SerializerMethodField()

    def get_count(self,obj):
        result = {}
        result["average"] = obj.count_average(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        result["total"] = obj.count_total(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        return result

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
        return result
    
    def get_duration(self,obj):
        result = {}
        result["average"] = obj.duration_average(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        result["days"] = obj.duration_days
        result["hours"] = obj.duration_hours
        result["minutes"] = obj.duration_minutes
        result["seconds"] = obj.duration_seconds
        result["formated"] = obj.duration_theoretical()
        return result

    def get_processes(self,obj):
        result = {}
        qs = obj.processdata(begin_datetime=self.context['request'].query_params.get('begin'), end_datetime=self.context['request'].query_params.get('end'))
        serializer = ProcessDataSerializer(instance=qs, many=True, read_only=True)
        result["count"] = qs.count()
        result["last"] = serializer.data[0] if qs.count() > 0 else None
        result["next"] = ProcessDataSerializer(instance=obj.processdata_next(), many=False, read_only=True).data if obj.processdata_next() else None
        result["running"] = ProcessDataSerializer(instance=obj.processdata_running(), many=False, read_only=True).data if obj.processdata_running() else None
        result["status"] = obj.processdata_status()
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
        result["data_list"] = obj.url_data_list()
        result["data_table"] = obj.url_data_table()
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result
    
    def get_utilization(self,obj):
        result = {}
        result["average"] = obj.utilization_average(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ProcessListSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Process
        exclude = [
            'create_user_id',
            'create_datetime',
            'duration_days',
            'duration_hours',
            'duration_minutes',
            'duration_seconds',
            'picture_id',
            'update_user_id',
            'update_datetime',
            'technical_data_sheet_id',
            ]
#--------------------------------------------------------------------------------
class ProcessDetailSerializer(serializers.ModelSerializer):

    count = serializers.SerializerMethodField()

    create = serializers.SerializerMethodField()

    devices = DeviceSerializer(many=True, read_only=True)

    duration = serializers.SerializerMethodField()

    picture = PictureSerializer(source="picture_id",many=False,read_only=True)

    processes = serializers.SerializerMethodField()

    technical_data_sheet = TechnicalDataSheetSerializer(source="technical_data_sheet_id",many=False,read_only=True)

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    utilization = serializers.SerializerMethodField()

    def get_count(self,obj):
        result = {}
        result["average"] = obj.count_average(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        result["data"] = obj.count_data(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        result["total"] = obj.count_total(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        return result

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
        return result
    
    def get_duration(self,obj):
        result = {}
        result["average"] = obj.duration_average(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        result["data"] = obj.duration_data(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        result["days"] = obj.duration_days
        result["hours"] = obj.duration_hours
        result["minutes"] = obj.duration_minutes
        result["seconds"] = obj.duration_seconds
        result["formated"] = obj.duration_theoretical()
        return result

    def get_processes(self,obj):
        result = {}
        qs = obj.processdata(begin_datetime=self.context['request'].query_params.get('begin'), end_datetime=self.context['request'].query_params.get('end'))
        serializer = ProcessDataSerializer(instance=qs, many=True, read_only=True)
        result["count"] = qs.count()
        result["data"] = serializer.data
        result["last"] = result["data"][0] if qs.count() > 0 else None
        result["next"] = ProcessDataSerializer(instance=obj.processdata_next(), many=False, read_only=True).data if obj.processdata_next() else None
        result["running"] = ProcessDataSerializer(instance=obj.processdata_running(), many=False, read_only=True).data if obj.processdata_running() else None
        result["status"] = obj.processdata_status()
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
        result["data_list"] = obj.url_data_list()
        result["data_table"] = obj.url_data_table()
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result
    
    def get_utilization(self,obj):
        result = {}
        result["average"] = obj.utilization_average(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        result["data"] = obj.utilization_data(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ProcessDetailSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Process
        exclude = [
            'create_user_id',
            'create_datetime',
            'duration_days',
            'duration_hours',
            'duration_minutes',
            'duration_seconds',
            'picture_id',
            'update_user_id',
            'update_datetime',
            'technical_data_sheet_id',
            ]
#--------------------------------------------------------------------------------
class ProcessDataListSerializer(serializers.ModelSerializer):

    begin = serializers.SerializerMethodField()

    create = serializers.SerializerMethodField()

    device = DeviceSerializer(source="device_id", many=False, read_only=True)

    duration = serializers.ReadOnlyField()
    duration_formated = serializers.ReadOnlyField()

    end = serializers.SerializerMethodField()

    process = ProcessSerializer(source="process_id", many=False, read_only=True)

    protocol = ProtocolSerializer(source="protocol_id", many=False, read_only=True)

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    utilization = serializers.SerializerMethodField()

    def get_begin(self,obj):
        result = {}
        result["id"] = obj.begin_user_id.id if obj.begin_user_id else None
        result["date"] = obj.begin_datetime.date().strftime("%d.%m.%Y") if obj.begin_datetime else None
        result["datetime"] = obj.begin_datetime if obj.begin_datetime else None
        result["datetime_formated"] = obj.begin_datetime.strftime("%d.%m.%Y %H:%M:%S") if obj.begin_datetime else None
        result["time"] = obj.begin_datetime.time().strftime("%H:%M:%S") if obj.begin_datetime else None
        result["username"] = obj.begin_user_id.username if obj.begin_user_id else None
        return result

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
        return result

    def get_end(self,obj):
        result = {}
        result["id"] = obj.end_user_id.id if obj.end_user_id else None
        result["date"] = obj.end_datetime.date().strftime("%d.%m.%Y") if obj.end_datetime else None
        result["datetime"] = obj.end_datetime if obj.end_datetime else None
        result["datetime_formated"] = obj.end_datetime.strftime("%d.%m.%Y %H:%M:%S") if obj.end_datetime else None
        result["time"] = obj.end_datetime.time().strftime("%H:%M:%S") if obj.end_datetime else None
        result["username"] = obj.end_user_id.username if obj.end_user_id else None
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

    def get_utilization(self,obj):
        result = {}
        result["value"] = obj.utilization()
        result["percentage"] = obj.utilization_percentage()
        result["formated"] = obj.utilization_percentage_formated()
        return result

    def get_url(self,obj):
        result = {}
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ProcessDataListSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = ProcessData
        exclude = [
            'begin_datetime',
            'begin_user_id',
            'create_datetime',
            'create_user_id',
            'end_datetime',
            'end_user_id',
            'device_id',
            'process_id',
            'protocol_id',
            'update_datetime',
            'update_user_id',
        ]
#--------------------------------------------------------------------------------
class ProcessDataDetailSerializer(serializers.ModelSerializer):

    begin = serializers.SerializerMethodField()

    create = serializers.SerializerMethodField()

    device = DeviceSerializer(source="device_id", many=False, read_only=True)

    duration = serializers.ReadOnlyField()
    duration_formated = serializers.ReadOnlyField()

    end = serializers.SerializerMethodField()

    process = ProcessSerializer(source="process_id", many=False, read_only=True)

    protocol = ProtocolSerializer(source="protocol_id", many=False, read_only=True)

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    utilization = serializers.SerializerMethodField()


    def get_begin(self,obj):
        result = {}
        result["id"] = obj.begin_user_id.id if obj.begin_user_id else None
        result["date"] = obj.begin_datetime.date().strftime("%d.%m.%Y") if obj.begin_datetime else None
        result["datetime"] = obj.begin_datetime if obj.begin_datetime else None
        result["datetime_formated"] = obj.begin_datetime.strftime("%d.%m.%Y %H:%M:%S") if obj.begin_datetime else None
        result["time"] = obj.begin_datetime.time().strftime("%H:%M:%S") if obj.begin_datetime else None
        result["username"] = obj.begin_user_id.username if obj.begin_user_id else None
        return result

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
        return result

    def get_end(self,obj):
        result = {}
        result["id"] = obj.end_user_id.id if obj.end_user_id else None
        result["date"] = obj.end_datetime.date().strftime("%d.%m.%Y") if obj.end_datetime else None
        result["datetime"] = obj.end_datetime if obj.end_datetime else None
        result["datetime_formated"] = obj.end_datetime.strftime("%d.%m.%Y %H:%M:%S") if obj.end_datetime else None
        result["time"] = obj.end_datetime.time().strftime("%H:%M:%S") if obj.end_datetime else None
        result["username"] = obj.end_user_id.username if obj.end_user_id else None
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

    def get_utilization(self,obj):
        result = {}
        result["value"] = obj.utilization()
        result["percentage"] = obj.utilization_percentage()
        result["formated"] = obj.utilization_percentage_formated()
        return result

    def get_url(self,obj):
        result = {}
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ProcessDataListSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = ProcessData
        exclude = [
            'begin_datetime',
            'begin_user_id',
            'create_datetime',
            'create_user_id',
            'end_datetime',
            'end_user_id',
            'device_id',
            'process_id',
            'protocol_id',
            'update_datetime',
            'update_user_id',
            ]
#--------------------------------------------------------------------------------