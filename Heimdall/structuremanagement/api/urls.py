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

app_name = 'structuremanagementAPI'

urlpatterns = [
    path('companystructure/',include('structuremanagement.companystructure.api.urls')),
    path('device/',include('structuremanagement.device.api.urls')),
    path('department/',include('structuremanagement.department.api.urls')),
    path('error/',include('structuremanagement.error.api.urls')),
    path('group/',include('structuremanagement.group.api.urls')),
    path('maintenance/',include('structuremanagement.maintenance.api.urls')),
    path('position/',include('structuremanagement.position.api.urls')),
    path('process/',include('structuremanagement.process.api.urls')),
    path('section/',include('structuremanagement.section.api.urls')),
    path('status/',include('structuremanagement.status.api.urls')),
]