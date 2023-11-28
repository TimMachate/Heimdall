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
from django.urls import path
from rest_framework.routers import DefaultRouter
from structuremanagement.process.api.views import ProcessListAPIView, ProcessDetailAPIView,ProcessDataListAPIView,ProcessDataDetailAPIView

urlpatterns = [

    #Process
    path('list/',ProcessListAPIView.as_view(),name='process_list'),
    path('detail/<slug:process>/',ProcessDetailAPIView.as_view(),name='process_detail'),

    # Process Data
    path('data/list/',ProcessDataListAPIView.as_view(),name='processdata_list'),
    path('data/detail/<slug:processdata>/',ProcessDataDetailAPIView.as_view(),name='processdata_detail'),
]