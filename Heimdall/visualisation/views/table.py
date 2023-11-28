from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.utils import timezone


from .main import VisualisationView
from visualisation.models import Tab
from visualisation.models import Table
from visualisation.models import TableItem
from visualisation.forms import TableForm
from visualisation.forms import TableItemForm
from django.forms import inlineformset_factory

class TableListView(VisualisationView):
    template_name = 'table/table_list.html'

    def get_queryset(self, *args, **kwargs):
        TABS = []
        for i in Tab.objects.filter(user = self.request.user.id):
            TABS.append(i.id)
        queryset = Table.objects.filter(tab__in = TABS).order_by('name')
        return queryset

class TableTableView(TableListView):
    template_name = 'table/table_table.html'

class TableDetailView(VisualisationView):
    template_name = 'table/table_detail.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Table.objects.get(id = self.kwargs.get('id'))
        return queryset

class TableCreateUpdateView(VisualisationView):
    template_name = 'table/table_createupdate.html'
    form_class = TableForm
    formset_class = inlineformset_factory(Table, TableItem, form=TableItemForm, extra=1)

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.context['form'] = self.form_class(instance = self.context['queryset'])
        self.context['formset'] = self.formset_class(instance = self.context['queryset'])
        self.get_context_data()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance=self.context['queryset'])
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            obj = form.save()
            if not obj.create_user:
                obj.create_user = user
            obj.update_user = user
            obj.update_time = timezone.now()
            obj.save()
            self.context['form'] = form
        else:
            self.context['form'] = form
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        formset = self.formset_class(request.POST,request.FILES,instance=obj)
        if formset.is_valid():
            formset.save()
            self.context['formset'] = formset
        else:
            self.context['formset'] = formset
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        return redirect('Visualisation:table_update', id = obj.id)
    
    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('id'):
            queryset = Table.objects.get(id = self.kwargs.get('id'))
        else:
            queryset = None
        return queryset

class TableDeleteView(VisualisationView):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get('id'):
            Table.objects.get(id = self.kwargs.get('id')).delete()
            messages.success(request,'Item-Gruppe wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item-Gruppe konnte nicht gelöscht werden!')
        return redirect('Visualisation:itemgroup_list')

#-----------------------------------------------------------------
class TableItemListView(VisualisationView):
    template_name = 'table/tableitem_list.html'

    def get_queryset(self, *args, **kwargs):
        TABS = []
        for i in Tab.objects.filter(user = self.request.user.id):
            TABS.append(i.id)
        TABLE = []
        for i in Table.objects.filter(tab__in = TABS):
            TABLE.append(i.id)
        queryset = TableItem.objects.filter(table__in = TABLE).order_by('name')
        return queryset

class TableItemTableView(TableItemListView):
    template_name = 'table/tableitem_table.html'

class TableItemDetailView(VisualisationView):
    template_name = 'table/tableitem_detail.html'

    def get_queryset(self, *args, **kwargs):
        queryset = TableItem.objects.get(id = self.kwargs.get('id'))
        return queryset

class TableItemCreateUpdateView(VisualisationView):
    template_name = 'table/tableitem_createupdate.html'
    form_class = TableItemForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.context['form'] = self.form_class(instance = self.context['queryset'])
        self.get_context_data()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance=self.context['queryset'])
        if form.is_valid():
            obj = form.save()
        else:
            self.context['form'] = form
            messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        return redirect('Visualisation:tableitem_update', id = obj.id)
    
    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('id'):
            queryset = TableItem.objects.get(id = self.kwargs.get('id'))
        else:
            queryset = None
        return queryset

class TableItemDeleteView(VisualisationView):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get('id'):
            TableItem.objects.get(id = self.kwargs.get('id')).delete()
            messages.success(request,'Item-Gruppe wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item-Gruppe konnte nicht gelöscht werden!')
        return redirect('Visualisation:itemgroup_list')
