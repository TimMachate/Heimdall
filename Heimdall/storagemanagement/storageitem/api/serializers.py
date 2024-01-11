"""
#--------------------------------------------------------------------------------
# Serializers File from Model Ware API
# 29.10.2023
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
from storagemanagement.booking.models import Booking
from storagemanagement.supplier.models import Supplier
from storagemanagement.supplieritem.models import SupplierItem
from storagemanagement.storage.models import Storage
from storagemanagement.storageitem.models import StorageItem
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
    SupplierItemLinkSerializer
)
from storagemanagement.booking.api.serializers import BookingBaseSerializer
from storagemanagement.supplieritem.api.serializers import SupplierItemBaseSerializer
from storagemanagement.storage.api.serializers import StorageBaseSerializer
#--------------------------------------------------------------------------------
class StorageItemBaseSerializer(
    CreateSerializer,
    UpdateSerializer
):
    """
    StorageItemBaseSerializer

    Args:
        CreateSerializer (_type_): _description_
        UpdateSerializer (_type_): _description_
        SupplierLinkSerializer (_type_): _description_
        SupplierItemLinkSerializer (_type_): _description_
    """
    booking_data = BookingBaseSerializer(
        many=True,
        read_only = True,
        fields = (
            'id',
            'create_date',
            'create_time',
            'supplier_name',
            'amount',
            'price',
            'value',
            'notice',
            'url_detail',
            'url_update',
            'url_delete',
        )
    )
    booking_count = serializers.ReadOnlyField()
    booking_last = BookingBaseSerializer(
        many=False,
        read_only=True,
        fields=(
            "id",
            "create_date",
            "create_time",
            'create_username',
            "url_detail"
        )
    )

    maximum = serializers.ReadOnlyField()

    minimum = serializers.ReadOnlyField()

    name = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    status = serializers.ReadOnlyField()

    stock_data = StorageBaseSerializer(
        many = True,
        read_only = True,
        fields = (
            'id',
            'create_date',
            'create_time',
            'supplier_name',
            'value',
            'notice',
            'url_detail',
            'url_update',
            'url_delete',
            'url_unload',
        )
    )
    stock_count = serializers.ReadOnlyField()
    stock_percentage = serializers.ReadOnlyField()
    stock_value = serializers.ReadOnlyField()

    supplier_id = serializers.ReadOnlyField()
    supplier_name = serializers.ReadOnlyField()
    supplier_reference_number = serializers.ReadOnlyField()
    supplier_slug = serializers.ReadOnlyField()
    supplier_url_detail = serializers.ReadOnlyField()

    supplieritem_data = SupplierItemBaseSerializer(
        many = True,
        read_only = True,
        fields=(
            'id',
            'name',
            'item_number',
            'price',
            'unit',
            'url_detail',
            'url_request_create',
        )
    )
    supplieritem_count = serializers.ReadOnlyField()
    supplieritem_id = serializers.ReadOnlyField()
    supplieritem_name = serializers.ReadOnlyField()
    supplieritem_item_number = serializers.ReadOnlyField()
    supplieritem_reference_number = serializers.ReadOnlyField()
    supplieritem_slug = serializers.ReadOnlyField()
    supplieritem_url_detail = serializers.ReadOnlyField()

    url_block = serializers.SerializerMethodField()
    url_booking = serializers.SerializerMethodField()
    url_booking_add = serializers.ReadOnlyField()
    url_booking_create = serializers.ReadOnlyField()
    url_booking_create_add_remove = serializers.ReadOnlyField()
    url_booking_remove = serializers.ReadOnlyField()
    url_delete = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:storageitem_delete',
        lookup_field = 'slug',
        lookup_url_kwarg = 'storageitem',
    )
    url_detail = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:storageitem_detail',
        lookup_field = 'slug',
        lookup_url_kwarg = 'storageitem',
    )
    url_qrcode = serializers.ReadOnlyField()
    url_qrcode_booking_add = serializers.ReadOnlyField()
    url_qrcode_booking_remove = serializers.ReadOnlyField()
    url_qrcode_request = serializers.ReadOnlyField()
    url_request_create = serializers.ReadOnlyField()
    url_update = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:storageitem_update',
        lookup_field = 'slug',
        lookup_url_kwarg = 'storageitem',
    )

    warning = serializers.ReadOnlyField()

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
    
    def get_url_booking(self,obj):
        """
        get_url_block

        Args:
            obj (_type_): _description_

        Returns:
            _type_: _description_
        """
        result = {}
        result["url_booking_remove"] = obj.url_delete()
        result["url_booking_add"] = obj.url_detail()
        return result

    class Meta:
        """
        Meta Data from Serializer
        """
        model = StorageItem
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------
class StorageItemDetailSerializer(BaseSerializer,StorageItemBaseSerializer):
    """
    StorageItemDetailSerializer

    Args:
        BaseSerializer (_type_): _description_
        StorageItemBaseSerializer (_type_): _description_
    """

    booking_last = None

    class Meta:
        """
        Meta Data from Serializer
        """
        model = StorageItem
        exclude = (
            'create_user_id',
            'create_datetime',
            'supplieritem',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------
class StorageItemListSerializer(BaseSerializer,StorageItemBaseSerializer):
    """
    StorageItemListSerializer

    Args:
        BaseSerializer (_type_): _description_
        StorageItemBaseSerializer (_type_): _description_
    """

    booking_data = None

    stock_data = None

    supplier_data = None

    supplieritem_data = None

    class Meta:
        """
        Meta Data from Serializer
        """
        model = StorageItem
        exclude = (
            'create_user_id',
            'create_datetime',
            'supplieritem',
            'supplieritem_data',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------
