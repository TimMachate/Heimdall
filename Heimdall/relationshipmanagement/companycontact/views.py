"""
#--------------------------------------------------------------------------------
# Views File from Model CompanyContact
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
from relationshipmanagement.companycontact.models import CompanyContact
from relationshipmanagement.relationshipmanagementusersetting.models import (
    RelationshipManagementCompanyContactListUserSetting,
    RelationshipManagementCompanyContactTableUserSetting
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from relationshipmanagement.companycontact.forms import (
    CompanyContactForm,
    CompanyContactEmailFormset,
    CompanyContactTelephoneFormset
)
from relationshipmanagement.relationshipmanagementusersetting.forms import (
    RelationshipManagementCompanyContactListUserSettingForm,
    RelationshipManagementCompanyContactTableUserSettingForm
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class CompanyContactView(PermissionRequiredMixin, MainView):
    """
    CompanyContactView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'relationshipmanagement.view_companycontact'

    template_name = 'relationshipmanagement_companycontact_overview.html'

    def get_queryset(self,):
        """
        get_queryset
        get all contacts from company

        Returns:
            queryset: contains all contacts
        """
        if self.kwargs.get('company'):
            queryset = CompanyContact.objects.filter(company__slug = self.kwargs.get('company'))
        else:
            queryset = CompanyContact.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains all context variables
        """
        super().get_context_data(**kwargs)
        self.context['model'] = 'companycontact'
        # Urls
        if self.kwargs.get('company'):
            self.context['url_overview'] = reverse(
                'relationshipmanagement:company_companycontact_overview',
                kwargs={'company':self.kwargs.get('company')}
            )
            self.context['url_list'] = reverse(
                'relationshipmanagement:company_companycontact_list',
                kwargs={'company':self.kwargs.get('company')}
            )
            self.context['url_table'] = reverse(
                'relationshipmanagement:company_companycontact_table',
                kwargs={'company':self.kwargs.get('company')}
            )
            self.context['url_create'] = reverse(
                'relationshipmanagement:company_companycontact_create',
                kwargs={'company':self.kwargs.get('company')}
            )
        else:
            self.context['url_overview'] = reverse('relationshipmanagement:companycontact_overview')
            self.context['url_list'] = reverse('relationshipmanagement:companycontact_list')
            self.context['url_table'] = reverse('relationshipmanagement:companycontact_table')
            self.context['url_create'] = reverse('relationshipmanagement:companycontact_create')
        # Data Url
        if self.kwargs.get('company'):
            self.context["company"] = self.kwargs.get('company')
        else:
            self.context["company"] = ""
        fields = (
            "id,",
            "reference_number,",
            "name,",
            "url_detail,",
            "company_name,",
            "company_url_detail,",
            "email_data,",
            "telephone_data,"
        )
        self.context["fields"] = "".join(fields)
        self.context["api_data_url"] = reverse(
            "relationshipmanagementAPI:companycontact_list"
        )+f"?values={self.context['fields']}&company__slug={self.context['company']}"
        return self.context
#--------------------------------------------------------------------------------
class CompanyContactListView(CompanyContactView):
    """
    CompanyContactListView

    Args:
        CompanyContactView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'relationshipmanagement.list_companycontact'

    template_name = 'relationshipmanagement_companycontact_list.html'

    form_setting = RelationshipManagementCompanyContactListUserSettingForm

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
        self.context["form_setting_queryset"] = RelationshipManagementCompanyContactListUserSetting.objects.get_or_create(
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
class CompanyContactTableView(CompanyContactView):
    """
    CompanyContactTableView

    Args:
        CompanyContactView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'relationshipmanagement.table_companycontact'

    template_name = 'relationshipmanagement_companycontact_table.html'

    form_setting = RelationshipManagementCompanyContactTableUserSettingForm

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
        self.context["form_setting_queryset"] = RelationshipManagementCompanyContactTableUserSetting.objects.get_or_create(
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
class CompanyContactCreateUpdateDetailView(CompanyContactView):
    """
    CompanyContactCreateUpdateDetailView

    Args:
        CompanyContactView (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name = 'relationshipmanagement_companycontact_createupdatedetail.html'

    form_class = CompanyContactForm
    formset_email = CompanyContactEmailFormset
    formset_telephone = CompanyContactTelephoneFormset

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
        self.context['form'] = self.form_class(instance=self.context['queryset'],)
        self.context['formset_email'] = self.formset_email(instance = self.context['queryset'])
        self.context['formset_telephone'] = self.formset_telephone(
            instance = self.context['queryset']
        )
        if self.get_initial():
            self.context['form'].initial = self.get_initial()
        return render(request, self.template_name, self.context)

    def get_initial(self):
        """
        get_initial

        Returns:
            dict: initial data for forms
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

        formset_email = self.formset_email(request.POST,request.FILES,instance=obj)
        if formset_email.is_valid():
            for form in formset_email:
                if form.is_valid():
                    email = form.save(commit=False)
                    email.companycontact = obj
                    if email.email:
                        email.save()
        self.context['formset_email'] = formset_email

        formset_telephone = self.formset_telephone(request.POST,request.FILES,instance=obj)
        if formset_telephone.is_valid():
            for form in formset_telephone:
                if form.is_valid():
                    telephone = form.save(commit=False)
                    telephone.companycontact = obj
                    if telephone.number:
                        telephone.save()
        self.context['formset_telephone'] = formset_telephone

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('relationshipmanagement:companycontact_update', companycontact=obj.slug)

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset

        Returns:
            queryset: contains one contact of a company
        """
        if self.kwargs.get('companycontact'):
            queryset = CompanyContact.objects.get(slug=self.kwargs.get('companycontact'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class CompanyContactCreateView(CompanyContactCreateUpdateDetailView):
    """
    CompanyContactCreateView

    Args:
        CompanyContactCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('relationshipmanagement.add_companycontact',)
#--------------------------------------------------------------------------------
class CompanyContactDetailView(CompanyContactCreateUpdateDetailView):
    """
    CompanyContactDetailView

    Args:
        CompanyContactCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('relationshipmanagement.detail_companycontact',)
#--------------------------------------------------------------------------------
class CompanyContactUpdateView(CompanyContactCreateUpdateDetailView):
    """
    CompanyContactUpdateView

    Args:
        CompanyContactCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('relationshipmanagement.update_companycontact',)
#--------------------------------------------------------------------------------
class CompanyContactDeleteView(PermissionRequiredMixin, MainView):
    """
    CompanyContactDeleteView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'relationshipmanagement.delete_companycontact'

    def get(self, request, *args, **kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('companycontact'):
            get_object_or_404(CompanyContact, slug = self.kwargs.get('companycontact')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('relationshipmanagement:companycontact_list')
#--------------------------------------------------------------------------------
