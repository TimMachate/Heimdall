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
from documentationmanagement.general.views import (
    GeneralListView,
    GeneralTableView,
    GeneralCreateUpdateDetailView,
    GeneralDeleteView
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Dateien
    path('',FileView.as_view(), name='general_overview'),
    path('list/',GeneralListView.as_view(), name='general_list'),
    path('table/',GeneralTableView.as_view(), name='general_table'),
    path('create/',GeneralCreateUpdateDetailView.as_view(), name='general_create'),
    path('update/<slug:general>/',GeneralCreateUpdateDetailView.as_view(), name='general_update'),
    path('detail/<slug:general>/',GeneralCreateUpdateDetailView.as_view(), name='general_detail'),
    path('delete/<slug:general>/',GeneralDeleteView.as_view(), name='general_delete'),
]