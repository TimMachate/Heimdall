#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Views
#--------------------------------------------------------------------------------
from documentationmanagement.picture.views import (
    PictureView,
    PictureListView,
    PictureTableView,
    PictureCreateUpdateDetailView,
    PictureDeleteView
    )
#--------------------------------------------------------------------------------

urlpatterns = [
    # Dateien
    path('',PictureView.as_view(), name='picture_overview'),
    path('list/',PictureListView.as_view(), name='picture_list'),
    path('table/',PictureTableView.as_view(), name='picture_table'),
    path('create/',PictureCreateUpdateDetailView.as_view(), name='picture_create'),
    path('update/<slug:picture>/',PictureCreateUpdateDetailView.as_view(), name='picture_update'),
    path('detail/<slug:picture>/',PictureCreateUpdateDetailView.as_view(), name='picture_detail'),
    path('delete/<slug:picture>/',PictureDeleteView.as_view(), name='picture_delete'),
]