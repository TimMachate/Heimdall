#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Views
#--------------------------------------------------------------------------------
from commission.views.commission import (
    CommissionView,
    CommissionTableView,
    CommissionCreateUpdateView,
    CommissionDetailView,
    CommissionDeleteView,
    CommissionSOSView,
    CommissionSOSChangeView,
    CommissionTicketView,
    CommissionTicketChangeView,
    CommissionDeliveryChangeView,
)
#--------------------------------------------------------------------------------

app_name = 'commission'

urlpatterns = [
    path('',CommissionView.as_view(), name='overview'),
    # Commission
    path('commission/',CommissionView.as_view(), name='commission'),
    path('commission/table/',CommissionTableView.as_view(), name='commission_table'),
    path('commission/create/',CommissionCreateUpdateView.as_view(), name='commission_create'),
    path('commission/update/<int:id>/',CommissionCreateUpdateView.as_view(), name='commission_update'),
    path('commission/detail/<int:id>/',CommissionDetailView.as_view(), name='commission_detail'),
    path('commission/delete/<int:id>/',CommissionDeleteView.as_view(), name='commission_delete'),
    path('commission/sos/',CommissionSOSView.as_view(), name='commission_sos'),
    path('commission/sos/change/<int:id>/',CommissionSOSChangeView.as_view(), name='commission_sos_change'),
    path('commission/ticket/',CommissionTicketView.as_view(), name='commission_ticket'),
    path('commission/ticket/change/<int:id>/',CommissionTicketChangeView.as_view(), name='commission_ticket_change'),
    path('commission/delivery/change/<int:id>/',CommissionDeliveryChangeView.as_view(), name='commission_delivery_change'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)