#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Views
#--------------------------------------------------------------------------------
from .views import (
    DepartmentView,
    DepartmentListView,
    DepartmentTableView,
    DepartmentCreateUpdateDetailView,
    DepartmentDeleteView,
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Department
    path('',DepartmentView.as_view(), name='department_overview'),
    path('list/',DepartmentListView.as_view(), name='department_list'),
    path('table/',DepartmentTableView.as_view(), name='department_table'),
    path('create/',DepartmentCreateUpdateDetailView.as_view(), name='department_create'),
    path('update/<slug:department>/',DepartmentCreateUpdateDetailView.as_view(), name='department_update'),
    path('detail/<slug:department>/',DepartmentCreateUpdateDetailView.as_view(), name='department_detail'),
    path('detail/<slug:department>/section/',DepartmentCreateUpdateDetailView.as_view(), name='department_section_table'),
    path('detail/<slug:department>/section/<slug:section>/position/',DepartmentCreateUpdateDetailView.as_view(), name='department_section_position_table'),
    path('detail/<slug:department>/section/<slug:section>/employee/',DepartmentCreateUpdateDetailView.as_view(), name='department_section_employee_table'),
    path('detail/<slug:department>/position/',DepartmentCreateUpdateDetailView.as_view(), name='department_position_table'),
    path('detail/<slug:department>/employee/',DepartmentCreateUpdateDetailView.as_view(), name='department_employee_table'),
    path('delete/<slug:department>/',DepartmentDeleteView.as_view(), name='department_delete'),
]