"""
#--------------------------------------------------------------------------------
# serializers File from App Relationshipmanagement API
# 16.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from tools.api.serializers import (
    BaseSerializer,
    CreateSerializer,
    UpdateSerializer
    )
class CompanyLinkSerializer(serializers.ModelSerializer):
    """ CompanyLinkSerializer contains all fields for info of a company object"""
    company_id = serializers.ReadOnlyField()
    company_name = serializers.ReadOnlyField()
    company_reference_number = serializers.ReadOnlyField()
    company_slug = serializers.ReadOnlyField()
    company_url_detail = serializers.ReadOnlyField()
#--------------------------------------------------------------------------------
class CompanyContactLinkSerializer(serializers.ModelSerializer):
    """ CompanyContactLinkSerializer contains all fields for info of a company contact object"""
    companycontact_id = serializers.ReadOnlyField()
    companycontact_name = serializers.ReadOnlyField()
    companycontact_reference_number = serializers.ReadOnlyField()
    companycontact_slug = serializers.ReadOnlyField()
    companycontact_url_detail = serializers.ReadOnlyField()
#--------------------------------------------------------------------------------

class CompanyItemLinkSerializer(serializers.ModelSerializer):
    """ CompanyItemLinkSerializer contains all fields for info of a company item object"""
    companyitem_id = serializers.ReadOnlyField()
    companyitem_name = serializers.ReadOnlyField()
    companyitem_item_number = serializers.ReadOnlyField()
    companyitem_reference_number = serializers.ReadOnlyField()
    companyitem_slug = serializers.ReadOnlyField()
    companyitem_url_detail = serializers.ReadOnlyField()
#--------------------------------------------------------------------------------
