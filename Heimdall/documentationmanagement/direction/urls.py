#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Views
#--------------------------------------------------------------------------------
from documentationmanagement.file.views import (
    FileView
)
from documentationmanagement.direction.views import (
    DirectionListView,
    DirectionTableView,
    DirectionCreateUpdateDetailView,
    DirectionDeleteView
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Dateien
    path('',FileView.as_view(), name='direction_overview'),
    path('list/',DirectionListView.as_view(), name='direction_list'),
    path('table/',DirectionTableView.as_view(), name='direction_table'),
    path('create/',DirectionCreateUpdateDetailView.as_view(), name='direction_create'),
    path('update/<slug:direction>/',DirectionCreateUpdateDetailView.as_view(), name='direction_update'),
    path('detail/<slug:direction>/',DirectionCreateUpdateDetailView.as_view(), name='direction_detail'),
    path('delete/<slug:direction>/',DirectionDeleteView.as_view(), name='direction_delete'),
]