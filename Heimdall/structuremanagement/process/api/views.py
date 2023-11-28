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
from structuremanagement.process.models import Process, ProcessData
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from structuremanagement.process.api.serializers import ProcessListSerializer, ProcessDetailSerializer, ProcessDataListSerializer, ProcessDataDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class ProcessListAPIView(ListCreateAPIView):
    serializer_class = ProcessListSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact'],
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        result = Process.objects.all()
        return result
#--------------------------------------------------------------------------------
class ProcessDetailAPIView(RetrieveAPIView):
    serializer_class = ProcessDetailSerializer
    queryset = Process.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "process"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class ProcessDataListAPIView(ListCreateAPIView):
    serializer_class = ProcessDataListSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'process_id__name':['exact'],
        'device_id__name':['exact'],
        'process_id__slug':['exact'],
        'device_id__slug':['exact'],
        'count':['gte', 'lte', 'exact', 'gt', 'lt'],
        'begin_datetime':['gte', 'lte', 'exact', 'gt', 'lt'],
        'end_datetime':['gte', 'lte', 'exact', 'gt', 'lt'],
        }
    search_fields = ['process_id__name','device_id__name','count']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        result = ProcessData.objects.all()
        if self.kwargs.get('device'):
            result = result.filter(device_id__slug=self.kwargs.get('device'))
        if self.kwargs.get('process'):
            result = result.filter(process_id__slug=self.kwargs.get('process'))
        return result
#--------------------------------------------------------------------------------
class ProcessDataDetailAPIView(RetrieveAPIView):
    serializer_class = ProcessDataListSerializer
    queryset = ProcessData.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "processdata"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------