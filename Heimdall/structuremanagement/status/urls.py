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
    StatusView,
    StatusListView,
    StatusTableView,
    StatusCreateUpdateDetailView,
    StatusDeleteView,
    StatusDataView,
    StatusDataListView,
    StatusDataTableView,
    StatusDataCreateUpdateDetailView,
    StatusDataDeleteView,
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Status
    path('',StatusView.as_view(), name='status_overview'),
    path('list/',StatusListView.as_view(), name='status_list'),
    path('table/',StatusTableView.as_view(), name='status_table'),
    path('create/',StatusCreateUpdateDetailView.as_view(), name='status_create'),
    path('update/<slug:status>/',StatusCreateUpdateDetailView.as_view(), name='status_update'),
    path('detail/<slug:status>/',StatusCreateUpdateDetailView.as_view(), name='status_detail'),
    path('detail/<slug:status>/data/',StatusDataView.as_view(), name='status_statusdata_overview'),
    path('detail/<slug:status>/data/list/',StatusDataListView.as_view(), name='status_statusdata_list'),
    path('detail/<slug:status>/data/table/',StatusDataTableView.as_view(), name='status_statusdata_table'),
    path('detail/<slug:status>/data/create/',StatusDataCreateUpdateDetailView.as_view(), name='status_statusdata_create'),
    path('delete/<slug:status>/',StatusDeleteView.as_view(), name='status_delete'),

    # Status Data
    path('data/',StatusDataView.as_view(), name='statusdata_overview'),
    path('data/list/',StatusDataListView.as_view(), name='statusdata_list'),
    path('data/table/',StatusDataTableView.as_view(), name='statusdata_table'),
    path('data/create/',StatusDataCreateUpdateDetailView.as_view(), name='statusdata_create'),
    path('data/detail/<slug:statusdata>/',StatusDataCreateUpdateDetailView.as_view(), name='statusdata_detail'),
    path('data/update/<slug:statusdata>/',StatusDataCreateUpdateDetailView.as_view(), name='statusdata_update'),
    path('data/delete/<slug:statusdata>/',StatusDataDeleteView.as_view(), name='statusdata_delete'),
]