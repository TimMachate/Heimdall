"""
#--------------------------------------------------------------------------------
# Url File from Model Order
# 10.11.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.order.views import (
    OrderView,
    OrderListView,
    OrderTableView,
    OrderCreateView,
    OrderDetailView,
    OrderUpdateView,
    OrderDeleteView,
    OrderAuthorizeTrueView,
    OrderAuthorizeFalseView,
    OrderBookingTrueView,
    OrderBookingFalseView,
    OrderRecivedView,
    OrderSentView,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
urlpatterns = [
    # Order
    path(
        '',
        OrderView.as_view(),
        name='order_overview'
    ),
    path(
        'list/',
        OrderListView.as_view(),
        name='order_list'
    ),
    path(
        'table/',
        OrderTableView.as_view(),
        name='order_table'
    ),
    path(
        'create/',
        OrderCreateView.as_view(),
        name='order_create'
    ),
    path(
        'update/<slug:order>/',
        OrderUpdateView.as_view(),
        name='order_update'
    ),
    path(
        'detail/<slug:order>/',
        OrderDetailView.as_view(),
        name='order_detail'
    ),
    path(
        'detail/<slug:order>/authorize/true/',
        OrderAuthorizeTrueView.as_view(),
        name='order_authorize_true'
    ),
    path(
        'detail/<slug:order>/authorize/false/',
        OrderAuthorizeFalseView.as_view(),
        name='order_authorize_false'
    ),
    path(
        'detail/<slug:order>/booking/true/',
        OrderBookingTrueView.as_view(),
        name='order_booking_true'
    ),
    path(
        'detail/<slug:order>/booking/false/',
        OrderBookingFalseView.as_view(),
        name='order_booking_false'
    ),
    path(
        'detail/<slug:order>/sent/',
        OrderSentView.as_view(),
        name='order_sent'
    ),
    path(
        'detail/<slug:order>/recived/',
        OrderRecivedView.as_view(),
        name='order_recived'
    ),
    path(
        'delete/<slug:order>/',
        OrderDeleteView.as_view(),
        name='order_delete'
    ),
]
#--------------------------------------------------------------------------------
