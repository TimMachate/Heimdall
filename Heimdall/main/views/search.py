#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Forms
#--------------------------------------------------------------------------------
from main.forms.search import SearchForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class SearchView(View):
    template_name = 'main.html'
    form_class_search = SearchForm
    context = {}

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context['queryset'] = self.get_queryset()
        if request.user.is_authenticated:
            self.context["form"] = self.form_class_search
            return render(request,self.template_name,self.context)
        else:
            return redirect("main:login_view")

    def post(self, request, *args, **kwargs):
        form = self.form_class_search(request.POST)
        user = get_user_model().objects.get(id=request.user.id)
        if form.is_valid():
            print("form ist True")
            request.POST.get("searchfield")
        if self.request.GET.get('next'):
            return redirect(self.request.GET.get('next'))
        else:
            return redirect('main:search_view')

    def get_queryset(self):
        queryset = None
        return queryset
    
    def get_context_data(self, **kwargs):
        installed_apps = []
        for app in apps.get_app_configs():
            installed_apps.append(app.name)
        self.context['installed_apps'] = installed_apps
        self.context['navbar'] = json.load(open('setting.json', encoding="utf8"))['navbar']
        self.context['company_name'] = 'MaTi'
        self.context['url_overview'] = None
        self.context['url_list'] = None
        self.context['url_table'] = None
        self.context['url_create'] = None
        return self.context
#--------------------------------------------------------------------------------