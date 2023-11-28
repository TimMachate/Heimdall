#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.ware.views import (
    WareView,
    WareListView,
    WareTableView,
    WareCreateView,
    WareDetailView,
    WareUpdateView,
    WareDeleteView
)
#--------------------------------------------------------------------------------
urlpatterns = [
    # Ware
    path('',WareView.as_view(), name='ware_overview'),
    path('list/',WareListView.as_view(), name='ware_list'),
    path('table/',WareTableView.as_view(), name='ware_table'),
    path('create/',WareCreateView.as_view(), name='ware_create'),
    path('update/<slug:ware>/',WareUpdateView.as_view(), name='ware_update'),
    path('detail/<slug:ware>/',WareDetailView.as_view(), name='ware_detail'),
    path('detail/<slug:ware>/request/',WareDetailView.as_view(), name='ware_request_add'),
    path('delete/<slug:ware>/',WareDeleteView.as_view(), name='ware_delete'),
]
#--------------------------------------------------------------------------------