#--------------------------------------------------------------------------------
# Views File from Model CompanyContact
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from storagemanagement.company.models import Company
from storagemanagement.companycontact.models import CompanyContact
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.companycontact.forms import CompanyContactForm,CompanyContactEmailFormset,CompanyContactTelephoneFormset
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class CompanyContactView(PermissionRequiredMixin, MainView):

    permission_required = 'storagemanagement.view_companycontact'

    template_name = 'storagemanagement_companycontact_overview.html'

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('company'):
            queryset = CompanyContact.objects.filter(company__slug = self.kwargs.get('company'))
        else:
            queryset = CompanyContact.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'companycontact'
        # Urls
        if self.kwargs.get('company'):
            self.context['url_overview'] = reverse('storagemanagement:company_companycontact_overview',kwargs={'company':self.kwargs.get('company')})
            self.context['url_list'] = reverse('storagemanagement:company_companycontact_list',kwargs={'company':self.kwargs.get('company')})
            self.context['url_table'] = reverse('storagemanagement:company_companycontact_table',kwargs={'company':self.kwargs.get('company')})
            self.context['url_create'] = reverse('storagemanagement:company_companycontact_create',kwargs={'company':self.kwargs.get('company')})
        else:
            self.context['url_overview'] = reverse('storagemanagement:companycontact_overview')
            self.context['url_list'] = reverse('storagemanagement:companycontact_list')
            self.context['url_table'] = reverse('storagemanagement:companycontact_table')
            self.context['url_create'] = reverse('storagemanagement:companycontact_create')
        # Data Url
        self.context["company"] = self.kwargs.get('company') if self.kwargs.get('company') else ""
        self.context["fields"] = "id,reference_number,name,url_detail,company_name,company_url_detail,email_data,telephone_data"
        self.context["api_data_url"] = reverse("storagemanagementAPI:companycontact_list")+"?values={}&company__slug={}".format(
            self.context["fields"],self.context["company"]
        )
#--------------------------------------------------------------------------------
class CompanyContactListView(CompanyContactView):

    permission_required = 'storagemanagement.list_companycontact'

    template_name = 'storagemanagement_companycontact_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,name,telephone_data,email_data,company_name,company_url_detail,notice,url_detail,url_update,url_delete"
        self.context["api_data_url"] = reverse("storagemanagementAPI:companycontact_list")+"?values={}&company__slug={}".format(
            self.context["fields"],self.context["company"]
        )
#--------------------------------------------------------------------------------
class CompanyContactTableView(CompanyContactView):

    permission_required = 'storagemanagement.table_companycontact'

    template_name = 'storagemanagement_companycontact_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,last_name,first_name,telephone_data,email_data,company_name,company_url_detail"
        self.context["api_data_url"] = reverse("storagemanagementAPI:companycontact_list")+"?values={}&company__slug={}".format(
            self.context["fields"],self.context["company"]
        )
#--------------------------------------------------------------------------------
class CompanyContactCreateUpdateDetailView(CompanyContactView):

    template_name = 'storagemanagement_companycontact_createupdatedetail.html'
    
    form_class = CompanyContactForm
    formset_email = CompanyContactEmailFormset
    formset_telephone = CompanyContactTelephoneFormset

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'],)
        self.context['formset_email'] = self.formset_email(instance = self.context['queryset'])
        self.context['formset_telephone'] = self.formset_telephone(instance = self.context['queryset'])
        if self.get_initial():
            self.context['form'].initial = self.get_initial()
        return render(request, self.template_name, self.context)

    def get_initial(self):
        result = {}
        if self.kwargs.get('company'):
            result['company'] = Company.objects.get(slug=self.kwargs.get('company'))
        if result == {}:
            result = None
        return result

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
                    email.companycontact = obj
                    if email.email:
                        email.save()
        self.context['formset_email'] = formset_email
        
        formset_telephone = self.formset_telephone(request.POST,request.FILES,instance=obj)
        if formset_telephone.is_valid():
            for form in formset_telephone:
                if form.is_valid():
                    telephone = form.save(commit=False)
                    telephone.companycontact = obj
                    if telephone.number:
                        telephone.save()
        self.context['formset_telephone'] = formset_telephone

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:companycontact_update', companycontact=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('companycontact'):
            queryset = CompanyContact.objects.get(slug=self.kwargs.get('companycontact'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class CompanyContactCreateView(CompanyContactCreateUpdateDetailView):
    permission_required = ('storagemanagement.add_companycontact',)
#--------------------------------------------------------------------------------
class CompanyContactDetailView(CompanyContactCreateUpdateDetailView):
    permission_required = ('storagemanagement.detail_companycontact',)
#--------------------------------------------------------------------------------
class CompanyContactUpdateView(CompanyContactCreateUpdateDetailView):
    permission_required = ('storagemanagement.update_companycontact',)
#--------------------------------------------------------------------------------
class CompanyContactDeleteView(PermissionRequiredMixin, MainView):

    permission_required = 'storagemanagement.delete_companycontact'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('companycontact'):
            get_object_or_404(CompanyContact, slug = self.kwargs.get('companycontact')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:companycontact_list')
#--------------------------------------------------------------------------------