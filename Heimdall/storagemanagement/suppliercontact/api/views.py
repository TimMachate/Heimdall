"""
#--------------------------------------------------------------------------------
# Views File from Model SupplierContact API
# 28.10.2023
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
from storagemanagement.suppliercontact.models import SupplierContact
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from storagemanagement.suppliercontact.api.serializers import (
    SupplierContactListSerializer,
    SupplierContactDetailSerializer
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class SupplierContactListAPIView(ListAPIView):
    """
    SupplierContactListAPIView

    Args:
        ListAPIView (_type_): _description_
    """
    serializer_class = SupplierContactListSerializer
    queryset = SupplierContact.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = {
        'last_name':['exact'],
        'first_name':['exact'],
        'company__slug':['exact'],
        }
    search_fields = ['last_name','first_name','supplier__name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class SupplierContactDetailAPIView(RetrieveAPIView):
    """
    SupplierContactDetailAPIView

    Args:
        RetrieveAPIView (_type_): _description_
    """
    serializer_class = SupplierContactDetailSerializer
    queryset = SupplierContact.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "suppliercontact"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
