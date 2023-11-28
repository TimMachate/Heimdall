#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path,include
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
#from .views.relationshipmanagement import RelationshipmanagmentView
#--------------------------------------------------------------------------------

app_name = 'relationshipmanagement'

urlpatterns = [
    #path('',RelationshipmanagmentView.as_view(), name='relationshipmanagement'),
    # Company
    path('company/',include('relationshipmanagement.company.urls')),
    # Customer
    path('customer/',include('relationshipmanagement.customer.urls')),
    # General Company
    path('general/',include('relationshipmanagement.general.urls')),
    # Person
    path('person/',include('relationshipmanagement.person.urls')),
    # Supplier
    path('supplier/',include('relationshipmanagement.supplier.urls')),
    # ware Company
    path('ware/',include('relationshipmanagement.ware.urls')),
]