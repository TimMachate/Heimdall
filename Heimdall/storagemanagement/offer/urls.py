"""
#--------------------------------------------------------------------------------
# Url File from Model Offer
# 09.11.2023
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
from storagemanagement.offer.views import (
    OfferView,
    OfferListView,
    OfferTableView,
    OfferCreateView,
    OfferDetailView,
    OfferUpdateView,
    OfferDeleteView,
    OfferAuthorizeTrueView,
    OfferAuthorizeFalseView,
    OfferRecivedView,
    OfferSentView,
    OfferOrderTrueView,
    OfferOrderFalseView
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
urlpatterns = [
    # Offer
    path(
        '',
        OfferView.as_view(),
        name='offer_overview'
    ),
    path(
        'list/',
        OfferListView.as_view(),
        name='offer_list'
    ),
    path(
        'table/',
        OfferTableView.as_view(),
        name='offer_table'
    ),
    path(
        'create/',
        OfferCreateView.as_view(),
        name='offer_create'
    ),
    path(
        'update/<slug:offer>/',
        OfferUpdateView.as_view(),
        name='offer_update'
    ),
    path(
        'detail/<slug:offer>/',
        OfferDetailView.as_view(),
        name='offer_detail'
    ),
    path(
        'detail/<slug:offer>/authorize/true/',
        OfferAuthorizeTrueView.as_view(),
        name='offer_authorize_true'
    ),
    path(
        'detail/<slug:offer>/authorize/false/',
        OfferAuthorizeFalseView.as_view(),
        name='offer_authorize_false'
    ),
    path(
        'detail/<slug:offer>/recived/',
        OfferRecivedView.as_view(),
        name='offer_recived'
    ),
    path(
        'detail/<slug:offer>/sent/',
        OfferSentView.as_view(),
        name='offer_sent'
    ),
    path(
        'detail/<slug:offer>/order/true/',
        OfferOrderTrueView.as_view(),
        name='offer_order_true'
    ),
    path(
        'detail/<slug:offer>/order/false/',
        OfferOrderFalseView.as_view(),
        name='offer_order_false'
    ),
    path(
        'delete/<slug:offer>/',
        OfferDeleteView.as_view(),
        name='offer_delete'
    ),
]
#--------------------------------------------------------------------------------
