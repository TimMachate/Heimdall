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
from documentationmanagement.workinginstruction.views import (
    WorkingInstructionListView,
    WorkingInstructionTableView,
    WorkingInstructionCreateUpdateDetailView,
    WorkingInstructionDeleteView
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Dateien
    path('',FileView.as_view(), name='workinginstruction_overview'),
    path('list/',WorkingInstructionListView.as_view(), name='workinginstruction_list'),
    path('table/',WorkingInstructionTableView.as_view(), name='workinginstruction_table'),
    path('create/',WorkingInstructionCreateUpdateDetailView.as_view(), name='workinginstruction_create'),
    path('update/<slug:workinginstruction>/',WorkingInstructionCreateUpdateDetailView.as_view(), name='workinginstruction_update'),
    path('detail/<slug:workinginstruction>/',WorkingInstructionCreateUpdateDetailView.as_view(), name='workinginstruction_detail'),
    path('delete/<slug:workinginstruction>/',WorkingInstructionDeleteView.as_view(), name='workinginstruction_delete'),
]