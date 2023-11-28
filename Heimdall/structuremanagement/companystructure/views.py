#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, reverse
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from personalmanagement.employee.models import Employee
from structuremanagement.department.models import Department
from structuremanagement.position.models import Position
from structuremanagement.section.models import Section
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class CompanyStructureView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.view_department'

    template_name = 'companystructure/templates/companystructure.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Department.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'structuremanagement'
        self.context['model'] = 'companystructure'
        self.context['department_count'] = Department.objects.all().count()
        self.context['section_count'] = Section.objects.all().count()
        self.context['position_count'] = Position.objects.all().count()
        self.context['employee_count'] = Employee.objects.all().count()
        self.context['menubar'] = {}
        self.context['menubar']['left'] = None
        self.context['menubar']['right'] = None
        self.context["api_data_url"] = reverse('structuremanagementAPI:companystructure')
#--------------------------------------------------------------------------------