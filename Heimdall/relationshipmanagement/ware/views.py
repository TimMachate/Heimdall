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
from relationshipmanagement.ware.models import Ware
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from relationshipmanagement.ware.forms import WareForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class WareView(PermissionRequiredMixin, MainView):

    permission_required = 'relationshipmanagement.view_ware'

    template_name = 'ware_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Ware.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'ware'
#--------------------------------------------------------------------------------
class WareListView(WareView):

    permission_required = 'relationshipmanagement.list_ware'

    template_name = 'ware_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,company,name,ware_number,url"
        self.context["api_data_url"] = reverse("relationshipmanagementAPI:ware_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class WareTableView(WareView):

    permission_required = 'relationshipmanagement.table_ware'

    template_name = 'ware_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,company,name,ware_number,unit_package,unit,price,create,update"
        self.context["api_data_url"] = reverse("relationshipmanagementAPI:ware_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class WareCreateUpdateDetailView(WareView):

    template_name = 'ware_createupdatedetail.html'
    
    form_class = WareForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'])
        return render(request, self.template_name, self.context)

    def post(self,request, *args, **kwargs):
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

        return redirect('relationshipmanagement:ware_update', ware=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('ware'):
            queryset = Ware.objects.get(slug=self.kwargs.get('ware'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class WareCreateView(WareCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.add_ware',)
#--------------------------------------------------------------------------------
class WareDetailView(WareCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.detail_ware',)
#--------------------------------------------------------------------------------
class WareUpdateView(WareCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.update_ware',)
#--------------------------------------------------------------------------------
class WareDeleteView(PermissionRequiredMixin, MainView):

    permission_required = 'relationshipmanagement.delete_ware'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('ware'):
            get_object_or_404(Ware, slug = self.kwargs.get('ware')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('relationshipmanagement:ware_list')
#--------------------------------------------------------------------------------