#--------------------------------------------------------------------------------
# pagination File from App Storagemanagement API
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.apps import apps
from rest_framework.pagination import PageNumberPagination
#--------------------------------------------------------------------------------

if 'tools' in [app.name for app in apps.get_app_configs()]:
    from tools.api.pagination import PageNumberPagination
else:
    class PageNumberPagination(PageNumberPagination):
        page_size = 10