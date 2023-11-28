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
from programs.views.programs import (
    ProgramListView,
    ProgramTableView,
    ProgramCreateUpdateView,
    ProgramDetailView,
    ProgramDeleteView
    )
#--------------------------------------------------------------------------------

app_name = 'programs'

urlpatterns = [
    path('',ProgramListView.as_view(), name='program'),
    path('list/',ProgramListView.as_view(), name='program_list'),
    path('table/',ProgramTableView.as_view(), name='program_table'),
    path('create/',ProgramCreateUpdateView.as_view(), name='program_create'),
    path('update/<int:id>/',ProgramCreateUpdateView.as_view(), name='program_update'),
    path('detail/<int:id>/',ProgramDetailView.as_view(), name='program_detail'),
    path('delete/<int:id>/',ProgramDeleteView.as_view(), name='program_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)