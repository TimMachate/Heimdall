#--------------------------------------------------------------------------------
# Url File from Model Booking
# 15.10.2023
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
from storagemanagement.booking.views import (
    BookingView,
    BookingListView,
    BookingTableView,
    BookingCreateView,
    BookingDetailView,
    BookingUpdateView,
    BookingDeleteView
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
urlpatterns = [
    # Booking
    path('',BookingView.as_view(), name='booking_overview'),
    path('list/',BookingListView.as_view(), name='booking_list'),
    path('table/',BookingTableView.as_view(), name='booking_table'),
    path('create/',BookingCreateView.as_view(), name='booking_create'),
    path('add/',BookingCreateView.as_view(), name='booking_add'),
    path('remove/',BookingCreateView.as_view(), name='booking_remove'),
    path('create/add/remove/',BookingCreateView.as_view(), name='booking_create_add_remove'),
    path('update/<slug:booking>/',BookingUpdateView.as_view(), name='booking_update'),
    path('detail/<slug:booking>/',BookingDetailView.as_view(), name='booking_detail'),
    path('delete/<slug:booking>/',BookingDeleteView.as_view(), name='booking_delete'),
]
#--------------------------------------------------------------------------------