"""
#--------------------------------------------------------------------------------
# Urls File from Model CompanyItem API
# 16.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
from relationshipmanagement.companyitem.api.views import (
    CompanyItemListAPIView,
    CompanyItemDetailAPIView
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
urlpatterns = [
    path(
        'list/',
        CompanyItemListAPIView.as_view(),
        name='companyitem_list'
    ),
    path(
        'detail/<slug:companyitem>/',
        CompanyItemDetailAPIView.as_view(),
        name='companyitem_detail'
    ),
]
#--------------------------------------------------------------------------------