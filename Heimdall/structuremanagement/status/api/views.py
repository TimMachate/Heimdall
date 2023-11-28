#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from structuremanagement.api.pagination import PageNumberPagination
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from structuremanagement.status.models import Status, StatusData
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from structuremanagement.status.api.serializers import StatusListSerializer,StatusDetailSerializer, StatusDataListSerializer,StatusDataDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class StatusListAPIView(ListCreateAPIView):
    serializer_class = StatusListSerializer
    queryset = Status.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact'],
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class StatusDetailAPIView(RetrieveAPIView):
    serializer_class = StatusDetailSerializer
    queryset = Status.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "status"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class StatusDataListAPIView(ListCreateAPIView):
    serializer_class = StatusDataListSerializer
    queryset = StatusData.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'device_id':['exact'],
        'status_id':['exact'],
        'device_id__slug':['exact'],
        'status_id__slug':['exact'],
        }
    search_fields = ['device_id','status_id']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class StatusDataDetailAPIView(RetrieveAPIView):
    serializer_class = StatusDataDetailSerializer
    queryset = StatusData.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "statusdata"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]