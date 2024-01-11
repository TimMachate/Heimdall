"""
#--------------------------------------------------------------------------------
# Serializers File from Model Booking API
# 07.01.2024
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
#--------------------------------------------------------------------------------
class BookingBaseSerializer(
    CreateSerializer,
    UpdateSerializer
):
    """
    BookingBaseSerializer
    contains all base fields for the Booking Object
    """

    amount = serializers.ReadOnlyField()

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

    supplier_id = serializers.ReadOnlyField()
    supplier_name = serializers.ReadOnlyField()
    supplier_reference_number = serializers.ReadOnlyField()
    supplier_slug = serializers.ReadOnlyField()
    supplier_url_detail = serializers.ReadOnlyField()

    supplieritem_id = serializers.ReadOnlyField()
    supplieritem_name = serializers.ReadOnlyField()
    supplieritem_item_number = serializers.ReadOnlyField()
    supplieritem_reference_number = serializers.ReadOnlyField()
    supplieritem_slug = serializers.ReadOnlyField()
    supplieritem_url_detail = serializers.ReadOnlyField()

    unit = serializers.ReadOnlyField()

    value = serializers.ReadOnlyField()

    url_block = serializers.SerializerMethodField()

    url_delete = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:booking_delete',
        lookup_field = 'slug',
        lookup_url_kwarg = 'booking',
    )
    url_detail = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:booking_detail',
        lookup_field = 'slug',
        lookup_url_kwarg = 'booking',
    )
    url_qrcode = serializers.ReadOnlyField()
    url_update = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:booking_update',
        lookup_field = 'slug',
        lookup_url_kwarg = 'booking',
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
        """ Meta Data for the Serializer """
        model = Booking
        exclude = (
            'supplieritem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class BookingDetailSerializer(BaseSerializer,BookingBaseSerializer):
    """
    BookingDetailSerializer
    contains all special booking detail fields for the Booking Object
    """
    class Meta:
        """ Meta Data for the Serializer """
        model = Booking
        exclude = (
            'supplieritem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class BookingListSerializer(BaseSerializer,BookingBaseSerializer):
    """
    BookingDetailSerializer
    contains all special booking list fields for the Booking Object
    """
    class Meta:
        """ Meta Data for the Serializer """
        model = Booking
        exclude = (
            'supplieritem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
