#--------------------------------------------------------------------------------
# Serializers File from Model Company API
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
from storagemanagement.company.models import Company
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from storagemanagement.api.serializers import BaseSerializer,CreateSerializer,UpdateSerializer
from storagemanagement.booking.api.serializers import BookingBaseSerializer
from storagemanagement.companycontact.api.serializers import CompanyContactBaseSerializer
from storagemanagement.companyitem.api.serializers import CompanyItemBaseSerializer
from storagemanagement.storage.api.serializers import StorageBaseSerializer
#--------------------------------------------------------------------------------
class CompanyBaseSerializer(CreateSerializer,UpdateSerializer):

    city = serializers.ReadOnlyField()

    booking_data = None
    booking_count = serializers.ReadOnlyField()

    companycontact_data = None
    companycontact_count = serializers.ReadOnlyField()

    companyitem_data = None
    companyitem_count = serializers.ReadOnlyField()
    
    country = serializers.ReadOnlyField()
    
    email = serializers.ReadOnlyField()

    house_number = serializers.ReadOnlyField()

    logo_url = serializers.ReadOnlyField()
    
    name = serializers.ReadOnlyField()

    notice = serializers.ReadOnlyField()

    post_code = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    stock_data = None
    stock_count = serializers.ReadOnlyField()
    stock_value = serializers.ReadOnlyField()

    storageitem_data = None
    storageitem_count = serializers.ReadOnlyField()

    street = serializers.ReadOnlyField()

    telephone = serializers.ReadOnlyField()
    
    url_delete = serializers.ReadOnlyField()
    url_detail = serializers.ReadOnlyField()
    url_qrcode = serializers.ReadOnlyField()
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
        model = Company
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class CompanyDetailSerializer(BaseSerializer,CompanyBaseSerializer):

    booking_data = BookingBaseSerializer(
        source="bookings",
        many=True,
        read_only=True,
        fields=(
            'id',
            'create_date',
            'create_time',
            'companyitem_name',
            'companyitem_item_number',
            'amount',
            'url_detail',
            'url_delete',
            'url_update',
            'notice'
        )
    )

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

    stock_data = StorageBaseSerializer(
        source="stock",
        many=True,
        read_only=True,
        fields=(
            'id',
            'create_date',
            'create_time',
            'storageitem_name',
            'storageitem_reference_number',
            'companyitem_name',
            'companyitem_item_number',
            'value',
            'notice',
            'url_detail',
            'url_unload'
        )
    )

    class Meta:
        model = Company
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class CompanyListSerializer(BaseSerializer,CompanyBaseSerializer):

    class Meta:
        model = Company
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------