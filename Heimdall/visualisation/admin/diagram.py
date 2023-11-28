from django.contrib import admin
from django.utils import timezone

from visualisation.models import (
    Font,
    Color,
    Label,
    Grid,
    Tick,
    Axes,
    Title,
    Subtitle,
    Legend,
    Graph,
    Diagram,
)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id','name','red','green','blue','alpha']
    list_display_links = ['id','name',]
    search_fields = ['name',]
    list_filter = []
    list_editable = ['red','green','blue','alpha']
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            )}),
        ('Farbe', {'fields':(
            ('red','green','blue'),
            )}),
        ('Transparenz', {'fields':(
            'alpha',
            )}),
    )
    filter_horizontal = []
    radio_fields = {}
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

@admin.register(Font)
class FontAdmin(admin.ModelAdmin):
    list_display = ['id','name','family','style','size','weight','lineHeight']
    list_display_links = ['id','name']
    search_fields = ['name',]
    list_filter = []
    list_editable = ['size','weight','lineHeight']
    ordering = []
    fieldsets = (
        (None, {'fields':(
            'name',
            'family',
            'style',
            )}),
        ('Farbe', {'fields':(
            ('size','weight','lineHeight'),
            )}),
    )
    filter_horizontal = []
    radio_fields = {}
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['id','label_text','label_display',]
    list_display_links = ['id','label_text',]
    search_fields = ['label_text',]
    list_filter = []
    list_editable = ['label_display',]
    ordering = ['id',]
    fieldsets = (
        ('Label', {'fields':(
            'label_text',
            'label_display',
            )}),
        ('Label Style', {'fields':(
            ('label_font','label_color',),
            )}),
        ('Label Layout', {'fields':(
            ('label_align','label_padding',),
            )}),
    )
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class LabelInLine(admin.StackedInline):
    model = Label
    extra = 1
    max_num = 1
    show_change_link = True
    fieldsets = (
        ('Label', {'fields':(
            'label_text',
            'label_display',
            )}),
        ('Label Style', {'fields':(
            ('label_font','label_color',),
            )}),
        ('Label Layout', {'fields':(
            ('label_align','label_padding',),
            )}),
    )

@admin.register(Grid)
class GridAdmin(admin.ModelAdmin):
    list_display = ['id','grid_display','grid_drawBorder','grid_drawTickLines',]
    list_display_links = ['id',]
    search_fields = []
    list_filter = []
    list_editable = ['grid_display','grid_drawBorder','grid_drawTickLines',]
    ordering = ['id',]
    fieldsets = (
        ('Grid', {'fields':(
            'grid_display',
            'grid_drawOnChartArea',
            'grid_z',
            )}),
        ('Grid Layout', {'fields':(
            'grid_color',
            'grid_lineWidth',
            'grid_offset',
            'grid_circular',
            )}),
        ('Grid Border', {'fields':(
            ('grid_drawBorder','grid_borderColor',),
            ('grid_borderDash','grid_borderDashOffset',),
            )}),
        ('Grid Tick', {'fields':(
            'grid_drawTickLines',
            'grid_tickColor',
            ('grid_tickLength','grid_tickWidth',),
            ('grid_tickBorderDash','grid_tickBorderDashOffset',),
            )}),
    )

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class GridInLine(admin.StackedInline):
    model = Grid
    extra = 1
    max_num = 1
    show_change_link = True
    fieldsets = (
        ('Grid', {'fields':(
            'grid_display',
            'grid_drawOnChartArea',
            'grid_z',
            )}),
        ('Grid Layout', {'fields':(
            ('grid_lineWidth', 'grid_color',),
            'grid_offset',
            'grid_circular',
            )}),
        ('Grid Border', {'fields':(
            ('grid_drawBorder','grid_borderColor','grid_borderDash','grid_borderDashOffset',),
            )}),
        ('Grid Tick', {'fields':(
            'grid_drawTickLines',
            'grid_tickColor',
            ('grid_tickLength','grid_tickWidth',),
            ('grid_tickBorderDash','grid_tickBorderDashOffset',),
            )}),
    )

@admin.register(Tick)
class TickAdmin(admin.ModelAdmin):
    list_display = ['id','tick_display',]
    list_display_links = ['id',]
    search_fields = []
    list_filter = []
    list_editable = ['tick_display',]
    ordering = ['id',]
    fieldsets = (
        ('Tick', {'fields':(
            'tick_display',
            ('tick_font','tick_color',),
            'tick_z',
            'tick_padding',
            )}),
        ('Tick Text Stroke', {'fields':(
            'tick_textStrokeColor',
            'tick_textStrokeWidth',
            )}),
        ('Tick Backdrop', {'fields':(
            'tick_backdropDisplay',
            'tick_backdropColor',
            'tick_backdropPadding',
            )}),
    )

    def get_model_perms(self, request):
            """
            Return empty perms dict thus hiding the model from admin index.
            """
            return {}

class TickInLine(admin.StackedInline):
    model = Tick
    extra = 1
    max_num = 1
    show_change_link = True
    fieldsets = (
        ('Tick', {'fields':(
            'tick_display',
            ('tick_font','tick_color',),
            'tick_z',
            'tick_padding',
            )}),
        ('Tick Text Stroke', {'fields':(
            'tick_textStrokeColor',
            'tick_textStrokeWidth',
            )}),
        ('Tick Backdrop', {'fields':(
            'tick_backdropDisplay',
            'tick_backdropColor',
            'tick_backdropPadding',
            )}),
    )

