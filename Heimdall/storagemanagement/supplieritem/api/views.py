"""
#--------------------------------------------------------------------------------
# Views File from Model SupplierItem API
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.supplieritem.models import SupplierItem
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from storagemanagement.supplieritem.api.serializers import (
    SupplierItemListSerializer,
    SupplierItemDetailSerializer
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class SupplierItemListAPIView(ListCreateAPIView):
    """
    SupplierItemListAPIView

    Args:
        ListCreateAPIView (_type_): _description_
    """
    serializer_class = SupplierItemListSerializer
    queryset = SupplierItem.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = {
        'name':['exact'],
        'item_number':['exact'],
        'company__name':['exact'],
        'company__slug':['exact'],
        #'storageitem__name':['exact'],
        #'storageitem__slug':['exact'],
        }
    search_fields = [
        'name',
        'item_number',
        'company__name',
        'storageitem__name'
    ]
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class SupplierItemDetailAPIView(RetrieveAPIView):
    """
    SupplierItemDetailAPIView

    Args:
        RetrieveAPIView (_type_): _description_
    """
    serializer_class = SupplierItemDetailSerializer
    queryset = SupplierItem.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "supplieritem"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
