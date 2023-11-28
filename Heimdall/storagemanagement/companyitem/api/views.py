#--------------------------------------------------------------------------------
# Views File from Model CompanyItem API
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from storagemanagement.api.pagination import PageNumberPagination
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.companyitem.models import CompanyItem
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from storagemanagement.companyitem.api.serializers import CompanyItemListSerializer,CompanyItemDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class CompanyItemListAPIView(ListCreateAPIView):
    serializer_class = CompanyItemListSerializer
    queryset = CompanyItem.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = {
        'name':['exact'],
        'item_number':['exact'],
        'company__name':['exact'],
        'company__slug':['exact'],
        'storageitem__name':['exact'],
        'storageitem__slug':['exact'],
        }
    search_fields = ['name','item_number','company__name','storageitem__name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class CompanyItemDetailAPIView(RetrieveAPIView):
    serializer_class = CompanyItemDetailSerializer
    queryset = CompanyItem.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "companyitem"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------