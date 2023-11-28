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
from relationshipmanagement.person.models import Person
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from relationshipmanagement.person.forms import PersonForm,EmailFormset,TelephoneFormset
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class PersonView(PermissionRequiredMixin, MainView):

    permission_required = 'relationshipmanagement.view_person'

    template_name = 'person_overview.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Person.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['model'] = 'person'
#--------------------------------------------------------------------------------
class PersonListView(PersonView):

    permission_required = 'relationshipmanagement.list_person'

    template_name = 'person_list.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,company,last_name,first_name,url"
        self.context["api_data_url"] = reverse("relationshipmanagementAPI:person_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class PersonTableView(PersonView):

    permission_required = 'relationshipmanagement.table_person'

    template_name = 'person_table.html'

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context["queryset"]= self.get_queryset()
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # Data Url
        self.context["fields"] = "id,reference_number,company,last_name,first_name,telephones,emails"
        self.context["api_data_url"] = reverse("relationshipmanagementAPI:person_list")+"?values={}".format(self.context["fields"])
#--------------------------------------------------------------------------------
class PersonCreateUpdateDetailView(PersonView):

    template_name = 'person_createupdatedetail.html'
    
    form_class = PersonForm
    formset_email = EmailFormset
    formset_telephone = TelephoneFormset

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.get_context_data()
        self.context['form'] = self.form_class(instance=self.context['queryset'])
        self.context['formset_email'] = self.formset_email(instance = self.context['queryset'])
        self.context['formset_telephone'] = self.formset_telephone(instance = self.context['queryset'])
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

        formset_email = self.formset_email(request.POST,request.FILES,instance=obj)
        if formset_email.is_valid():
            for form in formset_email:
                if form.is_valid():
                    email = form.save(commit=False)
                    email.person_id = obj
                    if email.email:
                        email.save()
        self.context['formset_email'] = formset_email
        
        formset_telephone = self.formset_telephone(request.POST,request.FILES,instance=obj)
        if formset_telephone.is_valid():
            for form in formset_telephone:
                if form.is_valid():
                    telephone = form.save(commit=False)
                    telephone.person_id = obj
                    if telephone.number:
                        telephone.save()
        self.context['formset_telephone'] = formset_telephone

        return redirect('relationshipmanagement:person_update', person=obj.slug)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('person'):
            queryset = Person.objects.get(slug=self.kwargs.get('person'))
        else:
            queryset = None
        return queryset
#--------------------------------------------------------------------------------
class PersonCreateView(PersonCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.add_person',)
#--------------------------------------------------------------------------------
class PersonDetailView(PersonCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.detail_person',)
#--------------------------------------------------------------------------------
class PersonUpdateView(PersonCreateUpdateDetailView):
    permission_required = ('relationshipmanagement.update_person',)
#--------------------------------------------------------------------------------
class PersonDeleteView(PermissionRequiredMixin, MainView):

    permission_required = 'relationshipmanagement.delete_person'

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('person'):
            get_object_or_404(Person, slug = self.kwargs.get('person')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('relationshipmanagement:person_list')
#--------------------------------------------------------------------------------