"""
#--------------------------------------------------------------------------------
# Serializers File from Model Storage API
# 29.10.2023
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
from storagemanagement.storage.models import Storage
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
class StorageBaseSerializer(
    CreateSerializer,
    UpdateSerializer
):
    """
    StorageBaseSerializer

    Args:
        CreateSerializer (_type_): _description_
        UpdateSerializer (_type_): _description_
    """

    booking_id = serializers.ReadOnlyField()
    booking_reference_number = serializers.ReadOnlyField()
    booking_slug = serializers.ReadOnlyField()
    booking_url_detail = serializers.ReadOnlyField()

    notice = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

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

    unload_date = serializers.ReadOnlyField()
    unload_time = serializers.ReadOnlyField()
    unload_username = serializers.ReadOnlyField()

    value = serializers.ReadOnlyField()

    url_block = serializers.SerializerMethodField()

    url_delete = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:storage_delete',
        lookup_field = 'slug',
        lookup_url_kwarg = 'storage',
    )
    url_detail = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:storage_detail',
        lookup_field = 'slug',
        lookup_url_kwarg = 'storage',
    )
    url_unload = serializers.ReadOnlyField()
    url_update = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:storage_update',
        lookup_field = 'slug',
        lookup_url_kwarg = 'storage',
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
        model = Storage
        exclude = [
            'booking',
            'supplieritem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            'unload_user_id',
            'unload_datetime',
            ]
#--------------------------------------------------------------------------------
class StorageListSerializer(BaseSerializer,StorageBaseSerializer):
    """
    StorageListSerializer

    Args:
        BaseSerializer (_type_): _description_
        StorageBaseSerializer (_type_): _description_
    """

    class Meta:
        """
        Meta Data from Serializer
        """
        model = Storage
        exclude = [
            'booking',
            'supplieritem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            'unload_user_id',
            'unload_datetime',
            ]
#--------------------------------------------------------------------------------
class StorageDetailSerializer(BaseSerializer,StorageBaseSerializer):
    """
    StorageDetailSerializer

    Args:
        BaseSerializer (_type_): _description_
        StorageBaseSerializer (_type_): _description_
    """

    class Meta:
        """
        Meta Data from Serializer
        """
        model = Storage
        exclude = [
            'booking',
            'supplieritem',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            'unload_user_id',
            'unload_datetime',
            ]
#--------------------------------------------------------------------------------
