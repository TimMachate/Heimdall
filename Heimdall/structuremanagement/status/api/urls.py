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
from structuremanagement.status.api.views import StatusListAPIView,StatusDetailAPIView,StatusDataListAPIView,StatusDataDetailAPIView

urlpatterns = [
    # Status
    path('list/',StatusListAPIView.as_view(),name='status_list'),
    path('detail/<slug:status>/',StatusDetailAPIView.as_view(),name='status_detail'),

    # Status Data
    path('data/list/',StatusDataListAPIView.as_view(),name='statusdata_list'),
    path('data/detail/<slug:statusdata>/',StatusDataDetailAPIView.as_view(),name='statusdata_detail'),
]