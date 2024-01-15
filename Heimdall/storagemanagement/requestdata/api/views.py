"""
#--------------------------------------------------------------------------------
# Views File from Model Request Data API
# 05.01.2024
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from storagemanagement.api.pagination import PageNumberPagination
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.requestdata.models import RequestData
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from storagemanagement.requestdata.api.serializers import (
    RequestDataListSerializer,
    RequestDataDetailSerializer
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class RequestDataListAPIView(ListAPIView):
    """
    RequestDataListAPIView

    Args:
        ListAPIView (_type_): _description_
    """
    serializer_class = RequestDataListSerializer
    queryset = RequestData.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = {
        'supplieritem__company__slug':['exact'],
        'supplieritem__slug':['exact'],
        #'supplieritem__storageitem__slug':['exact'],
        'authorized':['exact'],
        'done':['exact'],
        }
    search_fields = [
        'supplieritem__name',
        'supplieritem__company__name',
        #'supplieritem__storageitem__name'
    ]
    pagination_class = None
#--------------------------------------------------------------------------------
class RequestDataDetailAPIView(RetrieveAPIView):
    """
    RequestDataDetailAPIView

    Args:
        RetrieveAPIView (_type_): _description_
    """
    serializer_class = RequestDataDetailSerializer
    queryset = RequestData.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "requestdata"
#--------------------------------------------------------------------------------
