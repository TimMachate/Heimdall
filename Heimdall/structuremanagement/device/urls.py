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
    DeviceView,
    DeviceListView,
    DeviceTableView,
    DeviceCreateUpdateDetailView,
    DeviceDeleteView,
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Device
    path('',DeviceView.as_view(), name='device_overview'),
    path('list/',DeviceListView.as_view(), name='device_list'),
    path('table/',DeviceTableView.as_view(), name='device_table'),
    path('create/',DeviceCreateUpdateDetailView.as_view(), name='device_create'),
    path('update/<slug:device>/',DeviceCreateUpdateDetailView.as_view(), name='device_update'),
    path('detail/<slug:device>/',DeviceCreateUpdateDetailView.as_view(), name='device_detail'),
    path('detail/<slug:device>/error/data/',DeviceView.as_view(), name='device_errordata_overview'),
    path('detail/<slug:device>/error/data/create/',DeviceView.as_view(), name='device_errordata_create'),
    path('detail/<slug:device>/error/data/list/',DeviceView.as_view(), name='device_errordata_table'),
    path('detail/<slug:device>/error/data/table/',DeviceView.as_view(), name='device_errordata_table'),
    path('detail/<slug:device>/maintenance/',DeviceView.as_view(), name='device_maintenancedata_overview'),
    path('detail/<slug:device>/maintenance/create/',DeviceView.as_view(), name='device_maintenancedata_create'),
    path('detail/<slug:device>/maintenance/list/',DeviceView.as_view(), name='device_maintenancedata_list'),
    path('detail/<slug:device>/maintenance/table/',DeviceView.as_view(), name='device_maintenancedata_table'),
    path('detail/<slug:device>/process/data/',DeviceView.as_view(), name='device_processdata_overview'),
    path('detail/<slug:device>/process/data/create/',DeviceView.as_view(), name='device_processdata_create'),
    path('detail/<slug:device>/process/data/list/',DeviceView.as_view(), name='device_processdata_list'),
    path('detail/<slug:device>/process/data/table/',DeviceView.as_view(), name='device_processdata_table'),
    path('detail/<slug:device>/status/data/',DeviceView.as_view(), name='device_statusdata_overview'),
    path('detail/<slug:device>/status/data/create/',DeviceView.as_view(), name='device_statusdata_create'),
    path('detail/<slug:device>/status/data/list/',DeviceView.as_view(), name='device_statusdata_list'),
    path('detail/<slug:device>/status/data/table/',DeviceView.as_view(), name='device_statusdata_table'),
    path('delete/<slug:device>/',DeviceDeleteView.as_view(), name='device_delete'),
]