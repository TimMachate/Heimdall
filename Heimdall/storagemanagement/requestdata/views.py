#--------------------------------------------------------------------------------
# View File from Model Request Data
# 10.11.2023
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
from storagemanagement.companyitem.models import CompanyItem
from storagemanagement.offer.models import Offer
from storagemanagement.offerdata.models import OfferData
from storagemanagement.requestdata.models import RequestData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.requestdata.forms import RequestDataForm
from storagemanagement.storageitem.models import StorageItem
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class RequestDataView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.view_requestdata'

    template_name = 'storagemanagement_requestdata_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = RequestData.objects.filter(done=False)
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'requestdata'
        # Urls
        if self.kwargs.get('orderprocess'):
            self.context['url_overview'] = reverse('storagemanagement:orderprocess_requestdata_overview',kwargs={'orderprocess':self.kwargs.get('orderprocess')})
            self.context['url_list'] = reverse('storagemanagement:orderprocess_requestdata_list',kwargs={'orderprocess':self.kwargs.get('orderprocess')})
            self.context['url_table'] = reverse('storagemanagement:orderprocess_requestdata_table',kwargs={'orderprocess':self.kwargs.get('orderprocess')})
            self.context['url_create'] = reverse('storagemanagement:orderprocess_requestdata_create',kwargs={'orderprocess':self.kwargs.get('orderprocess')})
        else:
            self.context['url_overview'] = reverse('storagemanagement:requestdata_overview')
            self.context['url_list'] = reverse('storagemanagement:requestdata_list')
            self.context['url_table'] = reverse('storagemanagement:requestdata_table')
            self.context['url_create'] = reverse('storagemanagement:requestdata_create')
        # Data Url
        self.context["fields"] = "id,create_date,create_time,create_username,amount,unit,storageitem_name,storageitem_url_detail,storageitem_reference_number,companyitem_name,companyitem_url_detail,companyitem_item_number,company_name,company_url_detail,company_reference_number,price,value,notice,url_detail,url_authorize_true,url_authorize_false"
        self.context["api_data_url"] = reverse("storagemanagementAPI:requestdata_list")+"?values={}&done=false".format(
            self.context["fields"],
        )
#--------------------------------------------------------------------------------
class RequestDataListView(RequestDataView):

    permission_required = 'storagemanagement.list_requestdata'

    template_name = 'storagemanagement_requestdata_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = RequestData.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,authorized,authorized_date,authorized_time,authorized_username,create_date,create_time,amount,unit,storageitem_name,storageitem_url_detail,companyitem_name,companyitem_url_detail,company_name,company_url_detail,price,value,notice,url_detail"
        self.context["api_data_url"] = reverse("storagemanagementAPI:requestdata_list")+"?values={}".format(
            self.context["fields"]
        )
#--------------------------------------------------------------------------------
class RequestDataTableView(RequestDataView):

    permission_required = 'storagemanagement.table_requestdata'

    template_name = 'storagemanagement_requestdata_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = RequestData.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,authorized,authorized_date,authorized_time,authorized_username,done,create_date,create_time,create_username,update_date,update_time,update_username,reference_number,amount,unit,storageitem_name,storageitem_url_detail,notice,storageitem_reference_number,companyitem_name,companyitem_url_detail,companyitem_item_number,company_name,company_url_detail,price,value"
        self.context["api_data_url"] = reverse("storagemanagementAPI:requestdata_list")+"?values={}".format(
            self.context["fields"]
        )
