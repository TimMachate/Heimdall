"""
#--------------------------------------------------------------------------------
# View File from Model Company
# 17.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import reverse, render, redirect, get_object_or_404
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from programmmanagement.programm.models import Programm
from programmmanagement.programmmanagementusersetting.models import (
    ProgrammManagementProgrammListUserSetting,
    ProgrammManagementProgrammTableUserSetting,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from programmmanagement.programm.forms import ProgrammForm
from programmmanagement.programmmanagementusersetting.forms import (
    ProgrammManagementProgrammListUserSettingForm,
    ProgrammManagementProgrammTableUserSettingForm,
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class ProgrammView(PermissionRequiredMixin,MainView):
    """
    ProgrammView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'programmmanagement.view_programm'

    template_name = 'programmmanagement_programm_overview.html'

    def get_queryset(self):
        """
        get_queryset

        Returns:
            queryset: contains all programms
        """
        queryset = Programm.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        """
        get_context_data

        Returns:
            dict: contains all context data
        """
        super().get_context_data(**kwargs)
        self.context['model'] = 'programm'
        # Data Url
        fields = (
            "id,",
            "name,",
            "url_detail,",
            "description",
        )
        self.context["fields"] = "".join(fields)
        self.context["api_data_url"] = reverse(
            "programmmanagementAPI:programm_list"
        )+f"?values={self.context['fields']}"
        return self.context
#--------------------------------------------------------------------------------
class ProgrammListView(ProgrammView):
    """
    ProgrammListView

    Args:
        ProgrammView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'programmmanagement.list_programm'

    template_name = 'programmmanagement_programm_list.html'

    form_setting = ProgrammManagementProgrammListUserSettingForm

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
        self.context["form_setting_queryset"] = ProgrammManagementProgrammListUserSetting.objects.get_or_create(
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
class ProgrammTableView(ProgrammView):
    """
    ProgrammTableView

    Args:
        ProgrammView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'programmmanagement.table_programm'

    template_name = 'programmmanagement_programm_table.html'

    form_setting = ProgrammManagementProgrammTableUserSettingForm

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
        self.context["form_setting_queryset"] = ProgrammManagementProgrammTableUserSetting.objects.get_or_create(
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
class ProgrammCreateUpdateDetailView(ProgrammView):
    """
    ProgrammCreateUpdateDetailView

    Args:
        ProgrammView (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name = 'programmmanagement_programm_createupdatedetail.html'

    form_class = ProgrammForm

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
            return redirect('programmmanagement:programm_update',programm=obj.slug)

    def get_queryset(self):
        """
        get_queryset

        Returns:
            queryset: contains the programm object
        """
        if self.kwargs.get('programm'):
            queryset = Programm.objects.get(slug=self.kwargs.get('programm'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class ProgrammCreateView(ProgrammCreateUpdateDetailView):
    """
    ProgrammCreateView

    Args:
        ProgrammCreateUpdateDetailView (_type_): _description_
    """

    permission_required = ('programmmanagement.add_programm',)
#--------------------------------------------------------------------------------
class ProgrammDetailView(ProgrammCreateUpdateDetailView):
    """
    ProgrammDetailView

    Args:
        ProgrammCreateUpdateDetailView (_type_): _description_
    """

    permission_required = ('programmmanagement.detail_programm',)
#--------------------------------------------------------------------------------
class ProgrammUpdateView(ProgrammCreateUpdateDetailView):
    """
    ProgrammUpdateView

    Args:
        ProgrammCreateUpdateDetailView (_type_): _description_
    """

    permission_required = ('programmmanagement.change_programm',)
#--------------------------------------------------------------------------------
class ProgrammDeleteView(PermissionRequiredMixin,MainView):
    """
    ProgrammDeleteView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_

    Returns:
        _type_: _description_
    """

    permission_required = 'programmmanagement.delete_programm'

    def get(self, request, *args, **kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.kwargs.get('programm'):
            get_object_or_404(Programm,slug = self.kwargs.get('programm')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#--------------------------------------------------------------------------------
class ProgrammProgrammView(PermissionRequiredMixin,MainView):
    """
    ProgrammProgrammView

    Args:
        PermissionRequiredMixin (_type_): _description_
        MainView (_type_): _description_
    """

    permission_required = 'programmmanagement:programm_programm'

    template_name = None

    def get(self,request,*args,**kwargs):
        """
        get

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        if self.kwargs.get('programm'):
            self.template_name = self.context['queryset'].htmlfile.name
            return render(request,self.template_name,self.context)
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    def get_queryset(self):
        """
        get_queryset

        Returns:
            query: contains the programm object
        """
        if self.kwargs.get('programm'):
            queryset = Programm.objects.get(slug=self.kwargs.get('programm'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
