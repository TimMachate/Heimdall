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
from documentationmanagement.technicaldatasheet.models import TechnicalDataSheet
from documentationmanagement.file.models import TechnicalDataSheetProxy
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from documentationmanagement.technicaldatasheet.api.serializers import TechnicalDataSheetListSerializer, TechnicalDataSheetDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class TechnicalDataSheetListAPIView(ListCreateAPIView):
    serializer_class = TechnicalDataSheetListSerializer
    queryset = TechnicalDataSheetProxy.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact'],
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class TechnicalDataSheetDetailAPIView(RetrieveAPIView):
    serializer_class = TechnicalDataSheetDetailSerializer
    queryset=TechnicalDataSheetProxy.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "technicaldatasheet"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

    #def get_object(self):
    #    result = TechnicalDataSheetProxy.objects.get(id=TechnicalDataSheet.objects.get(slug=self.kwargs.get('technicaldatasheet')).file_id.id)
    #    return result
#--------------------------------------------------------------------------------