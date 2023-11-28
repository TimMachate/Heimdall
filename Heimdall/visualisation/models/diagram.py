from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

class Diagram(models.Model):

    class ColumnSpan(models.TextChoices):
        ONE = '1', _('1')
        TWO = '2', _('2')
        THREE = '3', _('3')
        FOUR = '4', _('4')
        FIVE = '5', _('5')
        SIX = '6', _('6')
        SEVEN = '7', _('7')
        EIGHT = '8', _('8')
        NINE = '9', _('9')
        TEN = '10', _('10')
        ELEVEN = '11', _('11')
        TWELVE = '12', _('12')
        THIRTEEN = '13', _('13')
        FOURTEEN = '14', _('14')
        FIFTEEN = '15', _('15')
        SIXTEEN = '16', _('16')
        SEVENTEEN = '17', _('17')
        EIGHTEEN = '18', _('18')
        NINETEEN = '19', _('19')
        TWENTY = '20', _('20')
        TWENTYONE = '21', _('21')
        TWENTYTWO = '22', _('22')
        TWENTYTHREE = '23', _('23')
        TWENTYFOUR = '24', _('24')

    user = models.ForeignKey(
        name = 'user',
        verbose_name = 'Benutzer',
        related_name = 'diagram_user',
        to = get_user_model(),
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    create_user = models.ForeignKey(
        name = 'create_user',
        verbose_name = 'Ersteller',
        related_name = 'diagram_create_user',
        to = get_user_model(),
        on_delete = models.PROTECT,
        editable = False,
        blank = True,
        null = True,
    )

    create_time = models.DateTimeField(
        name = 'create_time',
        verbose_name = 'Erstellungs Zeitpunkt',
        default = timezone.now,
        editable = False,
        blank = False,
        null = False,
    )

    update_user = models.ForeignKey(
        name = 'update_user',
        verbose_name = 'Updater',
        related_name = 'diagram_update_user',
        to = get_user_model(),
        on_delete = models.PROTECT,
        editable = False,
        blank = True,
        null = True,
    )

    update_time = models.DateTimeField(
        name = 'update_time',
        verbose_name = 'Update Zeitpunkt',
        default = timezone.now,
        editable = False,
        blank = False,
        null = False,
    )

    tab = models.ForeignKey(
        name = 'tab',
        verbose_name = 'Tab',
        related_name = 'diagramTab',
        help_text = 'Tab dem diese Itemgruppe zugeordnet ist.',
        to = 'Tab',
        on_delete = models.CASCADE,
        blank = False,
        null = False,
    )

    name = models.CharField(
        name = 'name',
        verbose_name = 'Diagramm',
        help_text = 'Name des angezeigten Diagrams',
        max_length = 255,
        blank = False,
        null = False,
    )

    order = models.IntegerField(
        name = 'order',
        verbose_name = 'Reihenfolge',
        help_text = 'Reihenfolge in der das Diagram angezeigt werden sollen.',
        default = 0,
        blank = True,
        null = False,
    )

    col_xs = models.IntegerField(
        name = 'col_xs',
        verbose_name = 'Spalte xs',
        help_text = 'Darstellung bei einer Bildschirmbreite von weniger als 576px. Maximaler Wert ist 24(100%) und Minimaler Wert 1(100%/24). Es sind nur ganze Zahlen möglich.',
        default = ColumnSpan.TWENTYFOUR,
        choices = ColumnSpan.choices,
        blank = True,
        null = True,
    )

    col_sm = models.IntegerField(
        name = 'col_sm',
        verbose_name = 'Spalte sm',
        help_text = 'Darstellung bei einer Bildschirmbreite von weniger als 768px aber mehr als 576px. Maximaler Wert ist 24(100%) und Minimaler Wert 1(100%/24). Es sind nur ganze Zahlen möglich.',
        default = ColumnSpan.TWENTYFOUR,
        choices = ColumnSpan.choices,
        blank = True,
        null = True,
    )

    col_md = models.IntegerField(
        name = 'col_md',
        verbose_name = 'Spalte md',
        help_text = 'Darstellung bei einer Bildschirmbreite von weniger als 992px aber mehr als 768px. Maximaler Wert ist 24(100%) und Minimaler Wert 1(100%/24). Es sind nur ganze Zahlen möglich.',
        default = ColumnSpan.TWENTYFOUR,
        choices = ColumnSpan.choices,
        blank = True,
        null = True,
    )

    col_lg = models.IntegerField(
        name = 'col_lg',
        verbose_name = 'Spalte lg',
        help_text = 'Darstellung bei einer Bildschirmbreite von weniger als 1200px aber mehr als 992px. Maximaler Wert ist 24(100%) und Minimaler Wert 1(100%/24). Es sind nur ganze Zahlen möglich.',
        default = ColumnSpan.TWENTYFOUR,
        choices = ColumnSpan.choices,
        blank = True,
        null = True,
    )

    col_xl = models.IntegerField(
        name = 'col_xl',
        verbose_name = 'Spalte xl',
        help_text = 'Darstellung bei einer Bildschirmbreite von mehr als 1200px. Maximaler Wert ist 24(100%) und Minimaler Wert 1(100%/24). Es sind nur ganze Zahlen möglich.',
        default = ColumnSpan.TWENTYFOUR,
        choices = ColumnSpan.choices,
        blank = True,
        null = True,
    )

    paddingTop = models.IntegerField(
        name = 'paddingTop',
        verbose_name = 'Padding Oben',
        default = 0,
        blank=False,
    )

    paddingRight = models.IntegerField(
        name = 'paddingRight',
        verbose_name = 'Padding Rechts',
        default = 0,
        blank=False,
    )

    paddingBottom = models.IntegerField(
        name = 'paddingBottom',
        verbose_name = 'Padding Unten',
        default = 0,
        blank=False,
    )

    paddingLeft = models.IntegerField(
        name = 'paddingLeft',
        verbose_name = 'Padding Links',
        default = 0,
        blank=False,
    )

    # Title
    title = models.ForeignKey(
        name = 'title',
        verbose_name = 'Titel',
        related_name = 'diagram_title',
        to = 'Title',
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )

    # Subtitle
    subtitle = models.ForeignKey(
        name = 'subtitle',
        verbose_name = 'Subtitel',
        related_name = 'diagram_subtitle',
        to = 'Subtitle',
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )

    # Legend
    legend = models.ForeignKey(
        name = 'legend',
        verbose_name = 'Legende',
        related_name = 'diagram_legend',
        to = 'Legend',
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )

    def data(self):
        return Graph.objects.filter(diagram=self.id)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Diagramm'
        verbose_name_plural = 'Diagramme'
        ordering = ['tab','order','name']

class Font(models.Model):

    class Family(models.TextChoices):
        ARIAL = '1', _('Arial')
        SANSSERIF = '2', _('sans-serif')
        HELVETICA = '3', _('Helvetica')
        HELVETICANEUE = '4', _('Helvetica Neue')

    class Style(models.TextChoices):
        NORMAL = '1', _('normal')
        ITALIC = '2', _('italic')
        OBLIQUE = '3', _('oblique')

    class Weight(models.TextChoices):
        LIGHTER = '1', _('lighter')
        NORMAL = '2', _('normal')
        BOLD = '3', _('bold')
        BOLDER = '4', _('bolder')

    name = models.CharField(
        name = 'name',
        verbose_name = 'Schrift',
        help_text = 'Name des Schriftstyles.',
        max_length = 255,
        blank = True,
        null = True,
    )

    family = models.CharField(
        name = 'family',
        verbose_name = 'Schriftart',
        help_text = 'Schriftart',
        max_length = 1,
        choices = Family.choices,
        default = Family.ARIAL,
        blank = False,
        null = False,
    )

    style = models.CharField(
        name = 'style',
        verbose_name = 'Style',
        help_text = 'Schriftstyle.',
        max_length = 255,
        choices = Style.choices,
        default = Style.NORMAL,
        blank = False,
        null = False,
    )

    size = models.IntegerField(
        name = 'size',
        verbose_name = 'Größe',
        help_text = 'Schriftgröße in Pixel.',
        default = 12,
        blank = False,
        null = False,
    )

    weight = models.CharField(
        name = 'weight',
        verbose_name = 'Breite',
        help_text = 'Schriftbreite.',
        max_length = 255,
        choices = Style.choices,
        default = Style.NORMAL,
        blank = False,
        null = False,
    )

    lineHeight = models.DecimalField(
        name = 'lineHeight',
        verbose_name = 'Zeilenabstand',
        help_text = 'Zeilenabstand.',
        max_digits=4,
        decimal_places=2,
        default = 1.20,
        blank = False,
        null = False,
    )

    def __str__(self):
        return str(self.Family(self.family).label)+'-'+str(self.Style(self.style).label)+'-'+str(self.size)+'-'+str(self.Weight(self.weight).label)+'-'+str(self.lineHeight)

    class Meta:
        verbose_name = 'Font'
        verbose_name_plural = 'Fonts'

class Color(models.Model):
    name = models.CharField(
        name = 'name',
        verbose_name = 'Farbe',
        help_text = 'Name der Farbe.',
        max_length = 255,
        blank = True,
        null = True,
    )

    red = models.IntegerField(
        name = 'red',
        verbose_name = 'Rot',
        help_text = 'Rot Wert. Minimaler Wert 0. Maximaler Wert 255.',
        default = 0,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    green = models.IntegerField(
        name = 'green',
        verbose_name = 'Grün',
        help_text = 'Grün Wert. Minimaler Wert 0. Maximaler Wert 255.',
        default = 0,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    blue = models.IntegerField(
        name = 'blue',
        verbose_name = 'Blau',
        help_text = 'Blau Wert. Minimaler Wert 0. Maximaler Wert 255.',
        default = 0,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    alpha = models.DecimalField(
        name = 'alpha',
        verbose_name = 'Transparenz Wert',
        help_text = 'Transparenz Wert. Minimaler Wert 0. Maximaler Wert 1.',
        max_digits=3,
        decimal_places=2,
        default = 1.00,
        validators = [
            MinValueValidator(0.00),
            MaxValueValidator(1.00),
        ],
        blank = True,
        null = True,
    )

    def rgba(self):
        return 'rgba('+str(self.red)+','+str(self.green)+','+str(self.blue)+','+str(self.alpha)+')'

    def __str__(self):
        return str(self.name)+'-('+str(self.red)+','+str(self.green)+','+str(self.blue)+','+str(self.alpha)+')'

    class Meta:
        verbose_name = 'Farbe'
        verbose_name_plural = 'Farben'

class Axes(models.Model):

    class Type(models.TextChoices):
        LINEAR = '1', _('linear')
        LOGARITHMIC = '2', _('logarithmic')
        CATEGORY = '3', _('category')
        TIME = '4', _('time')
        TIMESERIES = '5', _('timeseries')
        RADIALLINEAR = '6', _('radialLinear')

    axes_diagram = models.ForeignKey(
        name = 'axes_diagram',
        verbose_name = 'Diagram',
        to = 'Diagram',
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )

    axes_type = models.CharField(
        name = 'axes_type',
        verbose_name = 'Typ',
        help_text = 'Typ der Achse',
        max_length = 255,
        choices = Type.choices,
        default = Type.CATEGORY,
        blank = True,
        null = False,
    )

    axes_display = models.BooleanField(
        name = 'axes_display',
        verbose_name = 'Anzeige',
        help_text = 'Wird die Achse angezeigt Ja / Nein.',
        default = True,
        blank = False,
        null = False,
    )

    axes_backgroundColor = models.ForeignKey(
        name = 'axes_backgroundColor',
        verbose_name = 'Hintergrundfarbe',
        related_name = 'axes_backgroundColor',
        to = 'Color',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    """
    axes_backgroundColorRed = models.IntegerField(
        name = 'axes_backgroundColorRed',
        verbose_name = 'Hintergrund Rot Wert',
        help_text = 'Rot Wert für den Hintergrund der Achse. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    axes_backgroundColorGreen = models.IntegerField(
        name = 'axes_backgroundColorGreen',
        verbose_name = 'Hintergrund Grün Wert',
        help_text = 'Grün Wert für den Hintergrund der Achse. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    axes_backgroundColorBlue = models.IntegerField(
        name = 'axes_backgroundColorBlue',
        verbose_name = 'Hintergrund Blau Wert',
        help_text = 'Blau Wert für den Hintergrund der Achse. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    axes_backgroundColorAlpha = models.FloatField(
        name = 'axes_backgroundColorAlpha',
        verbose_name = 'Hintergrund Transparenz Wert',
        help_text = 'Transparenz Wert für den Hintergrund der Achse. Minimaler Wert 0. Maximaler Wert 1.',
        max_digits=3,
        decimal_places=2,
        default = 1.00,
        validators = [
            MinValueValidator(0.00),
            MaxValueValidator(1.00),
        ],
        blank = True,
        null = True,
    )
    """

    axes_reverse = models.BooleanField(
        name = 'axes_reverse',
        verbose_name = 'Reverse',
        help_text = 'Sollen die Daten Reverse angezeigt werden.',
        default = False,
        blank = False,
        null = False,
    )

    axes_stacked = models.BooleanField(
        name = 'axes_stacked',
        verbose_name = 'Daten Stapeln',
        help_text = 'Sollen die Daten gestapelt werden Ja / Nein.',
        default = False,
        blank = False,
        null = False,
    )

    axes_weight = models.PositiveIntegerField(
        name = 'axes_weight',
        verbose_name = 'Priorität',
        help_text = 'Priorität der Achse. Je höher der Wert desto weiter weg ist die Achse von dem Diagramm.',
        default = 0,
        blank = True,
        null = True,
    )

    axes_min = models.IntegerField(
        name = 'axes_min',
        verbose_name = 'Minimum',
        help_text = 'Minimum der Achse.',
        blank = True,
        null = True,
    )

    axes_max = models.IntegerField(
        name = 'axes_max',
        verbose_name = 'Maximum',
        help_text = 'Maximum der Achse.',
        blank = True,
        null = True,
    )

    axes_suggestedMin = models.IntegerField(
        name = 'axes_suggestedMin',
        verbose_name = 'Geschätztes Minimum',
        help_text = 'Geschätztes Minimum der Achse.',
        blank = True,
        null = True,
    )

    axes_suggestedMax = models.IntegerField(
        name = 'axes_suggestedMax',
        verbose_name = 'Geschätztes Maximum',
        help_text = 'Geschätztes Maximum der Achse.',
        blank = True,
        null = True,
    )

    class Meta:
        verbose_name = 'Achse'
        verbose_name = 'Achsen'

class Label(models.Model):
    label_axes = models.ForeignKey(
        name = 'label_axes',
        verbose_name = 'Achse',
        related_name = 'label_axes',
        to = 'Axes',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    label_display = models.BooleanField(
        name = 'label_display',
        verbose_name = 'Anzeigen',
        help_text = 'Wird das Label angezeigt Ja / Nein.',
        default = True,
        blank = False,
        null = False,
    )

    label_text = models.CharField(
        name = 'label_text',
        verbose_name = 'Text',
        help_text = 'Text der Achsenbeschriftung.',
        max_length = 255,
        blank = True,
        null = True,
    )

    label_font = models.ForeignKey(
        name = 'label_font',
        verbose_name = 'Text Style',
        related_name = 'label_font',
        to = 'Font',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    label_color = models.ForeignKey(
        name = 'label_color',
        verbose_name = 'Textfarbe',
        related_name = 'label_color',
        to = 'Color',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    """
    label_colorRed = models.IntegerField(
        name = 'label_colorRed',
        verbose_name = 'Rot Wert',
        help_text = 'Rot Wert für das Label. Minimaler Wert 0. Maximaler Wert 255.',
        default = 0,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    label_colorGreen = models.IntegerField(
        name = 'label_colorGreen',
        verbose_name = 'Grün Wert',
        help_text = 'Grün Wert für das Label. Minimaler Wert 0. Maximaler Wert 255.',
        default = 0,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    label_colorBlue = models.IntegerField(
        name = 'label_colorBlue',
        verbose_name = 'Blau Wert',
        help_text = 'Blau Wert für das Label. Minimaler Wert 0. Maximaler Wert 255.',
        default = 0,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    label_colorAlpha = models.FloatField(
        name = 'label_colorAlpha',
        verbose_name = 'Transparenz Wert',
        help_text = 'Transparenz Wert für das Label. Minimaler Wert 0. Maximaler Wert 1.',
        max_digits=3,
        decimal_places=2,
        default = 1.00,
        validators = [
            MinValueValidator(0.00),
            MaxValueValidator(1.00),
        ],
        blank = True,
        null = True,
    )
    """

    label_align = models.CharField(
        name = 'label_align',
        verbose_name = 'Align',
        help_text = 'Horizontales Alignment.',
        max_length=255,
        choices = [
            (1,'start'),
            (2,'center'),
            (3,'end'),
        ],
        default = 2,
        blank=False,
        null=False,
    )

    label_padding = models.IntegerField(
        name = 'label_padding',
        verbose_name = 'Padding',
        help_text = 'Abstand des Labels zur Achse.',
        default = 4,
        blank = False,
        null = False,
    )

    class Meta:
        verbose_name = 'Label'
        verbose_name = 'Labels'

class Grid(models.Model):
    label_axes = models.ForeignKey(
        name = 'grid_axes',
        verbose_name = 'Achse',
        related_name = 'grid_axes',
        to = 'Axes',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    grid_z = models.PositiveIntegerField(
        name = 'grid_z',
        verbose_name = 'Z',
        help_text = 'Priorität des Grids. Je höher der Wert desto weiter oben liegt das Grid von dem Diagramm.',
        default = 0,
        blank = True,
        null = True,
    )

    grid_display = models.BooleanField(
        name = 'grid_display',
        verbose_name = 'Anzeigen',
        help_text = 'Wird das Grid angezeigt Ja / Nein.',
        default = True,
        blank = False,
        null = False,
    )

    grid_drawOnChartArea = models.BooleanField(
        name = 'grid_drawOnChartArea',
        verbose_name = 'Grid Linien anzeigen',
        help_text = 'Grid Linien auf dem Diagramm anzeigen Ja / Nein.',
        default = True,
        blank = False,
        null = False,
    )

    grid_lineWidth = models.IntegerField(
        name = 'grid_lineWidth',
        verbose_name = 'Grid Dicke',
        help_text = 'Linien Dicke des Grids.',
        default = 1,
        blank = True,
        null = True,
    )

    grid_color = models.ForeignKey(
        name = 'grid_color',
        verbose_name = 'Gridfarbe',
        related_name = 'grid_color',
        to = 'Color',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    """
    grid_colorRed = models.IntegerField(
        name = 'grid_colorRed',
        verbose_name = 'Grid Rot Wert',
        help_text = 'Rot Wert für das Grid. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    grid_colorGreen = models.IntegerField(
        name = 'grid_colorGreen',
        verbose_name = 'Grid Grün Wert',
        help_text = 'Grün Wert für das Grid. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    grid_colorBlue = models.IntegerField(
        name = 'grid_colorBlue',
        verbose_name = 'Grid Blau Wert',
        help_text = 'Blau Wert für das Grid. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    grid_colorAlpha = models.FloatField(
        name = 'grid_colorAlpha',
        verbose_name = 'Grid Transparenz Wert',
        help_text = 'Transparenz Wert für das Grid. Minimaler Wert 0. Maximaler Wert 1.',
        max_digits=3,
        decimal_places=2,
        default = 1.00,
        validators = [
            MinValueValidator(0.00),
            MaxValueValidator(1.00),
        ],
        blank = True,
        null = True,
    )
    """

    grid_offset = models.BooleanField(
        name = 'grid_offset',
        verbose_name = 'Offset',
        help_text = 'Grid Linien werden zwischen den Tick-Labels angezeigt.',
        default = False,
        blank = False,
        null = False,
    )

    grid_circular = models.BooleanField(
        name = 'grid_circular',
        verbose_name = 'Kreisförmig',
        help_text = 'Grid Linien werden kreisförmig angezeigt.',
        default = False,
        blank = False,
        null = False,
    )

    grid_drawBorder = models.BooleanField(
        name = 'grid_drawBorder',
        verbose_name = 'Border anzeigen',
        help_text = 'Wird Border angezeigt Ja / Nein.',
        default = True,
        blank = False,
        null = False,
    )

    grid_borderColor = models.ForeignKey(
        name = 'grid_borderColor',
        verbose_name = 'Grid Borderfarbe',
        related_name = 'grid_borderColor',
        to = 'Color',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    """
    grid_borderColorRed = models.IntegerField(
        name = 'grid_borderColorRed',
        verbose_name = 'Grid Border Rot Wert',
        help_text = 'Rot Wert für Border des Grids. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    grid_borderColorGreen = models.IntegerField(
        name = 'grid_borderColorGreen',
        verbose_name = 'Grid Border Grün Wert',
        help_text = 'Grün Wert für Border des Grids. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    grid_borderColorBlue = models.IntegerField(
        name = 'grid_borderColorBlue',
        verbose_name = 'Grid Border Blau Wert',
        help_text = 'Blau Wert für Border des Grids. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    grid_borderColorAlpha = models.FloatField(
        name = 'grid_borderColorAlpha',
        verbose_name = 'Grid Border Transparenz Wert',
        help_text = 'Transparenz Wert für Border des Grids. Minimaler Wert 0. Maximaler Wert 1.',
        max_digits=3,
        decimal_places=2,
        default = 1.00,
        validators = [
            MinValueValidator(0.00),
            MaxValueValidator(1.00),
        ],
        blank = True,
        null = True,
    )
    """

    grid_borderDash = models.CharField(
        name = 'grid_borderDash',
        verbose_name = 'Border Dash',
        help_text = 'Länge und Abstand der Striche. [Länge des Striches,Länge der Lücke] -> Bsp.: [5,10]',
        max_length = 255,
        default = '[]',
        blank = True,
        null = True,
    )

    grid_borderDashOffset = models.IntegerField(
        name = 'grid_borderDashOffset',
        verbose_name = 'Border Dash Offset',
        help_text = 'Border Dash Offset.',
        default = 0,
        blank = True,
        null = True,
    )

    grid_drawTickLines = models.BooleanField(
        name = 'grid_drawTickLines',
        verbose_name = 'Tick-Linien anzeigen',
        help_text = 'Tick-Linien auf dem Diagramm anzeigen Ja / Nein.',
        default = True,
        blank = False,
        null = False,
    )

    grid_tickColor = models.ForeignKey(
        name = 'grid_tickColor',
        verbose_name = 'Grid Tickfarbe',
        related_name = 'grid_tickColor',
        to = 'Color',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    """
    grid_tickColorRed = models.IntegerField(
        name = 'grid_tickColorRed',
        verbose_name = 'Tick Rot Wert',
        help_text = 'Rot Wert für die Ticks des Grids. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    grid_tickColorGreen = models.IntegerField(
        name = 'grid_tickColorGreen',
        verbose_name = 'Tick Grün Wert',
        help_text = 'Grün Wert für die Ticks des Grids. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    grid_tickColorBlue = models.IntegerField(
        name = 'grid_tickColorBlue',
        verbose_name = 'Tick Blau Wert',
        help_text = 'Blau Wert für die Ticks des Grids. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    grid_tickColorAlpha = models.FloatField(
        name = 'grid_tickColorAlpha',
        verbose_name = 'Tick Transparenz Wert',
        help_text = 'Transparenz Wert für die Ticks des Grids. Minimaler Wert 0. Maximaler Wert 1.',
        max_digits=3,
        decimal_places=2,
        default = 1.00,
        validators = [
            MinValueValidator(0.00),
            MaxValueValidator(1.00),
        ],
        blank = True,
        null = True,
    )
    """

    grid_tickLength = models.IntegerField(
        name = 'grid_tickLength',
        verbose_name = 'Länge der Ticks',
        help_text = 'Länge der Ticks in Pixel.',
        default = 8,
        blank = True,
        null = True,
    )

    grid_tickWidth = models.IntegerField(
        name = 'grid_tickWidth',
        verbose_name = 'Breite der Ticks',
        help_text = 'Breite der Ticks in Pixel.',
        default = 1,
        blank = True,
        null = True,
    )

    grid_tickBorderDash = models.CharField(
        name = 'grid_tickBorderDash',
        verbose_name = 'Tick Border Dash',
        help_text = 'Länge und Abstand der Striche. [Länge des Striches,Länge der Lücke] -> Bsp.: [5,10]',
        max_length = 255,
        default = '[]',
        blank = True,
        null = True,
    )

    grid_tickBorderDashOffset = models.IntegerField(
        name = 'grid_tickBorderDashOffset',
        verbose_name = 'Tick Border Dash Offset',
        help_text = 'Tick Border Dash Offset.',
        default = 0,
        blank = True,
        null = True,
    )

    class Meta:
        verbose_name = 'Grid'
        verbose_name = 'Grids'

class Tick(models.Model):

    tick_axes = models.ForeignKey(
        name = 'tick_axes',
        verbose_name = 'Achse',
        related_name = 'tick_axes',
        to = 'Axes',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    tick_display = models.BooleanField(
        name = 'tick_display',
        verbose_name = 'Anzeigen',
        help_text = 'Werden die Ticks angezeigt Ja / Nein.',
        default = True,
        blank = False,
        null = False,
    )

    tick_font = models.ForeignKey(
        name = 'tick_font',
        verbose_name = 'Tick Text Style',
        related_name = 'tick_font',
        to = 'Font',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    tick_color = models.ForeignKey(
        name = 'tick_color',
        verbose_name = 'Tickfarbe',
        related_name = 'tick_color',
        to = 'Color',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    """
    tick_colorRed = models.IntegerField(
        name = 'tick_colorRed',
        verbose_name = 'Tick Rot Wert',
        help_text = 'Rot Wert für die Ticks. Minimaler Wert 0. Maximaler Wert 255.',
        default = 0,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    tick_colorGreen = models.IntegerField(
        name = 'tick_colorGreen',
        verbose_name = 'Tick Grün Wert',
        help_text = 'Grün Wert für die Ticks. Minimaler Wert 0. Maximaler Wert 255.',
        default = 0,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    tick_colorBlue = models.IntegerField(
        name = 'tick_colorBlue',
        verbose_name = 'Tick Blau Wert',
        help_text = 'Blau Wert für die Ticks. Minimaler Wert 0. Maximaler Wert 255.',
        default = 0,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    tick_colorAlpha = models.FloatField(
        name = 'tick_colorAlpha',
        verbose_name = 'Tick Transparenz Wert',
        help_text = 'Transparenz Wert für die Ticks. Minimaler Wert 0. Maximaler Wert 1.',
        max_digits=3,
        decimal_places=2,
        default = 1.00,
        validators = [
            MinValueValidator(0.00),
            MaxValueValidator(1.00),
        ],
        blank = True,
        null = True,
    )
    """

    tick_padding = models.IntegerField(
        name = 'tick_padding',
        verbose_name = 'Tick Padding',
        help_text = 'Abstand der Ticks zur Achse.',
        default = 3,
        blank = False,
        null = False,
    )

    tick_z = models.PositiveIntegerField(
        name = 'tick_z',
        verbose_name = 'Tick Z',
        help_text = 'Priorität der Ticks. Je höher der Wert desto weiter oben liegen die Ticks von dem Diagramm.',
        default = 0,
        blank = True,
        null = True,
    )

    tick_textStrokeColor = models.ForeignKey(
        name = 'tick_textStrokeColor',
        verbose_name = 'Text Strokefarbe',
        related_name = 'tick_textStrokeColor',
        to = 'Color',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    """
    tick_textStrokeColorRed = models.IntegerField(
        name = 'tick_textStrokeColorRed',
        verbose_name = 'Text Stroke Rot Wert',
        help_text = 'Rot Wert für den Text Stroke. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    tick_textStrokeColorGreen = models.IntegerField(
        name = 'tick_textStrokeColorGreen',
        verbose_name = 'Text Stroke Grün Wert',
        help_text = 'Grün Wert für den Text Stroke. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    tick_textStrokeColorBlue = models.IntegerField(
        name = 'tick_textStrokeColorBlue',
        verbose_name = 'Text Stroke Blau Wert',
        help_text = 'Blau Wert für den Text Stroke. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    tick_textStrokeColorAlpha = models.FloatField(
        name = 'tick_textStrokeColorAlpha',
        verbose_name = 'Text Stroke Transparenz Wert',
        help_text = 'Transparenz Wert für den Text Stroke. Minimaler Wert 0. Maximaler Wert 1.',
        max_digits=3,
        decimal_places=2,
        default = 1.00,
        validators = [
            MinValueValidator(0.00),
            MaxValueValidator(1.00),
        ],
        blank = True,
        null = True,
    )
    """

    tick_textStrokeWidth = models.IntegerField(
        name = 'tick_textStrokeWidth',
        verbose_name = 'Text Stroke Breite',
        help_text = 'Breite des Text Stroke.',
        default = 0,
        blank = True,
        null = True,
    )

    tick_backdropDisplay = models.BooleanField(
        name = 'tick_backdropDisplay',
        verbose_name = 'Backdrop anzeigen',
        help_text = 'Werden die Backdrops angezeigt Ja / Nein.',
        default = False,
        blank = False,
        null = False,
    )

    tick_backdropColor = models.ForeignKey(
        name = 'tick_backdropColor',
        verbose_name = 'Backdropfarbe',
        related_name = 'tick_backdropColor',
        to = 'Color',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    """
    tick_backdropColorRed = models.IntegerField(
        name = 'tick_backdropColorRed',
        verbose_name = 'Backdrop Rot Wert',
        help_text = 'Rot Wert für den Backdrop. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    tick_backdropColorGreen = models.IntegerField(
        name = 'tick_backdropColorGreen',
        verbose_name = 'Backdrop Grün Wert',
        help_text = 'Grün Wert für den Backdrop. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    tick_backdropColorBlue = models.IntegerField(
        name = 'tick_backdropColorBlue',
        verbose_name = 'Backdrop Blau Wert',
        help_text = 'Blau Wert für den Backdrop. Minimaler Wert 0. Maximaler Wert 255.',
        default = 255,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(255),
        ],
        blank = True,
        null = True,
    )

    tick_backdropColorAlpha = models.FloatField(
        name = 'tick_backdropColorAlpha',
        verbose_name = 'Backdrop Transparenz Wert',
        help_text = 'Transparenz Wert für den Backdrop. Minimaler Wert 0. Maximaler Wert 1.',
        max_digits=3,
        decimal_places=2,
        default = 1.00,
        validators = [
            MinValueValidator(0.00),
            MaxValueValidator(1.00),
        ],
        blank = True,
        null = True,
    )
    """

    tick_backdropPadding = models.IntegerField(
        name = 'tick_backdropPadding',
        verbose_name = 'Backdrop Padding',
        help_text = 'Abstand der Backdrops.',
        default = 2,
        blank = False,
        null = False,
    )

    class Meta:
        verbose_name = 'Tick'
        verbose_name = 'Ticks'

class Title(models.Model):

    class Position(models.TextChoices):
        TOP = '1', _('top')
        RIGHT = '2', _('right')
        BOTTOM = '3', _('bottom')
        LEFT = '4', _('left')

    class Align(models.TextChoices):
        START = '1', _('start')
        CENTER = '2', _('center')
        END = '3', _('end')

    display = models.BooleanField(
        name = 'display',
        verbose_name = 'Anzeigen',
        help_text = 'Titel wird angezeigt.',
        default = False,
        blank = False,
        null = False,
    )

    text = models.CharField(
        name = 'text',
        verbose_name = 'Text',
        help_text = 'Text des Titels.',
        max_length = 255,
        blank = True,
        null = True,
    )

    font = models.ForeignKey(
        name = 'font',
        verbose_name = 'Schrift Style',
        related_name = 'title_font',
        to = 'Font',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    color = models.ForeignKey(
        name = 'color',
        verbose_name = 'Farbe',
        related_name = 'title_color',
        to = 'Color',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    position = models.CharField(
        name = 'position',
        verbose_name = 'Position',
        help_text = 'Position des Titels innerhalb des Diagramms.',
        max_length=1,
        choices = Position.choices,
        default = Position.TOP,
        blank=False,
        null=False,
    )

    align = models.CharField(
        name = 'align',
        verbose_name = 'Align',
        help_text = 'Alignment des Titels.',
        max_length = 1,
        choices = Align.choices,
        default = Align.CENTER,
        blank = False,
        null = False,
    )

    paddingTop = models.IntegerField(
        name = 'paddingTop',
        verbose_name = 'Padding Top',
        default = 10,
        blank=False,
        null=False,
    )

    paddingRight = models.IntegerField(
        name = 'paddingRight',
        verbose_name = 'Padding Right',
        default = 10,
        blank=False,
        null=False,
    )

    paddingBottom = models.IntegerField(
        name = 'paddingBottom',
        verbose_name = 'Padding Bottom',
        default = 10,
        blank=False,
        null=False,
    )

    paddingLeft = models.IntegerField(
        name = 'paddingLeft',
        verbose_name = 'Padding Left',
        default = 10,
        blank=False,
        null=False,
    )

    fullSize = models.BooleanField(
        name = 'fullSize',
        verbose_name = 'Im Diagramm?',
        help_text = 'Titel wird innerhalb des Diagramms angezeigt.',
        default = True,
        blank = False,
        null = False,
    )

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'Titel'
        verbose_name_plural = 'Titel'

class Subtitle(models.Model):
    class Position(models.TextChoices):
        TOP = '1', _('top')
        RIGHT = '2', _('right')
        BOTTOM = '3', _('bottom')
        LEFT = '4', _('left')

    class Align(models.TextChoices):
        START = '1', _('start')
        CENTER = '2', _('center')
        END = '3', _('end')

    display = models.BooleanField(
        name = 'display',
        verbose_name = 'Anzeigen',
        help_text = 'Titel wird angezeigt.',
        default = False,
        blank = False,
        null = False,
    )

    text = models.CharField(
        name = 'text',
        verbose_name = 'Text',
        help_text = 'Text des Titels.',
        max_length = 255,
        blank = True,
        null = True,
    )

    font = models.ForeignKey(
        name = 'font',
        verbose_name = 'Schrift Style',
        related_name = 'subtitle_font',
        to = 'Font',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    color = models.ForeignKey(
        name = 'color',
        verbose_name = 'Farbe',
        related_name = 'subtitle_color',
        to = 'Color',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    position = models.CharField(
        name = 'position',
        verbose_name = 'Position',
        help_text = 'Position des Titels innerhalb des Diagramms.',
        max_length=1,
        choices = Position.choices,
        default = Position.TOP,
        blank=False,
        null=False,
    )

    align = models.CharField(
        name = 'align',
        verbose_name = 'Align',
        help_text = 'Alignment des Titels.',
        max_length = 1,
        choices = Align.choices,
        default = Align.CENTER,
        blank = False,
        null = False,
    )

    paddingTop = models.IntegerField(
        name = 'paddingTop',
        verbose_name = 'Padding Top',
        default = 10,
        blank=False,
        null=False,
    )

    paddingRight = models.IntegerField(
        name = 'paddingRight',
        verbose_name = 'Padding Right',
        default = 10,
        blank=False,
        null=False,
    )

    paddingBottom = models.IntegerField(
        name = 'paddingBottom',
        verbose_name = 'Padding Bottom',
        default = 10,
        blank=False,
        null=False,
    )

    paddingLeft = models.IntegerField(
        name = 'paddingLeft',
        verbose_name = 'Padding Left',
        default = 10,
        blank=False,
        null=False,
    )

    fullSize = models.BooleanField(
        name = 'fullSize',
        verbose_name = 'Im Diagramm?',
        help_text = 'Titel wird innerhalb des Diagramms angezeigt.',
        default = True,
        blank = False,
        null = False,
    )

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'Untertitel'
        verbose_name_plural = 'Untertitel'

class Legend(models.Model):
    class Position(models.TextChoices):
        TOP = '1', _('top')
        RIGHT = '2', _('right')
        BOTTOM = '3', _('bottom')
        LEFT = '4', _('left')

    class Align(models.TextChoices):
        START = '1', _('start')
        CENTER = '2', _('center')
        END = '3', _('end')

    class Style(models.TextChoices):
        CIRCLE = '1', _('circle')
        CROSS = '2', _('cross')
        CROSSROT = '3', _('crossRot')
        DASH = '4', _('dash')
        LINE = '5', _('line')
        RECT = '6', _('rect')
        RECTROUNDED = '7', _('rectRounded')
        RECTROT = '8', _('rectRot')
        STAR = '9', _('star')
        TRIANGLE = '10', _('triangle')

    class TextAlign(models.TextChoices):
        LEFT = '1', _('left')
        CENTER = '2', _('center')
        RIGHT = '3', _('right')
    
    display = models.BooleanField(
        name = 'display',
        verbose_name = 'Anzeigen',
        default = False,
        blank = False,
        null = False,
    )

    position = models.CharField(
        name = 'position',
        verbose_name = 'Position',
        max_length = 1,
        choices = Position.choices,
        default = Position.TOP,
        blank=False,
        null=False,
    )

    align = models.CharField(
        name = 'align',
        verbose_name = 'Align',
        max_length = 1,
        choices = Align.choices,
        default = Align.CENTER,
        blank=False,
        null=False,
    )

    fullSize = models.BooleanField(
        name = 'fullSize',
        verbose_name = 'Größenverhältnis',
        default = True,
        blank = False,
        null = False,
    )

    reverse = models.BooleanField(
        name = 'reverse',
        verbose_name = 'Reverse Anzeige',
        default = False,
        blank = False,
        null = False,
    )

    maxHeight = models.IntegerField(
        name = 'maxHeight',
        verbose_name = 'Maximale Höhe',
        help_text = 'Maximale Höhe der Legende in Pixel.',
        blank = True,
        null = True,
    )

    maxWidth = models.IntegerField(
        name = 'maxWidth',
        verbose_name = 'Maximale Breite',
        help_text = 'Maximale Breite der Legende in Pixel.',
        blank = True,
        null = True,
    )

    title_text = models.CharField(
        name = 'title_text',
        verbose_name = 'Text',
        help_text = 'Text des Titels der Legende.',
        max_length = 255,
        blank = True,
        null = True,
    )

    title_display = models.BooleanField(
        name = 'title_display',
        verbose_name = 'Anzeigen',
        default = False,
        blank = False,
        null = False,
    )

    title_font = models.ForeignKey(
        name = 'title_font',
        verbose_name = 'Schrift Style',
        related_name = 'legend_titleFont',
        to = 'Font',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    title_color = models.ForeignKey(
        name = 'title_color',
        verbose_name = 'Farbe',
        related_name = 'legend_titleColor',
        to = 'Color',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    title_paddingTop = models.IntegerField(
        name = 'title_paddingTop',
        verbose_name = 'Padding Top',
        default = 0,
        blank=False,
        null=False,
    )

    title_paddingRight = models.IntegerField(
        name = 'title_paddingRight',
        verbose_name = 'Padding Right',
        default = 0,
        blank=False,
        null=False,
    )

    title_paddingBottom = models.IntegerField(
        name = 'title_paddingBottom',
        verbose_name = 'Padding Bottom',
        default = 0,
        blank=False,
        null=False,
    )

    title_paddingLeft = models.IntegerField(
        name = 'title_paddingLeft',
        verbose_name = 'Padding Left',
        default = 0,
        blank=False,
        null=False,
    )

    label_font = models.ForeignKey(
        name = 'label_font',
        verbose_name = 'Schrift Style',
        related_name = 'legend_labelFont',
        to = 'Font',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    label_color = models.ForeignKey(
        name = 'label_color',
        verbose_name = 'Farbe',
        related_name = 'legend_labelColor',
        to = 'Color',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    boxWidth = models.IntegerField(
        name = 'boxWidth',
        verbose_name = 'Box Breite',
        help_text = 'Box Breite in Pixel.',
        default = 40,
        blank = True,
        null = True,
    )

    boxHeight = models.IntegerField(
        name = 'boxHeight',
        verbose_name = 'Box Höhe',
        help_text = 'Box Höhe in Pixel.',
        blank = True,
        null = True,
    )

    label_paddingTop = models.IntegerField(
        name = 'label_paddingTop',
        verbose_name = 'Padding Top',
        default = 10,
        blank=False,
        null=False,
    )

    label_paddingRight = models.IntegerField(
        name = 'label_paddingRight',
        verbose_name = 'Padding Right',
        default = 10,
        blank=False,
        null=False,
    )

    label_paddingBottom = models.IntegerField(
        name = 'label_paddingBottom',
        verbose_name = 'Padding Bottom',
        default = 10,
        blank=False,
        null=False,
    )

    label_paddingLeft = models.IntegerField(
        name = 'label_paddingLeft',
        verbose_name = 'Padding Left',
        default = 10,
        blank=False,
        null=False,
    )

    label_pointStyle = models.CharField(
        name = 'label_pointStyle',
        verbose_name = 'Point Style',
        max_length = 2,
        choices = Style.choices,
        default = Style.CIRCLE,
        blank=False,
        null=False,
    )

    label_usePointStyle = models.BooleanField(
        name = 'label_usePointStyle',
        verbose_name = 'Point Style',
        help_text = 'Point Style benutzen?',
        default = False,
        blank = False,
        null = False,
    )

    label_align = models.CharField(
        name = 'label_align',
        verbose_name = 'Align',
        max_length = 1,
        choices = TextAlign.choices,
        default = TextAlign.CENTER,
        blank=False,
        null=False,
    )

    def __str__(self):
        return str(self.title_text) + ' ' + str(self.id)

    class Meta:
        verbose_name = 'Legende'
        verbose_name_plural = 'Legenden'

class Graph(models.Model):
    graphDiagram = models.ForeignKey(
        name = 'diagram',
        verbose_name = 'Diagram',
        to = 'Diagram',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    name = models.CharField(
        name = 'name',
        verbose_name = 'Label',
        max_length=255,
        blank=True,
        null=True,
    )

    order = models.IntegerField(
        name = 'order',
        verbose_name = 'Reihenfolge',
        default = 1,
        blank=True,
        null=True,
    )

    graphType = models.CharField(
        name = 'graphType',
        verbose_name = 'Data Typ',
        max_length=255,
        choices = [
            ('line','line'),
            ('bar','bar'),
            ('radar','radar'),
            ('pie','pie'),
            ('doughnut','doughnut'),
            ('polarArea','polarArea'),
            ('bubble','bubble'),
            ('scatter','scatter'),
        ],
        default = 'scatter',
        blank=True,
        null=False,
    )

    graphURL = models.CharField(
        name = 'graphURL',
        verbose_name = 'URL',
        max_length=255,
        blank=True,
        null=True,
    )

    graphXData = models.CharField(
        name = 'graphXData',
        verbose_name = 'X Daten',
        max_length=255,
        blank=True,
        null=True,
    )

    graphYData = models.CharField(
        name = 'graphYData',
        verbose_name = 'Y Daten',
        max_length=255,
        blank=True,
        null=True,
    )

    graphPointBackgroundColorRed = models.IntegerField(
        name = 'graphPointBackgroundColorRed',
        verbose_name = 'Rot',
        default = 0,
        blank=True,
        null=False,
    )

    graphPointBackgroundColorGreen = models.IntegerField(
        name = 'graphPointBackgroundColorGreen',
        verbose_name = 'Grün',
        default = 0,
        blank=True,
        null=False,
    )

    graphPointBackgroundColorBlue = models.IntegerField(
        name = 'graphPointBackgroundColorBlue',
        verbose_name = 'Blau',
        default = 0,
        blank=True,
        null=False,
    )

    graphPointBackgroundColorAlpha = models.CharField(
        name = 'graphPointBackgroundColorAlpha',
        verbose_name = 'Alpha',
        max_length=255,
        default = 1,
        blank=True,
        null=False,
    )

    graphPointBorderColorRed = models.IntegerField(
        name = 'graphPointBorderColorRed',
        verbose_name = 'Rot',
        default = 0,
        blank=True,
        null=False,
    )

    graphPointBorderColorGreen = models.IntegerField(
        name = 'graphPointBorderColorGreen',
        verbose_name = 'Grün',
        default = 0,
        blank=True,
        null=False,
    )

    graphPointBorderColorBlue = models.IntegerField(
        name = 'graphPointBorderColorBlue',
        verbose_name = 'Blau',
        default = 0,
        blank=True,
        null=False,
    )

    graphPointBorderColorAlpha = models.CharField(
        name = 'graphPointBorderColorAlpha',
        verbose_name = 'Alpha',
        max_length=255,
        default = 1,
        blank=True,
        null=False,
    )

    graphPointBorderWidth = models.IntegerField(
        name = 'graphPointBorderWidth',
        verbose_name = 'Rahmenbreite',
        default = 1,
        blank=True,
        null=False,
    )

    graphPointHitRadius = models.IntegerField(
        name = 'graphPointHitRadius',
        verbose_name = 'Hitpoint Radius',
        default = 1,
        blank=True,
        null=False,
    )

    graphPointRadius = models.IntegerField(
        name = 'graphPointRadius',
        verbose_name = 'Radius',
        default = 10,
        blank=True,
        null=False,
    )

    graphPointStyle = models.CharField(
        name = 'graphPointStyle',
        verbose_name = 'Style',
        max_length = 255,
        choices = [
            ('circle','circle'),
            ('cross','cross'),
            ('crossRot','crossRot'),
            ('dash','dash'),
            ('line','line'),
            ('rect','rect'),
            ('rectRounded','rectRounded'),
            ('rectRot','rectRot'),
            ('star','star'),
            ('triangle','triangle'),
        ],
        default = 'circle',
        blank=True,
        null=False,
    )

    graphBackgroundColorRed = models.IntegerField(
        name = 'graphBackgroundColorRed',
        verbose_name = 'Rot',
        default = 0,
        blank=True,
        null=False,
    )

    graphBackgroundColorGreen = models.IntegerField(
        name = 'graphBackgroundColorGreen',
        verbose_name = 'Grün',
        default = 0,
        blank=True,
        null=False,
    )

    graphBackgroundColorBlue = models.IntegerField(
        name = 'graphBackgroundColorBlue',
        verbose_name = 'Blau',
        default = 0,
        blank=True,
        null=False,
    )

    graphBackgroundColorAlpha = models.CharField(
        name = 'graphBackgroundColorAlpha',
        verbose_name = 'Alpha',
        max_length=255,
        default = 1,
        blank=True,
        null=False,
    )

    graphBorderColorRed = models.IntegerField(
        name = 'graphBorderColorRed',
        verbose_name = 'Rot',
        default = 0,
        blank=True,
        null=False,
    )

    graphBorderColorGreen = models.IntegerField(
        name = 'graphBorderColorGreen',
        verbose_name = 'Grün',
        default = 0,
        blank=True,
        null=False,
    )

    graphBorderColorBlue = models.IntegerField(
        name = 'graphBorderColorBlue',
        verbose_name = 'Blau',
        default = 0,
        blank=True,
        null=False,
    )

    graphBorderColorAlpha = models.CharField(
        name = 'graphBorderColorAlpha',
        verbose_name = 'Alpha',
        max_length=255,
        default = 1,
        blank=True,
        null=False,
    )

    graphBorderWidth = models.IntegerField(
        name = 'graphBorderWidth',
        verbose_name = 'Rahmenbreite',
        default = 1,
        blank=True,
        null=False,
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Diagramm Data'
        verbose_name_plural = 'Diagramm Daten'
        ordering = ['diagram','order','name']