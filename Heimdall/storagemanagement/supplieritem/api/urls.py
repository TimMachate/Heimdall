"""
#--------------------------------------------------------------------------------
# Urls File from Model SupplierItem API
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
from storagemanagement.supplieritem.api.views import (
    SupplierItemListAPIView,
    SupplierItemDetailAPIView
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
urlpatterns = [
    path(
        'list/',
        SupplierItemListAPIView.as_view(),
        name='supplieritem_list'
    ),
    path(
        'detail/<slug:supplieritem>/',
        SupplierItemDetailAPIView.as_view(),
        name='supplieritem_detail'
    ),
]
#--------------------------------------------------------------------------------
