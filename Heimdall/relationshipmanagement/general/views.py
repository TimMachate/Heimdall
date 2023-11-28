#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.company.models import GeneralProxy
from relationshipmanagement.person.models import Person
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from relationshipmanagement.company.forms import CompanyForm,TelephoneFormset,EmailFormset,GeneralFormset
from relationshipmanagement.person.forms import PersonForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class GeneralView(PermissionRequiredMixin,MainView):

    permission_required = 'relationshipmanagement.view_general'

    template_name = 'general_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = GeneralProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'general'
#--------------------------------------------------------------------------------
class GeneralListView(GeneralView):

    permission_required = 'relationshipmanagement.list_general'

    template_name = 'general_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,name,url"
        self.context["api_data_url"] = reverse("relationshipmanagementAPI:general_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class GeneralTableView(GeneralView):

    permission_required = 'relationshipmanagement.table_general'

    template_name = 'general_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,name,street,house_number,post_code,city,country,telephones,emails,create,update"
        self.context["api_data_url"] = reverse("relationshipmanagementAPI:general_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class GeneralCreateUpdateDetailView(GeneralView):

    template_name = 'general_createupdatedetail.html'

    form_class = CompanyForm
    formset_email = EmailFormset
    formset_general = GeneralFormset
    formset_telephone = TelephoneFormset

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'])
        self.context['formset_email'] = self.formset_email(instance = self.context['queryset'])
        self.context['formset_general'] = self.formset_general(instance = self.context['queryset'])
        self.context['formset_telephone'] = self.formset_telephone(instance = self.context['queryset'])
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

        formset_email = self.formset_email(request.POST,request.FILES,instance=obj)
        if formset_email.is_valid():
            for form in formset_email:
                if form.is_valid():
                    email = form.save(commit=False)
                    email.company_id = obj
                    if email.email:
                        email.save()
        self.context['formset_email'] = formset_email

        formset_general = self.formset_general(request.POST,request.FILES,instance=obj)
        if formset_general.is_valid():
            for form in formset_general:
                if form.is_valid():
                    general = form.save(commit=False)
                    general.company_id = obj
                    general.save()
        self.context['formset_general'] = formset_general
        
        formset_telephone = self.formset_telephone(request.POST,request.FILES,instance=obj)
        if formset_telephone.is_valid():
            for form in formset_telephone:
                if form.is_valid():
                    telephone = form.save(commit=False)
                    telephone.company_id = obj
                    if telephone.number:
                        telephone.save()
        self.context['formset_telephone'] = formset_telephone

        return redirect('relationshipmanagement:general_update', general=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('general'):
            queryset = GeneralProxy.objects.get(slug=self.kwargs.get('general'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class GeneralCreateView(GeneralCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.add_general',)
#--------------------------------------------------------------------------------
class GeneralDetailView(GeneralCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.detail_general',)
#--------------------------------------------------------------------------------
class GeneralUpdateView(GeneralCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.change_general',)
#--------------------------------------------------------------------------------
class GeneralDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'relationshipmanagement.delete_general'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('general'):
            get_object_or_404(GeneralProxy,slug = self.kwargs.get('general')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('relationshipmanagement:general_list')
#--------------------------------------------------------------------------------