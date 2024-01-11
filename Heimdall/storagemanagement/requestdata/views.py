"""
#--------------------------------------------------------------------------------
# View File from Model Request Data
# 05.01.2024
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
from storagemanagement.offerdata.models import OfferData
from storagemanagement.requestdata.models import RequestData
from storagemanagement.storagemanagementusersetting.requestdata.models import (
    StorageManagementRequestDataListUserSetting,
    StorageManagementRequestDataTableUserSetting
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.requestdata.forms import RequestDataForm
from storagemanagement.storageitem.models import StorageItem
from storagemanagement.storagemanagementusersetting.requestdata.forms import(
    StorageManagementRequestDataListUserSettingForm,
    StorageManagementRequestDataTableUserSettingForm
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class RequestDataView(PermissionRequiredMixin,MainView):
    """
    RequestDataView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.view_requestdata'

    template_name = 'storagemanagement_requestdata_overview.html'

    def get_queryset(self):
        """
        get_queryset

        Returns:
            _type_: _description_
        """
        queryset = RequestData.objects.filter(done=False)
        return queryset

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains all context data
        """
        super().get_context_data(**kwargs)
        self.context['model'] = 'requestdata'
        # Urls
        if self.kwargs.get('orderprocess'):
            self.context['url_overview'] = reverse(
                'storagemanagement:orderprocess_requestdata_overview',
                kwargs={'orderprocess':self.kwargs.get('orderprocess')}
            )
            self.context['url_list'] = reverse(
                'storagemanagement:orderprocess_requestdata_list',
                kwargs={'orderprocess':self.kwargs.get('orderprocess')}
            )
            self.context['url_table'] = reverse(
                'storagemanagement:orderprocess_requestdata_table',
                kwargs={'orderprocess':self.kwargs.get('orderprocess')}
            )
            self.context['url_create'] = reverse(
                'storagemanagement:orderprocess_requestdata_create',
                kwargs={'orderprocess':self.kwargs.get('orderprocess')}
            )
        else:
            self.context['url_overview'] = reverse('storagemanagement:requestdata_overview')
            self.context['url_list'] = reverse('storagemanagement:requestdata_list')
            self.context['url_table'] = reverse('storagemanagement:requestdata_table')
            self.context['url_create'] = reverse('storagemanagement:requestdata_create')
        # Data Url
        self.context["fields"] = ""
        self.context["api_data_url"] = reverse(
            "storagemanagementAPI:storage_list"
        )+"?values={}&done=flase".format(
            self.context["fields"],
        )
#--------------------------------------------------------------------------------
class RequestDataListView(RequestDataView):
    """
    RequestDataListView

    Args:
        RequestDataView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.list_requestdata'

    template_name = 'storagemanagement_requestdata_list.html'

    form_setting = StorageManagementRequestDataListUserSettingForm
    model_setting = StorageManagementRequestDataListUserSetting

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def post(self,request):
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

    def get_queryset(self):
        """
        get_queryset

        Returns:
            _type_: _description_
        """
        queryset = RequestData.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains context data
        """
        super().get_context_data(**kwargs)
        # Setting
        self.context["form_setting_queryset"] = self.model_setting.objects.get_or_create(
            user=self.request.user
        )[0]
        # Data Url
        self.context["api_data_url"] = self.get_url_api(
            queryset=self.context["form_setting_queryset"]
        )
        # Queryset
        self.context["queryset"]= self.get_queryset()
        # Form
        self.context["form_setting"] = self.form_setting(
            instance = self.context["form_setting_queryset"]
        )
        return self.context

    def get_url_api(self,queryset):
        """
        get_url_api

        Returns:
            string: url to api
        """
        url = reverse(
            queryset.api
        )+"?values={}".format(
            queryset.fields(),
        )
        return url
#--------------------------------------------------------------------------------
class RequestDataTableView(RequestDataView):
    """
    RequestDataTableView

    Args:
        RequestDataView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.table_requestdata'

    template_name = 'storagemanagement_requestdata_table.html'

    form_setting = StorageManagementRequestDataTableUserSettingForm
    model_setting = StorageManagementRequestDataTableUserSetting

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.get_context_data()
        return render(request, self.template_name, self.context)

    def get_queryset(self):
        """
        get_queryset

        Returns:
            _type_: _description_
        """
        queryset = RequestData.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains context data
        """
        super().get_context_data(**kwargs)
        # Setting
        self.context["form_setting_queryset"] = self.model_setting.objects.get_or_create(
            user=self.request.user
        )[0]
        # Data Url
        self.context["api_data_url"] = self.get_url_api(
            queryset=self.context["form_setting_queryset"]
        )
        # Queryset
        self.context["queryset"]= self.get_queryset()
        # Form
        self.context["form_setting"] = self.form_setting(
            instance = self.context["form_setting_queryset"]
        )
        return self.context

    def get_url_api(self,queryset):
        """
        get_url_api

        Returns:
            string: url to api
        """
        url = reverse(
            queryset.api
        )+"?values={}".format(
            queryset.fields(),
        )
        return url
#--------------------------------------------------------------------------------
class RequestDataCreateUpdateDetailView(RequestDataView):
    """
    RequestDataCreateUpdateDetailView

    Args:
        RequestDataView (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name = 'storagemanagement_requestdata_createupdatedetail.html'

    form_class = RequestDataForm

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(
            instance=self.context['queryset'],
            initial = self.get_initial()
        )
        if self.context['queryset']:
            self.context['form'].fields['supplieritem'].queryset = SupplierItem.objects.filter(
                storageitem=self.context['queryset'].storageitem
            )
        return render(request, self.template_name, self.context)

    def get_initial(self):
        """
        get_initial

        Returns:
            dict: contains initial data
        """
        result = {}
        if self.kwargs.get("storageitem"):
            result["storageitem"] = StorageItem.objects.get(slug=self.kwargs.get("storageitem"))
            result["amount"] = result["storageitem"].maximum - result["storageitem"].stock_count()
            supplieritem = result["storageitem"].supplieritem if result["storageitem"].supplieritem else None
            supplieritem = SupplierItem.objects.filter(
                storageitem=result["storageitem"]
            ).order_by('price').first() if not supplieritem else supplieritem
            result["supplieritem"] = supplieritem
        return result if not result else None

    def post(self,request):
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

            # supplieritem must have storageitem as Foreign Key
            if obj.storageitem and not obj.supplieritem:
                obj.supplieritem = obj.storageitem.supplieritem
            if obj.supplieritem and not obj.storageitem:
                obj.storageitem = obj.supplieritem.storageitem
            if obj.storageitem != obj.supplieritem.storageitem:
                obj.supplieritem = obj.storageitem.supplieritem

            if not self.context['queryset']:
                # Price
                obj.price = obj.supplieritem.price

            obj.save()

        self.context['form'] = form

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:requestdata_update', requestdata=obj.slug)

    def get_queryset(self):
        """
        get_queryset

        Returns:
            queryset: contains request data object
        """
        if self.kwargs.get('requestdata'):
            queryset = RequestData.objects.get(slug=self.kwargs.get('requestdata'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class RequestDataCreateView(RequestDataCreateUpdateDetailView):
    """
    RequestDataCreateView

    Args:
        RequestDataCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.add_requestdata',)
#--------------------------------------------------------------------------------
class RequestDataDetailView(RequestDataCreateUpdateDetailView):
    """
    RequestDataDetailView

    Args:
        RequestDataCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.detail_requestdata',)
#--------------------------------------------------------------------------------
class RequestDataUpdateView(RequestDataCreateUpdateDetailView):
    """
    RequestDataUpdateView

    Args:
        RequestDataCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.change_requestdata',)
#--------------------------------------------------------------------------------
class RequestDataDeleteView(PermissionRequiredMixin,MainView):
    """
    RequestDataDeleteView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.delete_requestdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('requestdata'):
            get_object_or_404(RequestData,slug = self.kwargs.get('requestdata')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class RequestDataAuthorizedTrueView(PermissionRequiredMixin,MainView):
    """
    RequestDataAuthorizedTrueView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.authorize_true_requestdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('requestdata'):
            obj = RequestData.objects.get(slug=self.kwargs.get('requestdata'))
            if obj.done is False:
                obj.authorized = True
                obj.authorized_datetime = timezone.now()
                obj.authorized_user_id = user
                obj.done = True
                offerdatas = OfferData.objects.filter(
                    supplieritem__supplier=obj.supplieritem.supplier
                ).exclude(offer__sent=True)
                if offerdatas.exists():
                    offerdata = offerdatas.filter(supplieritem=obj.supplieritem)
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
                            supplieritem = obj.supplieritem,
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
                        supplieritem = obj.supplieritem,
                        price = obj.price,
                        storageitem = obj.storageitem,
                    )
                    offerdata.save()

                obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class RequestDataAuthorizedFalseView(PermissionRequiredMixin,MainView):
    """
    RequestDataAuthorizedFalseView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.authorize_false_requestdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('requestdata'):
            obj = RequestData.objects.get(slug=self.kwargs.get('requestdata'))
            if obj.done is False:
                obj.authorized = False
                obj.authorized_datetime = timezone.now()
                obj.authorized_user_id = user
                obj.done = True
                obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class RequestDataAuthorizedTrueAllView(PermissionRequiredMixin,MainView):
    """
    RequestDataAuthorizedTrueAllView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.authorize_true_requestdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        for obj in RequestData.objects.filter(done=False):
            if obj.done is False:
                obj.authorized = True
                obj.authorized_datetime = timezone.now()
                obj.authorized_user_id = user
                obj.done = True
                offerdatas = OfferData.objects.filter(
                    supplieritem__supplier=obj.supplieritem.supplier
                ).exclude(sent=True)
                if offerdatas.exists():
                    offerdata = offerdatas.filter(supplieritem=obj.supplieritem)
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
                            supplieritem = obj.supplieritem,
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
                        supplieritem = obj.supplieritem,
                        price = obj.price,
                        storageitem = obj.storageitem,
                    )
                    offerdata.save()

                obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class RequestDataAuthorizedFalseAllView(PermissionRequiredMixin,MainView):
    """
    RequestDataAuthorizedFalseAllView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.authorize_false_requestdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        for obj in RequestData.objects.filter(done=False):
            obj.authorized = False
            obj.authorized_datetime = timezone.now()
            obj.authorized_user_id = user
            obj.done = True
            obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
