"""
#--------------------------------------------------------------------------------
# Views File from Model Booking API
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
from storagemanagement.booking.models import Booking
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from storagemanagement.booking.api.serializers import (
    BookingListSerializer,
    BookingDetailSerializer
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class BookingListAPIView(ListAPIView):
    """
    BookingListApiView
    Responsible for the List API View
    """
    serializer_class = BookingListSerializer
    ordering = ('-create_datetime',)
    queryset = Booking.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = {
        'supplieritem__company__slug':['exact'],
        'supplieritem__slug':['exact'],
        #'supplieritem__storageitem__slug':['exact']
        }
    search_fields = [
        'supplieritem',
        'supplieritem__supplier__name',
        #'supplieritem_storageitem__name'
    ]
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class BookingDetailAPIView(RetrieveAPIView):
    """
    BookingDetailAPIView
    Responsible for the Detail API View
    """
    serializer_class = BookingDetailSerializer
    queryset = Booking.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "booking"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
