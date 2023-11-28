#--------------------------------------------------------------------------------
# Serializers File from Model Order Data API
# 10.11.2023
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
from storagemanagement.orderdata.models import OrderData
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from storagemanagement.api.serializers import BaseSerializer,CreateSerializer,UpdateSerializer
#--------------------------------------------------------------------------------
class OrderDataBaseSerializer(CreateSerializer,UpdateSerializer):

    amount = serializers.ReadOnlyField()
    amount_recived = serializers.ReadOnlyField()

    authorized = serializers.ReadOnlyField()
    authorized_date = serializers.ReadOnlyField()
    authorized_time = serializers.ReadOnlyField()
    authorized_username = serializers.ReadOnlyField()

    booking = serializers.ReadOnlyField()
    booking_date = serializers.ReadOnlyField()
    booking_time = serializers.ReadOnlyField()
    booking_username = serializers.ReadOnlyField()

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

    done = serializers.ReadOnlyField()

    offer_id = serializers.ReadOnlyField()
    offer_file_url = serializers.ReadOnlyField()
    offer_file_name = serializers.ReadOnlyField()
    offer_reference_number = serializers.ReadOnlyField()
    offer_slug = serializers.ReadOnlyField()
    offer_url_detail = serializers.ReadOnlyField()

    order_id = serializers.ReadOnlyField()
    order_reference_number = serializers.ReadOnlyField()
    order_slug = serializers.ReadOnlyField()
    order_url_detail = serializers.ReadOnlyField()

    notice = serializers.ReadOnlyField()

    price = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    storageitem_id = serializers.ReadOnlyField()
    storageitem_name = serializers.ReadOnlyField()
    storageitem_reference_number = serializers.ReadOnlyField()
    storageitem_slug = serializers.ReadOnlyField()
    storageitem_url_detail = serializers.ReadOnlyField()

    unit = serializers.ReadOnlyField()

    url_authorize_true = serializers.ReadOnlyField()
    url_authorize_false = serializers.ReadOnlyField()
    url_booking_true = serializers.ReadOnlyField()
    url_booking_false = serializers.ReadOnlyField()
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
        model = OrderData
        ordering = ('id')
        exclude = [
            'companyitem',
            'authorized_datetime',
            'authorized_user_id',
            'booking_datetime',
            'booking_user_id',
            'create_user_id',
            'create_datetime',
            'order',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class OrderDataListSerializer(BaseSerializer,OrderDataBaseSerializer):

    class Meta:
        model = OrderData
        exclude = [
            'companyitem',
            'authorized_datetime',
            'authorized_user_id',
            'booking_datetime',
            'booking_user_id',
            'create_user_id',
            'create_datetime',
            'order',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class OrderDataDetailSerializer(BaseSerializer,OrderDataBaseSerializer):

    class Meta:
        model = OrderData
        exclude = [
            'companyitem',
            'authorized_datetime',
            'authorized_user_id',
            'booking_datetime',
            'booking_user_id',
            'create_user_id',
            'create_datetime',
            'order',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------