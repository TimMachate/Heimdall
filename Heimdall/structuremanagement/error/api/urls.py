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
from structuremanagement.error.api.views import ErrorListAPIView,ErrorDetailAPIView,ErrorDataListAPIView,ErrorDataDetailAPIView

urlpatterns = [
    # Error
    path('list/',ErrorListAPIView.as_view(),name='error_list'),
    path('detail/<slug:error>/',ErrorDetailAPIView.as_view(),name='error_detail'),
    # Error Data
    path('data/list/',ErrorDataListAPIView.as_view(),name='errordata_list'),
    path('data/detail/<slug:errordata>/',ErrorDataDetailAPIView.as_view(),name='errordata_detail'),
]