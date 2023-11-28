#--------------------------------------------------------------------------------
# Serializers File from Model Offer API
# 11.11.2023
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
from storagemanagement.offer.models import Offer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from storagemanagement.api.serializers import BaseSerializer,CreateSerializer,UpdateSerializer
from storagemanagement.offerdata.api.serializers import OfferDataBaseSerializer
#--------------------------------------------------------------------------------
class OfferBaseSerializer(CreateSerializer,UpdateSerializer):

    authorized = serializers.ReadOnlyField()

    company_id = serializers.ReadOnlyField()
    company_name = serializers.ReadOnlyField()
    company_reference_number = serializers.ReadOnlyField()
    company_slug = serializers.ReadOnlyField()
    company_url_detail = serializers.ReadOnlyField()

    done = serializers.ReadOnlyField()

    item_data = OfferDataBaseSerializer(
        source="offerdata",
        many=True,
        read_only=True,
        fields=(
            'id',
            'authorized',
            'companyitem_name',
            'companyitem_item_number',
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

    url_authorize_true = serializers.ReadOnlyField()
    url_authorize_false = serializers.ReadOnlyField()
    url_delete = serializers.ReadOnlyField()
    url_detail = serializers.ReadOnlyField()
    url_order_true = serializers.ReadOnlyField()
    url_order_false = serializers.ReadOnlyField()
    url_qrcode = serializers.ReadOnlyField()
    url_recived = serializers.ReadOnlyField()
    url_sent = serializers.ReadOnlyField()
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

    class Meta:
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

    class Meta:
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