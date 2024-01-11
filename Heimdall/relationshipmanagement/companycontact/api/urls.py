"""
#--------------------------------------------------------------------------------
# Urls File from Model CompanyContact API
# 16.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
from relationshipmanagement.companycontact.api.views import (
    CompanyContactListAPIView,
    CompanyContactDetailAPIView
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
urlpatterns = [
    path(
        'list/',
        CompanyContactListAPIView.as_view(),
        name='companycontact_list'
    ),
    path(
        'detail/<slug:companycontact>/',
        CompanyContactDetailAPIView.as_view(),
        name='companycontact_detail'
    ),
]
#--------------------------------------------------------------------------------
