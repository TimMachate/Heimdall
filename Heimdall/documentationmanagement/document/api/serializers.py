#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.document.models import Document
from documentationmanagement.file.models import DocumentProxy
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
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        exclude = ['id','file_id','reference_number','slug']

class DocumentListSerializer(FileListSerializer):
    content = serializers.SerializerMethodField()

    #reference_number = serializers.SerializerMethodField()

    #slug = serializers.SerializerMethodField()

    def get_content(self,obj):
        return DocumentSerializer(instance=obj.content(), many=False, read_only=True).data

    #def get_reference_number(self,obj):
    #    return obj.content().reference_number

    #def get_slug(self,obj):
    #    return obj.content().slug

    #def get_content(self,obj):
    #    return obj.content().content

    class Meta:
        model = DocumentProxy
        exclude = ['create_user_id','update_user_id','create_datetime','update_datetime']

class DocumentDetailSerializer(FileDetailSerializer):
    content = serializers.SerializerMethodField()

    #reference_number = serializers.SerializerMethodField()

    #slug = serializers.SerializerMethodField()

    def get_content(self,obj):
        return DocumentSerializer(instance=obj.content(), many=False, read_only=True).data
    
    #def get_reference_number(self,obj):
    #    return obj.content().reference_number

    #def get_slug(self,obj):
    #    return obj.content().slug

    #def get_content(self,obj):
    #    return obj.content().content

    class Meta:
        model = DocumentProxy
        exclude = ['create_user_id','update_user_id','create_datetime','update_datetime']
#--------------------------------------------------------------------------------