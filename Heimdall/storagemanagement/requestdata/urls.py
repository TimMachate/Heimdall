#--------------------------------------------------------------------------------
# Urls File from Model Request Data
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
from storagemanagement.requestdata.views import (
    RequestDataView,
    RequestDataListView,
    RequestDataTableView,
    RequestDataCreateView,
    RequestDataDetailView,
    RequestDataUpdateView,
    RequestDataDeleteView,
    RequestDataAuthorizedTrueView,
    RequestDataAuthorizedFalseView,
    RequestDataAuthorizedTrueAllView,
    RequestDataAuthorizedFalseAllView
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
urlpatterns = [
    # RequestData
    path('',RequestDataView.as_view(), name='requestdata_overview'),
    path('list/',RequestDataListView.as_view(), name='requestdata_list'),
    path('table/',RequestDataTableView.as_view(), name='requestdata_table'),
    path('create/',RequestDataCreateView.as_view(), name='requestdata_create'),
    path('authorize/true/',RequestDataAuthorizedTrueAllView.as_view(), name='requestdata_authorize_all_true'),
    path('authorize/false/',RequestDataAuthorizedFalseAllView.as_view(), name='requestdata_authorize_all_false'),
    path('update/<slug:requestdata>/',RequestDataUpdateView.as_view(), name='requestdata_update'),
    path('detail/<slug:requestdata>/',RequestDataDetailView.as_view(), name='requestdata_detail'),
    path('detail/<slug:requestdata>/authorize/true/',RequestDataAuthorizedTrueView.as_view(), name='requestdata_authorize_true'),
    path('detail/<slug:requestdata>/authorize/false/',RequestDataAuthorizedFalseView.as_view(), name='requestdata_authorize_false'),
    path('detail/<slug:requestdata>/',RequestDataDetailView.as_view(), name='requestdata_detail'),
    path('delete/<slug:requestdata>/',RequestDataDeleteView.as_view(), name='requestdata_delete'),
]
#--------------------------------------------------------------------------------