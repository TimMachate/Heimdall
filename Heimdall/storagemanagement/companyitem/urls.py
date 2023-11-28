#--------------------------------------------------------------------------------
# Urls File from Model CompanyItem
# 27.10.2023
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
    BookingCreateView
)
from storagemanagement.companyitem.views import (
    CompanyItemView,
    CompanyItemListView,
    CompanyItemTableView,
    CompanyItemCreateView,
    CompanyItemUpdateView,
    CompanyItemDeleteView,
    CompanyItemDetailView
)
from storagemanagement.storage.views import (
    StorageView,
    StorageListView,
    StorageTableView,
    StorageCreateView
)
#--------------------------------------------------------------------------------
urlpatterns = [
    # CompanyItem
    path('',CompanyItemView.as_view(), name='companyitem_overview'),
    path('list/',CompanyItemListView.as_view(), name='companyitem_list'),
    path('table/',CompanyItemTableView.as_view(), name='companyitem_table'),
    path('create/',CompanyItemCreateView.as_view(), name='companyitem_create'),
    path('update/<slug:companyitem>/',CompanyItemUpdateView.as_view(), name='companyitem_update'),
    path('detail/<slug:companyitem>/',CompanyItemDetailView.as_view(), name='companyitem_detail'),
    path('detail/<slug:companyitem>/booking/',BookingView.as_view(), name='companyitem_booking_overview'),
    path('detail/<slug:companyitem>/booking/list/',BookingListView.as_view(), name='companyitem_booking_list'),
    path('detail/<slug:companyitem>/booking/table/',BookingTableView.as_view(), name='companyitem_booking_table'),
    path('detail/<slug:companyitem>/booking/create/',BookingCreateView.as_view(), name='companyitem_booking_create'),
    path('detail/<slug:companyitem>/booking/add/',BookingCreateView.as_view(), name='companyitem_booking_add'),
    path('detail/<slug:companyitem>/booking/remove/',BookingCreateView.as_view(), name='companyitem_booking_remove'),
    path('detail/<slug:companyitem>/booking/remove/<int:value>/',BookingCreateView.as_view(), name='companyitem_booking_remove_value'),
    path('detail/<slug:companyitem>/storage/',StorageView.as_view(), name='companyitem_storage_overview'),
    path('detail/<slug:companyitem>/storage/list/',StorageListView.as_view(), name='companyitem_storage_list'),
    path('detail/<slug:companyitem>/storage/table/',StorageTableView.as_view(), name='companyitem_storage_table'),
    path('detail/<slug:companyitem>/storage/create/',StorageCreateView.as_view(), name='companyitem_storage_create'),
    path('detail/<slug:companyitem>/request/',CompanyItemDetailView.as_view(), name='companyitem_request_create'),
    path('delete/<slug:companyitem>/',CompanyItemDeleteView.as_view(), name='companyitem_delete'),
]
#--------------------------------------------------------------------------------