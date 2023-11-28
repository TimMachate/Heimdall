from django.apps import apps
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, HyperlinkedRelatedField, SerializerMethodField,PrimaryKeyRelatedField,StringRelatedField


# import models
from visualisation.models import (
    ItemGroup,
    Item,
    Table,
    TableItem,
    Diagram,
    Graph,
)

#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Item
#--------------------------------------------------------------------------------
class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemGroupListSerializer(ModelSerializer):
    id = HyperlinkedIdentityField(view_name='visualisationAPI:item_detail',lookup_field='id')
    data = StringRelatedField(many=True)
    class Meta:
        model = ItemGroup
        fields = '__all__'

class ItemGroupDetailSerializer(ModelSerializer):
    data = ItemSerializer(many=True,read_only=True)
    class Meta:
        model = ItemGroup
        fields = '__all__'
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Table
#--------------------------------------------------------------------------------
class TableItemSerializer(ModelSerializer):
    class Meta:
        model = TableItem
        fields = '__all__'

class TableListSerializer(ModelSerializer):
    id = HyperlinkedIdentityField(view_name='visualisationAPI:table_detail',lookup_field='id')
    data = StringRelatedField(many=True)
    class Meta:
        model = Table
        fields = '__all__'

class TableDetailSerializer(ModelSerializer):
    data = TableItemSerializer(many=True,read_only=True)
    class Meta:
        model = Table
        fields = '__all__'
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Diagram
#--------------------------------------------------------------------------------
class GraphListSerializer(ModelSerializer):
    class Meta:
        model = Graph
        fields = '__all__'

class DiagramListSerializer(ModelSerializer):
    id = HyperlinkedIdentityField(view_name='visualisationAPI:diagram_detail',lookup_field='id')
    data = StringRelatedField(many=True)
    class Meta:
        model = Diagram
        fields = '__all__'

class DiagramDetailSerializer(ModelSerializer):
    data = GraphListSerializer(many=True,read_only=True)
    class Meta:
        model = Diagram
        fields = '__all__'
#--------------------------------------------------------------------------------

