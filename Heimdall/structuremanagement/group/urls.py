#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Views
#--------------------------------------------------------------------------------
from .views import (
    GroupView,
    GroupListView,
    GroupTableView,
    GroupCreateUpdateDetailView,
    GroupDeleteView,
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Group
    path('',GroupView.as_view(), name='group_overview'),
    path('list/',GroupListView.as_view(), name='group_list'),
    path('table/',GroupTableView.as_view(), name='group_table'),
    path('create/',GroupCreateUpdateDetailView.as_view(), name='group_create'),
    path('update/<slug:group>/',GroupCreateUpdateDetailView.as_view(), name='group_update'),
    path('detail/<slug:group>/',GroupCreateUpdateDetailView.as_view(), name='group_detail'),
    path('delete/<slug:group>/',GroupDeleteView.as_view(), name='group_delete'),
]