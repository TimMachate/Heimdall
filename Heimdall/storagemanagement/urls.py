#--------------------------------------------------------------------------------
# Url File from App Storagemanagement
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path,include
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
# There are no Models necessary
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Views
#--------------------------------------------------------------------------------
from storagemanagement.views import StorageManagementView,OrderProcessView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
app_name = 'storagemanagement'

urlpatterns = [
     # Mainpage
     path('',StorageManagementView.as_view(), name='storagemanagement'),
     # Booking
     path('booking/',include('storagemanagement.booking.urls')),
     # Company
     path('company/',include('storagemanagement.company.urls')),
     # CompanyContact
     path('companycontact/',include('storagemanagement.companycontact.urls')),
     # CompanyItem
     path('companyitem/',include('storagemanagement.companyitem.urls')),
     # Items
     path('storageitem/',include('storagemanagement.storageitem.urls')),
     # Offer
     path('offer/',include('storagemanagement.offer.urls')),
     # Offer Data
     path('offerdata/',include('storagemanagement.offerdata.urls')),
     # Order
     path('order/',include('storagemanagement.order.urls')),
     # Order
     path('orderdata/',include('storagemanagement.orderdata.urls')),
     # OrderProcess
     path('orderprocess/',OrderProcessView.as_view(), name='orderprocess'),
     # Request
     path('requestdata/',include('storagemanagement.requestdata.urls')),
     # Storage
     path('storage/',include('storagemanagement.storage.urls')),
]
#--------------------------------------------------------------------------------