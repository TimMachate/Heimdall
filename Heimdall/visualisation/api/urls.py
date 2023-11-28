from django.urls import path
from .views import (
    ItemGroupListAPIView,
    ItemGroupDetailAPIView,
    TableListAPIView,
    TableDetailAPIView,
    DiagramListAPIView,
    DiagramDetailAPIView,
)
app_name = 'visualisationAPI'

urlpatterns = [
    path('item/list/',ItemGroupListAPIView.as_view(), name='item_list'),
    path('item/detail/<int:id>/',ItemGroupDetailAPIView.as_view(), name='item_detail'),
    path('table/list/',TableListAPIView.as_view(), name='table_list'),
    path('table/detail/<int:id>/',TableDetailAPIView.as_view(), name='table_detail'),
    path('diagram/list/',DiagramListAPIView.as_view(), name='diagram_list'),
    path('diagram/detail/<int:id>/',DiagramDetailAPIView.as_view(), name='diagram_detail'),
]