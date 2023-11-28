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
from documentationmanagement.safetydatasheet.models import SafetyDataSheet
from documentationmanagement.file.models import SafetyDataSheetProxy
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from documentationmanagement.safetydatasheet.api.serializers import SafetyDataSheetListSerializer, SafetyDataSheetDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class SafetyDataSheetListAPIView(ListCreateAPIView):
    serializer_class = SafetyDataSheetListSerializer
    queryset = SafetyDataSheetProxy.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact'],
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class SafetyDataSheetDetailAPIView(RetrieveAPIView):
    serializer_class = SafetyDataSheetDetailSerializer
    queryset=SafetyDataSheetProxy.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "safetydatasheet"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

    #def get_object(self):
    #    result = SafetyDataSheetProxy.objects.get(id=SafetyDataSheet.objects.get(slug=self.kwargs.get('safetydatasheet')).file_id.id)
    #    return result
#--------------------------------------------------------------------------------