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
from documentationmanagement.picture.models import Picture
from documentationmanagement.file.models import PictureProxy
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from documentationmanagement.picture.api.serializers import PictureListSerializer, PictureDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class PictureListAPIView(ListCreateAPIView):
    serializer_class = PictureListSerializer
    queryset = PictureProxy.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact'],
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class PictureDetailAPIView(RetrieveAPIView):
    serializer_class = PictureDetailSerializer
    queryset=PictureProxy.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "picture"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

    #def get_object(self):
    #    result = PictureProxy.objects.get(id=Picture.objects.get(slug=self.kwargs.get('picture')).file_id.id)
    #    return result
#--------------------------------------------------------------------------------