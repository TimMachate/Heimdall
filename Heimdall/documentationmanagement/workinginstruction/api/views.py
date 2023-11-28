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
from documentationmanagement.workinginstruction.models import WorkingInstruction
from documentationmanagement.file.models import WorkingInstructionProxy
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from documentationmanagement.workinginstruction.api.serializers import WorkingInstructionListSerializer, WorkingInstructionDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class WorkingInstructionListAPIView(ListCreateAPIView):
    serializer_class = WorkingInstructionListSerializer
    queryset = WorkingInstructionProxy.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = {
        'name':['exact'],
        }
    search_fields = ['name']
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class WorkingInstructionDetailAPIView(RetrieveAPIView):
    serializer_class = WorkingInstructionDetailSerializer
    queryset=WorkingInstructionProxy.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "workinginstruction"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

    #def get_object(self):
    #    result = WorkingInstructionProxy.objects.get(id=WorkingInstruction.objects.get(slug=self.kwargs.get('workinginstruction')).file_id.id)
    #    return result
#--------------------------------------------------------------------------------