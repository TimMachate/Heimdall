#--------------------------------------------------------------------------------
# Url File from Model Company
# 25.10.2023
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
from storagemanagement.company.views import (
    CompanyView,
    CompanyListView,
    CompanyTableView,
    CompanyCreateView,
    CompanyDetailView,
    CompanyUpdateView,
    CompanyDeleteView
)
from storagemanagement.companycontact.views import (
    CompanyContactView,
    CompanyContactListView,
    CompanyContactTableView,
    CompanyContactCreateView,
    CompanyContactDetailView,
    CompanyContactUpdateView,
    CompanyContactDeleteView
)
from storagemanagement.companyitem.views import (
    CompanyItemView,
    CompanyItemListView,
    CompanyItemTableView,
    CompanyItemCreateView,
    CompanyItemDetailView,
    CompanyItemUpdateView,
    CompanyItemDeleteView
)
from storagemanagement.storage.views import (
    StorageView,
    StorageListView,
    StorageTableView,
    StorageCreateView
)
#--------------------------------------------------------------------------------
urlpatterns = [
    # Company
    path('',CompanyView.as_view(), name='company_overview'),
    path('list/',CompanyListView.as_view(), name='company_list'),
    path('table/',CompanyTableView.as_view(), name='company_table'),
    path('create/',CompanyCreateView.as_view(), name='company_create'),
    path('update/<slug:company>/',CompanyUpdateView.as_view(), name='company_update'),
    path('detail/<slug:company>/',CompanyDetailView.as_view(), name='company_detail'),
    path('detail/<slug:company>/booking/',BookingView.as_view(), name='company_booking_overview'),
    path('detail/<slug:company>/booking/list/',BookingListView.as_view(), name='company_booking_list'),
    path('detail/<slug:company>/booking/table/',BookingTableView.as_view(), name='company_booking_table'),
    path('detail/<slug:company>/booking/create/',BookingCreateView.as_view(), name='company_booking_create'),
    path('detail/<slug:company>/companycontact/',CompanyContactView.as_view(), name='company_companycontact_overview'),
    path('detail/<slug:company>/companycontact/list/',CompanyContactListView.as_view(), name='company_companycontact_list'),
    path('detail/<slug:company>/companycontact/table/',CompanyContactTableView.as_view(), name='company_companycontact_table'),
    path('detail/<slug:company>/companycontact/create/',CompanyContactCreateView.as_view(), name='company_companycontact_create'),
    path('detail/<slug:company>/companyitem/',CompanyItemView.as_view(), name='company_companyitem_overview'),
    path('detail/<slug:company>/companyitem/list/',CompanyItemListView.as_view(), name='company_companyitem_list'),
    path('detail/<slug:company>/companyitem/table/',CompanyItemTableView.as_view(), name='company_companyitem_table'),
    path('detail/<slug:company>/companyitem/create/',CompanyItemCreateView.as_view(), name='company_companyitem_create'),
    path('detail/<slug:company>/storage/',StorageView.as_view(), name='company_storage_overview'),
    path('detail/<slug:company>/storage/list/',StorageListView.as_view(), name='company_storage_list'),
    path('detail/<slug:company>/storage/table/',StorageTableView.as_view(), name='company_storage_table'),
    path('detail/<slug:company>/storage/create/',StorageCreateView.as_view(), name='company_storage_create'),
    path('delete/<slug:company>/',CompanyDeleteView.as_view(), name='company_delete'),
]
#--------------------------------------------------------------------------------