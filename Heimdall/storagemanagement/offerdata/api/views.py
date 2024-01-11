"""
#--------------------------------------------------------------------------------
# Views File from Model Offer Data API
# 09.11.2023
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
from storagemanagement.offerdata.models import OfferData
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from storagemanagement.offerdata.api.serializers import (
    OfferDataListSerializer,
    OfferDataDetailSerializer
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class OfferDataListAPIView(ListAPIView):
    """
    OfferDataListAPIView

    Args:
        ListAPIView (_type_): _description_
    """
    serializer_class = OfferDataListSerializer
    ordering = ('-create_datetime',)
    queryset = OfferData.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = {
        'companyitem__company__slug':['exact'],
        'companyitem__slug':['exact'],
        'companyitem__storageitem__slug':['exact'],
        'authorized':['exact'],
        'done':['exact']
        }
    search_fields = [
        'companyitem__name',
        'companyitem__company__name',
        'companyitem__storageitem__name'
    ]
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class OfferDataDetailAPIView(RetrieveAPIView):
    """
    OfferDataDetailAPIView

    Args:
        RetrieveAPIView (_type_): _description_
    """
    serializer_class = OfferDataDetailSerializer
    queryset = OfferData.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "offerdata"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
