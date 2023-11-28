#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.company.models import Company
from relationshipmanagement.ware.models import Ware
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
class WareListSerializer(CreateSerializer,UpdateSerializer):

    company = CompanySerializer(source='company_id',many=False,read_only=True)

    url = serializers.SerializerMethodField()

    def get_url(self,obj):
        result = {}
        if not self.values or 'url__delete' in self.values or 'url' in self.values:
            result['delete'] = obj.url_delete()
        if not self.values or 'url__detail' in self.values or 'url' in self.values:
            result['detail'] = obj.url_detail()
        if not self.values or 'url__update' in self.values or 'url' in self.values:
            result['update'] = obj.url_update()
        return result

    class Meta:
        model = Ware
        exclude = [
            'company_id',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class WareDetailSerializer(CreateSerializer,UpdateSerializer):

    company = CompanySerializer(source='company_id',many=False,read_only=True)

    url = serializers.SerializerMethodField()

    def get_url(self,obj):
        result = {}
        if not self.values or 'url__delete' in self.values or 'url' in self.values:
            result['delete'] = obj.url_delete()
        if not self.values or 'url__detail' in self.values or 'url' in self.values:
            result['detail'] = obj.url_detail()
        if not self.values or 'url__update' in self.values or 'url' in self.values:
            result['update'] = obj.url_update()
        return result

    class Meta:
        model = Ware
        exclude = [
            'company_id',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------