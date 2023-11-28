#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.utils import timezone

from main.views.main import MainView

import json
import os
import sys
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from programs.models.programs import Program
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from programs.forms.programs import ProgramForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class ProgramListView(PermissionRequiredMixin,MainView):

    permission_required = 'programs.list_programs'

    template_name = 'program_list.html'

    def get_queryset(self):
        queryset = Program.objects.all()
        return queryset
#--------------------------------------------------------------------------------
class ProgramTableView(ProgramListView):

    permission_required = 'programs.table_programs'

    template_name = 'program_table.html'

    def get_queryset(self):
        queryset = Program.objects.all()
        return queryset
#--------------------------------------------------------------------------------
class ProgramCreateUpdateView(ProgramListView):

    permission_required = ('programs.add_programs','programs.change_programs')

    template_name = 'program_createupdate.html'
    form_class = ProgramForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'])
        return render(request, self.template_name, self.context)

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance=self.context['queryset'])
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj = form.save()
            if not obj.createUser:
                obj.createUser = user
            obj.updateUser = user
            obj.updateTime = timezone.now()
            obj.save()
            self.context['form'] = form
            messages.success(request,'Die!')
        else:
            self.context['form'] = form
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        return redirect('programs:program_update', id=obj.id)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('id'):
            queryset = Program.objects.get(id=self.kwargs.get('id'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------     
class ProgramDetailView(ProgramListView):

    permission_required = 'programs.detail_programs'

    def get(self,request,*args,**kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        if self.context['queryset']:
            self.template_name =self.context['queryset'].htmlfile.name
            return render(request, self.template_name, self.context)
        else:
            return redirect('programs:programs_list')
    
    def post(self,request,*args,**kwargs):
        self.context['queryset'] = self.get_queryset()
        form = request
        sys.path.append(os.path.dirname(os.path.realpath(self.context['queryset'].htmlfile.path)))
        import script
        self.context["data"] = script.Data(form).jsonData()
        obj=Program.objects.get(id=self.kwargs.get('id'))
        obj.json = json.dumps(self.context["data"])
        obj.save()
        return render(request, self.context['queryset'].htmlfile.name, self.context)

    def get_queryset(self):
        if self.kwargs.get('id'):
            queryset = Program.objects.get(id=self.kwargs.get('id'))
        else:
            queryset = None
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        obj = self.get_queryset()
        self.context['data'] = obj.json
        return self.context
#--------------------------------------------------------------------------------
class ProgramDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'programs.delete_programs'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('id'):
            Program.objects.get(id = self.kwargs.get('id')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('programs:program_table')
#--------------------------------------------------------------------------------