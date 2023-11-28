from django.forms import ModelForm
from visualisation.models import (
    Font,
    Color,
    Axes,
    Label,
    Grid,
    Tick,
    Title,
    Subtitle,
    Legend,
    Graph,    
    Diagram,
)

class FontForm(ModelForm):
    class Meta:
        model = Font
        fields = '__all__'

class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = '__all__'

class AxesForm(ModelForm):
    class Meta:
        model = Axes
        fields = '__all__'

class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = '__all__'

class GridForm(ModelForm):
    class Meta:
        model = Grid
        fields = '__all__'

class TickForm(ModelForm):
    class Meta:
        model = Tick
        fields = '__all__'

class TitleForm(ModelForm):
    class Meta:
        model = Title
        fields = '__all__'

class SubtitleForm(ModelForm):
    class Meta:
        model = Subtitle
        fields = '__all__'

class LegendForm(ModelForm):
    class Meta:
        model = Legend
        fields = '__all__'

class GraphForm(ModelForm):
    class Meta:
        model = Graph
        fields = '__all__'

class DiagramForm(ModelForm):
    class Meta:
        model = Diagram
        fields = '__all__'