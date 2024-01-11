"""
#--------------------------------------------------------------------------------
# Serializers File from Model Order API
# 09.11.2023
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
from storagemanagement.order.models import Order
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
from storagemanagement.api.serializers import SupplierLinkSerializer
from storagemanagement.orderdata.api.serializers import OrderDataBaseSerializer
#--------------------------------------------------------------------------------
class OrderBaseSerializer(
    CreateSerializer,
    UpdateSerializer,
    SupplierLinkSerializer
):
    """
    OrderBaseSerializer

    Args:
        CreateSerializer (_type_): _description_
        UpdateSerializer (_type_): _description_
        SupplierLinkSerializer (_type_): _description_
    """

    authorized = serializers.ReadOnlyField()

    booked = serializers.ReadOnlyField()

    delivery_note_name = serializers.ReadOnlyField()
    delivery_note_url = serializers.ReadOnlyField()

    done = serializers.ReadOnlyField()

    item_data = OrderDataBaseSerializer(
        source="orderdata",
        many=True,
        read_only=True,
        fields=(
            'id',
            'authorized',
            'booked',
            'supplieritem_name',
            'supplieritem_item_number',
            'amount',
            'amount_recived',
            'price',
            'value',
            'unit',
            'notice',
            'offer_file_url',
            'offer_url_detail',
            'url_detail',
            'url_delete',
            'url_update',
            'url_authorize_true',
            'url_authorize_false',
            'url_booking_true',
            'url_booking_false'
        )
    )
    item_count = serializers.ReadOnlyField(source="orderdata_count")

    notice = serializers.ReadOnlyField()

    order_file_name = serializers.ReadOnlyField()
    order_file_url = serializers.ReadOnlyField()

    recived = serializers.ReadOnlyField()
    recived_date = serializers.ReadOnlyField()
    recived_time = serializers.ReadOnlyField()
    recived_username = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    sent = serializers.ReadOnlyField()
    sent_date = serializers.ReadOnlyField()
    sent_time = serializers.ReadOnlyField()
    sent_username = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    url_block = serializers.SerializerMethodField()

    url_authorize_true = serializers.ReadOnlyField()
    url_authorize_false = serializers.ReadOnlyField()
    url_booking_true = serializers.ReadOnlyField()
    url_booking_false = serializers.ReadOnlyField()
    url_delete = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:order_delete',
        lookup_field = 'slug',
        lookup_url_kwarg = 'order',
    )
    url_detail = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:order_detail',
        lookup_field = 'slug',
        lookup_url_kwarg = 'order',
    )
    url_qrcode = serializers.ReadOnlyField()
    url_recived = serializers.ReadOnlyField()
    url_sent = serializers.ReadOnlyField()
    url_update = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:order_update',
        lookup_field = 'slug',
        lookup_url_kwarg = 'order',
    )

    value = serializers.ReadOnlyField()

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
        model = Order
        exclude = [
            'create_user_id',
            'create_datetime',
            'delivery_note',
            'order_file',
            'recived_user_id',
            'recived_datetime',
            'sent_user_id',
            'sent_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class OrderListSerializer(BaseSerializer,OrderBaseSerializer):
    """
    OrderListSerializer

    Args:
        BaseSerializer (_type_): _description_
        OrderBaseSerializer (_type_): _description_
    """

    item_data = None

    class Meta:
        """
        Meta Data from Serializer
        """
        model = Order
        exclude = [
            'create_user_id',
            'create_datetime',
            'delivery_note',
            'order_file',
            'recived_user_id',
            'recived_datetime',
            'sent_user_id',
            'sent_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class OrderDetailSerializer(BaseSerializer,OrderBaseSerializer):
    """
    OrderDetailSerializer

    Args:
        BaseSerializer (_type_): _description_
        OrderBaseSerializer (_type_): _description_
    """

    class Meta:
        """
        Meta Data Serializer
        """
        model = Order
        exclude = [
            'create_user_id',
            'create_datetime',
            'delivery_note',
            'order_file',
            'recived_user_id',
            'recived_datetime',
            'sent_user_id',
            'sent_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
