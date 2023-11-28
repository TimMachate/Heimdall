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
from relationshipmanagement.company.models import SupplierProxy
from relationshipmanagement.person.models import Person
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from relationshipmanagement.company.forms import CompanyForm,TelephoneFormset,EmailFormset,SupplierFormset
from relationshipmanagement.person.forms import PersonForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class SupplierView(PermissionRequiredMixin,MainView):

    permission_required = 'relationshipmanagement.view_supplier'

    template_name = 'supplier_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = SupplierProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'supplier'
#--------------------------------------------------------------------------------
class SupplierListView(SupplierView):

    permission_required = 'relationshipmanagement.list_supplier'

    template_name = 'supplier_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,name,url"
        self.context["api_data_url"] = reverse("relationshipmanagementAPI:supplier_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class SupplierTableView(SupplierView):

    permission_required = 'relationshipmanagement.table_supplier'

    template_name = 'supplier_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,name,street,house_number,post_code,city,country,telephones,emails,create,update"
        self.context["api_data_url"] = reverse("relationshipmanagementAPI:supplier_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class SupplierCreateUpdateDetailView(SupplierView):

    template_name = 'supplier_createupdatedetail.html'

    form_class = CompanyForm
    formset_email = EmailFormset
    formset_supplier = SupplierFormset
    formset_telephone = TelephoneFormset

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'])
        self.context['formset_email'] = self.formset_email(instance = self.context['queryset'])
        self.context['formset_supplier'] = self.formset_supplier(instance = self.context['queryset'])
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
            obj.supplier = True
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

        formset_supplier = self.formset_supplier(request.POST,request.FILES,instance=obj)
        if formset_supplier.is_valid():
            for form in formset_supplier:
                if form.is_valid():
                    supplier = form.save(commit=False)
                    supplier.company_id = obj
                    supplier.save()
        self.context['formset_supplier'] = formset_supplier
        
        formset_telephone = self.formset_telephone(request.POST,request.FILES,instance=obj)
        if formset_telephone.is_valid():
            for form in formset_telephone:
                if form.is_valid():
                    telephone = form.save(commit=False)
                    telephone.company_id = obj
                    if telephone.number:
                        telephone.save()
        self.context['formset_telephone'] = formset_telephone

        return redirect('relationshipmanagement:supplier_update', supplier=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('supplier'):
            queryset = SupplierProxy.objects.get(slug=self.kwargs.get('supplier'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class SupplierCreateView(SupplierCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.add_supplier',)
#--------------------------------------------------------------------------------
class SupplierDetailView(SupplierCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.detail_supplier',)
#--------------------------------------------------------------------------------
class SupplierUpdateView(SupplierCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.change_supplier',)
#--------------------------------------------------------------------------------
class SupplierDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'relationshipmanagement.delete_supplier'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('supplier'):
            get_object_or_404(SupplierProxy,slug = self.kwargs.get('supplier')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('relationshipmanagement:supplier_list')
#--------------------------------------------------------------------------------