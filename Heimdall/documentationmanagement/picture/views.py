#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from main.views.main import MainView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.picture.models import Picture
from documentationmanagement.file.models import File, PictureProxy
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from django.forms import inlineformset_factory
from documentationmanagement.picture.forms import PictureForm
from documentationmanagement.file.forms import FileForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
from documentationmanagement.file.views import FileView
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class PictureView(FileView):
    permission_required = 'documentationmanagement.view_picture'

    template_name = 'picture/templates/picture_overview.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance=self.context["api_data"])
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj = form.save()
            messages.success(request,'Die eingegebenen Daten konnten validiert werden!')
        else:
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        self.context['form'] = form

    def get_queryset(self, *args, **kwargs):
        result = PictureProxy.objects.all()
        return result

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['app'] = 'documentationmanagement'
        self.context['model'] = 'picture'
        # Data Url
        fields = "id,url_detail,url_update,reference_number,name,url_file,url_file_qrcode"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:picture_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class PictureListView(PictureView):

    permission_required = 'documentationmanagement.list_picture'

    template_name = 'picture/templates/picture_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = PictureProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,url_detail,url_update,url_delete,reference_number,name,version,type,url_file,url_file_qrcode"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:picture_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class PictureTableView(PictureView):

    permission_required = 'documentationmanagement.table_picture'

    template_name = 'picture/templates/picture_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_queryset(self, *args, **kwargs):
        queryset = PictureProxy.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        fields = "id,reference_number,name,version,type,create,update"
        self.context["api_data_url"] = reverse("documentationmanagementAPI:picture_list")+"?values={}".format(fields)
#--------------------------------------------------------------------------------
class PictureCreateUpdateDetailView(PictureView):

    permission_required = ('documentationmanagement.add_picture','documentationmanagement.change_picture')

    template_name = 'picture/templates/picture_createupdatedetail.html'
    
    form_class = FileForm
    formset_class = PictureForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(
            instance=self.context['queryset'],
            initial=self.get_initial()["file"]
            )
        self.context['formset'] = self.formset_class(
            initial=self.get_initial()["picture"]
            )
        return render(request, self.template_name, self.context)

    def get_initial(self):
        result = {}
        result["file"]={}
        result["picture"] = {}
        if self.get_queryset():
            result["file"]["type"] = "PI"
            if self.get_queryset().content():
                result["picture"]["file_id"] = self.get_queryset().id
                result["picture"]["content"] = self.get_queryset().content().content
        return result

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance=self.get_queryset())
        formset = self.formset_class(request.POST,request.FILES, instance=self.get_queryset().content() if self.get_queryset() else None)
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid() and formset.is_valid():
            obj = form.save(commit=False)
            if not obj.create_user_id:
                obj.create_user_id = user
            obj.update_user_id = user
            obj.update_datetime = timezone.now()
            picture = formset.save(commit=False)
            picture.file_id = obj
            obj.save()
            picture.save()
            self.context['form'] = form
            self.context['formset'] = formset
        else:
            self.context['form'] = form
            self.context['formset'] = formset
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
            return redirect('documentationmanagement:picture_detail',picture=obj.slug)
        messages.success(request,'Die eingegeben Daten wurden validiert!')
        return redirect('documentationmanagement:picture_detail',picture=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('picture'):
            queryset=PictureProxy.objects.get(slug=self.kwargs.get('picture'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class PictureDeleteView(PermissionRequiredMixin,MainView):

    permission_required = 'documentationmanagement.delete_picture'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('picture'):
            File.objects.get(slug = self.kwargs.get('picture')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('documentationmanagement:picture_list')
#--------------------------------------------------------------------------------