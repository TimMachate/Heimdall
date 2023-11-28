#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.company.views import (
    CompanyView,
    CompanyListView,
    CompanyTableView,
    CompanyCreateView,
    CompanyDetailView,
    CompanyUpdateView,
    CompanyDeleteView
)
#--------------------------------------------------------------------------------
urlpatterns = [
    # Company
    path('',CompanyView.as_view(), name='company_overview'),
    path('list/',CompanyListView.as_view(), name='company_list'),
    path('table/',CompanyTableView.as_view(), name='company_table'),
    path('create/',CompanyCreateView.as_view(), name='company_create'),
    path('update/<slug:company>/',CompanyUpdateView.as_view(), name='company_update'),
    path('detail/<slug:company>/',CompanyDetailView.as_view(), name='company_detail'),
    path('delete/<slug:company>/',CompanyDeleteView.as_view(), name='company_delete'),
]
#--------------------------------------------------------------------------------