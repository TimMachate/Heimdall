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
from documentationmanagement.direction.models import Direction
from documentationmanagement.file.models import DirectionProxy
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from documentationmanagement.direction.api.serializers import DirectionListSerializer, DirectionDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class DirectionListAPIView(ListCreateAPIView):
    serializer_class = DirectionListSerializer
    queryset = DirectionProxy.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact'],
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class DirectionDetailAPIView(RetrieveAPIView):
    serializer_class = DirectionDetailSerializer
    queryset=DirectionProxy.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "direction"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

    #def get_object(self):
    #    result = DirectionProxy.objects.get(id=Direction.objects.get(slug=self.kwargs.get('direction')).file_id.id)
    #    return result
#--------------------------------------------------------------------------------