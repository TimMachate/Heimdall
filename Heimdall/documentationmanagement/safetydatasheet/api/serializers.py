#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.safetydatasheet.models import SafetyDataSheet
from documentationmanagement.file.models import SafetyDataSheetProxy
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
class SafetyDataSheetSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    termination = serializers.ReadOnlyField()
    class Meta:
        model = SafetyDataSheet
        exclude = ['id','file_id','reference_number','slug']

class SafetyDataSheetListSerializer(FileListSerializer):
    content = serializers.SerializerMethodField()

    #reference_number = serializers.SerializerMethodField()

    #slug = serializers.SerializerMethodField()

    def get_content(self,obj):
        return SafetyDataSheetSerializer(instance=obj.content(), many=False, read_only=True).data

    #def get_reference_number(self,obj):
    #    return obj.content().reference_number

    #def get_slug(self,obj):
    #    return obj.content().slug

    #def get_content(self,obj):
    #    return obj.content().content

    class Meta:
        model = SafetyDataSheetProxy
        exclude = ['create_user_id','update_user_id','create_datetime','update_datetime']

class SafetyDataSheetDetailSerializer(FileDetailSerializer):
    content = serializers.SerializerMethodField()

    #reference_number = serializers.SerializerMethodField()

    #slug = serializers.SerializerMethodField()

    def get_content(self,obj):
        return SafetyDataSheetSerializer(instance=obj.content(), many=False, read_only=True).data
    
    #def get_reference_number(self,obj):
    #    return obj.content().reference_number

    #def get_slug(self,obj):
    #    return obj.content().slug

    #def get_content(self,obj):
    #    return obj.content().content

    class Meta:
        model = SafetyDataSheetProxy
        exclude = ['create_user_id','update_user_id','create_datetime','update_datetime']
#--------------------------------------------------------------------------------