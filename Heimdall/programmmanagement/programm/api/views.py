"""
#--------------------------------------------------------------------------------
# Views File from Model Programm API
# 18.12.2023
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
from programmmanagement.programm.models import Programm
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from programmmanagement.programm.api.serializers import (
    ProgrammListSerializer,
    ProgrammDetailSerializer
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class ProgrammListAPIView(ListCreateAPIView):
    """
    ProgrammListAPIView

    Args:
        ListCreateAPIView (_type_): _description_
    """
    serializer_class = ProgrammListSerializer
    queryset = Programm.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact']
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class ProgrammDetailAPIView(RetrieveAPIView):
    """
    ProgrammDetailAPIView

    Args:
        RetrieveAPIView (_type_): _description_
    """
    serializer_class = ProgrammDetailSerializer
    queryset = Programm.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "programm"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
