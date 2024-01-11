"""
#--------------------------------------------------------------------------------
# Views File from Model SupplierContact
# 27.10.2023
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
from storagemanagement.supplier.models import Supplier
from storagemanagement.suppliercontact.models import SupplierContact
from storagemanagement.storagemanagementusersetting.suppliercontact.models import (
    StorageManagementSupplierContactOverviewUserSetting,
    StorageManagementSupplierContactListUserSetting,
    StorageManagementSupplierContactTableUserSetting
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from storagemanagement.suppliercontact.forms import (
    SupplierContactForm,
    SupplierContactEmailFormset,
    SupplierContactTelephoneFormset
)
from storagemanagement.storagemanagementusersetting.suppliercontact.forms import (
    StorageManagementSupplierContactOverviewUserSettingForm,
    StorageManagementSupplierContactListUserSettingForm,
    StorageManagementSupplierContactTableUserSettingForm
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class SupplierContactBaseView(PermissionRequiredMixin, MainView):
    """
    SupplierContactBaseView

    Args:
        PermissionRequiredMixin (class): permission class
        MainView (class): main app class

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

    def get_initial(self):
        """
        get_initial

        Returns:
            dict: initial data for forms
        """
        result = {}
        if self.kwargs.get('supplier'):
            result['company'] = Supplier.objects.get(slug=self.kwargs.get('supplier'))
        if not result:
            result = None
        return result

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains all context variables
        """
        super().get_context_data(**kwargs)
        self.context['model'] = 'suppliercontact'
        # Urls
        if self.kwargs.get('supplier'):
            self.context['url_overview'] = reverse(
                'storagemanagement:supplier_suppliercontact_overview',
                kwargs={'supplier':self.kwargs.get('supplier')}
            )
            self.context['url_list'] = reverse(
                'storagemanagement:supplier_suppliercontact_list',
                kwargs={'supplier':self.kwargs.get('supplier')}
            )
            self.context['url_table'] = reverse(
                'storagemanagement:supplier_suppliercontact_table',
                kwargs={'supplier':self.kwargs.get('supplier')}
            )
            self.context['url_create'] = reverse(
                'storagemanagement:supplier_suppliercontact_create',
                kwargs={'supplier':self.kwargs.get('supplier')}
            )
        else:
            self.context['url_overview'] = reverse('storagemanagement:suppliercontact_overview')
            self.context['url_list'] = reverse('storagemanagement:suppliercontact_list')
            self.context['url_table'] = reverse('storagemanagement:suppliercontact_table')
            self.context['url_create'] = reverse('storagemanagement:suppliercontact_create')
        # Setting
        if self.model_setting and self.form_setting:
            self.context["form_setting_queryset"] = self.model_setting.objects.get_or_create(
                user=self.request.user
            )[0]
            if self.kwargs.get('supplier'):
                self.context["supplier"] = self.kwargs.get('supplier')
            else:
                self.context["supplier"] = ""
            # Data Url
            self.context["api_data_url"] = self.get_url_api(
                queryset=self.context["form_setting_queryset"],
                supplier=self.context["supplier"]
            )
            # Form
            self.context["form_setting"] = self.form_setting(
                instance = self.context["form_setting_queryset"]
            )
        else:
            self.context["supplier"] = None
            self.context["form_setting_queryset"] = None
            self.context["form_setting"] = None
            self.context["api_data_url"] = None

        # Queryset
        self.context["queryset"]= self.get_queryset()
        return self.context

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset
        get all contacts from supplier

        Returns:
            queryset: contains all contacts
        """
        if self.kwargs.get('suppliercontact'):
            queryset = SupplierContact.objects.get(slug=self.kwargs.get('suppliercontact'))
        elif self.kwargs.get('supplier'):
            queryset = SupplierContact.objects.filter(company__slug = self.kwargs.get('supplier'))
        else:
            queryset = SupplierContact.objects.all()
        return queryset

    def get_url_api(self,queryset,supplier):
        """
        get_url_api

        Returns:
            string: url to api
        """
        url = queryset.api_url()+f"&company__slug={supplier}"
        return url
