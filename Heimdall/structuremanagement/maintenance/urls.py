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
    MaintenanceView,
    MaintenanceListView,
    MaintenanceTableView,
    MaintenanceCreateUpdateDetailView,
    MaintenanceDeleteView,
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Maintenance
    path('',MaintenanceView.as_view(), name='maintenance_overview'),
    path('list/',MaintenanceListView.as_view(), name='maintenance_list'),
    path('table/',MaintenanceTableView.as_view(), name='maintenance_table'),
    path('create/',MaintenanceCreateUpdateDetailView.as_view(), name='maintenance_create'),
    path('update/<slug:maintenance>/',MaintenanceCreateUpdateDetailView.as_view(), name='maintenance_update'),
    path('detail/<slug:maintenance>/',MaintenanceCreateUpdateDetailView.as_view(), name='maintenance_detail'),
    path('detail/<slug:maintenance>/data/list/',MaintenanceCreateUpdateDetailView.as_view(), name='maintenance_maintenancedata_list'),
    path('delete/<slug:maintenance>/',MaintenanceDeleteView.as_view(), name='maintenance_delete'),

    path('data/list/',MaintenanceCreateUpdateDetailView.as_view(), name='maintenancedata_list'),
]