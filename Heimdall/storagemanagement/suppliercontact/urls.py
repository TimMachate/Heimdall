"""
#--------------------------------------------------------------------------------
# Urls File from Model SupplierContact
# 27.10.2023
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
from storagemanagement.suppliercontact.views import (
    SupplierContactView,
    SupplierContactListView,
    SupplierContactTableView,
    SupplierContactCreateView,
    SupplierContactDetailView,
    SupplierContactUpdateView,
    SupplierContactDeleteView
)
#--------------------------------------------------------------------------------
urlpatterns = [
    # Contact
    path(
        '',
        SupplierContactView.as_view(),
        name='suppliercontact_overview'
    ),
    path(
        'list/',
        SupplierContactListView.as_view(),
        name='suppliercontact_list'
    ),
    path(
        'table/',
        SupplierContactTableView.as_view(),
        name='suppliercontact_table'
    ),
    path(
        'create/',
        SupplierContactCreateView.as_view(),
        name='suppliercontact_create'
    ),
    path(
        'update/<slug:suppliercontact>/',
        SupplierContactUpdateView.as_view(),
        name='suppliercontact_update'
    ),
    path(
        'detail/<slug:suppliercontact>/',
        SupplierContactDetailView.as_view(),
        name='suppliercontact_detail'
    ),
    path(
        'delete/<slug:suppliercontact>/',
        SupplierContactDeleteView.as_view(),
        name='suppliercontact_delete'
    ),
]
#--------------------------------------------------------------------------------