#--------------------------------------------------------------------------------
class SupplierContactView(SupplierContactBaseView):
    """
    SupplierContactView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.view_suppliercontact'

    template_name = 'storagemanagement_suppliercontact_overview.html'

    form_setting = StorageManagementSupplierContactOverviewUserSettingForm
    model_setting = StorageManagementSupplierContactOverviewUserSetting
#--------------------------------------------------------------------------------
class SupplierContactListView(SupplierContactBaseView):
    """
    SupplierContactListView

    Args:
        SupplierContactView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.list_suppliercontact'

    template_name = 'storagemanagement_suppliercontact_list.html'

    form_setting = StorageManagementSupplierContactListUserSettingForm
    model_setting = StorageManagementSupplierContactListUserSetting
#--------------------------------------------------------------------------------
class SupplierContactTableView(SupplierContactBaseView):
    """
    SupplierContactTableView

    Args:
        SupplierContactView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.table_suppliercontact'

    template_name = 'storagemanagement_suppliercontact_table.html'

    form_setting = StorageManagementSupplierContactTableUserSettingForm
    model_setting = StorageManagementSupplierContactTableUserSetting
#--------------------------------------------------------------------------------
class SupplierContactCreateUpdateDetailView(SupplierContactBaseView):
    """
    SupplierContactCreateUpdateDetailView

    Args:
        SupplierContactView (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name = 'storagemanagement_suppliercontact_createupdatedetail.html'

    form_class = SupplierContactForm
    formset_email = SupplierContactEmailFormset
    formset_telephone = SupplierContactTelephoneFormset

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
        self.context['form'] = self.form_class(
            instance=self.context['queryset']
        )
        self.context['formset_email'] = self.formset_email(instance = self.context['queryset'])
        self.context['formset_telephone'] = self.formset_telephone(
            instance = self.context['queryset']
        )
        if self.get_initial():
            self.context['form'].initial = self.get_initial()
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

        formset_email = self.formset_email(request.POST,request.FILES,instance=obj)
        if formset_email.is_valid():
            for form in formset_email:
                if form.is_valid():
                    email = form.save(commit=False)
                    email.suppliercontact = obj
                    if email.email:
                        email.save()
        self.context['formset_email'] = formset_email

        formset_telephone = self.formset_telephone(request.POST,request.FILES,instance=obj)
        if formset_telephone.is_valid():
            for form in formset_telephone:
                if form.is_valid():
                    telephone = form.save(commit=False)
                    telephone.suppliercontact = obj
                    if telephone.number:
                        telephone.save()
        self.context['formset_telephone'] = formset_telephone

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:suppliercontact_update', suppliercontact=obj.slug)

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset
        get all contacts from supplier

        Returns:
            queryset: contains all contacts
        """
        if self.kwargs.get('suppliercontact'):
            queryset = SupplierContact.objects.get(slug=self.kwargs.get('suppliercontact'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class SupplierContactCreateView(SupplierContactCreateUpdateDetailView):
    """
    SupplierContactCreateView

    Args:
        SupplierContactCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.add_suppliercontact',)
#--------------------------------------------------------------------------------
class SupplierContactDetailView(SupplierContactCreateUpdateDetailView):
    """
    SupplierContactDetailView

    Args:
        SupplierContactCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.detail_suppliercontact',)
#--------------------------------------------------------------------------------
class SupplierContactUpdateView(SupplierContactCreateUpdateDetailView):
    """
    SupplierContactUpdateView

    Args:
        SupplierContactCreateUpdateDetailView (_type_): _description_
    """
    permission_required = ('storagemanagement.update_suppliercontact',)
#--------------------------------------------------------------------------------
class SupplierContactDeleteView(PermissionRequiredMixin, MainView):
    """
    SupplierContactDeleteView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'storagemanagement.delete_suppliercontact'

    def get(self, request, *args, **kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('suppliercontact'):
            get_object_or_404(SupplierContact, slug = self.kwargs.get('suppliercontact')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('storagemanagement:suppliercontact_list')
#--------------------------------------------------------------------------------
