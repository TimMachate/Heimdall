"""
#--------------------------------------------------------------------------------
# Serializers File from Model SupplierItem API
# 27.10.2023
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
from storagemanagement.supplieritem.models import SupplierItem
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
from storagemanagement.booking.api.serializers import BookingBaseSerializer
from storagemanagement.storage.api.serializers import StorageBaseSerializer
#--------------------------------------------------------------------------------
class SupplierItemBaseSerializer(
    CreateSerializer,
    UpdateSerializer
):
    """
    SupplierItemBaseSerializer

    Args:
        CreateSerializer (_type_): _description_
        UpdateSerializer (_type_): _description_
        SupplierLinkSerializer (_type_): _description_
        StorageItemLinkSerializer (_type_): _description_
    """
    booking_data = None
    booking_count = serializers.ReadOnlyField()
    booking_last = BookingBaseSerializer(many=False, read_only=True)

    item_number = serializers.ReadOnlyField()

    name = serializers.ReadOnlyField()

    price = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    stock_data = None
    stock_count = serializers.ReadOnlyField()
    stock_value = serializers.ReadOnlyField()

    #storageitem_id = serializers.ReadOnlyField()
    #storageitem_name = serializers.ReadOnlyField()
    #storageitem_reference_number = serializers.ReadOnlyField()
    #storageitem_slug = serializers.ReadOnlyField()
    #storageitem_url_detail = serializers.ReadOnlyField()

    supplier_id = serializers.ReadOnlyField()
    supplier_name = serializers.ReadOnlyField()
    supplier_reference_number = serializers.ReadOnlyField()
    supplier_slug = serializers.ReadOnlyField()
    supplier_url_detail = serializers.ReadOnlyField()

    unit = serializers.ReadOnlyField()

    url_block = serializers.SerializerMethodField()

    url_booking_add = serializers.ReadOnlyField()
    url_booking_create = serializers.ReadOnlyField()
    url_booking_remove = serializers.ReadOnlyField()
    url_delete = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:supplieritem_delete',
        lookup_field = 'slug',
        lookup_url_kwarg = 'supplieritem',
    )
    url_detail = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:supplieritem_detail',
        lookup_field = 'slug',
        lookup_url_kwarg = 'supplieritem',
    )
    url_qrcode = serializers.ReadOnlyField()
    url_qrcode_booking_add = serializers.ReadOnlyField()
    url_qrcode_booking_create = serializers.ReadOnlyField()
    url_qrcode_booking_remove = serializers.ReadOnlyField()
    url_qrcode_request = serializers.ReadOnlyField()
    url_request_create = serializers.ReadOnlyField()
    url_update = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:supplieritem_update',
        lookup_field = 'slug',
        lookup_url_kwarg = 'supplieritem',
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
        contains all Meta data of the serializer
        """
        model = SupplierItem
        exclude = (
            'company',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class SupplierItemDetailSerializer(BaseSerializer,SupplierItemBaseSerializer):
    """
    SupplierItemDetailSerializer

    Args:
        BaseSerializer (_type_): _description_
        SupplierItemBaseSerializer (_type_): _description_
    """

    booking_data = BookingBaseSerializer(
        source="booking",
        many=True,
        read_only=True,
        fields=(
            "id",
            "create_date",
            "create_time",
            "create_username",
            "amount",
            "price",
            "value",
            "notice",
            "url_detail",
        )
    )

    stock_data = StorageBaseSerializer(
        source="stock",
        many=True,
        read_only=True,
        fields=(
            "id",
            "create_date",
            "create_time",
            "value",
            "notice",
            "url_detail",
            "url_unload"
        )
    )

    class Meta:
        """
        contains all Meta data of the serializer
        """
        model = SupplierItem
        exclude = (
            'company',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class SupplierItemListSerializer(BaseSerializer,SupplierItemBaseSerializer):
    """
    SupplierItemListSerializer

    Args:
        BaseSerializer (_type_): _description_
        SupplierItemBaseSerializer (_type_): _description_
    """

    class Meta:
        """
        contains all Meta data of the serializer
        """
        model = SupplierItem
        exclude = (
            'company',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
