#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Views
#--------------------------------------------------------------------------------
from .views.login import LoginView
from .views.logout import LogoutView
from .views.main import MainView
from .views.search import SearchView
#--------------------------------------------------------------------------------

app_name = 'main'

urlpatterns = [
    # Hauptseite
    path('', MainView.as_view(), name='main_overview'),
    # Login Seite
    path('login/', LoginView.as_view(), name='login_view'),
    # Logout Seite
    path('logout/', LogoutView.as_view(), name='logout_view'),
    # Search Seite
    path('search/', SearchView.as_view(), name='search_view'),
    
    #path('register/', views.register_view, name='register_view'),
    #path('contact/', views.contact_view, name='contact_view'),
    #path('user/', views.user_view, name='user_view'),
]