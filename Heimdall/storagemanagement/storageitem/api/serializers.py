#--------------------------------------------------------------------------------
# Serializers File from Model Ware API
# 29.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

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
from storagemanagement.company.models import Company
from storagemanagement.companyitem.models import CompanyItem
from storagemanagement.storage.models import Storage
from storagemanagement.storageitem.models import StorageItem
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from storagemanagement.api.serializers import BaseSerializer,CreateSerializer,UpdateSerializer
from storagemanagement.booking.api.serializers import BookingBaseSerializer
from storagemanagement.companyitem.api.serializers import CompanyItemBaseSerializer
from storagemanagement.storage.api.serializers import StorageBaseSerializer
#--------------------------------------------------------------------------------
class StorageItemBaseSerializer(CreateSerializer,UpdateSerializer):

    booking_data = None
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

    company_id = serializers.ReadOnlyField()
    company_name = serializers.ReadOnlyField()
    company_reference_number = serializers.ReadOnlyField()
    company_slug = serializers.ReadOnlyField()
    company_url_detail = serializers.ReadOnlyField()

    companyitem_id = serializers.ReadOnlyField()
    companyitem_item_number = serializers.ReadOnlyField()
    companyitem_name = serializers.ReadOnlyField()
    companyitem_reference_number = serializers.ReadOnlyField()
    companyitem_slug = serializers.ReadOnlyField()
    companyitem_url_detail = serializers.ReadOnlyField()

    maximum = serializers.ReadOnlyField()

    minimum = serializers.ReadOnlyField()

    name = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    status = serializers.ReadOnlyField()

    stock_data = None
    stock_count = serializers.ReadOnlyField()
    stock_percentage = serializers.ReadOnlyField()
    stock_value = serializers.ReadOnlyField()

    suppliers = None
    supplier_count = serializers.ReadOnlyField()

    url_booking_add = serializers.ReadOnlyField()
    url_booking_create = serializers.ReadOnlyField()
    url_booking_remove = serializers.ReadOnlyField()
    url_delete = serializers.ReadOnlyField()
    url_detail = serializers.ReadOnlyField()
    url_qrcode = serializers.ReadOnlyField()
    url_qrcode_booking_add = serializers.ReadOnlyField()
    url_qrcode_booking_remove = serializers.ReadOnlyField()
    url_qrcode_request = serializers.ReadOnlyField()
    url_request_create = serializers.ReadOnlyField()
    url_update = serializers.ReadOnlyField()

    warning = serializers.ReadOnlyField()

    class Meta:
        model = StorageItem
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------
class StorageItemDetailSerializer(BaseSerializer,StorageItemBaseSerializer):

    booking_data = BookingBaseSerializer(
        source = 'booking',
        many=True,
        read_only = True,
        fields = (
            'id',
            'create_date',
            'create_time',
            'company_name',
            'amount',
            'price',
            'value',
            'notice',
            'url_detail',
            'url_update',
            'url_delete',
        )
    )
    booking_last = None

    stock_data = StorageBaseSerializer(
        source = 'stock',
        many = True,
        read_only = True,
        fields = (
            'id',
            'create_date',
            'create_time',
            'company_name',
            'value',
            'notice',
            'url_detail',
            'url_update',
            'url_delete',
            'url_unload',
        )
    )

    supplier_data = CompanyItemBaseSerializer(
        source = "suppliers",
        many = True,
        read_only = True,
        fields=(
            'id',
            'name',
            'item_number',
            'company_name',
            'price',
            'url_booking_add',
            'url_booking_remove',
            'url_delete',
            'url_detail',
            'url_request_create',
            'url_update',
        )
    )

    class Meta:
        model = StorageItem
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------
class StorageItemListSerializer(BaseSerializer,StorageItemBaseSerializer):

    class Meta:
        model = StorageItem
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------