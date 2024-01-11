"""
#--------------------------------------------------------------------------------
# Serializers File from Model CompanyContact API
# 16.12.2023
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
from relationshipmanagement.companycontact.models import (
    CompanyContact,
    CompanyContactTelephone,
    CompanyContactEmail
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from relationshipmanagement.api.serializers import (
    BaseSerializer,
    CreateSerializer,
    UpdateSerializer,
    CompanyLinkSerializer
    )
#--------------------------------------------------------------------------------
class CompanyContactEmailSerializer(serializers.ModelSerializer):
    """
    CompanyContactEmailSerializer

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        """
        contains all Meta data of the serializer
        """
        model = CompanyContactEmail
        fields = ('id','email',)
#--------------------------------------------------------------------------------
class CompanyContactTelephoneSerializer(serializers.ModelSerializer):
    """
    CompanyContactTelephoneSerializer

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
        return CompanyContactTelephone.Types(obj.types).label

    class Meta:
        """
        contains all Meta data of the serializer
        """
        model = CompanyContactTelephone
        fields = ('id','number','types')
#--------------------------------------------------------------------------------
class CompanyContactBaseSerializer(
    CreateSerializer,
    UpdateSerializer,
    CompanyLinkSerializer
):
    """
    CompanyContactBaseSerializer

    Args:
        CreateSerializer (_type_): _description_
        UpdateSerializer (_type_): _description_
        CompanyLinkSerializer (_type_): _description_
    """

    email_data = CompanyContactEmailSerializer(source="emails",many=True,read_only=True)
    email_count = serializers.ReadOnlyField()

    first_name = serializers.ReadOnlyField()

    last_name = serializers.ReadOnlyField()

    name = serializers.ReadOnlyField()

    notice = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    telephone_data = CompanyContactTelephoneSerializer(
        source="telephones",
        many=True,
        read_only=True
    )
    telephone_count = serializers.ReadOnlyField()

    url_delete = serializers.HyperlinkedIdentityField(
        view_name = 'relationshipmanagement:companycontact_delete',
        lookup_field = 'slug',
        lookup_url_kwarg = 'companycontact',
    )
    url_detail = serializers.HyperlinkedIdentityField(
        view_name = 'relationshipmanagement:companycontact_detail',
        lookup_field = 'slug',
        lookup_url_kwarg = 'companycontact',
    )
    url_qrcode = serializers.ReadOnlyField()
    url_update = serializers.HyperlinkedIdentityField(
        view_name = 'relationshipmanagement:companycontact_update',
        lookup_field = 'slug',
        lookup_url_kwarg = 'companycontact',
    )

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
        model = CompanyContact
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------
class CompanyContactDetailSerializer(BaseSerializer,CompanyContactBaseSerializer):
    """
    CompanyContactDetailSerializer

    Args:
        BaseSerializer (_type_): _description_
        CompanyContactBaseSerializer (_type_): _description_
    """

    class Meta:
        """
        contains all Meta data of the serializer
        """
        model = CompanyContact
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------
class CompanyContactListSerializer(BaseSerializer,CompanyContactBaseSerializer):
    """
    CompanyContactListSerializer

    Args:
        BaseSerializer (_type_): _description_
        CompanyContactBaseSerializer (_type_): _description_
    """

    class Meta:
        """
        contains all Meta data of the serializer
        """
        model = CompanyContact
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------
