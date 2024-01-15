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
    StorageManagementRequestDataOverviewUserSetting,
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
    StorageManagementRequestDataOverviewUserSettingForm,
    StorageManagementRequestDataListUserSettingForm,
    StorageManagementRequestDataTableUserSettingForm
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class RequestDataBaseView(PermissionRequiredMixin,MainView):
    """
    RequestDataBaseView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
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
        if self.kwargs.get('supplieritem'):
            result['supplieritem'] = SupplierItem.objects.get(slug=self.kwargs.get('supplieritem'))
        if self.kwargs.get('storageitem'):
            result['storageitem'] = StorageItem.objects.get(slug=self.kwargs.get('storageitem'))
            if result['storageitem'].supplieritem:
                result['supplieritem'] = result['storageitem'].supplieritem
            else:
                result['supplieritem'] = result['storageitem'].supplieritem_data.all().order_by("price").first()
        if self.kwargs.get('amount'):
            result['amount'] = self.kwargs.get('amount')
        if not result:
            result = None
        return result

    def get_context_data(self, *args, **kwargs):
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
            queryset: contains the requestdata object
        """
        if self.kwargs.get('requestdata'):
            queryset = RequestData.objects.get(slug=self.kwargs.get('requestdata'))
        else:
            queryset = RequestData.objects.all()
        return queryset

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
class RequestDataView(RequestDataBaseView):
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

    form_setting = StorageManagementRequestDataOverviewUserSettingForm
    model_setting = StorageManagementRequestDataOverviewUserSetting

    def get(self, request, *kwargs, **args):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.get_context_data()
        self.context["api_data_url"] += "&done=false"
        return render(request, self.template_name, self.context)
#--------------------------------------------------------------------------------
class RequestDataListView(RequestDataBaseView):
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
#--------------------------------------------------------------------------------
class RequestDataTableView(RequestDataBaseView):
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
#--------------------------------------------------------------------------------
class RequestDataCreateUpdateDetailView(RequestDataBaseView):
    """
    RequestDataCreateUpdateDetailView

    Args:
        RequestDataView (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name = 'storagemanagement_requestdata_createupdatedetail.html'

    form_class = RequestDataForm

    def get(self, request, *kwargs, **args):
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
        #if self.context['queryset']:
        #    self.context['form'].fields['supplieritem'].queryset = SupplierItem.objects.filter(
        #        storageitem=self.context['queryset'].storageitem
        #    )
        return render(request, self.template_name, self.context)

    def post(self,request, *kwargs, **args):
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
            if obj.storageitem != obj.supplieritem.get_storageitem_object():
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

    def get_queryset(self, *kwargs, **args):
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

    def get(self, request, *kwargs, **args):
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
                    supplieritem__company=obj.supplieritem.get_supplier_object()
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

    def get(self, request, *kwargs, **args):
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

    def get(self, request, *kwargs, **args):
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
                    supplieritem__company=obj.supplieritem.get_supplier_object()
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

    def get(self, request, *kwargs, **args):
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
