#--------------------------------------------------------------------------------
# Serializers File from Model CompanyItem API
# 27.10.2023
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
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from storagemanagement.api.serializers import BaseSerializer,CreateSerializer,UpdateSerializer
from storagemanagement.booking.api.serializers import BookingBaseSerializer
from storagemanagement.storage.api.serializers import StorageBaseSerializer
#--------------------------------------------------------------------------------
class CompanyItemBaseSerializer(CreateSerializer,UpdateSerializer):

    booking_data = None
    booking_count = serializers.ReadOnlyField()
    booking_last = BookingBaseSerializer(many=False, read_only=True)

    company_id = serializers.ReadOnlyField()
    company_name = serializers.ReadOnlyField()
    company_reference_number = serializers.ReadOnlyField()
    company_slug = serializers.ReadOnlyField()
    company_url_detail = serializers.ReadOnlyField()

    item_number = serializers.ReadOnlyField()

    name = serializers.ReadOnlyField()

    price = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    stock_data = None
    stock_count = serializers.ReadOnlyField()
    stock_value = serializers.ReadOnlyField()

    storageitem_id = serializers.ReadOnlyField()
    storageitem_name = serializers.ReadOnlyField()
    storageitem_reference_number = serializers.ReadOnlyField()
    storageitem_slug = serializers.ReadOnlyField()
    storageitem_url_detail = serializers.ReadOnlyField()

    unit = serializers.ReadOnlyField()

    url_booking_add = serializers.ReadOnlyField()
    url_booking_create = serializers.ReadOnlyField()
    url_booking_remove = serializers.ReadOnlyField()
    url_delete = serializers.ReadOnlyField()
    url_detail = serializers.ReadOnlyField()
    url_qrcode = serializers.ReadOnlyField()
    url_qrcode_booking_add = serializers.ReadOnlyField()
    url_qrcode_booking_create = serializers.ReadOnlyField()
    url_qrcode_booking_remove = serializers.ReadOnlyField()
    url_qrcode_request = serializers.ReadOnlyField()
    url_request_create = serializers.ReadOnlyField()
    url_update = serializers.ReadOnlyField()

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
        model = CompanyItem
        exclude = (
            'company',
            'create_user_id',
            'create_datetime',
            'storageitem',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class CompanyItemDetailSerializer(BaseSerializer,CompanyItemBaseSerializer):

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
        model = CompanyItem
        exclude = (
            'company',
            'create_user_id',
            'create_datetime',
            'storageitem',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class CompanyItemListSerializer(BaseSerializer,CompanyItemBaseSerializer):

    class Meta:
        model = CompanyItem
        exclude = (
            'company',
            'create_user_id',
            'create_datetime',
            'storageitem',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------