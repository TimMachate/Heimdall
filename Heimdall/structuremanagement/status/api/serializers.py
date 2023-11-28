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
from structuremanagement.status.models import Status,StatusData
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id','reference_number', 'name', 'url_detail']
#--------------------------------------------------------------------------------
class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['id','reference_number','name','url_detail']
#--------------------------------------------------------------------------------
class StatusDataSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    device = DeviceSerializer(source="device_id",many=False, read_only=True)

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
        model = Status
        fields = ['id','create','device','url']
#--------------------------------------------------------------------------------
class StatusListSerializer(serializers.ModelSerializer):

    background_color = serializers.SerializerMethodField()

    create = serializers.SerializerMethodField()

    stati_last = StatusDataSerializer(many=False,read_only=True)

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

    def get_background_color(self,obj):
        result = {}
        result["value"] = obj.rgba_value()
        result["style"] = obj.rgba_style()
        result["red"] = obj.rgba_red
        result["green"] = obj.rgba_green
        result["blue"] = obj.rgba_blue
        result["alpha"] = obj.rgba_alpha
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
        super(StatusListSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Status
        exclude = [
            'create_user_id',
            'create_datetime',
            'rgba_red',
            'rgba_green',
            'rgba_blue',
            'rgba_alpha',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class StatusDetailSerializer(serializers.ModelSerializer):

    background_color = serializers.SerializerMethodField()

    create = serializers.SerializerMethodField()

    stati = StatusDataSerializer(many=True,read_only=True)
    stati_count = serializers.ReadOnlyField()

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

    def get_background_color(self,obj):
        result = {}
        result["value"] = obj.rgba_value()
        result["style"] = obj.rgba_style()
        result["red"] = obj.rgba_red
        result["green"] = obj.rgba_green
        result["blue"] = obj.rgba_blue
        result["alpha"] = obj.rgba_alpha
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
        super(StatusDetailSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Status
        exclude = [
            'create_user_id',
            'create_datetime',
            'rgba_red',
            'rgba_green',
            'rgba_blue',
            'rgba_alpha',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class StatusDataListSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    device = DeviceSerializer(source='device_id', many=False, read_only=True)

    status = StatusSerializer(source='status_id', many=False, read_only=True)

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
        super(StatusDataListSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = StatusData
        exclude = [
            'create_user_id',
            'create_datetime',
            'device_id',
            'status_id',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class StatusDataDetailSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    device = DeviceSerializer(source='device_id', many=False, read_only=True)

    status = StatusSerializer(source='status_id', many=False, read_only=True)

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
        super(StatusDataDetailSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = StatusData
        exclude = [
            'create_user_id',
            'create_datetime',
            'device_id',
            'status_id',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------