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

app_name = 'documentationmanagementAPI'

urlpatterns = [
    path('direction/',include('documentationmanagement.direction.api.urls')),
    path('document/',include('documentationmanagement.document.api.urls')),
    path('file/',include('documentationmanagement.file.api.urls')),
    path('formular/',include('documentationmanagement.formular.api.urls')),
    path('general/',include('documentationmanagement.general.api.urls')),
    path('manual/',include('documentationmanagement.manual.api.urls')),
    path('picture/',include('documentationmanagement.picture.api.urls')),
    path('processinstruction/',include('documentationmanagement.processinstruction.api.urls')),
    path('protocol/',include('documentationmanagement.protocol.api.urls')),
    path('safetydatasheet/',include('documentationmanagement.safetydatasheet.api.urls')),
    path('technicaldatasheet/',include('documentationmanagement.technicaldatasheet.api.urls')),
    path('workingdescription/',include('documentationmanagement.workingdescription.api.urls')),
    path('workinginstruction/',include('documentationmanagement.workinginstruction.api.urls')),
]