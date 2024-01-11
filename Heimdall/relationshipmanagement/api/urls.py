"""
#--------------------------------------------------------------------------------
# Url File from App Relationshipmanagement API
# 16.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path, include
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
app_name = 'relationshipmanagementAPI'

urlpatterns = [
    path('company/',include('relationshipmanagement.company.api.urls')),
    path('companycontact/',include('relationshipmanagement.companycontact.api.urls')),
    path('companyitem/',include('relationshipmanagement.companyitem.api.urls')),
]
#--------------------------------------------------------------------------------
