#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.urls import reverse
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
from main.forms.login import LoginForm
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Views
#--------------------------------------------------------------------------------
class LoginView(View):
    template_name = 'main.html'
    form_class = LoginForm
    context = {}

    def get(self, request, *args, **kwargs):
        self.get_context_data()
        self.context['queryset'] = self.get_queryset()
        if request.user.is_authenticated:
            self.context["form"] = self.form_class
            return redirect("main:main_overview")
        else:
            self.context["form"] = self.form_class
            return render(request,self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login war erfolgreich!')
                return redirect('main:main_overview')
            else:
                messages.error(request, 'Benutzername oder Passwort sind falsch!')
        else:
            messages.error(request, 'Die eingegebenen Daten konnten nicht validiert werden.')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    def get_queryset(self):
        queryset = None
        return queryset

    def get_context_data(self, **kwargs):
        return self.context
#--------------------------------------------------------------------------------