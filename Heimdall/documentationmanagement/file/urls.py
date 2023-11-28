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
    FileView,
    FileListView,
    FileTableView,
    FileCreateUpdateDetailView,
    FileDeleteView
)
#--------------------------------------------------------------------------------

urlpatterns = [
    # Dateien
    path('',FileView.as_view(), name='file_overview'),
    path('list/',FileListView.as_view(), name='file_list'),
    path('table/',FileTableView.as_view(), name='file_table'),
    path('create/',FileCreateUpdateDetailView.as_view(), name='file_create'),
    path('update/<slug:file>/',FileCreateUpdateDetailView.as_view(), name='file_update'),
    path('detail/<slug:file>/',FileCreateUpdateDetailView.as_view(), name='file_detail'),
    path('delete/<slug:file>/',FileDeleteView.as_view(), name='file_delete'),
]