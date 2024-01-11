"""
#--------------------------------------------------------------------------------
# Serializers File from Model CompanyItem API
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
from relationshipmanagement.companyitem.models import CompanyItem
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from relationshipmanagement.api.serializers import (
    BaseSerializer,
    CreateSerializer,
    UpdateSerializer,
    CompanyLinkSerializer,
)
#--------------------------------------------------------------------------------
class CompanyItemBaseSerializer(
    CreateSerializer,
    UpdateSerializer,
    CompanyLinkSerializer,
):
    """
    CompanyItemBaseSerializer

    Args:
        CreateSerializer (_type_): _description_
        UpdateSerializer (_type_): _description_
        CompanyLinkSerializer (_type_): _description_
    """

    item_number = serializers.ReadOnlyField()

    image_name = serializers.ReadOnlyField()
    image_url = serializers.ReadOnlyField()

    name = serializers.ReadOnlyField()

    price = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    unit = serializers.ReadOnlyField()

    url_delete = serializers.HyperlinkedIdentityField(
        view_name = 'relationshipmanagement:companyitem_delete',
        lookup_field = 'slug',
        lookup_url_kwarg = 'companyitem',
    )
    url_detail = serializers.HyperlinkedIdentityField(
        view_name = 'relationshipmanagement:companyitem_detail',
        lookup_field = 'slug',
        lookup_url_kwarg = 'companyitem',
    )
    url_qrcode = serializers.ReadOnlyField()
    url_request_create = serializers.ReadOnlyField()
    url_update = serializers.HyperlinkedIdentityField(
        view_name = 'relationshipmanagement:companyitem_update',
        lookup_field = 'slug',
        lookup_url_kwarg = 'companyitem',
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
        contains all Meta data of the serializer
        """
        model = CompanyItem
        exclude = (
            'company',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class CompanyItemDetailSerializer(BaseSerializer,CompanyItemBaseSerializer):
    """
    CompanyItemDetailSerializer

    Args:
        BaseSerializer (_type_): _description_
        CompanyItemBaseSerializer (_type_): _description_
    """

    class Meta:
        """
        contains all Meta data of the serializer
        """
        model = CompanyItem
        exclude = (
            'company',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class CompanyItemListSerializer(BaseSerializer,CompanyItemBaseSerializer):
    """
    CompanyItemListSerializer

    Args:
        BaseSerializer (_type_): _description_
        CompanyItemBaseSerializer (_type_): _description_
    """

    class Meta:
        """
        contains all Meta data of the serializer
        """
        model = CompanyItem
        exclude = (
            'company',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
