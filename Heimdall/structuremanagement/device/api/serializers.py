#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.file.models import DocumentProxy, ManualProxy, PictureProxy, WorkingInstructionProxy
from relationshipmanagement.company.models import Company
from structuremanagement.device.models import Device
from structuremanagement.error.models import Error,ErrorData
from structuremanagement.group.models import Group
from structuremanagement.maintenance.models import Maintenance
from structuremanagement.process.models import Process,ProcessData
from structuremanagement.status.models import Status,StatusData
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from main.api.serializers import CreateSerializer,UpdateSerializer
#--------------------------------------------------------------------------------
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name','reference_number','url_detail']
#--------------------------------------------------------------------------------
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id','name','reference_number','url_detail']
#--------------------------------------------------------------------------------
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentProxy
        fields = ['id','name','reference_number','url_detail']
#--------------------------------------------------------------------------------
class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = ['id','name','reference_number','url_detail']

class ErrorDataSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    device = DeviceSerializer(source='device_id',many=False,read_only=True)

    error = ErrorSerializer(source='error_id',many=False,read_only=True)

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id if obj.create_user_id else None
        result["date"] = obj.create_datetime.date().strftime("%d.%m.%Y") if obj.create_datetime else None
        result["datetime"] = obj.create_datetime if obj.create_datetime else None
        result["datetime_formated"] = obj.create_datetime.strftime("%d.%m.%Y %H:%M:%S") if obj.create_datetime else None
        result["time"] = obj.create_datetime.time().strftime("%H:%M:%S") if obj.create_datetime else None
        result["username"] = obj.create_user_id.username if obj.create_user_id else None
        return result

    class Meta:
        model = ErrorData
        fields = ['id','create','device','error','reference_number','url_detail']
#--------------------------------------------------------------------------------
class MaintenanceSerializer(serializers.ModelSerializer):

    next_maintenance = serializers.ReadOnlyField()

    protocol_last_time = serializers.ReadOnlyField()

    status = serializers.ReadOnlyField()

    url_protocol_data_add = serializers.ReadOnlyField()

    class Meta:
        model = Maintenance
        fields = ['id','reference_number','name','status','url_protocol_data_add','next_maintenance','protocol_last_time']
#--------------------------------------------------------------------------------
class ManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualProxy
        fields = ['id','name','reference_number','url_detail']
#--------------------------------------------------------------------------------
class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PictureProxy
        fields = ['id','name','reference_number','url_detail','url_file']
#--------------------------------------------------------------------------------
class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ['id','name','reference_number','url_detail']
#--------------------------------------------------------------------------------
class ProcessDataSerializer(serializers.ModelSerializer):

    begin = serializers.SerializerMethodField()

    process = ProcessSerializer(source='process_id',many=False,read_only=True)

    duration_formated = serializers.ReadOnlyField()

    end = serializers.SerializerMethodField()

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

    class Meta:
        model = ProcessData
        fields = ['id','reference_number','process','duration_formated','url_detail', 'begin', 'end', 'count', 'utilization_percentage_formated']
#--------------------------------------------------------------------------------
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id','name','reference_number','rgba_value','url_detail']
#--------------------------------------------------------------------------------
class StatusDataSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    device = DeviceSerializer(source='device_id',many=False,read_only=True)

    status = StatusSerializer(source='status_id',many=False,read_only=True)

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id if obj.create_user_id else None
        result["date"] = obj.create_datetime.date().strftime("%d.%m.%Y") if obj.create_datetime else None
        result["datetime"] = obj.create_datetime if obj.create_datetime else None
        result["datetime_formated"] = obj.create_datetime.strftime("%d.%m.%Y %H:%M:%S") if obj.create_datetime else None
        result["time"] = obj.create_datetime.time().strftime("%H:%M:%S") if obj.create_datetime else None
        result["username"] = obj.create_user_id.username if obj.create_user_id else None
        return result

    class Meta:
        model = StatusData
        fields = ['id','create','device','status','reference_number','url_detail']
#--------------------------------------------------------------------------------
class WorkingInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingInstructionProxy
        fields = ['id','name','reference_number','url_detail']
