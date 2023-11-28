#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView,ListCreateAPIView, RetrieveAPIView
from documentationmanagement.api.pagination import PageNumberPagination
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.protocol.models import Protocol, ProtocolData, Variable
from documentationmanagement.file.models import ProtocolProxy
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from documentationmanagement.protocol.api.serializers import (
    ProtocolListSerializer,
    ProtocolDetailSerializer,
    ProtocolDataListSerializer,
    ProtocolDataDetailSerializer,
    VariableListSerializer,
    VariableDetailSerializer
    )
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class ProtocolListAPIView(ListCreateAPIView):
    serializer_class = ProtocolListSerializer
    queryset = Protocol.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'file_id__name':['exact'],
        }
    search_fields = ['file_id__name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class ProtocolDetailAPIView(RetrieveAPIView):
    serializer_class = ProtocolDetailSerializer
    queryset=Protocol.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "protocol"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

    #def get_object(self):
    #    result = ProtocolProxy.objects.get(id=Protocol.objects.get(slug=self.kwargs.get('protocol')).file_id.id)
    #    return result
#--------------------------------------------------------------------------------
class ProtocolDataListAPIView(ListCreateAPIView):
    serializer_class = ProtocolDataListSerializer
    queryset = ProtocolData.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'protocol_id':['exact'],
        'protocol_id__slug':['exact'],
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        result = ProtocolData.objects.all()
        if self.request.query_params.get('begin'):
            begin = timezone.datetime.strptime(self.request.query_params.get('begin'),"%Y-%m-%d %H:%S")
            result = result.filter(create_datetime__gte = begin)
        if self.request.query_params.get('end'):
            end = timezone.datetime.strptime(self.request.query_params.get('end'),"%Y-%m-%d %H:%S")
            result = result.filter(create_datetime__lte = end)
        result = result.order_by('-create_datetime')
        return result

#--------------------------------------------------------------------------------
class ProtocolDataDetailAPIView(RetrieveAPIView):
    serializer_class = ProtocolDataDetailSerializer
    queryset=ProtocolData.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "protocoldata"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class VariableListAPIView(ListCreateAPIView):
    serializer_class = VariableListSerializer
    queryset = Variable.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['contains'],
        'symbol':['exact'],
        'unit':['contains'],
        'name':['contains'],
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class VariableDetailAPIView(RetrieveAPIView):
    serializer_class = VariableDetailSerializer
    queryset=Variable.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "variable"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------