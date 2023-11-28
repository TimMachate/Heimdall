#--------------------------------------------------------------------------------
# Serializers File from Model Booking API
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
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from storagemanagement.api.serializers import BaseSerializer,CreateSerializer,UpdateSerializer
#--------------------------------------------------------------------------------
class BookingBaseSerializer(CreateSerializer,UpdateSerializer):

    amount = serializers.ReadOnlyField()

    company_id = serializers.ReadOnlyField()
    company_name = serializers.ReadOnlyField()
    company_reference_number = serializers.ReadOnlyField()
    company_slug = serializers.ReadOnlyField()
    company_url_detail = serializers.ReadOnlyField()

    companyitem_id = serializers.ReadOnlyField()
    companyitem_name = serializers.ReadOnlyField()
    companyitem_item_number = serializers.ReadOnlyField()
    companyitem_reference_number = serializers.ReadOnlyField()
    companyitem_slug = serializers.ReadOnlyField()
    companyitem_url_detail = serializers.ReadOnlyField()

    notice = serializers.ReadOnlyField()

    price = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()
    stock = serializers.ReadOnlyField()

    storageitem_id = serializers.ReadOnlyField()
    storageitem_name = serializers.ReadOnlyField()
    storageitem_reference_number = serializers.ReadOnlyField()
    storageitem_slug = serializers.ReadOnlyField()
    storageitem_url_detail = serializers.ReadOnlyField()

    unit = serializers.ReadOnlyField()

    url_delete = serializers.ReadOnlyField()
    url_detail = serializers.ReadOnlyField()
    url_qrcode = serializers.ReadOnlyField()
    url_update = serializers.ReadOnlyField()

    value = serializers.ReadOnlyField()

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
        model = Booking
        exclude = (
            'companyitem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class BookingDetailSerializer(BaseSerializer,BookingBaseSerializer):
    class Meta:
        model = Booking
        exclude = (
            'companyitem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class BookingListSerializer(BaseSerializer,BookingBaseSerializer):
    class Meta:
        model = Booking
        exclude = (
            'companyitem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------