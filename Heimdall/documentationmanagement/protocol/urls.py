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
from documentationmanagement.protocol.views import (
    ProtocolListView,
    ProtocolTableView,
    ProtocolCreateUpdateDetailView,
    ProtocolDeleteView
    )
from documentationmanagement.protocol.views import (
    ProtocolDataView,
    ProtocolDataListView,
    ProtocolDataTableView,
    ProtocolDataCreateUpdateDetailView,
    ProtocolDataDeleteView,
)
from documentationmanagement.protocol.views import (
    VariableView,
    VariableListView,
    VariableTableView,
    VariableCreateUpdateDetailView,
    VariableDeleteView,
)
#--------------------------------------------------------------------------------

urlpatterns = [
    # Protokoll
    path('',FileView.as_view(), name='protocol_overview'),
    path('list/',ProtocolListView.as_view(), name='protocol_list'),
    path('table/',ProtocolTableView.as_view(), name='protocol_table'),
    path('create/',ProtocolCreateUpdateDetailView.as_view(), name='protocol_create'),
    path('update/<slug:protocol>/',ProtocolCreateUpdateDetailView.as_view(), name='protocol_update'),
    path('detail/<slug:protocol>/',ProtocolCreateUpdateDetailView.as_view(), name='protocol_detail'),
    path('detail/<slug:protocol>/data/list/',ProtocolDataListView.as_view(), name='protocol_protocoldata_list'),
    path('detail/<slug:protocol>/data/table/',ProtocolDataTableView.as_view(), name='protocol_protocoldata_table'),
    path('detail/<slug:protocol>/data/create/',ProtocolDataCreateUpdateDetailView.as_view(), name='protocol_protocoldata_create'),
    path('delete/<slug:protocol>/',ProtocolDeleteView.as_view(), name='protocol_delete'),
    # Protokoll Data
    path('data/',ProtocolDataView.as_view(), name='protocoldata_overview'),
    path('data/list/',ProtocolDataListView.as_view(), name='protocoldata_list'),
    path('data/table/',ProtocolDataTableView.as_view(), name='protocoldata_table'),
    path('data/create/',ProtocolDataCreateUpdateDetailView.as_view(), name='protocoldata_create'),
    path('data/update/<slug:protocoldata>/',ProtocolDataCreateUpdateDetailView.as_view(), name='protocoldata_update'),
    path('data/detail/<slug:protocoldata>/',ProtocolDataCreateUpdateDetailView.as_view(), name='protocoldata_detail'),
    path('data/delete/<slug:protocoldata>/',ProtocolDataDeleteView.as_view(), name='protocoldata_delete'),
    # Variable
    path('variable/',VariableListView.as_view(), name='variable_overview'),
    path('variable/list/',VariableListView.as_view(), name='variable_list'),
    path('variable/table/',VariableTableView.as_view(), name='variable_table'),
    path('variable/create/',VariableCreateUpdateDetailView.as_view(), name='variable_create'),
    path('variable/update/<slug:variable>/',VariableCreateUpdateDetailView.as_view(), name='variable_update'),
    path('variable/detail/<slug:variable>/',VariableCreateUpdateDetailView.as_view(), name='variable_detail'),
    path('variable/delete/<slug:variable>/',VariableDeleteView.as_view(), name='variable_delete'),
]