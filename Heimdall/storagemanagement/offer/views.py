#--------------------------------------------------------------------------------
# View File from Model Offer
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
from storagemanagement.companyitem.models import CompanyItem
from storagemanagement.offer.models import Offer
from storagemanagement.order.models import Order
from storagemanagement.orderdata.models import OrderData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.offer.forms import OfferForm,OfferDataFormset
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class OfferView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.view_offer'

    template_name = 'storagemanagement_offer_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Offer.objects.filter(ordered=False)
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'offer'
        # Urls
        self.context['url_overview'] = reverse('storagemanagement:offer_overview')
        self.context['url_list'] = reverse('storagemanagement:offer_list')
        self.context['url_table'] = reverse('storagemanagement:offer_table')
        self.context['url_create'] = reverse('storagemanagement:offer_create')
        # Data Url
        self.context["fields"] = "id,authorized,sent,recived,ordered,create_date,create_time,create_username,company_name,company_reference_number,company_url_detail,item_data,value,notice,url_detail,url_sent,url_recived,url_order_true,url_order_false"
        self.context["api_data_url"] = reverse("storagemanagementAPI:offer_list")+"?values={}&done=false".format(
            self.context["fields"]
        )
#--------------------------------------------------------------------------------
class OfferListView(OfferView):

    permission_required = 'storagemanagement.list_offer'

    template_name = 'storagemanagement_offer_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,authorized,sent,recived,ordered,create_date,create_time,reference_number,company_name,value,item_count,notice,url_detail,url_delete,url_update"
        self.context["api_data_url"] = reverse("storagemanagementAPI:offer_list")+"?values={}".format(
            self.context["fields"]
        )
#--------------------------------------------------------------------------------
class OfferTableView(OfferView):

    permission_required = 'storagemanagement.table_offer'

    template_name = 'storagemanagement_offer_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,authorized,sent,recived,ordered,create_date,create_time,create_user,create_username,update_date,update_time,update_username,company_name,reference_number,value,notice,item_count"
        self.context["api_data_url"] = reverse("storagemanagementAPI:offer_list")+"?values={}".format(
            self.context["fields"]
        )
#--------------------------------------------------------------------------------
class OfferCreateUpdateDetailView(OfferView):

    template_name = 'storagemanagement_offer_createupdatedetail.html'
    
    form_class = OfferForm
    formset_class = OfferDataFormset

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'])
        self.context['formset'] = self.formset_class(
            instance=self.context['queryset'],
        )
        if self.context['queryset']:
            for form in self.context['formset']:
                form.fields["companyitem"].queryset = CompanyItem.objects.filter(company=self.context['queryset'].company())
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

        formset = self.formset_class(request.POST,request.FILES,instance=obj)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    offerdata = form.save(commit=False)
                    if offerdata.companyitem:
                        offerdata.storageitem = offerdata.companyitem.storageitem
                    if not offerdata.create_user_id:
                        offerdata.create_user_id = user
                    offerdata.update_datetime = timezone.now()
                    offerdata.update_user_id = user
                    
                    if offerdata.amount != 0:
                        if offerdata.price:
                            companyitem = offerdata.companyitem
                            companyitem.price = offerdata.price
                            companyitem.update_datetime = timezone.now()
                            companyitem.update_user_id = user
                            companyitem.save()
                        else:
                            offerdata.price = offerdata.companyitem.price
                        offerdata.save()
        self.context['formset'] = formset

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:offer_update', offer=obj.slug if obj else offerdata.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('offer'):
            queryset = Offer.objects.get(slug=self.kwargs.get('offer'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class OfferCreateView(OfferCreateUpdateDetailView):
    permission_required = ('storagemanagement.add_offer',)
#--------------------------------------------------------------------------------
class OfferDetailView(OfferCreateUpdateDetailView):
    permission_required = ('storagemanagement.detail_offer',)
#--------------------------------------------------------------------------------
class OfferUpdateView(OfferCreateUpdateDetailView):
    permission_required = ('storagemanagement.change_offer',)
#--------------------------------------------------------------------------------
class OfferDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.delete_offer'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('offer'):
            get_object_or_404(Offer,slug = self.kwargs.get('offer')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferAuthorizeTrueView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.authorize_true_offer'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('offer'):
            offer = Offer.objects.get(slug=self.kwargs.get('offer'))
            if offer.done == False:
                offerdatas = offer.offerdata()
                for offerdata in offerdatas:
                    offerdata.authorized = True
                    offerdata.authorized_datetime = timezone.now()
                    offerdata.authorized_user_id = user
                    offerdata.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferAuthorizeFalseView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.authorize_false_offer'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('offer'):
            offer = Offer.objects.get(slug=self.kwargs.get('offer'))
            if offer.done == False:
                offerdatas = offer.offerdata()
                for offerdata in offerdatas:
                    offerdata.authorized = False
                    offerdata.authorized_datetime = timezone.now()
                    offerdata.authorized_user_id = user
                    offerdata.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferRecivedView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.recived_offer'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('offer'):
            offer = Offer.objects.get(slug=self.kwargs.get('offer'))
            if offer.sent and offer.offer_file:
                offer.recived = True
                offer.recived_datetime = timezone.now()
                offer.recived_user_id = user
                offer.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferSentView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.sent_offer'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('offer'):
            offer = Offer.objects.get(slug=self.kwargs.get('offer'))
            if offer.authorized():
                offer.sent = True
                offer.sent_datetime = timezone.now()
                offer.sent_user_id = user
                offer.save()
        
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferOrderTrueView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.order_true_offer'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('offer'):
            offer = Offer.objects.get(slug=self.kwargs.get('offer'))
            if offer.recived:
                offer.ordered = True
                offer.ordered_datetime = timezone.now()
                offer.ordered_user_id = user
                offer.done = True
                offer.save()
                if offer.done == True:
                    order = Order(
                        create_user_id=user,
                        update_user_id=user
                    )
                    order.save()
                    for obj in offer.offerdata():
                        orderdata = OrderData(
                            amount=obj.amount,
                            companyitem=obj.companyitem,
                            create_user_id=user,
                            offer=offer,
                            order=order,
                            price=obj.price,
                            update_user_id=user,
                        )
                        orderdata.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferOrderFalseView(PermissionRequiredMixin,MainView):

    permission_required = 'storagemanagement.order_false_offer'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('offer'):
            offer = Offer.objects.get(slug=self.kwargs.get('offer'))
            if offer.authorized:
                offer.ordered = False
                offer.ordered_datetime = timezone.now()
                offer.ordered_user_id = user
                offer.done = True
                offer.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------