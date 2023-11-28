#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers

import json
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.protocol.models import Protocol, ProtocolData, ProtocolStep, Variable
from documentationmanagement.file.models import File, ProtocolProxy
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from documentationmanagement.file.api.serializers import FileListSerializer, FileDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
class VariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variable
        fields = ('id','name','symbol','unit')
#--------------------------------------------------------------------------------
class ProtocolStepSerializer(serializers.ModelSerializer):

    variables = VariableSerializer(many=True,read_only=True)

    class Meta:
        model = ProtocolStep
        exclude = ['protocol_id']
#--------------------------------------------------------------------------------
class ProtocolDataSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id if obj.create_user_id else None
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username() if obj.create_user_id else None
        return result
    
    def get_url(self,obj):
        result = {}
        result["delete"] = obj.url_delete()
        result["detail"] = obj.url_detail()
        result["update"] = obj.url_update()
        return result

    class Meta:
        model = ProtocolData
        exclude = ['create_datetime','create_user_id','protocol_id','slug','update_datetime','update_user_id',]
#--------------------------------------------------------------------------------
class ProtocolProxySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProtocolProxy
        fields = ['id','reference_number','name','url_detail']
#--------------------------------------------------------------------------------
class ProtocolListSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    data_last = ProtocolDataSerializer(many=False,read_only=True)

    file = ProtocolProxySerializer(source='file_id',many=False,read_only=True)

    keywords = serializers.SerializerMethodField()

    name = serializers.ReadOnlyField()

    steps_count = serializers.ReadOnlyField()

    type = serializers.ReadOnlyField()

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    version = serializers.ReadOnlyField()

    def get_create(self,obj):
        if obj.file_id:
            result = {}
            result["id"] = obj.file_id.create_user_id.id if obj.file_id.create_user_id else None
            result["date"] = obj.file_id.create_date()
            result["datetime"] = obj.file_id.create_datetime
            result["datetime_formated"] = obj.file_id.create_datetime_formated()
            result["time"] = obj.file_id.create_time()
            result["username"] = obj.file_id.create_username() if obj.file_id.create_user_id else None
        else:
            result = None
        return result

    def get_keywords(self,obj):
        return obj.file_id.keywords if obj.file_id else None

    def get_steps(self,obj):
        result = ProtocolStepSerializer(instance=obj.steps(),many=True,read_only=True).data

    def get_update(self,obj):
        if obj.file_id:
            result = {}
            result["id"] = obj.file_id.update_user_id.id if obj.file_id.update_user_id else None
            result["date"] = obj.file_id.update_date()
            result["datetime"] = obj.file_id.update_datetime
            result["datetime_formated"] = obj.file_id.update_datetime_formated()
            result["time"] = obj.file_id.update_time()
            result["username"] = obj.file_id.update_username() if obj.file_id.update_user_id else None
        else:
            result = None
        return result

    def get_url(self,obj):
        result = {}
        result["data_create"] = obj.url_data_create()
        result["delete"] = obj.url_delete()
        result["detail"] = obj.url_detail()
        result["file"] = obj.file_id.url_file()
        result["update"] = obj.url_update()
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ProtocolListSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Protocol
        exclude = ['file_id']
#--------------------------------------------------------------------------------
class ProtocolDetailSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    data = ProtocolDataSerializer(many=True,read_only=True)
    data_last = ProtocolDataSerializer(many=False,read_only=True)

    file = ProtocolProxySerializer(source='file_id',many=False,read_only=True)

    keywords = serializers.SerializerMethodField()

    steps_count = serializers.ReadOnlyField()
    steps = ProtocolStepSerializer(many=True,read_only=True)

    type = serializers.ReadOnlyField()

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    version = serializers.ReadOnlyField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.file_id.create_user_id.id if obj.file_id.create_user_id else None
        result["date"] = obj.file_id.create_date()
        result["datetime"] = obj.file_id.create_datetime
        result["datetime_formated"] = obj.file_id.create_datetime_formated()
        result["time"] = obj.file_id.create_time()
        result["username"] = obj.file_id.create_username() if obj.file_id.create_user_id else None
        return result

    def get_keywords(self,obj):
        return obj.file_id.keywords if obj.file_id else None

    def get_steps(self,obj):
        result = ProtocolStepSerializer(instance=obj.steps(),many=True,read_only=True).data

    def get_update(self,obj):
        result = {}
        result["id"] = obj.file_id.update_user_id.id if obj.file_id.update_user_id else None
        result["date"] = obj.file_id.update_date()
        result["datetime"] = obj.file_id.update_datetime
        result["datetime_formated"] = obj.file_id.update_datetime_formated()
        result["time"] = obj.file_id.update_time()
        result["username"] = obj.file_id.update_username() if obj.file_id.update_user_id else None
        return result

    def get_url(self,obj):
        result = {}
        result["data_create"] = obj.url_data_create()
        result["delete"] = obj.url_delete()
        result["detail"] = obj.url_detail()
        result["file"] = obj.file_id.url_file()
        result["update"] = obj.url_update()
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ProtocolDetailSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Protocol
        exclude = ['file_id']
