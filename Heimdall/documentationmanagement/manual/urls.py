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
from documentationmanagement.manual.views import (
    ManualListView,
    ManualTableView,
    ManualCreateUpdateDetailView,
    ManualDeleteView
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Dateien
    path('',FileView.as_view(), name='manual_overview'),
    path('list/',ManualListView.as_view(), name='manual_list'),
    path('table/',ManualTableView.as_view(), name='manual_table'),
    path('create/',ManualCreateUpdateDetailView.as_view(), name='manual_create'),
    path('update/<slug:manual>/',ManualCreateUpdateDetailView.as_view(), name='manual_update'),
    path('detail/<slug:manual>/',ManualCreateUpdateDetailView.as_view(), name='manual_detail'),
    path('delete/<slug:manual>/',ManualDeleteView.as_view(), name='manual_delete'),
]