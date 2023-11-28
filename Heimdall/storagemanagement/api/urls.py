#--------------------------------------------------------------------------------
# Url File from App Storagemanagement API
# 04.11.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path, include
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
app_name = 'storagemanagementAPI'

urlpatterns = [
    # Booking
    path('booking/',include('storagemanagement.booking.api.urls')),
    # Company
    path('company/',include('storagemanagement.company.api.urls')),
    # CompanyContact
    path('companycontact/',include('storagemanagement.companycontact.api.urls')),
    # CompanyItem
    path('companyitem/',include('storagemanagement.companyitem.api.urls')),
    # Offer Data
    path('offerdata/',include('storagemanagement.offerdata.api.urls')),
    # Offer
    path('offer/',include('storagemanagement.offer.api.urls')),
    # Order Data
    path('orderdata/',include('storagemanagement.orderdata.api.urls')),
    # Order
    path('order/',include('storagemanagement.order.api.urls')),
    # Request
    path('requestdata/',include('storagemanagement.requestdata.api.urls')),
    # Storage
    path('storage/',include('storagemanagement.storage.api.urls')),
    # Storage Item
    path('storageitem/',include('storagemanagement.storageitem.api.urls')),
    
]
#--------------------------------------------------------------------------------