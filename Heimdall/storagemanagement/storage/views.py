#--------------------------------------------------------------------------------
# View File from Model Storage
# 04.11.2023
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
from storagemanagement.booking.models import Booking
from storagemanagement.companyitem.models import CompanyItem
from storagemanagement.storage.models import Storage
from storagemanagement.storageitem.models import StorageItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.storage.forms import StorageForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class StorageView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.view_storage'

    template_name = 'storagemanagement_storage_overview.html'

    def get_queryset(self, *args, **kwargs):
        if Storage.objects.all().count()>0:
            objects = set([obj.companyitem.storageitem.id for obj in Storage.objects.filter(unload_datetime=None)])
            queryset = StorageItem.objects.filter(id__in = objects)
        else:
            queryset = None
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'storage'

        # Urls
        if self.kwargs.get('company') and not self.kwargs.get('companyitem'):
            self.context['url_overview'] = reverse('storagemanagement:company_storage_overview',kwargs={'company':self.kwargs.get('company')})
            self.context['url_list'] = reverse('storagemanagement:company_storage_list',kwargs={'company':self.kwargs.get('company')})
            self.context['url_table'] = reverse('storagemanagement:company_storage_table',kwargs={'company':self.kwargs.get('company')})
            self.context['url_create'] = reverse('storagemanagement:company_storage_create',kwargs={'company':self.kwargs.get('company')})
        elif self.kwargs.get('companyitem'):
            self.context['url_overview'] = reverse('storagemanagement:companyitem_storage_overview',kwargs={'companyitem':self.kwargs.get('companyitem')})
            self.context['url_list'] = reverse('storagemanagement:companyitem_storage_list',kwargs={'companyitem':self.kwargs.get('companyitem')})
            self.context['url_table'] = reverse('storagemanagement:companyitem_storage_table',kwargs={'companyitem':self.kwargs.get('companyitem')})
            self.context['url_create'] = reverse('storagemanagement:companyitem_storage_create',kwargs={'companyitem':self.kwargs.get('companyitem')})
        elif self.kwargs.get('storageitem'):
            self.context['url_overview'] = reverse('storagemanagement:storageitem_storage_overview',kwargs={'storageitem':self.kwargs.get('storageitem')})
            self.context['url_list'] = reverse('storagemanagement:storageitem_storage_list',kwargs={'storageitem':self.kwargs.get('storageitem')})
            self.context['url_table'] = reverse('storagemanagement:storageitem_storage_table',kwargs={'storageitem':self.kwargs.get('storageitem')})
            self.context['url_create'] = reverse('storagemanagement:storageitem_storage_create',kwargs={'storageitem':self.kwargs.get('storageitem')})
        else:
            self.context['url_overview'] = reverse('storagemanagement:storage_overview')
            self.context['url_list'] = reverse('storagemanagement:storage_list')
            self.context['url_table'] = reverse('storagemanagement:storage_table')
            self.context['url_create'] = reverse('storagemanagement:storage_create')

        # Data Url
        self.context["company"] = self.kwargs.get('company') if self.kwargs.get('company') else ""
        self.context["companyitem"] = self.kwargs.get('companyitem') if self.kwargs.get('companyitem') else ""
        self.context["storageitem"] = self.kwargs.get('storageitem') if self.kwargs.get('storageitem') else ""
        self.context["fields"] = ""
        self.context["api_data_url"] = reverse("storagemanagementAPI:storage_list")+"?values={}&companyitem__company__slug={}&companyitem__slug={}&companyitem__storageitem__slug={}".format(
            self.context["fields"],
            self.context["company"],
            self.context["companyitem"],
            self.context["storageitem"]
        )
