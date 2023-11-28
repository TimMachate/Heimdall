#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path, include
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Views
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------

app_name = 'documentationmanagement'

urlpatterns = [
    # Fieles
    path('',include('documentationmanagement.file.urls')),

    # Direction
    path('direction/',include('documentationmanagement.direction.urls')),

    # Document
    path('document/',include('documentationmanagement.document.urls')),

    # Formular
    path('formular/',include('documentationmanagement.formular.urls')),

    # General
    path('general/',include('documentationmanagement.general.urls')),

    # Manual
    path('manual/',include('documentationmanagement.manual.urls')),

    # Picture
    path('picture/',include('documentationmanagement.picture.urls')),

    # Processinstruction
    path('processinstruction/',include('documentationmanagement.processinstruction.urls')),

    # Protocol
    path('protocol/',include('documentationmanagement.protocol.urls')),
    
    # Saftydatasheet
    path('safetydatasheet/',include('documentationmanagement.safetydatasheet.urls')),

    # Technicaldatasheet
    path('technicaldatasheet/',include('documentationmanagement.technicaldatasheet.urls')),

    # Workingdescription
    path('workingdescription/',include('documentationmanagement.workingdescription.urls')),

    # Workinginstruction
    path('workinginstruction/',include('documentationmanagement.workinginstruction.urls')),
]