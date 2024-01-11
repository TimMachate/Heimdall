"""
#--------------------------------------------------------------------------------
# Views File from Model Company API
# 16.12.2023
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
from relationshipmanagement.company.models import Company
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from relationshipmanagement.company.api.serializers import (
    CompanyListSerializer,
    CompanyDetailSerializer
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class CompanyListAPIView(ListCreateAPIView):
    """
    CompanyListAPIView

    Args:
        ListCreateAPIView (_type_): _description_
    """
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
    """
    CompanyDetailAPIView

    Args:
        RetrieveAPIView (_type_): _description_
    """
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "company"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
