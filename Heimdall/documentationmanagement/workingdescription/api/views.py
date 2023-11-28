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
from documentationmanagement.workingdescription.models import WorkingDescription
from documentationmanagement.file.models import WorkingDescriptionProxy
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from documentationmanagement.workingdescription.api.serializers import WorkingDescriptionListSerializer, WorkingDescriptionDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class WorkingDescriptionListAPIView(ListCreateAPIView):
    serializer_class = WorkingDescriptionListSerializer
    queryset = WorkingDescriptionProxy.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact'],
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class WorkingDescriptionDetailAPIView(RetrieveAPIView):
    serializer_class = WorkingDescriptionDetailSerializer
    queryset=WorkingDescriptionProxy.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "workingdescription"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

    #def get_object(self):
    #    result = WorkingDescriptionProxy.objects.get(id=WorkingDescription.objects.get(slug=self.kwargs.get('workingdescription')).file_id.id)
    #    return result
#--------------------------------------------------------------------------------