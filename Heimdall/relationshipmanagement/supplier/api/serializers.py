#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.company.models import SupplierProxy
from relationshipmanagement.ware.models import Ware
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from relationshipmanagement.company.api.serializers import CompanyListSerializer,CompanyDetailSerializer
#--------------------------------------------------------------------------------
class WareSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField()

    def get_url(self,obj):
        result = {}
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    class Meta:
        model = Ware
        fields = ['id','name','ware_number','unit_package','unit','price','url']
#--------------------------------------------------------------------------------
class SupplierListSerializer(CompanyListSerializer):

    wares = serializers.SerializerMethodField()

    def get_wares(self,obj):
        result = {}
        result["count"] = obj.wares().count()
        result["data"] = WareSerializer(instance=obj.wares(),many=True,read_only=True).data
        return result

    class Meta:
        model = SupplierProxy
        exclude = [
            'create_user_id',
            'create_datetime',
            'customer',
            'supplier',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class SupplierDetailSerializer(CompanyListSerializer):

    wares = serializers.SerializerMethodField()

    def get_wares(self,obj):
        result = {}
        result["count"] = obj.wares().count()
        result["data"] = WareSerializer(instance=obj.wares(),many=True,read_only=True).data
        return result

    class Meta:
        model = SupplierProxy
        exclude = [
            'create_user_id',
            'create_datetime',
            'customer',
            'supplier',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------