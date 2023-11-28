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
from documentationmanagement.safetydatasheet.views import (
    SafetyDataSheetListView,
    SafetyDataSheetTableView,
    SafetyDataSheetCreateUpdateDetailView,
    SafetyDataSheetDeleteView
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Dateien
    path('',FileView.as_view(), name='safetydatasheet_overview'),
    path('list/',SafetyDataSheetListView.as_view(), name='safetydatasheet_list'),
    path('table/',SafetyDataSheetTableView.as_view(), name='safetydatasheet_table'),
    path('create/',SafetyDataSheetCreateUpdateDetailView.as_view(), name='safetydatasheet_create'),
    path('update/<slug:safetydatasheet>/',SafetyDataSheetCreateUpdateDetailView.as_view(), name='safetydatasheet_update'),
    path('detail/<slug:safetydatasheet>/',SafetyDataSheetCreateUpdateDetailView.as_view(), name='safetydatasheet_detail'),
    path('delete/<slug:safetydatasheet>/',SafetyDataSheetDeleteView.as_view(), name='safetydatasheet_delete'),
]