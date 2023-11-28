#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.urls import path
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.person.views import (
    PersonView,
    PersonListView,
    PersonTableView,
    PersonCreateView,
    PersonDetailView,
    PersonUpdateView,
    PersonDeleteView
)
#--------------------------------------------------------------------------------
urlpatterns = [
    # Person
    path('',PersonView.as_view(), name='person_overview'),
    path('list/',PersonListView.as_view(), name='person_list'),
    path('table/',PersonTableView.as_view(), name='person_table'),
    path('create/',PersonCreateView.as_view(), name='person_create'),
    path('update/<slug:person>/',PersonUpdateView.as_view(), name='person_update'),
    path('detail/<slug:person>/',PersonDetailView.as_view(), name='person_detail'),
    path('delete/<slug:person>/',PersonDeleteView.as_view(), name='person_delete'),
]
#--------------------------------------------------------------------------------