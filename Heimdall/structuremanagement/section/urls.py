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
    SectionView,
    SectionListView,
    SectionTableView,
    SectionCreateUpdateDetailView,
    SectionDeleteView,
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Section
    path('',SectionView.as_view(), name='section_overview'),
    path('list/',SectionListView.as_view(), name='section_list'),
    path('table/',SectionTableView.as_view(), name='section_table'),
    path('create/',SectionCreateUpdateDetailView.as_view(), name='section_create'),
    path('update/<slug:section>/',SectionCreateUpdateDetailView.as_view(), name='section_update'),
    path('detail/<slug:section>/',SectionCreateUpdateDetailView.as_view(), name='section_detail'),
    path('detail/<slug:section>/position/',SectionCreateUpdateDetailView.as_view(), name='section_position_table'),
    path('detail/<slug:section>/employee/',SectionCreateUpdateDetailView.as_view(), name='section_employee_table'),
    path('delete/<slug:section>/',SectionDeleteView.as_view(), name='section_delete'),
]