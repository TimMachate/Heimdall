from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.utils import timezone

from .main import VisualisationView
from visualisation.models import Tab
from visualisation.forms import TabForm

class TabListView(VisualisationView):
    template_name = 'tab/tab_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Tab.objects.filter(user = self.request.user.id)
        return queryset

class TabTableView(VisualisationView):
    template_name = 'tab/tab_table.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Tab.objects.filter(user = self.request.user.id)
        return queryset

class TabDetailView(VisualisationView):
    template_name = 'tab/tab_detail.html'

    def get_queryset(self, *args, **kwargs):
        tab = Tab.objects.get(id = self.kwargs.get('id'))
        return tab

class TabCreateUpdateView(VisualisationView):
    template_name = 'tab/tab_createupdate.html'
    form_class = TabForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.context['form'] = self.form_class(instance = self.context['queryset'])
        self.get_context_data()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj , create = Tab.objects.update_or_create(
                id  = request.POST['id'] if request.POST['id'] != '' else None,
                defaults = {
                    'name' : request.POST['name'],
                    'order' : request.POST['order'],
                }
            )
            if create:
                obj.user = user
                obj.create_user = user
                obj.update_user = user
                messages.success(request,'Tab wurde erfolgreich erstellt!')
            else:
                obj.update_user = user
                obj.update_time = timezone.now()
                messages.success(request,'Tab wurde erfolgreich geupdated!')
            obj.save()
            return redirect('Visualisation:visualisation_detail', slug = obj.slug)
        messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        return redirect('Visualisation:tab_create')
    
    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('id'):
            queryset = Tab.objects.get(id = self.kwargs.get('id'))
        else:
            queryset = None
        return queryset

class TabDeleteView(VisualisationView):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get('id'):
            Tab.objects.get(id = self.kwargs.get('id')).delete()
            messages.success(request,'Tab wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Tab konnte nicht gelöscht werden!')
        return redirect('Visualisation:tab_list')