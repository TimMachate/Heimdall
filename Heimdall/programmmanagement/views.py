"""
#--------------------------------------------------------------------------------
# Views File from App Programmmanagement
# 17.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from programmmanagement.programm.models import Programm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
# There are no Forms necessary
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
class ProgrammmanagementView(PermissionRequiredMixin,MainView):
    """
    ProgrammmanagementView shows some App informations on html page
    """

    permission_required = 'programmmanagement.view_programm'

    template_name = 'programmmanagement.html'

    def get_queryset(self):
        """
        get_queryset

        Returns:
            queryset: contains all Programm
        """
        queryset = Programm.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains data
        """
        context = super().get_context_data(**kwargs)
        context["programm_count"] = Programm.objects.all().count()
        return context
#--------------------------------------------------------------------------------
