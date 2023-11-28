#--------------------------------------------------------------------------------
# Serializers File from Model CompanyContact API
# 28.10.2023
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
from storagemanagement.companycontact.models import CompanyContact,CompanyContactTelephone,CompanyContactEmail
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from storagemanagement.api.serializers import (
    BaseSerializer,
    CreateSerializer,
    UpdateSerializer
    )
#--------------------------------------------------------------------------------
class CompanyContactEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyContactEmail
        fields = ('id','email',)
#--------------------------------------------------------------------------------
class CompanyContactTelephoneSerializer(serializers.ModelSerializer):
    
    types = serializers.SerializerMethodField()

    def get_types(self,obj):
        return CompanyContactTelephone.Types(obj.types).label
    
    class Meta:
        model = CompanyContactTelephone
        fields = ('id','number','types')
#--------------------------------------------------------------------------------
class CompanyContactBaseSerializer(CreateSerializer,UpdateSerializer):

    company_id = serializers.ReadOnlyField()
    company_name = serializers.ReadOnlyField()
    company_reference_number = serializers.ReadOnlyField()
    company_slug = serializers.ReadOnlyField()
    company_url_detail = serializers.ReadOnlyField()

    email_data = CompanyContactEmailSerializer(source="emails",many=True,read_only=True)
    email_count = serializers.ReadOnlyField()

    first_name = serializers.ReadOnlyField()

    last_name = serializers.ReadOnlyField()

    name = serializers.ReadOnlyField()

    notice = serializers.ReadOnlyField()

    reference_number = serializers.ReadOnlyField()

    slug = serializers.ReadOnlyField()

    telephone_data = CompanyContactTelephoneSerializer(source="telephones",many=True,read_only=True)
    telephone_count = serializers.ReadOnlyField()
    
    url_delete = serializers.ReadOnlyField()
    url_detail = serializers.ReadOnlyField()
    url_qrcode = serializers.ReadOnlyField()
    url_update = serializers.ReadOnlyField()

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
        model = CompanyContact
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------
class CompanyContactDetailSerializer(BaseSerializer,CompanyContactBaseSerializer):

    email_data = CompanyContactEmailSerializer(source="emails",many=True,read_only=True)

    telephone_data = CompanyContactTelephoneSerializer(source="telephones",many=True,read_only=True)

    class Meta:
        model = CompanyContact
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------
class CompanyContactListSerializer(BaseSerializer,CompanyContactBaseSerializer):

    email_data = CompanyContactEmailSerializer(source="emails",many=True,read_only=True)

    telephone_data = CompanyContactTelephoneSerializer(source="telephones",many=True,read_only=True)

    class Meta:
        model = CompanyContact
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            )
#--------------------------------------------------------------------------------