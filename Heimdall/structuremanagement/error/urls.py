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
    ErrorView,
    ErrorListView,
    ErrorTableView,
    ErrorCreateUpdateDetailView,
    ErrorDeleteView,
    ErrorDataView,
    ErrorDataListView,
    ErrorDataTableView,
    ErrorDataCreateUpdateDetailView,
    ErrorDataDeleteView,
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Error
    path('',ErrorView.as_view(), name='error_overview'),
    path('list/',ErrorListView.as_view(), name='error_list'),
    path('table/',ErrorTableView.as_view(), name='error_table'),
    path('create/',ErrorCreateUpdateDetailView.as_view(), name='error_create'),
    path('update/<slug:error>/',ErrorCreateUpdateDetailView.as_view(), name='error_update'),
    path('detail/<slug:error>/',ErrorCreateUpdateDetailView.as_view(), name='error_detail'),
    path('detail/<slug:error>/data/',ErrorDataView.as_view(), name='error_errordata_overview'),
    path('detail/<slug:error>/data/create/',ErrorDataCreateUpdateDetailView.as_view(), name='error_errordata_create'),
    path('detail/<slug:error>/data/list/',ErrorDataListView.as_view(), name='error_errordata_list'),
    path('detail/<slug:error>/data/table/',ErrorDataTableView.as_view(), name='error_errordata_table'),
    path('delete/<slug:error>/',ErrorDeleteView.as_view(), name='error_delete'),

    # Error Data
    path('data/',ErrorDataView.as_view(), name='errordata_overview'),
    path('data/list/',ErrorDataListView.as_view(), name='errordata_list'),
    path('data/table/',ErrorDataTableView.as_view(), name='errordata_table'),
    path('data/create/',ErrorDataCreateUpdateDetailView.as_view(), name='errordata_create'),
    path('data/update/<slug:errordata>/',ErrorDataCreateUpdateDetailView.as_view(), name='errordata_update'),
    path('data/detail/<slug:errordata>/',ErrorDataCreateUpdateDetailView.as_view(), name='errordata_detail'),
    path('data/delete/<slug:errordata>/',ErrorDataDeleteView.as_view(), name='errordata_delete'),
]