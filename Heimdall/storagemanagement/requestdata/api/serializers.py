#--------------------------------------------------------------------------------
# Serializers File from Model Request Data API
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
from storagemanagement.requestdata.models import RequestData
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from storagemanagement.api.serializers import BaseSerializer,CreateSerializer,UpdateSerializer
#--------------------------------------------------------------------------------
class RequestDataBaseSerializer(CreateSerializer,UpdateSerializer):

    amount = serializers.ReadOnlyField()

    authorized = serializers.ReadOnlyField()
    authorized_date = serializers.ReadOnlyField()
    authorized_time = serializers.ReadOnlyField()
    authorized_username = serializers.ReadOnlyField()

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
    url_delete = serializers.ReadOnlyField()
    url_detail = serializers.ReadOnlyField()
    url_offer = serializers.ReadOnlyField()
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
        model = RequestData
        exclude = [
            'companyitem',
            'storageitem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class RequestDataListSerializer(BaseSerializer,RequestDataBaseSerializer):

    class Meta:
        model = RequestData
        exclude = [
            'companyitem',
            'storageitem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class RequestDataDetailSerializer(BaseSerializer,RequestDataBaseSerializer):

    class Meta:
        model = RequestData
        exclude = [
            'companyitem',
            'storageitem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------