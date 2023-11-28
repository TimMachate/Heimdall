#--------------------------------------------------------------------------------
# Url File from Model Order Data
# 10.11.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.orderdata.views import (
    OrderDataView,
    OrderDataListView,
    OrderDataTableView,
    OrderDataCreateView,
    OrderDataDetailView,
    OrderDataUpdateView,
    OrderDataDeleteView,
    OrderDataAuthorizedTrueView,
    OrderDataAuthorizedFalseView,
    OrderDataAuthorizedTrueAllView,
    OrderDataAuthorizedFalseAllView,
    OrderDataBookingTrueView,
    OrderDataBookingFalseView,
    OrderDataBookingTrueAllView,
    OrderDataBookingFalseAllView
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
urlpatterns = [
    # OrderData
    path('',OrderDataView.as_view(), name='orderdata_overview'),
    path('list/',OrderDataListView.as_view(), name='orderdata_list'),
    path('table/',OrderDataTableView.as_view(), name='orderdata_table'),
    path('create/',OrderDataCreateView.as_view(), name='orderdata_create'),
    path('authorize/true/',OrderDataAuthorizedTrueAllView.as_view(), name='orderdata_authorize_all_true'),
    path('authorize/false/',OrderDataAuthorizedFalseAllView.as_view(), name='orderdata_authorize_all_false'),
    path('booking/true/',OrderDataBookingTrueAllView.as_view(), name='orderdata_booking_all_true'),
    path('booking/false/',OrderDataBookingFalseAllView.as_view(), name='orderdata_booking_all_false'),
    path('update/<slug:orderdata>/',OrderDataUpdateView.as_view(), name='orderdata_update'),
    path('detail/<slug:orderdata>/',OrderDataDetailView.as_view(), name='orderdata_detail'),
    path('detail/<slug:orderdata>/authorize/true/',OrderDataAuthorizedTrueView.as_view(), name='orderdata_authorize_true'),
    path('detail/<slug:orderdata>/authorize/false/',OrderDataAuthorizedFalseView.as_view(), name='orderdata_authorize_false'),
    path('detail/<slug:orderdata>/booking/true/',OrderDataBookingTrueView.as_view(), name='orderdata_booking_true'),
    path('detail/<slug:orderdata>/booking/false/',OrderDataBookingFalseView.as_view(), name='orderdata_booking_false'),
    path('delete/<slug:orderdata>/',OrderDataDeleteView.as_view(), name='orderdata_delete'),
]
#--------------------------------------------------------------------------------