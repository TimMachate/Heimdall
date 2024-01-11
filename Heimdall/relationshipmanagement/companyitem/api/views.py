"""
#--------------------------------------------------------------------------------
# Views File from Model CompanyItem API
# 16.12.2023
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
from relationshipmanagement.companyitem.models import CompanyItem
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from relationshipmanagement.companyitem.api.serializers import (
    CompanyItemListSerializer,
    CompanyItemDetailSerializer
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class CompanyItemListAPIView(ListCreateAPIView):
    """
    CompanyItemListAPIView

    Args:
        ListCreateAPIView (_type_): _description_
    """
    serializer_class = CompanyItemListSerializer
    queryset = CompanyItem.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = {
        'name':['exact'],
        'item_number':['exact'],
        'company__name':['exact'],
        'company__slug':['exact'],
        }
    search_fields = ['name','item_number','company__name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class CompanyItemDetailAPIView(RetrieveAPIView):
    """
    CompanyItemDetailAPIView

    Args:
        RetrieveAPIView (_type_): _description_
    """
    serializer_class = CompanyItemDetailSerializer
    queryset = CompanyItem.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "companyitem"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
