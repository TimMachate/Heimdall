#--------------------------------------------------------------------------------
# View File from Model StorageItem
# 28.10.2023
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
from storagemanagement.storageitem.models import StorageItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.storageitem.forms import StorageItemForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class StorageItemView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.view_storageitem'

    template_name = 'storageitem_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = StorageItem.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'storageitem'
        # Data Url
        self.context["fields"] = "id,name,url_detail,status,stock_count,stock_unit,stock_percentage,url_booking_add,url_booking_create,url_booking_remove,url_order,order_count,url_request_create,request_count"
        self.context["api_data_url"] = reverse("storagemanagementAPI:storageitem_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class StorageItemListView(StorageItemView):

    permission_required = 'storagemanagement.list_storageitem'

    template_name = 'storageitem_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,status,name,reference_number,company_name,company_url_detail,stock_count,stock_percentage,booking_last,url_request_create,url_booking_add,url_booking_remove,url_detail,url_update,url_delete"
        self.context["api_data_url"] = reverse("storagemanagementAPI:storageitem_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class StorageItemTableView(StorageItemView):

    permission_required = 'storagemanagement.table_storageitem'

    template_name = 'storageitem_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,name,reference_number,company_name,company_url_detail,companyitem_name,companyitem_url_detail,companyitem_item_number,stock_count,stock_percentage,stock_value,minimum,warning,maximum,booking_count,booking_last,"
        self.context["api_data_url"] = reverse("storagemanagementAPI:storageitem_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class StorageItemCreateUpdateDetailView(StorageItemView):

    template_name = 'storageitem_createupdatedetail.html'
    
    form_class = StorageItemForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'])
        return render(request, self.template_name, self.context)

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
            return redirect('storagemanagement:storageitem_update', storageitem=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('storageitem'):
            queryset = StorageItem.objects.get(slug=self.kwargs.get('storageitem'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class StorageItemCreateView(StorageItemCreateUpdateDetailView):
    permission_required = ('storagemanagement.add_storageitem',)
#--------------------------------------------------------------------------------
class StorageItemDetailView(StorageItemCreateUpdateDetailView):
    permission_required = ('storagemanagement.detail_storageitem',)
#--------------------------------------------------------------------------------
class StorageItemUpdateView(StorageItemCreateUpdateDetailView):
    permission_required = ('storagemanagement.change_storageitem',)
#--------------------------------------------------------------------------------
class StorageItemDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.delete_storageitem'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('storageitem'):
            get_object_or_404(StorageItem,slug = self.kwargs.get('storageitem')).delete()
            messages.success(request,'StorageItem wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'StorageItem konnte nicht gelöscht werden!')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:storageitem_list')
#--------------------------------------------------------------------------------