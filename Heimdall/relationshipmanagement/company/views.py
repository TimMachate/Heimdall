"""
#--------------------------------------------------------------------------------
# View File from Model Company
# 16.12.2023
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
from relationshipmanagement.company.models import Company
from relationshipmanagement.relationshipmanagementusersetting.models import (
    RelationshipManagementCompanyListUserSetting,
    RelationshipManagementCompanyTableUserSetting
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from relationshipmanagement.company.forms import CompanyForm
from relationshipmanagement.relationshipmanagementusersetting.forms import (
    RelationshipManagementCompanyListUserSettingForm,
    RelationshipManagementCompanyTableUserSettingForm
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class CompanyView(PermissionRequiredMixin,MainView):
    """
    CompanyView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'relationshipmanagement.view_company'

    template_name = 'relationshipmanagement_company_overview.html'

    def get_queryset(self):
        """
        get_queryset

        Returns:
            queryset: contains all companys
        """
        queryset = Company.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains all context data
        """
        super().get_context_data(**kwargs)
        self.context['model'] = 'company'
        # Data Url
        fields = (
            "id,",
            "name,",
            "url_detail,",
            "telephone,",
            "email,",
            "companycontact_count,",
            "companyitem_count,"
        )
        self.context["fields"] = "".join(fields)
        self.context["api_data_url"] = reverse(
            "relationshipmanagementAPI:company_list"
        )+f"?values={self.context['fields']}"
        return self.context
#--------------------------------------------------------------------------------
class CompanyListView(CompanyView):
    """
    CompanyListView

    Args:
        CompanyView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'relationshipmanagement.list_company'

    template_name = 'relationshipmanagement_company_list.html'

    form_setting = RelationshipManagementCompanyListUserSettingForm

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

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains all context data
        """
        super().get_context_data(**kwargs)
        # Setting
        self.context["form_setting_queryset"] = RelationshipManagementCompanyListUserSetting.objects.get_or_create(
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
        url = reverse(queryset.api)+f"?values={queryset.fields()}"
        return url
#--------------------------------------------------------------------------------
class CompanyTableView(CompanyView):
    """
    CompanyTableView

    Args:
        CompanyView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'relationshipmanagement.table_company'

    template_name = 'relationshipmanagement_company_table.html'

    form_setting = RelationshipManagementCompanyTableUserSettingForm

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

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains all context data
        """
        super().get_context_data(**kwargs)
        # Setting
        self.context["form_setting_queryset"] = RelationshipManagementCompanyTableUserSetting.objects.get_or_create(
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
        url = reverse(queryset.api)+f"?values={queryset.fields()}"
        return url
#--------------------------------------------------------------------------------
class CompanyCreateUpdateDetailView(CompanyView):
    """
    CompanyCreateUpdateDetailView

    Args:
        CompanyView (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name = 'relationshipmanagement_company_createupdatedetail.html'

    form_class = CompanyForm

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
            obj = form.save()
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            obj.save()
        self.context['form'] = form

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    def get_queryset(self):
        """
        get_queryset

        Returns:
            queryset: contains one company
        """
        if self.kwargs.get('company'):
            queryset = Company.objects.get(slug=self.kwargs.get('company'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class CompanyCreateView(CompanyCreateUpdateDetailView):
    """
    CompanyCreateView

    Args:
        CompanyCreateUpdateDetailView (_type_): _description_
    """

    permission_required = ('relationshipmanagement.add_company',)
#--------------------------------------------------------------------------------
class CompanyDetailView(CompanyCreateUpdateDetailView):
    """
    CompanyDetailView

    Args:
        CompanyCreateUpdateDetailView (_type_): _description_
    """

    permission_required = ('relationshipmanagement.detail_company',)
#--------------------------------------------------------------------------------
class CompanyUpdateView(CompanyCreateUpdateDetailView):
    """
    CompanyUpdateView

    Args:
        CompanyCreateUpdateDetailView (_type_): _description_
    """

    permission_required = ('relationshipmanagement.change_company',)
#--------------------------------------------------------------------------------
class CompanyDeleteView(PermissionRequiredMixin,MainView):
    """
    CompanyDeleteView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'relationshipmanagement.delete_company'

    def get(self, request, *args, **kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('company'):
            get_object_or_404(Company,slug = self.kwargs.get('company')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
