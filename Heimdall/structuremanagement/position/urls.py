#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Views
#--------------------------------------------------------------------------------
from .views import (
    PositionView,
    PositionListView,
    PositionTableView,
    PositionCreateUpdateDetailView,
    PositionDeleteView,
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Position
    path('',PositionView.as_view(), name='position_overview'),
    path('list/',PositionListView.as_view(), name='position_list'),
    path('table/',PositionTableView.as_view(), name='position_table'),
    path('create/',PositionCreateUpdateDetailView.as_view(), name='position_create'),
    path('update/<slug:position>/',PositionCreateUpdateDetailView.as_view(), name='position_update'),
    path('detail/<slug:position>/',PositionCreateUpdateDetailView.as_view(), name='position_detail'),
    path('delete/<slug:position>/',PositionDeleteView.as_view(), name='position_delete'),
]