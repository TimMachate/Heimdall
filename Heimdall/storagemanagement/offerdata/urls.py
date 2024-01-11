"""
#--------------------------------------------------------------------------------
# Url File from Model Offer Data
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
from storagemanagement.offerdata.views import (
    OfferDataView,
    OfferDataListView,
    OfferDataTableView,
    OfferDataCreateView,
    OfferDataDetailView,
    OfferDataUpdateView,
    OfferDataDeleteView,
    OfferDataAuthorizedTrueView,
    OfferDataAuthorizedFalseView,
    OfferDataAuthorizedTrueAllView,
    OfferDataAuthorizedFalseAllView,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
urlpatterns = [
    # OfferData
    path(
        '',
        OfferDataView.as_view(),
        name='offerdata_overview'
    ),
    path(
        'list/',
        OfferDataListView.as_view(),
        name='offerdata_list'
    ),
    path(
        'table/',
        OfferDataTableView.as_view(),
        name='offerdata_table'
    ),
    path(
        'create/',
        OfferDataCreateView.as_view(),
        name='offerdata_create'
    ),
    path(
        'authorize/true/',
        OfferDataAuthorizedTrueAllView.as_view(),
        name='offerdata_authorize_all_true'
    ),
    path(
        'authorize/false/',
        OfferDataAuthorizedFalseAllView.as_view(),
        name='offerdata_authorize_all_false'
    ),
    path(
        'update/<slug:offerdata>/',
        OfferDataUpdateView.as_view(),
        name='offerdata_update'
    ),
    path(
        'detail/<slug:offerdata>/',
        OfferDataDetailView.as_view(),
        name='offerdata_detail'
    ),
    path(
        'detail/<slug:offerdata>/authorize/true/',
        OfferDataAuthorizedTrueView.as_view(),
        name='offerdata_authorize_true'
    ),
    path(
        'detail/<slug:offerdata>/authorize/false/',
        OfferDataAuthorizedFalseView.as_view(),
        name='offerdata_authorize_false'
    ),
    path(
        'delete/<slug:offerdata>/',
        OfferDataDeleteView.as_view(),
        name='offerdata_delete'
    ),
]
#--------------------------------------------------------------------------------
