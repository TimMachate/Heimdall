#--------------------------------------------------------------------------------
# View File from Model Booking
# 15.10.2023
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
from storagemanagement.company.models import Company
from storagemanagement.companyitem.models import CompanyItem
from storagemanagement.storage.models import Storage
from storagemanagement.storageitem.models import StorageItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.booking.forms import BookingForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class BookingView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.view_booking'

    template_name = 'storagemanagement_booking_overview.html'

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('company') and not self.kwargs.get('companyitem'):
            queryset = Booking.objects.filter(companyitem__company__slug=self.kwargs.get('company'))
        elif self.kwargs.get('companyitem'):
            queryset = Booking.objects.filter(companyitem__slug=self.kwargs.get('companyitem'))
        elif self.kwargs.get('storageitem'):
            queryset = Booking.objects.filter(companyitem__storageitem__slug=self.kwargs.get('storageitem'))
        else:
            queryset = Booking.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'booking'

        # Urls
        if self.kwargs.get('company') and not self.kwargs.get('companyitem'):
            self.context['url_overview'] = reverse('storagemanagement:company_booking_overview',kwargs={'company':self.kwargs.get('company')})
            self.context['url_list'] = reverse('storagemanagement:company_booking_list',kwargs={'company':self.kwargs.get('company')})
            self.context['url_table'] = reverse('storagemanagement:company_booking_table',kwargs={'company':self.kwargs.get('company')})
            self.context['url_create'] = reverse('storagemanagement:company_booking_create',kwargs={'company':self.kwargs.get('company')})
        elif self.kwargs.get('companyitem'):
            self.context['url_overview'] = reverse('storagemanagement:companyitem_booking_overview',kwargs={'companyitem':self.kwargs.get('companyitem')})
            self.context['url_list'] = reverse('storagemanagement:companyitem_booking_list',kwargs={'companyitem':self.kwargs.get('companyitem')})
            self.context['url_table'] = reverse('storagemanagement:companyitem_booking_table',kwargs={'companyitem':self.kwargs.get('companyitem')})
            self.context['url_create'] = reverse('storagemanagement:companyitem_booking_create',kwargs={'companyitem':self.kwargs.get('companyitem')})
        elif self.kwargs.get('storageitem'):
            self.context['url_overview'] = reverse('storagemanagement:storageitem_booking_overview',kwargs={'storageitem':self.kwargs.get('storageitem')})
            self.context['url_list'] = reverse('storagemanagement:storageitem_booking_list',kwargs={'storageitem':self.kwargs.get('storageitem')})
            self.context['url_table'] = reverse('storagemanagement:storageitem_booking_table',kwargs={'storageitem':self.kwargs.get('storageitem')})
            self.context['url_create'] = reverse('storagemanagement:storageitem_booking_create',kwargs={'storageitem':self.kwargs.get('storageitem')})
        else:
            self.context['url_overview'] = reverse('storagemanagement:booking_overview')
            self.context['url_list'] = reverse('storagemanagement:booking_list')
            self.context['url_table'] = reverse('storagemanagement:booking_table')
            self.context['url_create'] = reverse('storagemanagement:booking_create')
        
        # Data Url
        self.context["company"] = self.kwargs.get('company') if self.kwargs.get('company') else ""
        self.context["companyitem"] = self.kwargs.get('companyitem') if self.kwargs.get('companyitem') else ""
        self.context["storageitem"] = self.kwargs.get('storageitem') if self.kwargs.get('storageitem') else ""
        self.context["fields"] = ""
        self.context["api_data_url"] = reverse("storagemanagementAPI:booking_list")+"?values={}&companyitem__company__slug={}&companyitem__slug={}&companyitem__storageitem__slug={}".format(
            self.context["fields"],
            self.context["company"],
            self.context["companyitem"],
            self.context["storageitem"]
        )
#--------------------------------------------------------------------------------
class BookingListView(BookingView):

    permission_required = 'storagemanagement.list_booking'

    template_name = 'storagemanagement_booking_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "create_date,create_time,reference_number,storageitem_name,storageitem_url_detail,storageitem_reference_number,companyitem_name,companyitem_url_detail,companyitem_item_number,company_name,company_url_detail,price,amount,value,unit,notice,url_detail,url_update,url_delete"
        self.context["api_data_url"] = reverse("storagemanagementAPI:booking_list")+"?values={}&companyitem__company__slug={}&companyitem__slug={}&companyitem__storageitem__slug={}".format(
            self.context["fields"],
            self.context["company"],
            self.context["companyitem"],
            self.context["storageitem"]
        )
