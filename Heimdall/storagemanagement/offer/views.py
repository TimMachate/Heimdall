"""
#--------------------------------------------------------------------------------
# View File from Model Offer
# 15.10.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
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
from storagemanagement.supplieritem.models import SupplierItem
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
class OfferBaseView(PermissionRequiredMixin,MainView):
    """
    OfferDataBaseView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_
    """

    form_setting = None
    model_setting = None

    def get(self, request, *args, **kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.get_context_data()
        return render(request, self.template_name, self.context)

    def post(self,request, *args, **kwargs):
        """
        post

        Args:
            request (_type_): _description_
        """
        form = self.form_setting(
            request.POST,
            request.FILES,
            instance=self.context["form_setting_queryset"]
        )
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj = form.save()
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            obj.save()
        self.context['form'] = form
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    def get_initial(self, *args, **kwargs):
        """
        get_initial

        Returns:
            dict: contains all initial values
        """
        result = {}
        return result

    def get_context_data(self, *args, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains all context data
        """
        super().get_context_data(**kwargs)
        self.context['model'] = 'offer'
        # Urls
        self.context['url_overview'] = reverse('storagemanagement:offer_overview')
        self.context['url_list'] = reverse('storagemanagement:offer_list')
        self.context['url_table'] = reverse('storagemanagement:offer_table')
        self.context['url_create'] = reverse('storagemanagement:offer_create')
        # Setting
        if self.model_setting and self.form_setting:
            self.context["form_setting_queryset"] = self.model_setting.objects.get_or_create(
                user=self.request.user
            )[0]
            # Data Url
            self.context["api_data_url"] = self.get_url_api(
                queryset=self.context["form_setting_queryset"]
            )
            # Form
            self.context["form_setting"] = self.form_setting(
                instance = self.context["form_setting_queryset"]
            )
        else:
            self.context["form_setting_queryset"] = None
            self.context["api_data_url"] = None
            self.context["form_setting"] = None
        # Queryset
        self.context["queryset"]= self.get_queryset()
        return self.context

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset

        Returns:
            queryset: contains the offer object
        """
        if self.kwargs.get('offer'):
            queryset = Offer.objects.get(slug=self.kwargs.get('offer'))
        else:
            queryset = Offer.objects.all()
        return queryset

    def get_url_api(self,queryset):
        """
        get_url_api

        Returns:
            string: url to api
        """
        url = reverse(
            queryset.api
        )+f"?values={queryset.fields()}"
        return url
#--------------------------------------------------------------------------------
class OfferView(OfferBaseView):
    """
    OfferView

    Args:
        OfferBaseView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.view_offer'

    template_name = 'storagemanagement_offer_overview.html'

    form_setting = None
    model_setting = None
#--------------------------------------------------------------------------------
class OfferListView(OfferBaseView):
    """
    OfferListView

    Args:
        OfferBaseView (_type_): _description_
    """

    permission_required = 'storagemanagement.list_offer'

    template_name = 'storagemanagement_offer_list.html'

    form_setting = None
    model_setting = None
#--------------------------------------------------------------------------------
class OfferTableView(OfferBaseView):
    """
    OfferTableView

    Args:
        OfferBaseView (_type_): _description_
    """

    permission_required = 'storagemanagement.table_offer'

    template_name = 'storagemanagement_offer_table.html'

    form_setting = None
    model_setting = None
#--------------------------------------------------------------------------------
class OfferCreateUpdateDetailView(OfferBaseView):
    """
    OfferCreateUpdateDetailView

    Args:
        OfferView (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name = 'storagemanagement_offer_createupdatedetail.html'

    form_class = OfferForm
    formset_class = OfferDataFormset

    form_setting = None
    model_setting = None

    def get(self, request, *args, **kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'])
        self.context['formset'] = self.formset_class(
            instance=self.context['queryset'],
        )
        if self.context['queryset']:
            for form in self.context['formset']:
                form.fields["supplieritem"].queryset = SupplierItem.objects.filter(
                    company=self.context['queryset'].get_supplier_object()
                )
        return render(request, self.template_name, self.context)

    def post(self,request, *args, **kwargs):
        """
        post

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
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
                    if offerdata.supplieritem:
                        offerdata.storageitem = offerdata.supplieritem.storageitem
                    if not offerdata.create_user_id:
                        offerdata.create_user_id = user
                    offerdata.update_datetime = timezone.now()
                    offerdata.update_user_id = user

                    if offerdata.amount != 0:
                        if offerdata.price:
                            supplieritem = offerdata.supplieritem
                            supplieritem.price = offerdata.price
                            supplieritem.update_datetime = timezone.now()
                            supplieritem.update_user_id = user
                            supplieritem.save()
                        else:
                            offerdata.price = offerdata.supplieritem.price
                        offerdata.save()
        self.context['formset'] = formset

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect(
                'storagemanagement:offer_update',
                offer=obj.slug if obj else offerdata.slug
            )

    def get_queryset(self):
        """
        get_queryset

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('offer'):
            queryset = Offer.objects.get(slug=self.kwargs.get('offer'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class OfferCreateView(OfferCreateUpdateDetailView):
    """
    OfferCreateView

    Args:
        OfferCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.add_offer',)
