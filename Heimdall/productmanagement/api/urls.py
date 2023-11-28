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

app_name = 'productmanagementAPI'

urlpatterns = [
    path('cart/',include('productmanagement.cart.api.urls')),
    path('offer/',include('productmanagement.offer.api.urls')),
    path('order/',include('productmanagement.order.api.urls')),
    path('request/',include('productmanagement.request.api.urls')),
]