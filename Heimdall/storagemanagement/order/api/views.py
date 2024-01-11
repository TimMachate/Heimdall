"""
#--------------------------------------------------------------------------------
# Views File from Model Order API
# 09.11.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.order.models import Order
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Serializers
#--------------------------------------------------------------------------------
from storagemanagement.order.api.serializers import OrderListSerializer,OrderDetailSerializer
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class OrderListAPIView(ListAPIView):
    """
    OrderListAPIView

    Args:
        ListAPIView (_type_): _description_
    """
    serializer_class = OrderListSerializer
    ordering = ('-create_datetime',)
    queryset = Order.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = {}
    search_fields = []
    pagination_class = None
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
class OrderDetailAPIView(RetrieveAPIView):
    """
    OrderDetailAPIView

    Args:
        RetrieveAPIView (_type_): _description_
    """
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
    pagination_class = None
    lookup_field = "slug"
    lookup_url_kwarg = "order"
    #permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
#--------------------------------------------------------------------------------
