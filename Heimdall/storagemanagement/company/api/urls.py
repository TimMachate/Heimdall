#--------------------------------------------------------------------------------
# Urls File from Model Company API
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
from storagemanagement.company.api.views import CompanyListAPIView,CompanyDetailAPIView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
urlpatterns = [
    path('list/',CompanyListAPIView.as_view(),name='company_list'),
    path('detail/<slug:company>/',CompanyDetailAPIView.as_view(),name='company_detail'),
]
#--------------------------------------------------------------------------------