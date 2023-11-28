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
from documentationmanagement.processinstruction.models import ProcessInstruction
from documentationmanagement.file.models import ProcessInstructionProxy
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from documentationmanagement.processinstruction.api.serializers import ProcessInstructionListSerializer, ProcessInstructionDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class ProcessInstructionListAPIView(ListCreateAPIView):
    serializer_class = ProcessInstructionListSerializer
    queryset = ProcessInstructionProxy.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact'],
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class ProcessInstructionDetailAPIView(RetrieveAPIView):
    serializer_class = ProcessInstructionDetailSerializer
    queryset=ProcessInstructionProxy.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "processinstruction"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

    #def get_object(self):
    #    result = ProcessInstructionProxy.objects.get(id=ProcessInstruction.objects.get(slug=self.kwargs.get('processinstruction')).file_id.id)
    #    return result
#--------------------------------------------------------------------------------