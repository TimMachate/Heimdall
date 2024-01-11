"""
#--------------------------------------------------------------------------------
# Serializers File from Model SupplierContact API
# 28.10.2023
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
from storagemanagement.suppliercontact.models import (
    SupplierContact,
    SupplierContactTelephone,
    SupplierContactEmail
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from storagemanagement.api.serializers import SupplierLinkSerializer
from tools.api.serializers import (
    BaseSerializer,
    CreateSerializer,
    UpdateSerializer
    )
#--------------------------------------------------------------------------------
class SupplierContactEmailSerializer(serializers.ModelSerializer):
    """
    SupplierContactEmailSerializer

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        """
        contains all Meta data of the serializer
        """
        model = SupplierContactEmail
        fields = ('id','email',)
#--------------------------------------------------------------------------------
class SupplierContactTelephoneSerializer(serializers.ModelSerializer):
    """
    SupplierContactTelephoneSerializer

    Args:
        serializers (_type_): _description_

    Returns:
        _type_: _description_
    """

    types = serializers.SerializerMethodField()

    def get_types(self,obj):
        """
        get_types

        Args:
            obj (_type_): _description_

        Returns:
            _type_: _description_
        """
        return SupplierContactTelephone.Types(obj.types).label

    class Meta:
        """
        contains all Meta data of the serializer
        """
        model = SupplierContactTelephone
        fields = ('id','number','types')
#--------------------------------------------------------------------------------
class SupplierContactBaseSerializer(
    CreateSerializer,
    UpdateSerializer,
    SupplierLinkSerializer
):
    """
    SupplierContactBaseSerializer

    Args:
        CreateSerializer (_type_): _description_
        UpdateSerializer (_type_): _description_
        SupplierLinkSerializer (_type_): _description_
    """

    email_data = SupplierContactEmailSerializer(source="emails",many=True,read_only=True)
    email_count = serializers.ReadOnlyField()

    first_name = serializers.ReadOnlyField()

    last_name = serializers.ReadOnlyField()

    name = serializers.ReadOnlyField()

    notice = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    telephone_data = SupplierContactTelephoneSerializer(
        source="telephones",
        many=True,
        read_only=True
    )
    telephone_count = serializers.ReadOnlyField()

    url_block = serializers.SerializerMethodField()

    url_delete = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:suppliercontact_delete',
        lookup_field = 'slug',
        lookup_url_kwarg = 'suppliercontact',
    )
    url_detail = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:suppliercontact_detail',
        lookup_field = 'slug',
        lookup_url_kwarg = 'suppliercontact',
    )
    url_qrcode = serializers.ReadOnlyField()
    url_update = serializers.HyperlinkedIdentityField(
        view_name = 'storagemanagement:suppliercontact_update',
        lookup_field = 'slug',
        lookup_url_kwarg = 'suppliercontact',
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
        contains all Meta data of the serializer
        """
        model = SupplierContact
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------
class SupplierContactDetailSerializer(BaseSerializer,SupplierContactBaseSerializer):
    """
    SupplierContactDetailSerializer

    Args:
        BaseSerializer (_type_): _description_
        SupplierContactBaseSerializer (_type_): _description_
    """

    class Meta:
        """
        contains all Meta data of the serializer
        """
        model = SupplierContact
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------
class SupplierContactListSerializer(BaseSerializer,SupplierContactBaseSerializer):
    """
    SupplierContactListSerializer

    Args:
        BaseSerializer (_type_): _description_
        SupplierContactBaseSerializer (_type_): _description_
    """

    class Meta:
        """
        contains all Meta data of the serializer
        """
        model = SupplierContact
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------
