#--------------------------------------------------------------------------------
# Views File from Model CompanyItem
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
from storagemanagement.companyitem.models import CompanyItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.companyitem.forms import CompanyItemForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class CompanyItemView(PermissionRequiredMixin, MainView):

    permission_required = 'storagemanagement.view_companyitem'

    template_name = 'storagemanagement_companyitem_overview.html'

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('company'):
            queryset = CompanyItem.objects.filter(company__slug = self.kwargs.get('company'))
        else:
            queryset = CompanyItem.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'companyitem'
        # Urls
        if self.kwargs.get('company'):
            self.context['url_overview'] = reverse('storagemanagement:company_companyitem_overview',kwargs={'company':self.kwargs.get('company')})
            self.context['url_list'] = reverse('storagemanagement:company_companyitem_list',kwargs={'company':self.kwargs.get('company')})
            self.context['url_table'] = reverse('storagemanagement:company_companyitem_table',kwargs={'company':self.kwargs.get('company')})
            self.context['url_create'] = reverse('storagemanagement:company_companyitem_create',kwargs={'company':self.kwargs.get('company')})
        else:
            self.context['url_overview'] = reverse('storagemanagement:companyitem_overview')
            self.context['url_list'] = reverse('storagemanagement:companyitem_list')
            self.context['url_table'] = reverse('storagemanagement:companyitem_table')
            self.context['url_create'] = reverse('storagemanagement:companyitem_create')
        # Data Url
        self.context["company"] = self.kwargs.get('company') if self.kwargs.get('company') else ""
        self.context["fields"] = "id,name,reference_number,url_detail,company_name,company_reference_number,company_url_detail,storageitem_name,storageitem_reference_number,storageitem_url_detail,stock_count,stock_value"
        self.context["api_data_url"] = reverse("storagemanagementAPI:companyitem_list")+"?values={}&company__slug={}".format(
            self.context["fields"],self.context["company"]
        )
#--------------------------------------------------------------------------------
class CompanyItemListView(CompanyItemView):

    permission_required = 'storagemanagement.list_companyitem'

    template_name = 'storagemanagement_companyitem_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["company"] = self.kwargs.get('company') if self.kwargs.get('company') else ""
        self.context["api_data_url"] = reverse("storagemanagementAPI:companyitem_list")+"?values={}&company__slug={}".format(
            self.context["fields"],self.context["company"]
        )
#--------------------------------------------------------------------------------
class CompanyItemTableView(CompanyItemView):

    permission_required = 'storagemanagement.table_companyitem'

    template_name = 'storagemanagement_companyitem_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["company"] = self.kwargs.get('company') if self.kwargs.get('company') else ""
        self.context["api_data_url"] = reverse("storagemanagementAPI:companyitem_list")+"?values={}&company__slug={}".format(
            self.context["fields"],self.context["company"]
        )
#--------------------------------------------------------------------------------
class CompanyItemCreateUpdateDetailView(CompanyItemView):

    template_name = 'storagemanagement_companyitem_createupdatedetail.html'
    
    form_class = CompanyItemForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'])
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
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:companyitem_update', companyitem=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('companyitem'):
            queryset = CompanyItem.objects.get(slug=self.kwargs.get('companyitem'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class CompanyItemCreateView(CompanyItemCreateUpdateDetailView):
    permission_required = ('storagemanagement.add_companyitem',)
#--------------------------------------------------------------------------------
class CompanyItemDetailView(CompanyItemCreateUpdateDetailView):
    permission_required = ('storagemanagement.detail_companyitem',)
#--------------------------------------------------------------------------------
class CompanyItemUpdateView(CompanyItemCreateUpdateDetailView):
    permission_required = ('storagemanagement.update_companyitem',)
#--------------------------------------------------------------------------------
class CompanyItemDeleteView(PermissionRequiredMixin, MainView):

    permission_required = 'storagemanagement.delete_companyitem'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('companyitem'):
            get_object_or_404(CompanyItem, slug = self.kwargs.get('companyitem')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:companyitem_list')
#--------------------------------------------------------------------------------