"""
#--------------------------------------------------------------------------------
# Serializers File from Model Offer API
# 11.11.2023
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
from storagemanagement.offer.models import Offer
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
    SupplierLinkSerializer
)
from storagemanagement.offerdata.api.serializers import OfferDataBaseSerializer
#--------------------------------------------------------------------------------
class OfferBaseSerializer(
    CreateSerializer,
    UpdateSerializer,
    SupplierLinkSerializer
):
    """
    OfferBaseSerializer

    Args:
        CreateSerializer (_type_): _description_
        UpdateSerializer (_type_): _description_
        SupplierLinkSerializer (_type_): _description_
    """

    authorized = serializers.ReadOnlyField()

    done = serializers.ReadOnlyField()

    item_data = OfferDataBaseSerializer(
        source="offerdata",
        many=True,
        read_only=True,
        fields=(
            'id',
            'authorized',
            'supplieritem_name',
            'supplieritem_item_number',
            'amount',
            'price',
            'value',
            'unit',
            'notice',
            'url_detail',
            'url_delete',
            'url_update',
            'url_authorize_true',
            'url_authorize_false'
        )
    )
    item_count = serializers.ReadOnlyField(source="offerdata_count")

    offer_file_name = serializers.ReadOnlyField()
    offer_file_url = serializers.ReadOnlyField()

    ordered = serializers.ReadOnlyField()
    ordered_date = serializers.ReadOnlyField()
    ordered_time = serializers.ReadOnlyField()
    ordered_username = serializers.ReadOnlyField()

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

    value = serializers.ReadOnlyField()

    url_authorize_true = serializers.ReadOnlyField()
    url_authorize_false = serializers.ReadOnlyField()
    url_block = serializers.SerializerMethodField()
    url_delete = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:offer_delete',
        lookup_field = 'slug',
        lookup_url_kwarg = 'offer',
    )
    url_detail = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:offer_detail',
        lookup_field = 'slug',
        lookup_url_kwarg = 'offer',
    )
    url_order_true = serializers.ReadOnlyField()
    url_order_false = serializers.ReadOnlyField()
    url_qrcode = serializers.ReadOnlyField()
    url_recived = serializers.ReadOnlyField()
    url_sent = serializers.ReadOnlyField()
    url_update = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:offer_update',
        lookup_field = 'slug',
        lookup_url_kwarg = 'offer',
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
        model = Offer
        exclude = [
            'create_user_id',
            'create_datetime',
            'ordered_user_id',
            'ordered_datetime',
            'recived_user_id',
            'recived_datetime',
            'sent_user_id',
            'sent_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class OfferListSerializer(BaseSerializer,OfferBaseSerializer):
    """
    OfferListSerializer

    Args:
        BaseSerializer (_type_): _description_
        OfferBaseSerializer (_type_): _description_
    """

    class Meta:
        """
        Meta Data from Serializer
        """
        model = Offer
        exclude = [
            'create_user_id',
            'create_datetime',
            'ordered_user_id',
            'ordered_datetime',
            'recived_user_id',
            'recived_datetime',
            'sent_user_id',
            'sent_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class OfferDetailSerializer(BaseSerializer,OfferBaseSerializer):
    """
    OfferDetailSerializer

    Args:
        BaseSerializer (_type_): _description_
        OfferBaseSerializer (_type_): _description_
    """

    class Meta:
        """
        Meta Data from Serializer
        """
        model = Offer
        exclude = [
            'create_user_id',
            'create_datetime',
            'ordered_user_id',
            'ordered_datetime',
            'recived_user_id',
            'recived_datetime',
            'sent_user_id',
            'sent_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