@admin.register(Axes)
class AxesAdmin(admin.ModelAdmin):
    list_display = ['id','axes_diagram','axes_display','axes_type','axes_stacked',]
    list_display_links = ['id',]
    search_fields = []
    list_filter = []
    list_editable = ['axes_display','axes_stacked',]
    ordering = ['id',]
    fieldsets = (
        ('Achse', {'fields':(
            'axes_diagram',
            ('axes_display','axes_type',),
            ('axes_stacked','axes_weight','axes_reverse',),
            ('axes_min','axes_max','axes_suggestedMin','axes_suggestedMax',),
            )}),
    )
    inlines = [LabelInLine,GridInLine,TickInLine]

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class AxesInLine(admin.StackedInline):
    model = Axes
    extra = 0
    show_change_link = True
    fieldsets = (
        ('Achse', {'fields':(
            ('axes_display','axes_type',),
            ('axes_stacked','axes_weight','axes_reverse',),
            ('axes_min','axes_max','axes_suggestedMin','axes_suggestedMax',),
            )}),
    )

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ['id','text','display',]
    list_display_links = ['id','text',]
    search_fields = ['text',]
    list_filter = []
    list_editable = ['display',]
    ordering = ['text',]
    fieldsets = (
        (None, {'fields':(
            'text',
            ('display','fullSize',),
            'font',
            'color',
            )}),
        ('Layout', {'fields':(
            'position',
            'align',
            ('paddingTop','paddingRight','paddingBottom','paddingLeft',),
            )}),
    )
    filter_horizontal = []
    radio_fields = {}
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

@admin.register(Subtitle)
class SubtitleAdmin(admin.ModelAdmin):
    list_display = ['id','text','display',]
    list_display_links = ['id','text',]
    search_fields = ['text',]
    list_filter = []
    list_editable = ['display',]
    ordering = ['text',]
    fieldsets = (
        (None, {'fields':(
            'text',
            ('display','fullSize',),
            'font',
            'color',
            )}),
        ('Layout', {'fields':(
            'position',
            'align',
            ('paddingTop','paddingRight','paddingBottom','paddingLeft',),
            )}),
    )
    filter_horizontal = []
    radio_fields = {}
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

@admin.register(Legend)
class LegendAdmin(admin.ModelAdmin):
    list_display = ['id','display',]
    list_display_links = ['id',]
    search_fields = []
    list_filter = []
    list_editable = ['display',]
    ordering = []
    fieldsets = (
        (None, {'fields':(
            'display',
            ('fullSize','reverse'),
            )}),
        ('Layout', {'fields':(
            'position',
            'align',
            ('maxHeight','maxWidth',),
            )}),
        ('Titel', {'fields':(
            ('title_text','title_display',),
            'title_font',
            'title_color',
            ('title_paddingTop','title_paddingRight','title_paddingBottom','title_paddingLeft',),
            )}),
        ('Label', {'fields':(
            'label_font',
            'label_color',
            ('boxWidth','boxHeight',),
            ('label_paddingTop','label_paddingRight','label_paddingBottom','label_paddingLeft',),
            ('label_pointStyle','label_usePointStyle','label_align',),
            )}),
    )
    filter_horizontal = []
    radio_fields = {}
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class GraphAdmin(admin.StackedInline):
    model = Graph
    extra = 0
    ordering = ['order',]
    fieldsets = (
        (None, {'fields':(
            ('name','order',),
            ('graphType',),
            ('graphURL','graphXData','graphYData',),
            ('graphPointBorderWidth','graphPointHitRadius','graphPointRadius','graphPointStyle',),
            ('graphPointBackgroundColorRed','graphPointBackgroundColorGreen','graphPointBackgroundColorBlue','graphPointBackgroundColorAlpha',),
            ('graphPointBorderColorRed','graphPointBorderColorGreen','graphPointBorderColorBlue','graphPointBorderColorAlpha',),
            'graphBorderWidth',
            ('graphBackgroundColorRed','graphBackgroundColorGreen','graphBackgroundColorBlue','graphBackgroundColorAlpha',),
            ('graphBorderColorRed','graphBorderColorGreen','graphBorderColorBlue','graphBorderColorAlpha',),
            )}),
    )

@admin.register(Diagram)
class DiagramAdmin(admin.ModelAdmin):
    list_display = ['id','name','user','create_user','create_time','update_user','update_time','order',]
    list_display_links = ['id', 'name']
    search_fields = ['name',]
    list_filter = ['user']
    list_editable = ['order',]
    ordering = ['user','name','order',]
    fieldsets = (
        (None, {'fields':(
            'user',
            'tab',
            )}),
        ('Diagramm', {'fields':(
            ('name','order',),
            )}),
        ('Layout', {'fields':(
            ('col_xs','col_sm','col_md','col_lg','col_xl',),
            ('paddingTop','paddingRight','paddingBottom','paddingLeft',),
            )}),
        ('Title', {'fields':(
            'title',
            )}),
        ('Subtitle', {'fields':(
            'subtitle',
            )}),
        ('Legende', {'fields':(
            'legend',
            )}),
    )
    inlines = [
        AxesInLine,
        GraphAdmin,
    ]
    filter_horizontal = []
    radio_fields = {}

    def save_model(self, request, instance, form, change):
        if not instance.create_user:
            instance.create_user = request.user
        if not instance.create_time:
            instance.create_time = timezone.now()
        instance.update_user = request.user
        instance.update_time = timezone.now()
        return super().save_model(request, instance, form, change = True)