#--------------------------------------------------------------------------------
class ProtocolDataListSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    protocol = ProtocolProxySerializer(source='protocol_id',many=False,read_only=True)

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id if obj.create_user_id else None
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username() if obj.create_user_id else None
        return result

    def get_update(self,obj):
        result = {}
        result["id"] = obj.update_user_id.id if obj.update_user_id else None
        result["date"] = obj.update_date()
        result["datetime"] = obj.update_datetime
        result["datetime_formated"] = obj.update_datetime_formated()
        result["time"] = obj.update_time()
        result["username"] = obj.update_username() if obj.update_user_id else None
        return result
    
    def get_url(self,obj):
        result = {}
        result["url_delete"] = obj.url_delete()
        result["url_detail"] = obj.url_detail()
        result["url_update"] = obj.url_update()
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ProtocolDataListSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = ProtocolData
        exclude = ['create_datetime','create_user_id','protocol_id','update_datetime','update_user_id']
#--------------------------------------------------------------------------------
class ProtocolDataDetailSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    procedure = serializers.SerializerMethodField()

    protocol = ProtocolProxySerializer(source='protocol_id',many=False,read_only=True)

    result = serializers.SerializerMethodField()

    steps = serializers.SerializerMethodField()

    topic = serializers.SerializerMethodField()

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id if obj.create_user_id else None
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username() if obj.create_user_id else None
        return result

    def get_procedure(self,obj):
        result = obj.protocol_id.procedure
        return result

    def get_result(self,obj):
        if obj.json:
            result = {}
            j=json.loads(obj.json)
            for variable in j:
                var = Variable.objects.get(id=variable.split('-')[1])
                ps = ProtocolStep.objects.get(id=variable.split('-')[0]).name
                if not ps in result:
                    result[ps] = {}
                if not var.name in result[ps]:
                    result[ps][var.name] = {}
                result[ps][var.name]['id'] = var.id
                result[ps][var.name]['symbol'] = var.symbol
                result[ps][var.name]['unit'] = var.unit
                result[ps][var.name]['value'] = j[variable] if j[variable] else None
        else:
            result = None
        return result

    def get_steps(self,obj):
        result = ProtocolStepSerializer(instance=ProtocolStep.objects.filter(protocol_id=obj.protocol_id),many=True,read_only=True).data
        for step in result:
            for variable in step["variables"]:
                if obj.results():
                    if str(step["id"])+'-'+str(variable["id"]) in obj.results():
                        variable["value"]=obj.results()[str(step["id"])+'-'+str(variable["id"])]
                else:
                    variable["value"] = None
        return result

    def get_topic(self,obj):
        result = obj.protocol_id.topic
        return result

    def get_update(self,obj):
        result = {}
        result["id"] = obj.update_user_id.id if obj.update_user_id else None
        result["date"] = obj.update_date()
        result["datetime"] = obj.update_datetime
        result["datetime_formated"] = obj.update_datetime_formated()
        result["time"] = obj.update_time()
        result["username"] = obj.update_username() if obj.update_user_id else None
        return result

    def get_url(self,obj):
        result = {}
        result["url_delete"] = obj.url_delete()
        result["url_detail"] = obj.url_detail()
        result["url_update"] = obj.url_update()
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ProtocolDataDetailSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = ProtocolData
        exclude = ['create_datetime','create_user_id','update_datetime','update_user_id']
#--------------------------------------------------------------------------------
class VariableListSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    input_type = serializers.SerializerMethodField()

    update = serializers.SerializerMethodField()

    url_delete = serializers.ReadOnlyField()
    url_detail = serializers.ReadOnlyField()
    url_update = serializers.ReadOnlyField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id if obj.create_user_id else None
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username() if obj.create_user_id else None
        return result

    def get_input_type(self,obj):
        return obj.InputTypes(obj.input_type).label

    def get_update(self,obj):
        result = {}
        result["id"] = obj.update_user_id.id if obj.update_user_id else None
        result["date"] = obj.update_date()
        result["datetime"] = obj.update_datetime
        result["datetime_formated"] = obj.update_datetime_formated()
        result["time"] = obj.update_time()
        result["username"] = obj.update_username() if obj.update_user_id else None
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(VariableListSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Variable
        exclude = ['create_user_id','update_user_id','create_datetime','update_datetime']
#--------------------------------------------------------------------------------
class VariableDetailSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    input_type = serializers.SerializerMethodField()

    update = serializers.SerializerMethodField()

    url_delete = serializers.ReadOnlyField()
    url_detail = serializers.ReadOnlyField()
    url_update = serializers.ReadOnlyField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id if obj.create_user_id else None
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username() if obj.create_user_id else None
        return result

    def get_input_type(self,obj):
        return obj.InputTypes(obj.input_type).label

    def get_update(self,obj):
        result = {}
        result["id"] = obj.update_user_id.id if obj.update_user_id else None
        result["date"] = obj.update_date()
        result["datetime"] = obj.update_datetime
        result["datetime_formated"] = obj.update_datetime_formated()
        result["time"] = obj.update_time()
        result["username"] = obj.update_username() if obj.update_user_id else None
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(VariableDetailSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Variable
        exclude = ['create_user_id','update_user_id','create_datetime','update_datetime']
#--------------------------------------------------------------------------------