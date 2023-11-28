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
    ProcessView,
    ProcessListView,
    ProcessTableView,
    ProcessCreateUpdateDetailView,
    ProcessDeleteView,

    ProcessDataView,
    ProcessDataListView,
    ProcessDataTableView,
    ProcessDataDetailView,
    ProcessDataCreateView,
    ProcessDataUpdateView,
    ProcessDataUpdateEndTimeView,
    ProcessDataUpdateBeginTimeView,
    ProcessDataUpdateCountView,
    ProcessDataDeleteView
    )
#--------------------------------------------------------------------------------
urlpatterns = [
    # Process
    path('',ProcessView.as_view(), name='process_overview'),
    path('list/',ProcessListView.as_view(), name='process_list'),
    path('table/',ProcessTableView.as_view(), name='process_table'),
    path('create/',ProcessCreateUpdateDetailView.as_view(), name='process_create'),
    path('update/<slug:process>/',ProcessCreateUpdateDetailView.as_view(), name='process_update'),
    path('detail/<slug:process>/',ProcessCreateUpdateDetailView.as_view(), name='process_detail'),
    path('detail/<slug:process>/processdata/',ProcessDataView.as_view(), name='process_processdata_overview'),
    path('detail/<slug:process>/processdata/create/',ProcessDataCreateView.as_view(), name='process_processdata_create'),
    path('detail/<slug:process>/processdata/list/',ProcessDataListView.as_view(), name='process_processdata_list'),
    path('detail/<slug:process>/processdata/table/',ProcessDataTableView.as_view(), name='process_processdata_table'),
    path('delete/<slug:process>/',ProcessDeleteView.as_view(), name='process_delete'),

    # Process Data
    path('data/',ProcessDataView.as_view(), name='processdata_overview'),
    path('data/list/',ProcessDataListView.as_view(), name='processdata_list'),
    path('data/table/',ProcessDataTableView.as_view(), name='processdata_table'),
    path('data/create/',ProcessDataCreateView.as_view(), name='processdata_create'),
    path('data/detail/<slug:processdata>/',ProcessDataDetailView.as_view(), name='processdata_detail'),
    path('data/update/<slug:processdata>/',ProcessDataUpdateView.as_view(), name='processdata_update'),
    path('data/update/<slug:processdata>/begintime/',ProcessDataUpdateBeginTimeView.as_view(), name='processdata_update_begintime'),
    path('data/update/<slug:processdata>/endtime/',ProcessDataUpdateEndTimeView.as_view(), name='processdata_update_endtime'),
    path('data/update/<slug:processdata>/count/',ProcessDataUpdateCountView.as_view(), name='processdata_update_count'),
    path('data/delete/<slug:processdata>/',ProcessDataDeleteView.as_view(), name='processdata_delete'),
]