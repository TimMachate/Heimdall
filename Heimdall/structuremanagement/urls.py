#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path, include
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Views
#--------------------------------------------------------------------------------
from structuremanagement.department.views import DepartmentView,DepartmentListView,DepartmentTableView
#--------------------------------------------------------------------------------

app_name = 'structuremanagement'

urlpatterns = [
    path('companystructure/',include('structuremanagement.companystructure.urls')),
    # Data
    path('',DepartmentView.as_view(), name='data_overview'),
    path('list/',DepartmentListView.as_view(), name='data_list'),
    path('table/',DepartmentTableView.as_view(), name='data_table'),
    # Error & ErrorData
    path('error/',include('structuremanagement.error.urls')),
    # Device
    path('device/',include('structuremanagement.device.urls')),
    # Department
    path('department/',include('structuremanagement.department.urls')),
    # Machine Group
    path('group/',include('structuremanagement.group.urls')),
    # Maintenance
    path('maintenance/',include('structuremanagement.maintenance.urls')),
    # Process & ProcessData
    path('process/',include('structuremanagement.process.urls')),
    # Position
    path('position/',include('structuremanagement.position.urls')),
    # Section
    path('section/',include('structuremanagement.section.urls')),
    # Status & StatusData
    path('status/',include('structuremanagement.status.urls')),
]