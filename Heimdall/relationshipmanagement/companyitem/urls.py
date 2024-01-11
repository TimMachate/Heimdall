"""
#--------------------------------------------------------------------------------
# Urls File from Model CompanyItem
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
from relationshipmanagement.companyitem.views import (
    CompanyItemView,
    CompanyItemListView,
    CompanyItemTableView,
    CompanyItemCreateView,
    CompanyItemUpdateView,
    CompanyItemDeleteView,
    CompanyItemDetailView
)
#--------------------------------------------------------------------------------
urlpatterns = [
    # CompanyItem
    path(
        '',
        CompanyItemView.as_view(),
        name='companyitem_overview'
    ),
    path(
        'list/',
        CompanyItemListView.as_view(),
        name='companyitem_list'
    ),
    path(
        'table/',
        CompanyItemTableView.as_view(),
        name='companyitem_table'
    ),
    path(
        'create/',
        CompanyItemCreateView.as_view(),
        name='companyitem_create'
    ),
    path(
        'update/<slug:companyitem>/',
        CompanyItemUpdateView.as_view(),
        name='companyitem_update'
    ),
    path(
        'detail/<slug:companyitem>/',
        CompanyItemDetailView.as_view(),
        name='companyitem_detail'
    ),
    path(
        'delete/<slug:companyitem>/',
        CompanyItemDeleteView.as_view(),
        name='companyitem_delete'
    ),
]
#--------------------------------------------------------------------------------
