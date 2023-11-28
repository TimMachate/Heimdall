#--------------------------------------------------------------------------------
# Serializers File from Model Storage API
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
from storagemanagement.storage.models import Storage
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from storagemanagement.api.serializers import BaseSerializer,CreateSerializer,UpdateSerializer
#--------------------------------------------------------------------------------
class StorageBaseSerializer(CreateSerializer,UpdateSerializer):

    booking_id = serializers.ReadOnlyField()
    booking_reference_number = serializers.ReadOnlyField()
    booking_slug = serializers.ReadOnlyField()
    booking_url_detail = serializers.ReadOnlyField()

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

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    storageitem_id = serializers.ReadOnlyField()
    storageitem_name = serializers.ReadOnlyField()
    storageitem_reference_number = serializers.ReadOnlyField()
    storageitem_slug = serializers.ReadOnlyField()
    storageitem_url_detail = serializers.ReadOnlyField()

    unit = serializers.ReadOnlyField()

    url_delete = serializers.ReadOnlyField()
    url_detail = serializers.ReadOnlyField()
    url_unload = serializers.ReadOnlyField()
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
        model = Storage
        exclude = [
            'booking',
            'companyitem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            'unload_user_id',
            'unload_datetime',
            ]
#--------------------------------------------------------------------------------
class StorageListSerializer(BaseSerializer,StorageBaseSerializer):

    class Meta:
        model = Storage
        exclude = [
            'booking',
            'companyitem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            'unload_user_id',
            'unload_datetime',
            ]
#--------------------------------------------------------------------------------
class StorageDetailSerializer(BaseSerializer,StorageBaseSerializer):

    class Meta:
        model = Storage
        exclude = [
            'booking',
            'companyitem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            'unload_user_id',
            'unload_datetime',
            ]
#--------------------------------------------------------------------------------