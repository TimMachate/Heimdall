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
from personalmanagement.sectionsettings.models import SectionSettings
from structuremanagement.section.models import Section
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from personalmanagement.sectionsettings.forms import SectionSettingsListForm, SectionSettingsTableForm
from structuremanagement.section.forms import SectionForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class SectionView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.view_section'

    template_name = 'section/templates/section_overview.html'

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
        queryset = Section.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'structuremanagement'
        self.context['model'] = 'section'
        # Data Url
        fields = "id,name,reference_number,responsible,substitute,url"
        self.context["api_data_url"] = reverse("structuremanagementAPI:section_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class SectionListView(SectionView):

    permission_required = 'structuremanagement.list_section'

    template_name = 'section/templates/section_list.html'

    form_class = SectionSettingsListForm

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
        fields = "reference_number,name,department,short_form,color,process_instruction,picture,url"
        self.context["api_data_url"] = reverse("structuremanagementAPI:section_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class SectionTableView(SectionView):

    permission_required = 'structuremanagement.table_section'

    template_name = 'section/templates/section_table.html'

    form_class = SectionSettingsTableForm

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
        fields = "reference_number,name,department,color,position_count,employee_count,create,update"
        self.context["api_data_url"] = reverse("structuremanagementAPI:section_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class SectionCreateUpdateDetailView(SectionView):

    permission_required = 'structuremanagement.add_section'

    template_name = 'section/templates/section_createupdatedetail.html'
    
    form_class = SectionForm

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

        return redirect('structuremanagement:section_update', section=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('section'):
            queryset = get_object_or_404(Section, slug=self.kwargs.get('section'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class SectionDeleteView(PermissionRequiredMixin, MainView):

    permission_required = 'structuremanagement.delete_section'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('section'):
            Section.objects.get(slug = self.kwargs.get('section')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------