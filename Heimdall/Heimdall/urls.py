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
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    #path('documentationmanagement/', include('documentationmanagement.urls')),
    #path('personalmanagement/',include('personalmanagement.urls')),
    # path('productmanagement/',include('productmanagement.urls')),
    #path('relationshipmanagement/',include('relationshipmanagement.urls')),
    path('storagemanagement/',include('storagemanagement.urls')),
    #path('structuremanagement/',include('structuremanagement.urls')),
    # Rest Framework urls
    #path('api/documentationmanagement/', include('documentationmanagement.api.urls', namespace = 'documentationmanagementAPI')),
    #path('api/relationshipmanagement/', include('relationshipmanagement.api.urls', namespace = 'relationshipmanagementAPI')),
    path('api/storagemanagement/', include('storagemanagement.api.urls', namespace = 'storagemanagementAPI')),
    #path('api/structuremanagement/', include('structuremanagement.api.urls', namespace = 'structuremanagementAPI')),
    # Thirdparty packages
    path('tinymce/', include('tinymce.urls')),
    path('qr_code/', include('qr_code.urls', namespace="qr_code"))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)