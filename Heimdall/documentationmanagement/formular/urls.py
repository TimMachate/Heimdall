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
from documentationmanagement.formular.views import (
    FormularListView,
    FormularTableView,
    FormularCreateUpdateDetailView,
    FormularDeleteView
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Dateien
    path('',FileView.as_view(), name='formular_overview'),
    path('list/',FormularListView.as_view(), name='formular_list'),
    path('table/',FormularTableView.as_view(), name='formular_table'),
    path('create/',FormularCreateUpdateDetailView.as_view(), name='formular_create'),
    path('update/<slug:formular>/',FormularCreateUpdateDetailView.as_view(), name='formular_update'),
    path('detail/<slug:formular>/',FormularCreateUpdateDetailView.as_view(), name='formular_detail'),
    path('delete/<slug:formular>/',FormularDeleteView.as_view(), name='formular_delete'),
]