#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from structuremanagement.device.models import Device
from structuremanagement.error.models import Error,ErrorData
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id','reference_number','name','url_detail']
#--------------------------------------------------------------------------------
class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = ['id','reference_number','name','url_detail']
#--------------------------------------------------------------------------------
class ErrorDataSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    device = DeviceSerializer(source='device_id',many=False,read_only=True)

    url = serializers.SerializerMethodField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
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
        model = ErrorData
        fields = ['id','create','device','url']
#--------------------------------------------------------------------------------
class ErrorListSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    errors_count = serializers.ReadOnlyField()
    error_last = ErrorDataSerializer(many=False, read_only=True)

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
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

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ErrorListSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Error
        exclude = [
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class ErrorDetailSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    errors = ErrorDataSerializer(many=True, read_only=True)
    errors_count = serializers.ReadOnlyField()
    error_last = ErrorDataSerializer(many=False, read_only=True)

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
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

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ErrorDetailSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Error
        exclude = [
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class ErrorDataListSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    device = DeviceSerializer(source='device_id', many=False, read_only=True)

    error = ErrorSerializer(source='error_id', many=False, read_only=True)

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
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
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ErrorDataListSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = ErrorData
        exclude = [
            'create_user_id',
            'create_datetime',
            'device_id',
            'error_id',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class ErrorDataDetailSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    device = DeviceSerializer(source='device_id', many=False, read_only=True)

    error = ErrorSerializer(source='error_id', many=False, read_only=True)

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
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
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ErrorDataDetailSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = ErrorData
        exclude = [
            'create_user_id',
            'create_datetime',
            'device_id',
            'error_id',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------