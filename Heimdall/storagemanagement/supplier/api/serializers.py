"""
#--------------------------------------------------------------------------------
# Serializers File from Model Supplier API
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
from storagemanagement.supplier.models import Supplier
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
from storagemanagement.suppliercontact.api.serializers import SupplierContactBaseSerializer
from storagemanagement.supplieritem.api.serializers import SupplierItemBaseSerializer
from storagemanagement.storage.api.serializers import StorageBaseSerializer
#--------------------------------------------------------------------------------
class SupplierBaseSerializer(CreateSerializer,UpdateSerializer):
    """
    SupplierBaseSerializer

    Args:
        CreateSerializer (_type_): add create fields
        UpdateSerializer (_type_): add update fields
    """

    booking_data = BookingBaseSerializer(
        many=True,
        read_only=True,
        fields=(
            'id',
            'create_date',
            'create_time',
            'supplieritem_name',
            'supplieritem_item_number',
            'amount',
            'url_detail',
            'url_delete',
            'url_update',
            'notice'
        )
    )
    booking_count = serializers.ReadOnlyField()

    city = serializers.ReadOnlyField()

    country = serializers.ReadOnlyField()

    email = serializers.ReadOnlyField()

    email_address_offer = serializers.ReadOnlyField(
        source="supplier_info.email_address_offer"
    )
    email_address_cc_offer = serializers.ReadOnlyField(
        source="supplier_info.email_address_cc_offer"
    )
    email_body_offer = serializers.ReadOnlyField(
        source="supplier_info.email_body_offer"
    )
    email_subject_offer = serializers.ReadOnlyField(
        source="supplier_info.email_subject_offer"
    )

    email_address_order = serializers.ReadOnlyField(
        source="supplier_info.email_address_order"
    )
    email_address_cc_order = serializers.ReadOnlyField(
        source="supplier_info.email_address_cc_order"
    )
    email_body_order = serializers.ReadOnlyField(
        source="supplier_info.email_body_order"
    )
    email_subject_order = serializers.ReadOnlyField(
        source="supplier_info.email_subject_order"
    )

    house_number = serializers.ReadOnlyField()

    logo_url = serializers.ReadOnlyField()

    name = serializers.ReadOnlyField()

    notice = serializers.ReadOnlyField()

    post_code = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    stock_data = StorageBaseSerializer(
        many=True,
        read_only=True,
        fields=(
            'id',
            'create_date',
            'create_time',
            'storageitem_name',
            'storageitem_reference_number',
            'supplieritem_name',
            'supplieritem_item_number',
            'value',
            'notice',
            'url_detail',
            'url_unload'
        )
    )
    stock_count = serializers.ReadOnlyField()
    stock_value = serializers.ReadOnlyField()

    street = serializers.ReadOnlyField()

    suppliercontact_data = SupplierContactBaseSerializer(
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
    suppliercontact_count = serializers.ReadOnlyField()

    supplieritem_data = SupplierItemBaseSerializer(
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
    supplieritem_count = serializers.ReadOnlyField()

    telephone = serializers.ReadOnlyField()

    url_block = serializers.SerializerMethodField()

    url_delete = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:supplier_delete',
        lookup_field = 'slug',
        lookup_url_kwarg = 'supplier',
    )
    url_detail = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:supplier_detail',
        lookup_field = 'slug',
        lookup_url_kwarg = 'supplier',
    )
    url_qrcode = serializers.ReadOnlyField()
    url_update = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:supplier_update',
        lookup_field = 'slug',
        lookup_url_kwarg = 'supplier',
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
        model = Supplier
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class SupplierDetailSerializer(BaseSerializer,SupplierBaseSerializer):
    """
    SupplierDetailSerializer

    Args:
        BaseSerializer (_type_): add field choice
        SupplierBaseSerializer (_type_): add SupplierBaseSerializer fields
    """

    class Meta:
        """
        Meta Data from Serializer
        """
        model = Supplier
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class SupplierListSerializer(BaseSerializer,SupplierBaseSerializer):
    """
    SupplierListSerializer

    Args:
        BaseSerializer (_type_): add field choice
        SupplierBaseSerializer (_type_): add SupplierBaseSerializer fields
    """

    booking_data = None

    stock_data = None

    suppliercontact_data = None

    supplieritem_data = None

    class Meta:
        """
        Meta Data from Serializer
        """
        model = Supplier
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
