"""
#--------------------------------------------------------------------------------
# Views File from Model CompanyContact API
# 16.12.2023
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
from relationshipmanagement.companycontact.models import CompanyContact
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from relationshipmanagement.companycontact.api.serializers import (
    CompanyContactListSerializer,
    CompanyContactDetailSerializer
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class CompanyContactListAPIView(ListAPIView):
    """
    CompanyContactListAPIView

    Args:
        ListAPIView (_type_): _description_
    """
    serializer_class = CompanyContactListSerializer
    queryset = CompanyContact.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = {
        'last_name':['exact'],
        'first_name':['exact'],
        'company__slug':['exact'],
        }
    search_fields = ['last_name','first_name','company__name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class CompanyContactDetailAPIView(RetrieveAPIView):
    """
    CompanyContactDetailAPIView

    Args:
        RetrieveAPIView (_type_): _description_
    """
    serializer_class = CompanyContactDetailSerializer
    queryset = CompanyContact.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "companycontact"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
