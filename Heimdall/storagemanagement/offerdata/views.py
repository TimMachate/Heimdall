"""
#--------------------------------------------------------------------------------
# View File from Model Offer Data
# 11.11.2023
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
from storagemanagement.offer.models import Offer
from storagemanagement.offerdata.models import OfferData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.offerdata.forms import OfferDataForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class OfferDataBaseView(PermissionRequiredMixin,MainView):
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
        self.context['model'] = 'offerdata'
        # Urls
        self.context['url_overview'] = reverse('storagemanagement:offerdata_overview')
        self.context['url_list'] = reverse('storagemanagement:offerdata_list')
        self.context['url_table'] = reverse('storagemanagement:offerdata_table')
        self.context['url_create'] = reverse('storagemanagement:offerdata_create')
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
            queryset: contains the offerdata object
        """
        if self.kwargs.get('offerdata'):
            queryset = OfferData.objects.get(slug=self.kwargs.get('offerdata'))
        else:
            queryset = OfferData.objects.all()
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
class OfferDataView(OfferDataBaseView):
    """
    OfferDataView

    Args:
        OfferDataBaseView (class): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.view_offerdata'

    template_name = 'storagemanagement_offerdata_overview.html'

    form_setting = None
    model_setting = None
#--------------------------------------------------------------------------------
class OfferDataListView(OfferDataBaseView):
    """
    OfferDataListView

    Args:
        OfferDataBaseView (_type_): _description_
    """

    permission_required = 'storagemanagement.list_offerdata'

    template_name = 'storagemanagement_offerdata_list.html'

    form_setting = None
    model_setting = None
#--------------------------------------------------------------------------------
class OfferDataTableView(OfferDataBaseView):
    """
    OfferDataTableView

    Args:
        OfferDataBaseView (_type_): _description_
    """

    permission_required = 'storagemanagement.table_offerdata'

    template_name = 'storagemanagement_offerdata_table.html'

    form_setting = None
    model_setting = None
#--------------------------------------------------------------------------------
class OfferDataCreateUpdateDetailView(OfferDataBaseView):
    """
    OfferDataCreateUpdateDetailView

    Args:
        OfferDataView (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name = 'storagemanagement_offerdata_createupdatedetail.html'

    form_class = OfferDataForm

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

            if obj.price:
                companyitem = obj.companyitem
                companyitem.price = obj.price
                companyitem.update_datetime = timezone.now()
                companyitem.update_user_id = user
                companyitem.save()
            else:
                obj.price = obj.companyitem.price

            if not obj.offer:
                offers = OfferData.objects.filter(
                    companyitem__company = obj.companyitem.company
                ).exclude(offer__sent = True)
                if offers.exists():
                    offer = offers.first()
                    offerdatas = offer.offer.offerdata().filter(companyitem=obj.companyitem)
                    if offerdatas.exists():
                        offerdata = offerdatas.first()
                        offerdata.amount += obj.amount
                        obj = offerdata
                    else:
                        obj.offer = offer.offer

                else:
                    offer = Offer(
                        create_user_id=user,
                        update_user_id=user
                    )
                    offer.save()
                    obj.offer = offer

            obj.save()
        self.context['form'] = form

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect(
                'storagemanagement:offerdata_update',
                offerdata=obj.slug if obj else offerdata.slug
            )

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('offerdata'):
            queryset = OfferData.objects.get(slug=self.kwargs.get('offerdata'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class OfferDataCreateView(OfferDataCreateUpdateDetailView):
    """
    OfferDataCreateView

    Args:
        OfferDataCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.add_offerdata',)
#--------------------------------------------------------------------------------
class OfferDataDetailView(OfferDataCreateUpdateDetailView):
    """
    OfferDataDetailView

    Args:
        OfferDataCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.detail_offerdata',)
#--------------------------------------------------------------------------------
class OfferDataUpdateView(OfferDataCreateUpdateDetailView):
    """
    OfferDataUpdateView

    Args:
        OfferDataCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.change_offerdata',)
#--------------------------------------------------------------------------------
class OfferDataDeleteView(PermissionRequiredMixin,MainView):
    """
    OfferDataDeleteView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.delete_offerdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('offerdata'):
            get_object_or_404(OfferData,slug = self.kwargs.get('offerdata')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferDataAuthorizedTrueView(PermissionRequiredMixin,MainView):
    """
    OfferDataAuthorizedTrueView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.authorize_true_offerdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('offerdata'):
            obj = OfferData.objects.get(slug=self.kwargs.get('offerdata'))
            obj.authorized = True
            obj.authorized_datetime = timezone.now()
            obj.authorized_user_id = user
            obj.done = True
            obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferDataAuthorizedFalseView(PermissionRequiredMixin,MainView):
    """
    OfferDataAuthorizedFalseView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.authorize_false_offerdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        if self.kwargs.get('offerdata'):
            obj = OfferData.objects.get(slug=self.kwargs.get('offerdata'))
            obj.authorized = False
            obj.authorized_datetime = timezone.now()
            obj.authorized_user_id = user
            obj.done = True
            obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferDataAuthorizedTrueAllView(PermissionRequiredMixin,MainView):
    """
    OfferDataAuthorizedTrueAllView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.authorize_true_offerdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        for obj in OfferData.objects.filter(authorized=None):
            obj.authorized = True
            obj.authorized_datetime = timezone.now()
            obj.authorized_user_id = user
            obj.done = True
            obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class OfferDataAuthorizedFalseAllView(PermissionRequiredMixin,MainView):
    """
    OfferDataAuthorizedFalseAllView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.authorize_false_offerdata'

    def get(self, request):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = get_user_model().objects.get(id=request.user.id)
        for obj in OfferData.objects.filter(authorized=None):
            obj.authorized = False
            obj.authorized_datetime = timezone.now()
            obj.authorized_user_id = user
            obj.done = True
            obj.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
