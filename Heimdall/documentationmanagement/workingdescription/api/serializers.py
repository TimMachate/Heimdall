#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.workingdescription.models import WorkingDescription
from documentationmanagement.file.models import WorkingDescriptionProxy
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
class WorkingDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingDescription
        exclude = ['id','file_id','reference_number','slug']

class WorkingDescriptionListSerializer(FileListSerializer):
    content = serializers.SerializerMethodField()

    #reference_number = serializers.SerializerMethodField()

    #slug = serializers.SerializerMethodField()

    def get_content(self,obj):
        return WorkingDescriptionSerializer(instance=obj.content(), many=False, read_only=True).data

    #def get_reference_number(self,obj):
    #    return obj.content().reference_number

    #def get_slug(self,obj):
    #    return obj.content().slug

    #def get_content(self,obj):
    #    return obj.content().content

    class Meta:
        model = WorkingDescriptionProxy
        exclude = ['create_user_id','update_user_id','create_datetime','update_datetime']

class WorkingDescriptionDetailSerializer(FileDetailSerializer):
    content = serializers.SerializerMethodField()

    #reference_number = serializers.SerializerMethodField()

    #slug = serializers.SerializerMethodField()

    def get_content(self,obj):
        return WorkingDescriptionSerializer(instance=obj.content(), many=False, read_only=True).data
    
    #def get_reference_number(self,obj):
    #    return obj.content().reference_number

    #def get_slug(self,obj):
    #    return obj.content().slug

    #def get_content(self,obj):
    #    return obj.content().content

    class Meta:
        model = WorkingDescriptionProxy
        exclude = ['create_user_id','update_user_id','create_datetime','update_datetime']
#--------------------------------------------------------------------------------