#--------------------------------------------------------------------------------
class OfferDetailView(OfferCreateUpdateDetailView):
    """
    OfferDetailView

    Args:
        OfferCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.detail_offer',)
#--------------------------------------------------------------------------------
class OfferUpdateView(OfferCreateUpdateDetailView):
    """
    OfferUpdateView

    Args:
        OfferCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.change_offer',)
#--------------------------------------------------------------------------------
class OfferDeleteView(PermissionRequiredMixin,MainView):
    """
    OfferDeleteView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.delete_offer'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('offer'):
            get_object_or_404(Offer,slug = self.kwargs.get('offer')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferAuthorizeTrueView(PermissionRequiredMixin,MainView):
    """
    OfferAuthorizeTrueView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.authorize_true_offer'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('offer'):
            offer = Offer.objects.get(slug=self.kwargs.get('offer'))
            if offer.done is False:
                objs = offer.offerdata()
                for obj in objs:
                    obj.authorized = True
                    obj.authorized_datetime = timezone.now()
                    obj.authorized_user_id = user
                    obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferAuthorizeFalseView(PermissionRequiredMixin,MainView):
    """
    OfferAuthorizeFalseView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.authorize_false_offer'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('offer'):
            offer = Offer.objects.get(slug=self.kwargs.get('offer'))
            if offer.done is False:
                objs = offer.offerdata()
                for obj in objs:
                    obj.authorized = False
                    obj.authorized_datetime = timezone.now()
                    obj.authorized_user_id = user
                    obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferRecivedView(PermissionRequiredMixin,MainView):
    """
    OfferRecivedView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.recived_offer'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('offer'):
            obj = Offer.objects.get(slug=self.kwargs.get('offer'))
            if obj.sent and obj.offer_file:
                obj.recived = True
                obj.recived_datetime = timezone.now()
                obj.recived_user_id = user
                obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferSentView(PermissionRequiredMixin,MainView):
    """
    OfferSentView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.sent_offer'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('offer'):
            obj = Offer.objects.get(slug=self.kwargs.get('offer'))
            if obj.authorized():
                obj.sent = True
                obj.sent_datetime = timezone.now()
                obj.sent_user_id = user
                obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferOrderTrueView(PermissionRequiredMixin,MainView):
    """
    OfferOrderTrueView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.order_true_offer'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('offer'):
            obj = Offer.objects.get(slug=self.kwargs.get('offer'))
            if obj.recived:
                obj.ordered = True
                obj.ordered_datetime = timezone.now()
                obj.ordered_user_id = user
                obj.done = True
                obj.save()
                if obj.done is True:
                    order = Order(
                        create_user_id=user,
                        update_user_id=user
                    )
                    order.save()
                    for item in obj.offerdata():
                        orderdata = OrderData(
                            amount=item.amount,
                            supplieritem=item.supplieritem,
                            create_user_id=user,
                            offer=obj,
                            order=order,
                            price=item.price,
                            update_user_id=user,
                        )
                        orderdata.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferOrderFalseView(PermissionRequiredMixin,MainView):
    """
    OfferOrderFalseView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.order_false_offer'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('offer'):
            obj = Offer.objects.get(slug=self.kwargs.get('offer'))
            if obj.authorized:
                obj.ordered = False
                obj.ordered_datetime = timezone.now()
                obj.ordered_user_id = user
                obj.done = True
                obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
