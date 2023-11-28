#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.company.models import GeneralProxy
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from relationshipmanagement.company.api.serializers import CompanyListSerializer,CompanyDetailSerializer
#--------------------------------------------------------------------------------
class GeneralListSerializer(CompanyListSerializer):

    class Meta:
        model = GeneralProxy
        exclude = [
            'create_user_id',
            'create_datetime',
            'customer',
            'supplier',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class GeneralDetailSerializer(CompanyListSerializer):

    class Meta:
        model = GeneralProxy
        exclude = [
            'create_user_id',
            'create_datetime',
            'customer',
            'supplier',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------