"""
#--------------------------------------------------------------------------------
# Urls File from Model CompanyContact
# 16.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.companycontact.views import (
    CompanyContactView,
    CompanyContactListView,
    CompanyContactTableView,
    CompanyContactCreateView,
    CompanyContactDetailView,
    CompanyContactUpdateView,
    CompanyContactDeleteView
)
#--------------------------------------------------------------------------------
urlpatterns = [
    # Contact
    path(
        '',
        CompanyContactView.as_view(),
        name='companycontact_overview'
    ),
    path(
        'list/',
        CompanyContactListView.as_view(),
        name='companycontact_list'
    ),
    path(
        'table/',
        CompanyContactTableView.as_view(),
        name='companycontact_table'
    ),
    path(
        'create/',
        CompanyContactCreateView.as_view(),
        name='companycontact_create'
    ),
    path(
        'update/<slug:companycontact>/',
        CompanyContactUpdateView.as_view(),
        name='companycontact_update'
    ),
    path(
        'detail/<slug:companycontact>/',
        CompanyContactDetailView.as_view(),
        name='companycontact_detail'
    ),
    path(
        'delete/<slug:companycontact>/',
        CompanyContactDeleteView.as_view(),
        name='companycontact_delete'
    ),
]
#--------------------------------------------------------------------------------
