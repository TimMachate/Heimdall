#--------------------------------------------------------------------------------
# View File from Model Company
# 25.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

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
from storagemanagement.company.models import Company
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.company.forms import CompanyForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class CompanyView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.view_company'

    template_name = 'storagemanagement_company_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Company.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'company'
        # Data Url
        self.context["fields"] = "id,name,url_detail,telephone,email,companycontact_count,companyitem_count"
        self.context["api_data_url"] = reverse("storagemanagementAPI:company_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class CompanyListView(CompanyView):

    permission_required = 'storagemanagement.list_company'

    template_name = 'storagemanagement_company_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,name,companycontact_count,companyitem_count,storageitem_count,stock_count,stock_value,booking_count,notice,url_detail,url_update,url_delete"
        self.context["api_data_url"] = reverse("storagemanagementAPI:company_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class CompanyTableView(CompanyView):

    permission_required = 'storagemanagement.table_company'

    template_name = 'storagemanagement_company_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,name,street,house_number,post_code,city,country,telephone,email,companycontact_count,companyitem_count,storageitem_count,stock_count,stock_value,booking_count"
        self.context["api_data_url"] = reverse("storagemanagementAPI:company_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class CompanyCreateUpdateDetailView(CompanyView):

    template_name = 'storagemanagement_company_createupdatedetail.html'

    form_class = CompanyForm

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

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:company_update', company=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('company'):
            queryset = Company.objects.get(slug=self.kwargs.get('company'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class CompanyCreateView(CompanyCreateUpdateDetailView):
    permission_required = ('storagemanagement.add_company',)
#--------------------------------------------------------------------------------
class CompanyDetailView(CompanyCreateUpdateDetailView):
    permission_required = ('storagemanagement.detail_company',)
#--------------------------------------------------------------------------------
class CompanyUpdateView(CompanyCreateUpdateDetailView):
    permission_required = ('storagemanagement.change_company',)
#--------------------------------------------------------------------------------
class CompanyDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.delete_company'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('company'):
            get_object_or_404(Company,slug = self.kwargs.get('company')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:company_list')
#--------------------------------------------------------------------------------