"""
#--------------------------------------------------------------------------------
# Serializers File from Model Programm API
# 18.12.2023
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
from programmmanagement.programm.models import Programm
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from programmmanagement.api.serializers import (
    BaseSerializer,
    CreateSerializer,
    UpdateSerializer
)
#--------------------------------------------------------------------------------
class ProgrammBaseSerializer(CreateSerializer,UpdateSerializer):
    """
    ProgrammBaseSerializer

    Args:
        CreateSerializer (_type_): add create fields
        UpdateSerializer (_type_): add update fields
    """

    name = serializers.ReadOnlyField()

    description = serializers.ReadOnlyField()

    htmlfile_name = serializers.ReadOnlyField()
    htmlfile_url = serializers.ReadOnlyField()

    #users = serializers.ReadOnlyField()

    users_count = serializers.ReadOnlyField()

    url_delete = serializers.HyperlinkedIdentityField(
        view_name = 'programmmanagement:programm_delete',
        lookup_field = 'slug',
        lookup_url_kwarg = 'programm',
    )
    url_detail = serializers.HyperlinkedIdentityField(
        view_name = 'programmmanagement:programm_detail',
        lookup_field = 'slug',
        lookup_url_kwarg = 'programm',
    )
    url_detail = serializers.HyperlinkedIdentityField(
        view_name = 'programmmanagement:programm_detail',
        lookup_field = 'slug',
        lookup_url_kwarg = 'programm',
    )
    url_programm = serializers.HyperlinkedIdentityField(
        view_name = 'programmmanagement:programmmanagement_page',
        lookup_field = 'slug',
        lookup_url_kwarg = 'programm',
    )
    url_qrcode = serializers.ReadOnlyField()
    url_update = serializers.HyperlinkedIdentityField(
        view_name = 'programmmanagement:programm_update',
        lookup_field = 'slug',
        lookup_url_kwarg = 'programm',
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
        Meta Data from Serializer
        """
        model = Programm
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class ProgrammDetailSerializer(BaseSerializer,ProgrammBaseSerializer):
    """
    ProgrammDetailSerializer

    Args:
        BaseSerializer (_type_): add field choice
        ProgrammBaseSerializer (_type_): add ProgrammBaseSerializer fields
    """

    class Meta:
        """
        Meta Data from Serializer
        """
        model = Programm
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
class ProgrammListSerializer(BaseSerializer,ProgrammBaseSerializer):
    """
    ProgrammListSerializer

    Args:
        BaseSerializer (_type_): add field choice
        ProgrammBaseSerializer (_type_): add ProgrammBaseSerializer fields
    """

    class Meta:
        """
        Meta Data from Serializer
        """
        model = Programm
        exclude = (
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
        )
#--------------------------------------------------------------------------------
