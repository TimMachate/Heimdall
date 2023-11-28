#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from personalmanagement.positionsettings.models import PositionSettings
from structuremanagement.position.models import Position
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from personalmanagement.positionsettings.forms import PositionSettingsListForm, PositionSettingsTableForm
from structuremanagement.position.forms import PositionForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class PositionView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.view_position'

    template_name = 'position/templates/position_overview.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance=self.context["api_data"])
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj = form.save()
            messages.success(request,'Die eingegebenen Daten konnten validiert werden!')
        else:
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        self.context['form'] = form
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    def get_queryset(self, *args, **kwargs):
        queryset = Position.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'structuremanagement'
        self.context['model'] = 'position'
        # URL data
        fields = "id,name,reference_number,responsible,substitute,url"
        self.context["api_data_url"] = reverse("structuremanagementAPI:position_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class PositionListView(PositionView):

    permission_required = 'structuremanagement.list_position'

    template_name = 'position/templates/position_list.html'

    form_class = PositionSettingsListForm

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        self.context["form_data"] = self.form_class(
            #instance = self.context["api_data"]
            )
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,name,reference_number,url,section,department"
        self.context["api_data_url"] = reverse("structuremanagementAPI:position_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class PositionTableView(PositionView):

    permission_required = 'structuremanagement.table_position'

    template_name = 'position/templates/position_table.html'

    form_class = PositionSettingsTableForm

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        self.context["form_data"] = self.form_class(
            #instance = self.context["api_data"]
            )
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,name,reference_number,department,section,directions,working_instructions,documents,safety_data_sheets"
        self.context["api_data_url"] = reverse("structuremanagementAPI:position_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class PositionCreateUpdateDetailView(PositionView):

    permission_required = 'structuremanagement.add_position'

    template_name = 'position/templates/position_createupdatedetail.html'
    
    form_class = PositionForm

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
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            obj.save()
            self.context['form'] = form
            messages.success(request,'Die!')
        else:
            self.context['form'] = form
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')

        return redirect('structuremanagement:position_update', position=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('position'):
            queryset = get_object_or_404(Position,slug = self.kwargs.get('position'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class PositionDeleteView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.delete_position'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('position'):
            Position.objects.get(slug = self.kwargs.get('position')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------