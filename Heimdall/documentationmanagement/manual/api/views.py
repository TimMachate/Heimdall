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
from documentationmanagement.manual.models import Manual
from documentationmanagement.file.models import ManualProxy
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from documentationmanagement.manual.api.serializers import ManualListSerializer, ManualDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class ManualListAPIView(ListCreateAPIView):
    serializer_class = ManualListSerializer
    queryset = ManualProxy.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact'],
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class ManualDetailAPIView(RetrieveAPIView):
    serializer_class = ManualDetailSerializer
    queryset=ManualProxy.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "manual"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

    #def get_object(self):
    #    result = ManualProxy.objects.get(id=Manual.objects.get(slug=self.kwargs.get('manual')).file_id.id)
    #    return result
#--------------------------------------------------------------------------------