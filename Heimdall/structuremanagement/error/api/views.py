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
from structuremanagement.error.models import Error,ErrorData
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from structuremanagement.error.api.serializers import ErrorListSerializer,ErrorDetailSerializer,ErrorDataListSerializer,ErrorDataDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class ErrorListAPIView(ListCreateAPIView):
    serializer_class = ErrorListSerializer
    queryset = Error.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact'],
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class ErrorDetailAPIView(RetrieveAPIView):
    serializer_class = ErrorDetailSerializer
    queryset = Error.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "error"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class ErrorDataListAPIView(ListCreateAPIView):
    serializer_class = ErrorDataListSerializer
    queryset = ErrorData.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'device_id':['exact'],
        'error_id':['exact'],
        'device_id__slug':['exact'],
        'error_id__slug':['exact'],
        }
    search_fields = ['device_id','error_id']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class ErrorDataDetailAPIView(RetrieveAPIView):
    serializer_class = ErrorDataDetailSerializer
    queryset = ErrorData.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "errordata"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------