#--------------------------------------------------------------------------------
class BookingTableView(BookingView):

    permission_required = 'storagemanagement.table_booking'

    template_name = 'storagemanagement_booking_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "create_date,create_time,reference_number,storageitem_name,storageitem_url_detail,storageitem_reference_number,companyitem_name,companyitem_url_detail,companyitem_item_number,company_name,company_url_detail,price,amount,value,unit,stock"
        self.context["api_data_url"] = reverse("storagemanagementAPI:booking_list")+"?values={}&companyitem__company__slug={}&companyitem__slug={}&companyitem__storageitem__slug={}".format(
            self.context["fields"],
            self.context["company"],
            self.context["companyitem"],
            self.context["storageitem"]
        )
#--------------------------------------------------------------------------------
class BookingCreateUpdateDetailView(BookingView):

    template_name = 'storagemanagement_booking_createupdatedetail.html'
    
    form_class = BookingForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(
            instance=self.context['queryset'],
            initial=self.get_initial()
        )
        if self.kwargs.get("company"):
            self.context['form'].fields["companyitem"].queryset = Company.objects.get(slug=self.kwargs.get("company")).companyitems()
        if self.kwargs.get("storageitem"):
            self.context['form'].fields["companyitem"].queryset = CompanyItem.objects.filter(storageitem__slug=self.kwargs.get("storageitem"))
        return render(request, self.template_name, self.context)
    
    def get_initial(self):
        result = {}
        if self.kwargs.get('companyitem'):
            result['companyitem'] = CompanyItem.objects.get(slug=self.kwargs.get('companyitem'))
        if self.kwargs.get('storageitem'):
            companyitem = StorageItem.objects.get(slug=self.kwargs.get('storageitem')).companyitem if StorageItem.objects.get(slug=self.kwargs.get('storageitem')).companyitem else None
            companyitem = CompanyItem.objects.filter(storageitem__slug=self.kwargs.get('storageitem')).order_by('-price').first() if not companyitem else companyitem
            result['companyitem'] = companyitem
        if self.kwargs.get('amount'):
            result['amount'] = self.kwargs.get('amount')
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

            if 'add_value' in request.POST:
                # take amount and abs
                obj.amount = abs(obj.amount)

            if 'remove_value' in request.POST:
                # take amount and abs
                obj.amount = 0-abs(obj.amount)

            old_stock = Booking.objects.filter(companyitem = obj.companyitem).last().stock if Booking.objects.filter(companyitem = obj.companyitem) else 0
            new_stock = old_stock + obj.amount
            
            # set stock to 0 if new_stock is smaller then 0
            if new_stock <0:
                new_stock = 0

            # save the new stock value in stock of booking model
            obj.stock = new_stock
            obj.price = obj.companyitem.price
            obj.save()

            # load items in stock or unload items in stock
            if obj.amount > 0:
                # create the items in stock
                for i in range(0,obj.amount,1):
                    storage = Storage(
                        booking = Booking.objects.get(id=obj.id),
                        companyitem = CompanyItem.objects.get(id=obj.companyitem.id),
                        create_user_id = user,
                        update_user_id = user,
                        update_datetime = timezone.now(),
                    )
                    storage.save()
            if obj.amount < 0:
                # unload the items in stock
                storages = Storage.objects.filter(
                    companyitem = obj.companyitem,
                    unload_datetime = None,
                ).values_list('id',flat=True)[0:abs(obj.amount)]
                Storage.objects.filter(id__in = list(storages)).update(
                    unload_user_id = user,
                    unload_datetime = timezone.now(),
                    update_user_id = user,
                    update_datetime = timezone.now(),
                )

        self.context['form'] = form
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:booking_update', booking=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('booking'):
            queryset = Booking.objects.get(slug=self.kwargs.get('booking'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class BookingCreateView(BookingCreateUpdateDetailView):
    permission_required = ('storagemanagement.add_booking',)
#--------------------------------------------------------------------------------
class BookingDetailView(BookingCreateUpdateDetailView):
    permission_required = ('storagemanagement.detail_booking',)
#--------------------------------------------------------------------------------
class BookingUpdateView(BookingCreateUpdateDetailView):
    permission_required = ('storagemanagement.change_booking',)
#--------------------------------------------------------------------------------
class BookingDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.delete_booking'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('booking'):
            get_object_or_404(Booking,slug = self.kwargs.get('booking')).delete()
            messages.success(request,'Booking wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Booking konnte nicht gelöscht werden!')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:booking_list')
#--------------------------------------------------------------------------------