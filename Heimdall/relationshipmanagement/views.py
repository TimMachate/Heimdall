"""
#--------------------------------------------------------------------------------
# Views File from App Relationshipmanagement
# 16.12.2023
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
from relationshipmanagement.company.models import Company
from relationshipmanagement.companycontact.models import CompanyContact
from relationshipmanagement.companyitem.models import CompanyItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
# There are no Forms necessary
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
class RelationshipmanagmentView(PermissionRequiredMixin,MainView):
    """
    Relationshipmanagement View shows some App informations on html page
    """

    permission_required = 'relationshipmanagement.view_company'

    template_name = 'relationshipmanagement.html'

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains data
        """
        context = super().get_context_data(**kwargs)
        context["company_count"] = Company.objects.all().count()
        context["companycontact_count"] = CompanyContact.objects.all().count()
        context["companyitem_count"] = CompanyItem.objects.all().count()
        return context
#--------------------------------------------------------------------------------
