"""
#--------------------------------------------------------------------------------
# serializers File from App Storagemanagement API
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
# Serializer
#--------------------------------------------------------------------------------

class SupplierLinkSerializer(serializers.ModelSerializer):
    """ SupplierLinkSerializer contains all fields for info of a supplier object"""
    supplier_id = serializers.ReadOnlyField()
    supplier_name = serializers.ReadOnlyField()
    supplier_reference_number = serializers.ReadOnlyField()
    supplier_slug = serializers.ReadOnlyField()
    supplier_url_detail = serializers.ReadOnlyField()
#--------------------------------------------------------------------------------
class SupplierItemLinkSerializer(serializers.ModelSerializer):
    """ SupplierItemLinkSerializer contains all fields for info of a supplier item object"""
    supplieritem_id = serializers.ReadOnlyField()
    supplieritem_name = serializers.ReadOnlyField()
    supplieritem_item_number = serializers.ReadOnlyField()
    supplieritem_reference_number = serializers.ReadOnlyField()
    supplieritem_slug = serializers.ReadOnlyField()
    supplieritem_url_detail = serializers.ReadOnlyField()
#--------------------------------------------------------------------------------
class StorageItemLinkSerializer(serializers.ModelSerializer):
    """ StorageItemLinkSerializer contains all fields for info of a storage item object"""
    storageitem_id = serializers.ReadOnlyField()
    storageitem_name = serializers.ReadOnlyField()
    storageitem_reference_number = serializers.ReadOnlyField()
    storageitem_slug = serializers.ReadOnlyField()
    storageitem_url_detail = serializers.ReadOnlyField()
#--------------------------------------------------------------------------------
class BookingLinkSerializer(serializers.ModelSerializer):
    """ BookingItemLinkSerializer contains all fields for info of a booking object"""
    booking_id = serializers.ReadOnlyField()
    booking_reference_number = serializers.ReadOnlyField()
    booking_slug = serializers.ReadOnlyField()
    booking_url_detail = serializers.ReadOnlyField()
#--------------------------------------------------------------------------------
