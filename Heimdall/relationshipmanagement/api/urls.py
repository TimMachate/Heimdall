"""Heimdall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

app_name = 'relationshipmanagementAPI'

urlpatterns = [
    path('company/',include('relationshipmanagement.company.api.urls')),
    path('customer/',include('relationshipmanagement.customer.api.urls')),
    path('general/',include('relationshipmanagement.general.api.urls')),
    path('person/',include('relationshipmanagement.person.api.urls')),
    path('supplier/',include('relationshipmanagement.supplier.api.urls')),
    path('ware/',include('relationshipmanagement.ware.api.urls')),
]