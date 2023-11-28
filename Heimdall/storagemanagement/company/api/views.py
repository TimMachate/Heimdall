#--------------------------------------------------------------------------------
# Views File from Model Company API
# 28.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.apps import apps
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from storagemanagement.api.pagination import PageNumberPagination
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.company.models import Company
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from storagemanagement.company.api.serializers import CompanyListSerializer,CompanyDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class CompanyListAPIView(ListCreateAPIView):
    serializer_class = CompanyListSerializer
    queryset = Company.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact']
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class CompanyDetailAPIView(RetrieveAPIView):
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "company"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------