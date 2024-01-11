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
from storagemanagement.supplier.models import Supplier
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from storagemanagement.supplier.api.serializers import (
    SupplierListSerializer,
    SupplierDetailSerializer
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class SupplierListAPIView(ListCreateAPIView):
    """
    SupplierListAPIView

    Args:
        ListCreateAPIView (_type_): _description_
    """
    serializer_class = SupplierListSerializer
    queryset = Supplier.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact']
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class SupplierDetailAPIView(RetrieveAPIView):
    """
    SupplierDetailAPIView

    Args:
        RetrieveAPIView (_type_): _description_
    """
    serializer_class = SupplierDetailSerializer
    queryset = Supplier.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "supplier"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
