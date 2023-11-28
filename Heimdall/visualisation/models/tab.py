from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from itertools import chain

from .item import ItemGroup
from .item import Item
from .table import Table
from .diagram import Diagram

class Tab(models.Model):

    user = models.ForeignKey(
        name = 'user',
        verbose_name = 'Benutzer',
        related_name = 'tab_user',
        to = get_user_model(),
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    create_user = models.ForeignKey(
        name = 'create_user',
        verbose_name = 'Ersteller',
        related_name = 'tab_create_user',
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
        related_name = 'tab_update_user',
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

    slug = models.SlugField(
        name = 'slug',
        verbose_name = 'Slug',
        editable = False,
        blank = True,
        null = True,
    )

    name = models.CharField(
        name = 'name',
        verbose_name = 'Tab',
        help_text = 'Name des Tabs in dem die Items angezeigt werden sollen.',
        max_length = 200,
        blank = False,
        null = False,
    )

    order = models.IntegerField(
        name = 'order',
        verbose_name = 'Tab-Reihenfolge',
        help_text = 'Reihenfolge in der die Tabs angezeigt werden sollen.',
        blank = True,
        null = True,
    )

    def get_absolute_url(self):
        return reverse('Visualisation:tab_detail',kwargs={'id':self.id})

    def get_absolute_url_delete(self):
        return reverse('Visualisation:tab_delete',kwargs={'id':self.id})

    def get_absolute_url_create(self):
        return reverse('Visualisation:tab_create',kwargs={'id':self.id})

    def get_all(self):
        queries = sorted(chain(
            ItemGroup.objects.filter(tab = self.id),
            Table.objects.filter(tab = self.id),
            Diagram.objects.filter(tab = self.id),
            ),key=lambda instance: instance.order)
        return queries

    def itemgroup(self):
        return ItemGroup.objects.filter(tab=self.id)

    def itemgroup_count(self):
        return self.itemgroup().count()

    def item(self):
        ITEMGROUP = []
        for i in ItemGroup.objects.filter(tab=self.id):
            ITEMGROUP.append(i.id)
        return Item.objects.filter(itemGroup__in=ITEMGROUP)

    def item_count(self):
        return self.item().count()
    
    def table(self):
        return Table.objects.filter(tab=self.id)

    def table_count(self):
        return self.table().count()
    
    def diagram(self):
        return Diagram.objects.filter(tab=self.id)

    def diagram_count(self):
        return self.diagram().count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save()

    def __str__(self):
        return str(self.user.username)+ '-' +str(self.name)

    class Meta:
        verbose_name = 'Tab'
        verbose_name_plural = 'Tabs'
        app_label = 'visualisation'
        ordering = ['user', 'order', 'name']
        unique_together = ['user', 'name']