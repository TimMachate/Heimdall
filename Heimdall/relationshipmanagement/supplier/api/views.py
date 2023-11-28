#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from relationshipmanagement.api.pagination import PageNumberPagination
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.company.models import SupplierProxy
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from relationshipmanagement.supplier.api.serializers import SupplierListSerializer,SupplierDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class SupplierListAPIView(ListCreateAPIView):
    serializer_class = SupplierListSerializer
    queryset = SupplierProxy.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact']
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class SupplierDetailAPIView(RetrieveAPIView):
    serializer_class = SupplierDetailSerializer
    queryset = SupplierProxy.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "supplier"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------