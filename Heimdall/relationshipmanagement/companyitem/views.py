"""
#--------------------------------------------------------------------------------
# Views File from Model CompanyItem
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
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.company.models import Company
from relationshipmanagement.companyitem.models import CompanyItem
from relationshipmanagement.relationshipmanagementusersetting.models import (
    RelationshipManagementCompanyItemListUserSetting,
    RelationshipManagementCompanyItemTableUserSetting
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from relationshipmanagement.companyitem.forms import CompanyItemForm
from relationshipmanagement.relationshipmanagementusersetting.forms import (
    RelationshipManagementCompanyItemListUserSettingForm,
    RelationshipManagementCompanyItemTableUserSettingForm
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class CompanyItemView(PermissionRequiredMixin, MainView):
    """
    CompanyItemView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'relationshipmanagement.view_companyitem'

    template_name = 'relationshipmanagement_companyitem_overview.html'

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset

        Returns:
            queryset: contains all company items
        """
        if self.kwargs.get('company'):
            queryset = CompanyItem.objects.filter(company__slug = self.kwargs.get('company'))
        else:
            queryset = CompanyItem.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains all context variables
        """
        super().get_context_data(**kwargs)
        self.context['model'] = 'companyitem'
        # Urls
        if self.kwargs.get('company'):
            self.context['url_overview'] = reverse(
                'relationshipmanagement:company_companyitem_overview',
                kwargs={'company':self.kwargs.get('company')}
            )
            self.context['url_list'] = reverse(
                'relationshipmanagement:company_companyitem_list',
                kwargs={'company':self.kwargs.get('company')}
            )
            self.context['url_table'] = reverse(
                'relationshipmanagement:company_companyitem_table',
                kwargs={'company':self.kwargs.get('company')}
            )
            self.context['url_create'] = reverse(
                'relationshipmanagement:company_companyitem_create',
                kwargs={'company':self.kwargs.get('company')}
            )
        else:
            self.context['url_overview'] = reverse('relationshipmanagement:companyitem_overview')
            self.context['url_list'] = reverse('relationshipmanagement:companyitem_list')
            self.context['url_table'] = reverse('relationshipmanagement:companyitem_table')
            self.context['url_create'] = reverse('relationshipmanagement:companyitem_create')
        # Data Url
        if self.kwargs.get('company'):
            self.context["company"] = self.kwargs.get('company')
        else:
            self.context["company"] = ""
        fields = (
            "id,",
            "name,",
            "reference_number,",
            "url_detail,",
            "company_name,",
            "company_reference_number,",
            "company_url_detail,",
            "storageitem_name,",
            "storageitem_reference_number,",
            "storageitem_url_detail,",
            "stock_count,",
            "stock_value,"
        )
        self.context["fields"] = "".join(fields)
        self.context["api_data_url"] = reverse(
            "relationshipmanagementAPI:companyitem_list"
        )+f"?values={self.context['fields']}&company__slug={self.context['company']}"
        return self.context
#--------------------------------------------------------------------------------
class CompanyItemListView(CompanyItemView):
    """
    CompanyItemListView

    Args:
        CompanyItemView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'relationshipmanagement.list_companyitem'

    template_name = 'relationshipmanagement_companyitem_list.html'

    form_setting = RelationshipManagementCompanyItemListUserSettingForm

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
            dict: contains all context variables
        """
        super().get_context_data(**kwargs)
        # Setting
        self.context["form_setting_queryset"] = RelationshipManagementCompanyItemListUserSetting.objects.get_or_create(
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
        if self.kwargs.get("company"):
            company = self.kwargs.get("company")
        else:
            company = ""
        url = reverse(queryset.api)+f"?values={queryset.fields()}&company__slug={company}"
        return url
#--------------------------------------------------------------------------------
class CompanyItemTableView(CompanyItemView):
    """
    CompanyItemTableView

    Args:
        CompanyItemView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'relationshipmanagement.table_companyitem'

    template_name = 'relationshipmanagement_companyitem_table.html'

    form_setting = RelationshipManagementCompanyItemTableUserSettingForm

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
        super().get_context_data(**kwargs)
        # Setting
        self.context["form_setting_queryset"] = RelationshipManagementCompanyItemTableUserSetting.objects.get_or_create(
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
        if self.kwargs.get("company"):
            company = self.kwargs.get("company")
        else:
            company = ""
        url = reverse(queryset.api)+f"?values={queryset.fields()}&company__slug={company}"
        return url
#--------------------------------------------------------------------------------
class CompanyItemCreateUpdateDetailView(CompanyItemView):
    """
    CompanyItemCreateUpdateDetailView

    Args:
        CompanyItemView (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name = 'relationshipmanagement_companyitem_createupdatedetail.html'

    form_class = CompanyItemForm

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
        if self.get_initial():
            self.context['form'].initial = self.get_initial()
        return render(request, self.template_name, self.context)

    def get_initial(self):
        """
        get_initial

        Returns:
            dict: contains all initial data
        """
        result = {}
        if self.kwargs.get('company'):
            result['company'] = Company.objects.get(slug=self.kwargs.get('company'))
        if not result:
            result = None
        return result

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
        if self.kwargs.get('company'):
            return redirect(
                'relationshipmanagement:company_companyitem_list',
                company=self.kwargs.get('company')
            )
        else:
            return redirect('relationshipmanagement:companyitem_update', companyitem=obj.slug)

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset

        Returns:
            queryset: contains the company item
        """
        if self.kwargs.get('companyitem'):
            queryset = CompanyItem.objects.get(slug=self.kwargs.get('companyitem'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class CompanyItemCreateView(CompanyItemCreateUpdateDetailView):
    """
    CompanyItemCreateView

    Args:
        CompanyItemCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('relationshipmanagement.add_companyitem',)
#--------------------------------------------------------------------------------
class CompanyItemDetailView(CompanyItemCreateUpdateDetailView):
    """
    CompanyItemDetailView

    Args:
        CompanyItemCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('relationshipmanagement.detail_companyitem',)
#--------------------------------------------------------------------------------
class CompanyItemUpdateView(CompanyItemCreateUpdateDetailView):
    """
    CompanyItemUpdateView

    Args:
        CompanyItemCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('relationshipmanagement.update_companyitem',)
#--------------------------------------------------------------------------------
class CompanyItemDeleteView(PermissionRequiredMixin, MainView):
    """
    CompanyItemDeleteView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'relationshipmanagement.delete_companyitem'

    def get(self, request, *args, **kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('companyitem'):
            get_object_or_404(CompanyItem, slug = self.kwargs.get('companyitem')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('relationshipmanagement:companyitem_list')
#--------------------------------------------------------------------------------
