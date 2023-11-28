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
from documentationmanagement.document.views import (
    DocumentListView,
    DocumentTableView,
    DocumentCreateUpdateDetailView,
    DocumentDeleteView
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Dateien
    path('',FileView.as_view(), name='document_overview'),
    path('list/',DocumentListView.as_view(), name='document_list'),
    path('table/',DocumentTableView.as_view(), name='document_table'),
    path('create/',DocumentCreateUpdateDetailView.as_view(), name='document_create'),
    path('update/<slug:document>/',DocumentCreateUpdateDetailView.as_view(), name='document_update'),
    path('detail/<slug:document>/',DocumentCreateUpdateDetailView.as_view(), name='document_detail'),
    path('delete/<slug:document>/',DocumentDeleteView.as_view(), name='document_delete'),
]