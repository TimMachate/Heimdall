"""
#--------------------------------------------------------------------------------
# Serializers File from Model Company API
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
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.company.models import Company
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from relationshipmanagement.api.serializers import (
    BaseSerializer,
    CreateSerializer,
    UpdateSerializer
)
from relationshipmanagement.companycontact.api.serializers import CompanyContactBaseSerializer
from relationshipmanagement.companyitem.api.serializers import CompanyItemBaseSerializer
#--------------------------------------------------------------------------------
class CompanyBaseSerializer(CreateSerializer,UpdateSerializer):
    """
    CompanyBaseSerializer

    Args:
        CreateSerializer (_type_): add create fields
        UpdateSerializer (_type_): add update fields
    """

    city = serializers.ReadOnlyField()

    companycontact_data = None
    companycontact_count = serializers.ReadOnlyField()

    companyitem_data = None
    companyitem_count = serializers.ReadOnlyField()

    country = serializers.ReadOnlyField()

    email = serializers.ReadOnlyField()

    house_number = serializers.ReadOnlyField()

    logo_name = serializers.ReadOnlyField()
    logo_url = serializers.ReadOnlyField()

    name = serializers.ReadOnlyField()

    notice = serializers.ReadOnlyField()

    post_code = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    street = serializers.ReadOnlyField()

    supplier = serializers.ReadOnlyField()

    telephone = serializers.ReadOnlyField()

    url_delete = serializers.HyperlinkedIdentityField(
        view_name = 'relationshipmanagement:company_delete',
        lookup_field = 'slug',
        lookup_url_kwarg = 'company',
    )
    url_detail = serializers.HyperlinkedIdentityField(
        view_name = 'relationshipmanagement:company_detail',
        lookup_field = 'slug',
        lookup_url_kwarg = 'company',
    )
    url_qrcode = serializers.ReadOnlyField()
    url_update = serializers.HyperlinkedIdentityField(
        view_name = 'relationshipmanagement:company_update',
        lookup_field = 'slug',
        lookup_url_kwarg = 'company',
    )

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        """
        Meta Data from Serializer
        """
        model = Company
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class CompanyDetailSerializer(BaseSerializer,CompanyBaseSerializer):
    """
    CompanyDetailSerializer

    Args:
        BaseSerializer (_type_): add field choice
        CompanyBaseSerializer (_type_): add CompanyBaseSerializer fields
    """

    companycontact_data = CompanyContactBaseSerializer(
        source="companycontacts",
        many=True,
        read_only=True,
        fields=(
            'id',
            'name',
            'telephone_data',
            'email_data',
            'url_detail',
            'url_delete',
            'url_update'
        )
    )

    companyitem_data = CompanyItemBaseSerializer(
        source="companyitems",
        many=True,
        read_only=True,
        fields=(
            'id',
            'name',
            'item_number',
            'unit',
            'price',
            'url_detail',
            'url_delete',
            'url_update'
        )
    )

    class Meta:
        """
        Meta Data from Serializer
        """
        model = Company
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class CompanyListSerializer(BaseSerializer,CompanyBaseSerializer):
    """
    CompanyListSerializer

    Args:
        BaseSerializer (_type_): add field choice
        CompanyBaseSerializer (_type_): add CompanyBaseSerializer fields
    """

    class Meta:
        """
        Meta Data from Serializer
        """
        model = Company
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
