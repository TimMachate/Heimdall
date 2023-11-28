from main.views.main import MainView
from itertools import chain

from visualisation.models import (
    Tab,
    ItemGroup,
    Table,
    Diagram,
)

class VisualisationView(MainView):
    template_name= 'visualisation.html'

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context['tabs'] = Tab.objects.filter(user=self.request.user.id).order_by('order')

class VisualisationDetailView(VisualisationView):
    template_name= 'visualisation_detail.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Tab.objects.get(user=self.request.user.id,slug=self.kwargs.get('slug'))
        return queryset