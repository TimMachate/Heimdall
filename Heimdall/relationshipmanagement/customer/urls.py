#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.customer.views import (
    CustomerView,
    CustomerListView,
    CustomerTableView,
    CustomerCreateView,
    CustomerDetailView,
    CustomerUpdateView,
    CustomerDeleteView
)
#--------------------------------------------------------------------------------
urlpatterns = [
    # Customer
    path('',CustomerView.as_view(), name='customer_overview'),
    path('list/',CustomerListView.as_view(), name='customer_list'),
    path('table/',CustomerTableView.as_view(), name='customer_table'),
    path('create/',CustomerCreateView.as_view(), name='customer_create'),
    path('update/<slug:customer>/',CustomerUpdateView.as_view(), name='customer_update'),
    path('detail/<slug:customer>/',CustomerDetailView.as_view(), name='customer_detail'),
    path('delete/<slug:customer>/',CustomerDeleteView.as_view(), name='customer_delete'),
]
#--------------------------------------------------------------------------------