#--------------------------------------------------------------------------------
class StorageListView(StorageView):

    permission_required = 'storagemanagement.list_storage'

    template_name = 'storagemanagement_storage_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,create_date,create_time,storageitem_name,storageitem_url_detail,companyitem_name,companyitem_url_detail,company_name,company_url_detail,unit,value,notice,url_detail,url_unload"
        self.context["api_data_url"] = reverse("storagemanagementAPI:storage_list")+"?values={}&companyitem__company__slug={}&companyitem__slug={}&companyitem__storageitem__slug={}".format(
            self.context["fields"],
            self.context["company"],
            self.context["companyitem"],
            self.context["storageitem"]
        )
#--------------------------------------------------------------------------------
class StorageTableView(StorageView):

    permission_required = 'storagemanagement.table_storage'

    template_name = 'storagemanagement_storage_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,create_date,create_time,storageitem_name,storageitem_url_detail,storageitem_reference_number,companyitem_name,companyitem_url_detail,companyitem_item_number,company_name,company_url_detail,unit,value"
        self.context["api_data_url"] = reverse("storagemanagementAPI:storage_list")+"?values={}&companyitem__company__slug={}&companyitem__slug={}&companyitem__storageitem__slug={}".format(
            self.context["fields"],
            self.context["company"],
            self.context["companyitem"],
            self.context["storageitem"]
        )
#--------------------------------------------------------------------------------
class StorageCreateUpdateDetailView(StorageView):

    template_name = 'storagemanagement_storage_createupdatedetail.html'
    
    form_class = StorageForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'])
        if self.kwargs.get("storageitem"):
            self.context['form'].fields["companyitem"].queryset = StorageItem.objects.get(slug=self.kwargs.get("storageitem")).companyitems()
        if self.get_initial():
            self.context['form'].initial = self.get_initial()
        return render(request, self.template_name, self.context)
    
    def get_initial(self):
        result = {}
        if self.kwargs.get('companyitem'):
            result['companyitem'] = CompanyItem.objects.get(slug=self.kwargs.get('companyitem'))
        if self.kwargs.get('booking'):
            result['booking'] = Booking.objects.get(slug=self.kwargs.get('booking'))
        if result == {}:
            result = None
        return result

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance=self.context['queryset'])
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj = form.save(commit=False)
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            obj.save()

        self.context['form'] = form
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:storage_update', storage=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('storage'):
            queryset = Storage.objects.get(slug=self.kwargs.get('storage'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class StorageCreateView(StorageCreateUpdateDetailView):
    permission_required = ('storagemanagement.add_storage',)
#--------------------------------------------------------------------------------
class StorageDetailView(StorageCreateUpdateDetailView):
    permission_required = ('storagemanagement.detail_storage',)
#--------------------------------------------------------------------------------
class StorageUpdateView(StorageCreateUpdateDetailView):
    permission_required = ('storagemanagement.change_storage',)
#--------------------------------------------------------------------------------
class StorageDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.delete_storage'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('storage'):
            get_object_or_404(Storage,slug = self.kwargs.get('storage')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:storage_list')
#--------------------------------------------------------------------------------
class StorageUnloadView(PermissionRequiredMixin,MainView):
    permission_required = 'storagemanagement.unload_storage'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        query = self.get_queryset()
        query.unload_user_id = user
        query.unload_datetime = timezone.now()
        query.save()

        old_stock = Booking.objects.filter(companyitem = query.companyitem).last().stock if Booking.objects.filter(companyitem = query.companyitem) else 0
        new_stock = old_stock -1
        
        # set stock to 0 if new_stock is smaller then 0
        if new_stock <0:
            new_stock = 0

        booking = Booking(
            amount = -1,
            create_user_id = user,
            price = query.companyitem.price,
            stock = new_stock,
            companyitem = CompanyItem.objects.get(id=query.companyitem.id),
            update_user_id = user,
            update_datetime = timezone.now(),
        )
        booking.save()
        if 'next' in request.GET:
            return redirect(request.GET.get('next'))
        else:
            return redirect("storagemanagement:storage_overview")

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('storage'):
            queryset = get_object_or_404(Storage,slug = self.kwargs.get('storage'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------