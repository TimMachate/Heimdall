"""
#--------------------------------------------------------------------------------
# Urls File from Model SupplierContact API
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
from storagemanagement.suppliercontact.api.views import (
    SupplierContactListAPIView,
    SupplierContactDetailAPIView
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
urlpatterns = [
    path(
        'list/',
        SupplierContactListAPIView.as_view(),
        name='suppliercontact_list'
    ),
    path(
        'detail/<slug:suppliercontact>/',
        SupplierContactDetailAPIView.as_view(),
        name='suppliercontact_detail'
    ),
]
#--------------------------------------------------------------------------------