#--------------------------------------------------------------------------------
class RequestDataCreateUpdateDetailView(RequestDataView):

    template_name = 'storagemanagement_requestdata_createupdatedetail.html'
    
    form_class = RequestDataForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(
            instance=self.context['queryset'],
            initial = self.get_initial()
        )
        if self.context['queryset']:
            self.context['form'].fields['companyitem'].queryset = CompanyItem.objects.filter(storageitem=self.context['queryset'].storageitem)
        return render(request, self.template_name, self.context)
    
    def get_initial(self,*args,**kwargs):
        result = {}
        if self.kwargs.get("storageitem"):
            result["storageitem"] = StorageItem.objects.get(slug=self.kwargs.get("storageitem"))
            result["amount"] = result["storageitem"].maximum - result["storageitem"].stock_count()
            companyitem = result["storageitem"].companyitem if result["storageitem"].companyitem else None
            companyitem = CompanyItem.objects.filter(storageitem=result["storageitem"]).order_by('price').first() if not companyitem else companyitem
            result["companyitem"] = companyitem
        return result if result != {} else None

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance=self.context['queryset'])
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj = form.save(commit=False)
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()

            # companyitem must have storageitem as Foreign Key
            if obj.storageitem and not obj.companyitem:
                obj.companyitem = obj.storageitem.companyitem
            if obj.companyitem and not obj.storageitem:
                obj.storageitem = obj.companyitem.storageitem
            if obj.storageitem != obj.companyitem.storageitem:
                obj.companyitem = obj.storageitem.companyitem

            if not self.context['queryset']:
                # Price
                obj.price = obj.companyitem.price
            
            obj.save()

        self.context['form'] = form

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:requestdata_update', requestdata=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('requestdata'):
            queryset = RequestData.objects.get(slug=self.kwargs.get('requestdata'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class RequestDataCreateView(RequestDataCreateUpdateDetailView):
    permission_required = ('storagemanagement.add_requestdata',)
#--------------------------------------------------------------------------------
class RequestDataDetailView(RequestDataCreateUpdateDetailView):
    permission_required = ('storagemanagement.detail_requestdata',)
#--------------------------------------------------------------------------------
class RequestDataUpdateView(RequestDataCreateUpdateDetailView):
    permission_required = ('storagemanagement.change_requestdata',)
#--------------------------------------------------------------------------------
class RequestDataDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.delete_requestdata'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('requestdata'):
            get_object_or_404(RequestData,slug = self.kwargs.get('requestdata')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class RequestDataAuthorizedTrueView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.authorize_true_requestdata'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('requestdata'):
            obj = RequestData.objects.get(slug=self.kwargs.get('requestdata'))
            if obj.done == False:
                obj.authorized = True
                obj.authorized_datetime = timezone.now()
                obj.authorized_user_id = user
                obj.done = True
                offerdatas = OfferData.objects.filter(companyitem__company=obj.companyitem.company).exclude(offer__sent=True)
                if offerdatas.exists():
                    offerdata = offerdatas.filter(companyitem=obj.companyitem)
                    if offerdata.exists():
                        offerdata = offerdata.first()
                        offerdata.amount += obj.amount
                        offerdata.save()
                    else:
                        offer = offerdatas.first().offer
                        offerdata=OfferData(
                            create_user_id=user,
                            update_user_id=user,
                            offer = offer,
                            amount = obj.amount,
                            companyitem = obj.companyitem,
                            price = obj.price,
                            storageitem = obj.storageitem,
                        )
                        offerdata.save()
                else:
                    offer = Offer(
                        create_user_id=user,
                        update_user_id=user
                    )
                    offer.save()
                    offerdata=OfferData(
                        create_user_id=user,
                        update_user_id=user,
                        offer = offer,
                        amount = obj.amount,
                        companyitem = obj.companyitem,
                        price = obj.price,
                        storageitem = obj.storageitem,
                    )
                    offerdata.save()
                    
                obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class RequestDataAuthorizedFalseView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.authorize_false_requestdata'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('requestdata'):
            obj = RequestData.objects.get(slug=self.kwargs.get('requestdata'))
            if obj.done == False:
                obj.authorized = False
                obj.authorized_datetime = timezone.now()
                obj.authorized_user_id = user
                obj.done = True
                obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class RequestDataAuthorizedTrueAllView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.authorize_true_requestdata'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        for obj in RequestData.objects.filter(done=False):
            if obj.done == False:
                obj.authorized = True
                obj.authorized_datetime = timezone.now()
                obj.authorized_user_id = user
                obj.done = True
                offerdatas = OfferData.objects.filter(companyitem__company=obj.companyitem.company).exclude(sent=True)
                if offerdatas.exists():
                    offerdata = offerdatas.filter(companyitem=obj.companyitem)
                    if offerdata.exists():
                        offerdata = offerdata.first()
                        offerdata.amount += obj.amount
                        offerdata.save()
                    else:
                        offer = offerdatas.first().offer
                        offerdata=OfferData(
                            create_user_id=user,
                            update_user_id=user,
                            offer = offer,
                            amount = obj.amount,
                            companyitem = obj.companyitem,
                            price = obj.price,
                            storageitem = obj.storageitem,
                        )
                        offerdata.save()
                else:
                    offer = Offer(
                        create_user_id=user,
                        update_user_id=user
                    )
                    offer.save()
                    offerdata=OfferData(
                        create_user_id=user,
                        update_user_id=user,
                        offer = offer,
                        amount = obj.amount,
                        companyitem = obj.companyitem,
                        price = obj.price,
                        storageitem = obj.storageitem,
                    )
                    offerdata.save()
                    
                obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class RequestDataAuthorizedFalseAllView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.authorize_false_requestdata'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        for obj in RequestData.objects.filter(done=False):
            obj.authorized = False
            obj.authorized_datetime = timezone.now()
            obj.authorized_user_id = user
            obj.done = True
            obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------