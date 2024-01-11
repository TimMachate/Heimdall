"""
#--------------------------------------------------------------------------------
# Url File from Model Storage
# 03.11.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.storage.views import (
    StorageView,
    StorageListView,
    StorageTableView,
    StorageCreateView,
    StorageDeleteView,
    StorageDetailView,
    StorageUpdateView,
    StorageUnloadView,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
urlpatterns = [
    # StorageItem
    path('',StorageView.as_view(), name='storage_overview'),
    path('list/',StorageListView.as_view(), name='storage_list'),
    path('table/',StorageTableView.as_view(), name='storage_table'),
    path('create/',StorageCreateView.as_view(), name='storage_create'),
    path('delete/<slug:storage>/',StorageDeleteView.as_view(), name='storage_delete'),
    path('detail/<slug:storage>/',StorageDetailView.as_view(), name='storage_detail'),
    path('unload/<slug:storage>/',StorageUnloadView.as_view(), name='storage_unload'),
    path('update/<slug:storage>/',StorageUpdateView.as_view(), name='storage_update'),
]
#--------------------------------------------------------------------------------
