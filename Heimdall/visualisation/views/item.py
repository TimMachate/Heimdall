from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.utils import timezone


from .main import VisualisationView
from visualisation.models import Tab
from visualisation.models import ItemGroup
from visualisation.models import Item
from visualisation.forms import ItemGroupForm
from visualisation.forms import ItemForm
from django.forms import inlineformset_factory

class ItemGroupListView(VisualisationView):
    template_name = 'item/itemgroup_list.html'

    def get_queryset(self, *args, **kwargs):
        TABS = []
        for i in Tab.objects.filter(user = self.request.user.id):
            TABS.append(i.id)
        queryset = ItemGroup.objects.filter(tab__in = TABS).order_by('name')
        return queryset

class ItemGroupTableView(ItemGroupListView):
    template_name = 'item/itemgroup_table.html'

class ItemGroupDetailView(VisualisationView):
    template_name = 'item/itemgroup_detail.html'

    def get_queryset(self, *args, **kwargs):
        itemgroup = ItemGroup.objects.get(id = self.kwargs.get('id'))
        return itemgroup

class ItemGroupCreateUpdateView(VisualisationView):
    template_name = 'item/itemgroup_createupdate.html'
    form_class = ItemGroupForm
    formset_class = inlineformset_factory(ItemGroup, Item, form=ItemForm, extra=1)

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
        #return render(request, self.template_name, self.context)
        return redirect('Visualisation:itemgroup_update', id = obj.id)
    
    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('id'):
            queryset = ItemGroup.objects.get(id = self.kwargs.get('id'))
        else:
            queryset = None
        return queryset

class ItemGroupDeleteView(VisualisationView):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get('id'):
            ItemGroup.objects.get(id = self.kwargs.get('id')).delete()
            messages.success(request,'Item-Gruppe wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item-Gruppe konnte nicht gelöscht werden!')
        return redirect('Visualisation:itemgroup_list')

#-----------------------------------------------------------------
class ItemListView(VisualisationView):
    template_name = 'item/item_list.html'

    def get_queryset(self, *args, **kwargs):
        TABS = []
        for i in Tab.objects.filter(user = self.request.user.id):
            TABS.append(i.id)
        ITEMGROUP = []
        for i in ItemGroup.objects.filter(tab__in = TABS):
            ITEMGROUP.append(i.id)
        queryset = Item.objects.filter(itemGroup__in = ITEMGROUP).order_by('name')
        return queryset

class ItemTableView(ItemListView):
    template_name = 'item/item_table.html'

class ItemDetailView(VisualisationView):
    template_name = 'item/item_detail.html'

    def get_queryset(self, *args, **kwargs):
        item = Item.objects.get(id = self.kwargs.get('id'))
        return item

class ItemCreateUpdateView(VisualisationView):
    template_name = 'item/item_createupdate.html'
    form_class = ItemForm

    def get(self, request, *args, **kwargs):
        self.context['queryset'] = self.get_queryset()
        self.context['form'] = self.form_class(instance = self.context['queryset'])
        self.get_context_data()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES,instance = self.context['queryset'])
        if form.is_valid():
            form.save()
            return redirect('Visualisation:item_list')
        messages.error(request,'Die eingegebenen Daten können nicht validiert werden!')
        return redirect('Visualisation:item_create')
    
    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('id'):
            queryset = Item.objects.get(id = self.kwargs.get('id'))
        else:
            queryset = None
        return queryset

class ItemDeleteView(VisualisationView):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get('id'):
            Item.objects.get(id = self.kwargs.get('id')).delete()
            messages.success(request,'Item wurde erfolgreich gelöscht!')
        else:
            messages.error(request,'Item konnte nicht gelöscht werden!')
        return redirect('Visualisation:item_list')