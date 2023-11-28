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
from documentationmanagement.technicaldatasheet.views import (
    TechnicalDataSheetListView,
    TechnicalDataSheetTableView,
    TechnicalDataSheetCreateUpdateDetailView,
    TechnicalDataSheetDeleteView
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Dateien
    path('',FileView.as_view(), name='technicaldatasheet_overview'),
    path('list/',TechnicalDataSheetListView.as_view(), name='technicaldatasheet_list'),
    path('table/',TechnicalDataSheetTableView.as_view(), name='technicaldatasheet_table'),
    path('create/',TechnicalDataSheetCreateUpdateDetailView.as_view(), name='technicaldatasheet_create'),
    path('update/<slug:technicaldatasheet>/',TechnicalDataSheetCreateUpdateDetailView.as_view(), name='technicaldatasheet_update'),
    path('detail/<slug:technicaldatasheet>/',TechnicalDataSheetCreateUpdateDetailView.as_view(), name='technicaldatasheet_detail'),
    path('delete/<slug:technicaldatasheet>/',TechnicalDataSheetDeleteView.as_view(), name='technicaldatasheet_delete'),
]