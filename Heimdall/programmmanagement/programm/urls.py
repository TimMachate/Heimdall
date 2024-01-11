"""
#--------------------------------------------------------------------------------
# Urls File from Model Programm
# 16.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from programmmanagement.programm.views import (
    ProgrammView,
    ProgrammListView,
    ProgrammTableView,
    ProgrammCreateView,
    ProgrammUpdateView,
    ProgrammDeleteView,
    ProgrammDetailView,
    ProgrammProgrammView
)
#--------------------------------------------------------------------------------
urlpatterns = [
    # Programm
    path(
        '',
        ProgrammView.as_view(),
        name='programm_overview'
    ),
    path(
        'list/',
        ProgrammListView.as_view(),
        name='programm_list'
    ),
    path(
        'table/',
        ProgrammTableView.as_view(),
        name='programm_table'
    ),
    path(
        'create/',
        ProgrammCreateView.as_view(),
        name='programm_create'
    ),
    path(
        'update/<slug:programm>/',
        ProgrammUpdateView.as_view(),
        name='programm_update'
    ),
    path(
        'detail/<slug:programm>/',
        ProgrammDetailView.as_view(),
        name='programm_detail'
    ),
    path(
        'delete/<slug:programm>/',
        ProgrammDeleteView.as_view(),
        name='programm_delete'
    ),
    path(
        'detail/<slug:programm>/programm',
        ProgrammProgrammView.as_view(),
        name='programmmanagement_page'
    ),
]
#--------------------------------------------------------------------------------
