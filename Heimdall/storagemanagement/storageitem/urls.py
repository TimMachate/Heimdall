#--------------------------------------------------------------------------------
# Url File from Model StorageItem
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
    BookingCreateView
)
from storagemanagement.requestdata.views import (
    RequestDataCreateView
)
from storagemanagement.storageitem.views import (
    StorageItemView,
    StorageItemListView,
    StorageItemTableView,
    StorageItemCreateView,
    StorageItemDetailView,
    StorageItemUpdateView,
    StorageItemDeleteView
)
from storagemanagement.storage.views import (
    StorageView,
    StorageListView,
    StorageTableView,
    StorageCreateView
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Url Configuration
#--------------------------------------------------------------------------------
urlpatterns = [
    # StorageItem
    path('',StorageItemView.as_view(), name='storageitem_overview'),
    path('list/',StorageItemListView.as_view(), name='storageitem_list'),
    path('table/',StorageItemTableView.as_view(), name='storageitem_table'),
    path('create/',StorageItemCreateView.as_view(), name='storageitem_create'),
    path('update/<slug:storageitem>/',StorageItemUpdateView.as_view(), name='storageitem_update'),
    path('detail/<slug:storageitem>/',StorageItemDetailView.as_view(), name='storageitem_detail'),
    path('detail/<slug:storageitem>/booking/',BookingView.as_view(), name='storageitem_booking_overview'),
    path('detail/<slug:storageitem>/booking/list/',BookingListView.as_view(), name='storageitem_booking_list'),
    path('detail/<slug:storageitem>/booking/table/',BookingTableView.as_view(), name='storageitem_booking_table'),
    path('detail/<slug:storageitem>/booking/create/',BookingCreateView.as_view(), name='storageitem_booking_create'),
    path('detail/<slug:storageitem>/booking/add/',BookingCreateView.as_view(), name='storageitem_booking_add'),
    path('detail/<slug:storageitem>/booking/remove/',BookingCreateView.as_view(), name='storageitem_booking_remove'),
    path('detail/<slug:storageitem>/booking/remove/<int:value>/',BookingCreateView.as_view(), name='storageitem_booking_remove_value'),
    path('detail/<slug:storageitem>/request/create/',RequestDataCreateView.as_view(), name='storageitem_request_create'),
    path('detail/<slug:storageitem>/storage/',StorageView.as_view(), name='storageitem_storage_overview'),
    path('detail/<slug:storageitem>/storage/list/',StorageListView.as_view(), name='storageitem_storage_list'),
    path('detail/<slug:storageitem>/storage/table/',StorageTableView.as_view(), name='storageitem_storage_table'),
    path('detail/<slug:storageitem>/storage/create/',StorageCreateView.as_view(), name='storageitem_storage_create'),
    path('delete/<slug:storageitem>/',StorageItemDeleteView.as_view(), name='storageitem_delete'),
]
#--------------------------------------------------------------------------------