#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.file.models import File
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
class FileSerializer(serializers.ModelSerializer):

    count = serializers.SerializerMethodField()

    name = serializers.SerializerMethodField()

    url_detail = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(FileSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = File
        fields = [
            'count',
            'name',
            'url_detail',
        ]

class FileListSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    type = serializers.SerializerMethodField()

    update = serializers.SerializerMethodField()

    url_delete = serializers.ReadOnlyField()
    url_detail = serializers.ReadOnlyField()
    url_file = serializers.ReadOnlyField()
    url_file_qrcode = serializers.ReadOnlyField()
    url_update = serializers.ReadOnlyField()

    version = serializers.ReadOnlyField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id if obj.create_user_id else None
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username() if obj.create_user_id else None
        return result

    def get_type(self,obj):
        return obj.Types(obj.type).label

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
        super(FileListSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = File
        exclude = [
            'create_datetime',
            'create_user_id',
            'file',
            'qrcode_detail',
            'update_datetime',
            'update_user_id',
            'version_prefix',
            'version_suffix'
        ]
#--------------------------------------------------------------------------------
class FileDetailSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    type = serializers.SerializerMethodField()

    update = serializers.SerializerMethodField()

    url_delete = serializers.ReadOnlyField()
    url_detail = serializers.ReadOnlyField()
    url_file = serializers.ReadOnlyField()
    url_file_qrcode = serializers.ReadOnlyField()
    url_update = serializers.ReadOnlyField()

    version = serializers.ReadOnlyField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id if obj.create_user_id else None
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username() if obj.create_user_id else None
        return result

    def get_type(self,obj):
        return obj.Types(obj.type).label
    
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
        super(FileDetailSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = File
        exclude = [
            'create_user_id',
            'create_datetime',
            'file',
            'qrcode_detail',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------