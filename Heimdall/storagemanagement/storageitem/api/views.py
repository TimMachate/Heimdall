"""
#--------------------------------------------------------------------------------
# Views File from Model Supplier API
# 28.10.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.storageitem.models import StorageItem
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from storagemanagement.storageitem.api.serializers import (
    StorageItemListSerializer,
    StorageItemDetailSerializer
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class StorageItemListAPIView(ListCreateAPIView):
    """
    StorageItemListAPIView

    Args:
        ListCreateAPIView (_type_): _description_
    """
    serializer_class = StorageItemListSerializer
    queryset = StorageItem.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {}
    search_fields = ['name','company','status']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class StorageItemDetailAPIView(RetrieveAPIView):
    """
    StorageItemDetailAPIView

    Args:
        RetrieveAPIView (_type_): _description_
    """
    serializer_class = StorageItemDetailSerializer
    queryset = StorageItem.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "storageitem"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
