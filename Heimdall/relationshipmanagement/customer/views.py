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
from relationshipmanagement.company.models import CustomerProxy
from relationshipmanagement.person.models import Person
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from relationshipmanagement.company.forms import CompanyForm,TelephoneFormset,EmailFormset,CustomerFormset
from relationshipmanagement.person.forms import PersonForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class CustomerView(PermissionRequiredMixin,MainView):

    permission_required = 'relationshipmanagement.view_customer'

    template_name = 'customer_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = CustomerProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'customer'
#--------------------------------------------------------------------------------
class CustomerListView(CustomerView):

    permission_required = 'relationshipmanagement.list_customer'

    template_name = 'customer_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,name,url"
        self.context["api_data_url"] = reverse("relationshipmanagementAPI:customer_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class CustomerTableView(CustomerView):

    permission_required = 'relationshipmanagement.table_customer'

    template_name = 'customer_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,name,street,house_number,post_code,city,country,telephones,emails,create,update"
        self.context["api_data_url"] = reverse("relationshipmanagementAPI:customer_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class CustomerCreateUpdateDetailView(CustomerView):

    template_name = 'customer_createupdatedetail.html'

    form_class = CompanyForm
    formset_customer = CustomerFormset
    formset_email = EmailFormset
    formset_telephone = TelephoneFormset

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'])
        self.context['formset_customer'] = self.formset_customer(instance = self.context['queryset'])
        self.context['formset_email'] = self.formset_email(instance = self.context['queryset'])
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
            obj.customer = True
            obj.save()
        self.context['form'] = form
            
        formset_customer = self.formset_customer(request.POST,request.FILES,instance=obj)
        if formset_customer.is_valid():
            for form in formset_customer:
                if form.is_valid():
                    customer = form.save(commit=False)
                    customer.company_id = obj
                    customer.save()
        self.context['formset_customer'] = formset_customer

        formset_email = self.formset_email(request.POST,request.FILES,instance=obj)
        if formset_email.is_valid():
            for form in formset_email:
                if form.is_valid():
                    email = form.save(commit=False)
                    email.company_id = obj
                    if email.email:
                        email.save()
        self.context['formset_email'] = formset_email
        
        formset_telephone = self.formset_telephone(request.POST,request.FILES,instance=obj)
        if formset_telephone.is_valid():
            for form in formset_telephone:
                if form.is_valid():
                    telephone = form.save(commit=False)
                    telephone.company_id = obj
                    if telephone.number:
                        telephone.save()
        self.context['formset_telephone'] = formset_telephone

        return redirect('relationshipmanagement:customer_update', customer=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('customer'):
            queryset = get_object_or_404(CustomerProxy,slug=self.kwargs.get('customer'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class CustomerCreateView(CustomerCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.add_customer',)
#--------------------------------------------------------------------------------
class CustomerDetailView(CustomerCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.detail_customer',)
#--------------------------------------------------------------------------------
class CustomerUpdateView(CustomerCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.change_customer',)
#--------------------------------------------------------------------------------
class CustomerDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'relationshipmanagement.delete_customer'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('customer'):
            get_object_or_404(CustomerProxy,slug = self.kwargs.get('customer')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('relationshipmanagement:customer_list')
#--------------------------------------------------------------------------------