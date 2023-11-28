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
from documentationmanagement.protocol.api.views import (
    ProtocolListAPIView,
    ProtocolDetailAPIView,
    ProtocolDataListAPIView,
    ProtocolDataDetailAPIView,
    VariableDetailAPIView,
    VariableListAPIView
    )

urlpatterns = [
    path('list/',ProtocolListAPIView.as_view(),name='protocol_list'),
    path('detail/<slug:protocol>/',ProtocolDetailAPIView.as_view(),name='protocol_detail'),
    path('data/list/',ProtocolDataListAPIView.as_view(),name='protocoldata_list'),
    path('data/detail/<slug:protocoldata>/',ProtocolDataDetailAPIView.as_view(),name='protocoldata_detail'),
    path('variable/list/',VariableListAPIView.as_view(),name='variable_list'),
    path('variable/detail/<slug:variable>/',VariableDetailAPIView.as_view(),name='variable_detail'),
]