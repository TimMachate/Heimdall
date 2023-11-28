from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Table(models.Model):

    class ColumnSpan(models.IntegerChoices):
        ONE = 1, _('1')
        TWO = 2, _('2')
        THREE = 3, _('3')
        FOUR = 4, _('4')
        FIVE = 5, _('5')
        SIX = 6, _('6')
        SEVEN = 7, _('7')
        EIGHT = 8, _('8')
        NINE = 9, _('9')
        TEN = 10, _('10')
        ELEVEN = 11, _('11')
        TWELVE = 12, _('12')
        THIRTEEN = 13, _('13')
        FOURTEEN = 14, _('14')
        FIFTEEN = 15, _('15')
        SIXTEEN = 16, _('16')
        SEVENTEEN = 17, _('17')
        EIGHTEEN = 18, _('18')
        NINETEEN = 19, _('19')
        TWENTY = 20, _('20')
        TWENTYONE = 21, _('21')
        TWENTYTWO = 22, _('22')
        TWENTYTHREE = 23, _('23')
        TWENTYFOUR = 24, _('24')

    create_user = models.ForeignKey(
        name = 'create_user',
        verbose_name = 'Ersteller',
        related_name = 'table_create_user',
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
        related_name = 'table_update_user',
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
        related_name = 'tableTab',
        help_text = 'Tab dem diese Itemgruppe zugeordnet ist.',
        to = 'Tab',
        on_delete = models.CASCADE,
        blank = False,
        null = False,
    )

    name = models.CharField(
        name = 'name',
        verbose_name = 'Tabelle',
        help_text = 'Name der angezeigten Tabelle',
        max_length = 255,
        blank = False,
        null = False,
    )

    order = models.IntegerField(
        name = 'order',
        verbose_name = 'Reihenfolge',
        help_text = 'Reihenfolge in der die Tabelle angezeigt werden sollen.',
        default = 0,
        blank = True,
        null = False,
    )

    dataURL = models.CharField(
        name = 'dataURL',
        verbose_name = 'URL',
        help_text = 'API Url in der die anzuzeigende Information enthalten ist.',
        max_length = 255,
        blank = False,
        null = False,
    )

    time = models.IntegerField(
        name = 'time',
        verbose_name = 'Zeit',
        help_text = 'Zeit der Aktualisierungsintervalle in Sekunden.',
        blank = True,
        null = True,
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

    rowspan = models.IntegerField(
        name = 'rowspan',
        verbose_name = 'Reihen',
        help_text = 'Anzahl der Reihen.',
        default = 1,
        blank = True,
        null = True,
    )

    def get_absolute_url(self):
        return reverse('Visualisation:table_detail',kwargs={'id':self.id})
    
    def get_absolute_url_delete(self):
        return reverse('Visualisation:table_delete',kwargs={'id':self.id})

    def get_absolute_url_create(self):
        return reverse('Visualisation:table_create',kwargs={'id':self.id})

    def tableItem(self):
        return TableItem.objects.filter(table=self.id)

    def __str__(self):
        return str(self.name) + ' - ' + str(self.tab.name)

    class Meta:
        verbose_name = 'Tabelle'
        verbose_name_plural = 'Tabellen'
        app_label = "visualisation"
        ordering = ['tab','order','name']

class TableItem(models.Model):

    class HALIGN(models.TextChoices):
        LEFT = '1', _('left')
        CENTER = '2', _('center')
        RIGHT = '3', _('right')

    class VALIGN(models.TextChoices):
        TOP = '1', _('top')
        MIDDLE = '2', _('middle')
        BOTTOM = '3', _('bottom')

    table = models.ForeignKey(
        name = 'table',
        verbose_name = 'Tabelle',
        to = 'Table',
        on_delete = models.CASCADE,
    )

    name = models.CharField(
        name = 'name',
        verbose_name = 'Item',
        help_text = 'Name des angezeigten Items',
        max_length = 255,
        blank = False,
        null = False,
    )

    order = models.IntegerField(
        name = 'order',
        verbose_name = 'Item Reihenfolge',
        help_text = 'Reihenfolge in der das Item dargestellt wurde.',
        default = 0,
        blank = True,
        null = False,
    )

    itemData = models.CharField(
        name = 'itemData',
        verbose_name = 'Item Daten',
        help_text = 'Key der Information das aus den Daten angezeigt werden soll.',
        max_length = 255,
        blank = False,
        null = False,
    )

    col_width = models.IntegerField(
        name = 'col_width',
        verbose_name = 'Spaltenbreite',
        help_text = 'Spaltenbreite in px',
        blank = True,
        null = True,
    )

    halign = models.CharField(
        name = 'hAlign',
        verbose_name = 'h. Align',
        help_text = 'Horizontal Align.',
        max_length = 255,
        default = HALIGN.LEFT,
        choices = HALIGN.choices,
        blank = True,
        null = True,
    )

    valign = models.CharField(
        name = 'vAlign',
        verbose_name = 'v. Align',
        help_text = 'Vertical Align.',
        max_length = 255,
        default = VALIGN.TOP,
        choices = VALIGN.choices,
        blank = True,
        null = True,
    )

    def get_absolute_url(self):
        return reverse('Visualisation:tableitem_detail',kwargs={'id':self.id})

    def get_absolute_url_delete(self):
        return reverse('Visualisation:tableitem_delete',kwargs={'id':self.id})

    def get_absolute_url_create(self):
        return reverse('Visualisation:tableitem_create',kwargs={'id':self.id})

    def __str__(self):
        return str(self.name) + '-' + str(self.table.name) + '-' + str(self.table.tab.name)

    class Meta:
        verbose_name = 'Tabellen Data'
        verbose_name_plural = 'Tabellen Daten'
        app_label = 'visualisation'
        ordering = ['table','order','name',]