#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.general.views import (
    GeneralView,
    GeneralListView,
    GeneralTableView,
    GeneralCreateView,
    GeneralDetailView,
    GeneralUpdateView,
    GeneralDeleteView
)
#--------------------------------------------------------------------------------
urlpatterns = [
    # General
    path('',GeneralView.as_view(), name='general_overview'),
    path('list/',GeneralListView.as_view(), name='general_list'),
    path('table/',GeneralTableView.as_view(), name='general_table'),
    path('create/',GeneralCreateView.as_view(), name='general_create'),
    path('update/<slug:general>/',GeneralUpdateView.as_view(), name='general_update'),
    path('detail/<slug:general>/',GeneralDetailView.as_view(), name='general_detail'),
    path('delete/<slug:general>/',GeneralDeleteView.as_view(), name='general_delete'),
]
#--------------------------------------------------------------------------------