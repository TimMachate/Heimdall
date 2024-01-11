"""
#--------------------------------------------------------------------------------
# Urls File from App Relationshipmanagement
# 16.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path,include
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.views import RelationshipmanagmentView
#--------------------------------------------------------------------------------

app_name = 'relationshipmanagement'

#--------------------------------------------------------------------------------
urlpatterns = [
    path('',RelationshipmanagmentView.as_view(), name='relationshipmanagement'),
    # Company
    path('company/',include('relationshipmanagement.company.urls')),
    # Company Contacts
    path('companycontact/',include('relationshipmanagement.companycontact.urls')),
    # Company Items
    path('companyitem/',include('relationshipmanagement.companyitem.urls')),
]
#--------------------------------------------------------------------------------