#--------------------------------------------------------------------------------
class DeviceListSerializer(CreateSerializer,UpdateSerializer):

    documents = DocumentSerializer(many=True,read_only=True)
    documents_count = serializers.ReadOnlyField()

    errors = serializers.SerializerMethodField()
    errordata = serializers.SerializerMethodField()

    fabricator = CompanySerializer(source="fabricator_id",many=False,read_only=True)

    maintenance = serializers.SerializerMethodField()

    manuals = ManualSerializer(many=True,read_only=True)
    manuals_count = serializers.ReadOnlyField()

    picture = PictureSerializer(source="picture_id",many=False,read_only=True)

    processes = serializers.SerializerMethodField()
    processdata = serializers.SerializerMethodField()

    status = serializers.SerializerMethodField()
    statusdata = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    working_instructions = WorkingInstructionSerializer(many=True,read_only=True)
    working_instructions_count = serializers.ReadOnlyField()

    def get_errors(self,obj):
        result = {}
        result["count"] = obj.errors_count()
        result["data"] = ErrorSerializer(instance=obj.errors,many=True,read_only=True).data
        return result
    
    def get_errordata(self,obj):
        result = {}
        result["count"] = obj.errordata_count(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        result["last"] = ErrorDataSerializer(instance=obj.errordata_last(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end')),many=False,read_only=True).data
        return result
    
    def get_maintenance(self,obj):
        result = {}
        result["count"] = obj.maintenances_count()
        result["open"] = obj.maintenances_open()
        return result

    def get_processes(self,obj):
        result = {}
        result["count"] = obj.processes_count()
        result["data"] = ProcessSerializer(instance=obj.processes,many=True,read_only=True).data
        return result

    def get_processdata(self,obj):
        result = {}
        result["count"] = obj.processdata_count(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        result["last"] = ProcessDataSerializer(instance=obj.processdata_last(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end')), many=False, read_only=True).data
        result["next"] = ProcessDataSerializer(instance=obj.processdata_next(), many=False, read_only=True).data if obj.processdata_next() else None
        result["running"] = ProcessDataSerializer(instance=obj.processdata_running(), many=False, read_only=True).data if obj.processdata_running() else None
        result["status"] = obj.processdata_status()
        return result

    def get_status(self,obj):
        result = {}
        result["count"] = obj.status_count()
        result["data"] = StatusSerializer(instance=obj.status,many=True,read_only=True).data
        return result
    
    def get_statusdata(self,obj):
        result = {}
        result["count"] = obj.statusdata_count()
        result["last"] = StatusDataSerializer(instance=obj.statusdata_last(),many=False,read_only=True).data
        return result

    def get_url(self,obj):
        result = {}
        if not self.values or 'url__delete' in self.values or 'url' in self.values:
            result['delete'] = obj.url_delete()
        if not self.values or 'url__detail' in self.values or 'url' in self.values:
            result['detail'] = obj.url_detail()
        if not self.values or 'url__update' in self.values or 'url' in self.values:
            result['update'] = obj.url_update()
        if not self.values or 'url__error__overview' in self.values or 'url__error' in self.values or 'url' in self.values:
            if not result.get('error'):
                result['error'] = {}
            result['error']['overview'] = obj.url_errordata_overview()
        if not self.values or 'url__error__data_create' in self.values or 'url__error' in self.values or 'url' in self.values:
            if not result.get('error'):
                result['error'] = {}
            result['error']['data_create'] = obj.url_errordata_create()
        if not self.values or 'url__maintenance__overview' in self.values or 'url__maintenance' in self.values or 'url' in self.values:
            if not result.get('maintenance'):
                result['maintenance'] = {}
            result['maintenance']['overview'] = obj.url_maintenancedata_overview()
        if not self.values or 'url__maintenance__data_create' in self.values or 'url__maintenance' in self.values or 'url' in self.values:
            if not result.get('maintenance'):
                result['maintenance'] = {}
            result['maintenance']['data_create'] = obj.url_maintenancedata_create()
        if not self.values or 'url__process__overview' in self.values or 'url__process' in self.values or 'url' in self.values:
            if not result.get('process'):
                result['process'] = {}
            result['process']['overview'] = obj.url_processdata_overview()
        if not self.values or 'url__process__data_create' in self.values or 'url__process' in self.values or 'url' in self.values:
            if not result.get('process'):
                result['process'] = {}
            result['process']['data_create'] = obj.url_processdata_create()
        if not self.values or 'url__status__overview' in self.values or 'url__status' in self.values or 'url' in self.values:
            if not result.get('status'):
                result['status'] = {}
            result['status']['overview'] = obj.url_statusdata_overview()
        if not self.values or 'url__status__data_create' in self.values or 'url__status' in self.values or 'url' in self.values:
            if not result.get('status'):
                result['status'] = {}
            result['status']['data_create'] = obj.url_statusdata_create()
        return result

    class Meta:
        model = Device
        exclude = [
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class DeviceDetailSerializer(CreateSerializer,UpdateSerializer):

    documents = DocumentSerializer(many=True,read_only=True)
    documents_count = serializers.ReadOnlyField()

    errors = serializers.SerializerMethodField()
    errordata = serializers.SerializerMethodField()

    fabricator = CompanySerializer(source="fabricator_id",many=False,read_only=True)

    maintenances = MaintenanceSerializer(many=True, read_only=True)

    manuals = ManualSerializer(many=True,read_only=True)
    manuals_count = serializers.ReadOnlyField()

    picture = PictureSerializer(source="picture_id",many=False,read_only=True)

    processes = serializers.SerializerMethodField()
    processdata = serializers.SerializerMethodField()

    status = serializers.SerializerMethodField()
    statusdata = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    working_instructions = WorkingInstructionSerializer(many=True,read_only=True)
    working_instructions_count = serializers.ReadOnlyField()

    def get_errors(self,obj):
        result = {}
        result["count"] = obj.errors_count()
        result["data"] = ErrorSerializer(instance=obj.errors,many=True,read_only=True).data
        return result
    
    def get_errordata(self,obj):
        result = {}
        result["count"] = obj.errordata_count(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        result["data"] = ErrorDataSerializer(instance=obj.errordata(begin_datetime=self.context['request'].query_params.get('begin'), end_datetime=self.context['request'].query_params.get('end')),many=True,read_only=True).data if obj.errordata(begin_datetime=self.context['request'].query_params.get('begin'), end_datetime=self.context['request'].query_params.get('end')) else None
        result["last"] = ErrorDataSerializer(instance=obj.errordata_last(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end')),many=False,read_only=True).data
        return result

    def get_processes(self,obj):
        result = {}
        result["count"] = obj.processes_count()
        result["data"] = ProcessSerializer(instance=obj.processes,many=True,read_only=True).data
        return result

    def get_processdata(self,obj):
        result = {}
        result["count"] = obj.processdata_count(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        result["data"] = ProcessDataSerializer(instance=obj.processdata(begin_datetime=self.context['request'].query_params.get('begin'), end_datetime=self.context['request'].query_params.get('end')), many=True, read_only=True).data if obj.processdata(begin_datetime=self.context['request'].query_params.get('begin'), end_datetime=self.context['request'].query_params.get('end')) else None
        result["last"] = ProcessDataSerializer(instance=obj.processdata_last(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end')), many=False, read_only=True).data
        result["next"] = ProcessDataSerializer(instance=obj.processdata_next(), many=False, read_only=True).data if obj.processdata_next() else None
        result["running"] = ProcessDataSerializer(instance=obj.processdata_running(), many=False, read_only=True).data if obj.processdata_running() else None
        result["status"] = obj.processdata_status()
        return result

    def get_status(self,obj):
        result = {}
        result["count"] = obj.status_count()
        result["data"] = StatusSerializer(instance=obj.status,many=True,read_only=True).data
        return result
    
    def get_statusdata(self,obj):
        result = {}
        result["count"] = obj.statusdata_count(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end'))
        result["data"] = StatusDataSerializer(instance=obj.statusdata(begin_datetime=self.context['request'].query_params.get('begin'), end_datetime=self.context['request'].query_params.get('end')),many=True,read_only=True).data
        result["last"] = StatusDataSerializer(instance=obj.statusdata_last(tb=self.context['request'].query_params.get('begin'), te=self.context['request'].query_params.get('end')),many=False,read_only=True).data
        return result

    def get_url(self,obj):
        result = {}
        if not self.values or 'url__delete' in self.values or 'url' in self.values:
            result['delete'] = obj.url_delete()
        if not self.values or 'url__detail' in self.values or 'url' in self.values:
            result['detail'] = obj.url_detail()
        if not self.values or 'url__update' in self.values or 'url' in self.values:
            result['update'] = obj.url_update()
        if not self.values or 'url__error__overview' in self.values or 'url__error' in self.values or 'url' in self.values:
            if not result.get('error'):
                result['error'] = {}
            result['error']['overview'] = obj.url_errordata_overview()
        if not self.values or 'url__error__data_create' in self.values or 'url__error' in self.values or 'url' in self.values:
            if not result.get('error'):
                result['error'] = {}
            result['error']['data_create'] = obj.url_errordata_create()
        if not self.values or 'url__maintenance__overview' in self.values or 'url__maintenance' in self.values or 'url' in self.values:
            if not result.get('maintenance'):
                result['maintenance'] = {}
            result['maintenance']['overview'] = obj.url_maintenancedata_overview()
        if not self.values or 'url__maintenance__data_create' in self.values or 'url__maintenance' in self.values or 'url' in self.values:
            if not result.get('maintenance'):
                result['maintenance'] = {}
            result['maintenance']['data_create'] = obj.url_maintenancedata_create()
        if not self.values or 'url__process__overview' in self.values or 'url__process' in self.values or 'url' in self.values:
            if not result.get('process'):
                result['process'] = {}
            result['process']['overview'] = obj.url_processdata_overview()
        if not self.values or 'url__process__data_create' in self.values or 'url__process' in self.values or 'url' in self.values:
            if not result.get('process'):
                result['process'] = {}
            result['process']['data_create'] = obj.url_processdata_create()
        if not self.values or 'url__status__overview' in self.values or 'url__status' in self.values or 'url' in self.values:
            if not result.get('status'):
                result['status'] = {}
            result['status']['overview'] = obj.url_statusdata_overview()
        if not self.values or 'url__status__data_create' in self.values or 'url__status' in self.values or 'url' in self.values:
            if not result.get('status'):
                result['status'] = {}
            result['status']['data_create'] = obj.url_statusdata_create()
        return result

    class Meta:
        model = Device
        exclude = [
            'create_user_id',
            'create_datetime',
            'fabricator_id',
            'picture_id',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------