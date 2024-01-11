"""
#--------------------------------------------------------------------------------
# Views File from Model Storage API
# 07.01.2024
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.storage.models import Storage
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from storagemanagement.storage.api.serializers import StorageListSerializer,StorageDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class StorageListAPIView(ListAPIView):
    """
    StorageListAPIView

    Args:
        ListAPIView (_type_): _description_
    """
    serializer_class = StorageListSerializer
    ordering = ('-create_datetime',)
    queryset = Storage.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = {
        'supplieritem__company__slug':['exact'],
        'supplieritem__slug':['exact'],
        #'supplieritem__storageitem__slug':['exact'],
        }
    search_fields = ['supplieritem']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class StorageDetailAPIView(RetrieveAPIView):
    """
    StorageDetailAPIView

    Args:
        RetrieveAPIView (_type_): _description_
    """
    serializer_class = StorageDetailSerializer
    queryset = Storage.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "storage"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
