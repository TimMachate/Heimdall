#--------------------------------------------------------------------------------
# Views File from Model Order Data API
# 10.11.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.apps import apps
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView, RetrieveAPIView
from storagemanagement.api.pagination import PageNumberPagination
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.orderdata.models import OrderData
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from storagemanagement.orderdata.api.serializers import OrderDataListSerializer,OrderDataDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class OrderDataListAPIView(ListAPIView):
    serializer_class = OrderDataListSerializer
    ordering = ('-create_datetime')
    queryset = OrderData.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = {
        'companyitem__company__slug':['exact'],
        'companyitem__slug':['exact'],
        'companyitem__storageitem__slug':['exact'],
        'authorized':['exact'],
        'booking':['exact'],
        'done':['exact'],
        }
    search_fields = ['companyitem__name','companyitem__company__name','companyitem__storageitem__name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class OrderDataDetailAPIView(RetrieveAPIView):
    serializer_class = OrderDataDetailSerializer
    queryset = OrderData.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "orderdata"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------