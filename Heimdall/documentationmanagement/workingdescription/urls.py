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
from documentationmanagement.workingdescription.views import (
    WorkingDescriptionListView,
    WorkingDescriptionTableView,
    WorkingDescriptionCreateUpdateDetailView,
    WorkingDescriptionDeleteView
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Dateien
    path('',FileView.as_view(), name='workingdescription_overview'),
    path('list/',WorkingDescriptionListView.as_view(), name='workingdescription_list'),
    path('table/',WorkingDescriptionTableView.as_view(), name='workingdescription_table'),
    path('create/',WorkingDescriptionCreateUpdateDetailView.as_view(), name='workingdescription_create'),
    path('update/<slug:workingdescription>/',WorkingDescriptionCreateUpdateDetailView.as_view(), name='workingdescription_update'),
    path('detail/<slug:workingdescription>/',WorkingDescriptionCreateUpdateDetailView.as_view(), name='workingdescription_detail'),
    path('delete/<slug:workingdescription>/',WorkingDescriptionDeleteView.as_view(), name='workingdescription_delete'),
]