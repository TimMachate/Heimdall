#--------------------------------------------------------------------------------
# Urls File from Model CompanyContact API
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
from storagemanagement.companycontact.api.views import CompanyContactListAPIView,CompanyContactDetailAPIView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
urlpatterns = [
    path('list/',CompanyContactListAPIView.as_view(),name='companycontact_list'),
    path('detail/<slug:companycontact>/',CompanyContactDetailAPIView.as_view(),name='companycontact_detail'),
]
#--------------------------------------------------------------------------------