"""
#--------------------------------------------------------------------------------
# Views File from Model Offer API
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
from storagemanagement.offer.models import Offer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from storagemanagement.offer.api.serializers import (
    OfferListSerializer,
    OfferDetailSerializer
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class OfferListAPIView(ListAPIView):
    """
    OfferListAPIView

    Args:
        ListAPIView (_type_): _description_
    """
    serializer_class = OfferListSerializer
    ordering = ('-create_datetime',)
    queryset = Offer.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = {
        'done':['exact']
    }
    search_fields = ['company_name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class OfferDetailAPIView(RetrieveAPIView):
    """
    OfferDetailAPIView

    Args:
        RetrieveAPIView (_type_): _description_
    """
    serializer_class = OfferDetailSerializer
    queryset = Offer.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "offer"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
