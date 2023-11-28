#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.company.models import CustomerProxy
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from relationshipmanagement.company.api.serializers import CompanyListSerializer,CompanyDetailSerializer
#--------------------------------------------------------------------------------
class CustomerListSerializer(CompanyListSerializer):

    class Meta:
        model = CustomerProxy
        exclude = [
            'create_user_id',
            'create_datetime',
            'customer',
            'supplier',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class CustomerDetailSerializer(CompanyListSerializer):

    class Meta:
        model = CustomerProxy
        exclude = [
            'create_user_id',
            'create_datetime',
            'customer',
            'supplier',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------