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
from documentationmanagement.processinstruction.views import (
    ProcessInstructionListView,
    ProcessInstructionTableView,
    ProcessInstructionCreateUpdateDetailView,
    ProcessInstructionDeleteView
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Dateien
    path('',FileView.as_view(), name='processinstruction_overview'),
    path('list/',ProcessInstructionListView.as_view(), name='processinstruction_list'),
    path('table/',ProcessInstructionTableView.as_view(), name='processinstruction_table'),
    path('create/',ProcessInstructionCreateUpdateDetailView.as_view(), name='processinstruction_create'),
    path('update/<slug:processinstruction>/',ProcessInstructionCreateUpdateDetailView.as_view(), name='processinstruction_update'),
    path('detail/<slug:processinstruction>/',ProcessInstructionCreateUpdateDetailView.as_view(), name='processinstruction_detail'),
    path('delete/<slug:processinstruction>/',ProcessInstructionDeleteView.as_view(), name='processinstruction_delete'),
]