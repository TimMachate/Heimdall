#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.supplier.views import (
    SupplierView,
    SupplierListView,
    SupplierTableView,
    SupplierCreateView,
    SupplierDetailView,
    SupplierUpdateView,
    SupplierDeleteView
)
#--------------------------------------------------------------------------------
urlpatterns = [
    # Supplier
    path('',SupplierView.as_view(), name='supplier_overview'),
    path('list/',SupplierListView.as_view(), name='supplier_list'),
    path('table/',SupplierTableView.as_view(), name='supplier_table'),
    path('create/',SupplierCreateView.as_view(), name='supplier_create'),
    path('update/<slug:supplier>/',SupplierUpdateView.as_view(), name='supplier_update'),
    path('detail/<slug:supplier>/',SupplierDetailView.as_view(), name='supplier_detail'),
    path('delete/<slug:supplier>/',SupplierDeleteView.as_view(), name='supplier_delete'),
]
#--------------------------------------------------------------------------------