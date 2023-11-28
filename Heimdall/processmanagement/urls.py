#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Views
#--------------------------------------------------------------------------------
from processmanagement.views.processmanagement import ProcessManagementView

from processmanagement.views.data import (
    DataTableView,
    DataCreateUpdateView,
    DataBatchCreateUpdateView,
    DataDeleteView,
)

from processmanagement.views.defect import (
    DefectView,
    DefectListView,
    DefectTableView,
    DefectCreateUpdateView,
    DefectDetailView,
    DefectDeleteView,
)

from processmanagement.views.statusreport import (
    StatusReportView,
    StatusReportListView,
    StatusReportTableView,
    StatusReportCreateUpdateView,
    StatusReportDetailView,
    StatusReportDeleteView,
)
#--------------------------------------------------------------------------------

app_name = 'processmanagement'

urlpatterns = [
    path('',ProcessManagementView.as_view(), name='processmanagement'),
    # Batch
    path('batch/table/',DefectTableView.as_view(), name='batch_table'),
    path('batch/create/',DefectCreateUpdateView.as_view(), name='batch_create'),
    path('batch/update/<int:id>/',DefectCreateUpdateView.as_view(), name='batch_update'),
    path('batch/delete/<int:id>/',DefectDeleteView.as_view(), name='batch_delete'),
    # Data
    path('data/table/',DataTableView.as_view(), name='data_table'),
    path('data/create/',DataCreateUpdateView.as_view(), name='data_create'),
    path('data/delete/<int:id>/',DataDeleteView.as_view(), name='data_delete'),
    path('data/batch/<int:batch>/create/',DataBatchCreateUpdateView.as_view(), name='data_batch_create'),
    path('data/batch/<int:batch>/update/<int:id>',DataBatchCreateUpdateView.as_view(), name='data_batch_update'),
    # Defect
    path('defect/',DefectView.as_view(), name='defect'),
    path('defect/list/',DefectListView.as_view(), name='defect_list'),
    path('defect/table/',DefectTableView.as_view(), name='defect_table'),
    path('defect/create/',DefectCreateUpdateView.as_view(), name='defect_create'),
    path('defect/update/<int:id>/',DefectCreateUpdateView.as_view(), name='defect_update'),
    path('defect/detail/<int:id>/',DefectDetailView.as_view(), name='defect_detail'),
    path('defect/delete/<int:id>/',DefectDeleteView.as_view(), name='defect_delete'),
    # Status Report
    path('statusreport/',StatusReportView.as_view(), name='statusreport'),
    path('statusreport/list/',StatusReportListView.as_view(), name='statusreport_list'),
    path('statusreport/table/',StatusReportTableView.as_view(), name='statusreport_table'),
    path('statusreport/create/',StatusReportCreateUpdateView.as_view(), name='statusreport_create'),
    path('statusreport/update/<int:id>/',StatusReportCreateUpdateView.as_view(), name='statusreport_update'),
    path('statusreport/detail/<int:id>/',StatusReportDetailView.as_view(), name='statusreport_detail'),
    path('statusreport/delete/<int:id>/',StatusReportDeleteView.as_view(), name='statusreport_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)