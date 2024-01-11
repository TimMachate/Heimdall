"""
#--------------------------------------------------------------------------------
# Serializers File from Model Request Data API
# 10.11.2023
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
from storagemanagement.requestdata.models import RequestData
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
from storagemanagement.api.serializers import (
    SupplierLinkSerializer,
    SupplierItemLinkSerializer,
    StorageItemLinkSerializer
)
#--------------------------------------------------------------------------------
class RequestDataBaseSerializer(
    CreateSerializer,
    UpdateSerializer,
    SupplierLinkSerializer,
    SupplierItemLinkSerializer,
    StorageItemLinkSerializer
):
    """
    RequestDataBaseSerializer

    Args:
        CreateSerializer (_type_): _description_
        UpdateSerializer (_type_): _description_
        SupplierLinkSerializer (_type_): _description_
        SupplierItemLinkSerializer (_type_): _description_
        StorageItemLinkSerializer (_type_): _description_
    """

    amount = serializers.ReadOnlyField()

    authorized = serializers.ReadOnlyField()
    authorized_date = serializers.ReadOnlyField()
    authorized_time = serializers.ReadOnlyField()
    authorized_username = serializers.ReadOnlyField()

    done = serializers.ReadOnlyField()

    notice = serializers.ReadOnlyField()

    price = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    unit = serializers.ReadOnlyField()

    value = serializers.ReadOnlyField()

    url_block = serializers.SerializerMethodField()

    url_authorize_true = serializers.ReadOnlyField()
    url_authorize_false = serializers.ReadOnlyField()
    url_delete = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:requestdata_delete',
        lookup_field = 'slug',
        lookup_url_kwarg = 'requestdata',
    )
    url_detail = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:requestdata_detail',
        lookup_field = 'slug',
        lookup_url_kwarg = 'requestdata',
    )
    url_offer = serializers.ReadOnlyField()
    url_qrcode = serializers.ReadOnlyField()
    url_update = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:requestdata_update',
        lookup_field = 'slug',
        lookup_url_kwarg = 'requestdata',
    )

    def get_url_block(self,obj):
        """
        get_url_block

        Args:
            obj (_type_): _description_

        Returns:
            _type_: _description_
        """
        result = {}
        result["url_delete"] = obj.url_delete()
        result["url_detail"] = obj.url_detail()
        result["url_update"] = obj.url_update()
        return result

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
        model = RequestData
        exclude = [
            'supplieritem',
            'storageitem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class RequestDataListSerializer(BaseSerializer,RequestDataBaseSerializer):
    """
    RequestDataListSerializer

    Args:
        BaseSerializer (_type_): _description_
        RequestDataBaseSerializer (_type_): _description_
    """

    class Meta:
        """
        Meta Data from Serializer
        """
        model = RequestData
        exclude = [
            'supplieritem',
            'storageitem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class RequestDataDetailSerializer(BaseSerializer,RequestDataBaseSerializer):
    """
    RequestDataDetailSerializer

    Args:
        BaseSerializer (_type_): _description_
        RequestDataBaseSerializer (_type_): _description_
    """

    class Meta:
        """
        Meta Data from Serializer
        """
        model = RequestData
        exclude = [
            'supplieritem',
            'storageitem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
