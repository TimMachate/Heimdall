from django.apps                    import apps
from django.db.models.query import QuerySet
from django.http                    import HttpResponse, JsonResponse
from rest_framework.views           import APIView
from rest_framework                 import authentication, status
from django.http                    import Http404

from rest_framework.permissions     import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

from rest_framework.filters         import (
    SearchFilter,
    OrderingFilter
)

from rest_framework.generics        import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)

from .pagination import PageNumberPagination

#from Storage.models import Stock
from .serializers                   import (
    ItemGroupListSerializer,
    ItemGroupDetailSerializer,
    TableListSerializer,
    TableDetailSerializer,
    DiagramListSerializer,
    DiagramDetailSerializer,
)

#import Models from other Apps
from visualisation.models                 import (
    ItemGroup,
    Table,
    Diagram,
)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Item
#--------------------------------------------------------------------------------
class ItemGroupListAPIView(ListAPIView):
    queryset = ItemGroup.objects.all()
    serializer_class = ItemGroupListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = []
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

class ItemGroupDetailAPIView(RetrieveUpdateAPIView):
    queryset = ItemGroup.objects.all()
    lookup_field = 'id'
    serializer_class = ItemGroupDetailSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = []
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Table
#--------------------------------------------------------------------------------
class TableListAPIView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = []
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

class TableDetailAPIView(RetrieveUpdateAPIView):
    queryset = Table.objects.all()
    lookup_field = 'id'
    serializer_class = TableDetailSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = []
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Diagram
#--------------------------------------------------------------------------------
class DiagramListAPIView(ListAPIView):
    queryset = Diagram.objects.all()
    serializer_class = DiagramListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = []
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]

class DiagramDetailAPIView(RetrieveUpdateAPIView):
    queryset = Diagram.objects.all()
    lookup_field = 'id'
    serializer_class = DiagramDetailSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = []
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------