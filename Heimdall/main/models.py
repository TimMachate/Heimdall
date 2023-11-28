from tabnanny import verbose
from django.db import models

# Create your models here.
class NavigationbarItem(models.Model):
    label = models.CharField(
        name = 'name',
        verbose_name = 'Name',
        max_length = 200,
        blank = False,
        null = False,
    )

    order = models.IntegerField(
        name = 'order',
        verbose_name = 'Reihenfolge',
        blank = True,
        null = True,
        )

    link = models.CharField(
        name = 'link',
        verbose_name = 'Link',
        max_length = 200,
        default = '#',
        blank = False,
        null = False,
    )

    def get_menuItems(self):
        return MenuItem.objects.filter(navigationbarItem = self.id)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Navigationbar'
        verbose_name_plural = 'Navigationbar'

class MenuItem(models.Model):
    navigationbaritem = models.ForeignKey(
        name = 'navigationbarItem',
        verbose_name = 'Menu Item',
        related_name='menuItemNavigationbarItem',
        help_text = 'Navigationbar Item in der das Menu Item angezeigt werden soll.',
        to = 'NavigationbarItem',
        on_delete = models.CASCADE,
        blank = False,
        null = False,
    )

    label = models.CharField(
        name = 'name',
        verbose_name = 'Name',
        max_length = 200,
        blank = False,
        null = False,
    )

    order = models.IntegerField(
        name = 'order',
        verbose_name = 'Reihenfolge',
        blank = True,
        null = True,
        )

    link = models.CharField(
        name = 'link',
        verbose_name = 'Link',
        max_length = 200,
        default = '#',
        blank = False,
        null = False,
    )

    def get_links(self):
        return Link.objects.filter(menuItem = self.id).order_by('order')

    def __str__(self):
        return str(self.name)

class Link(models.Model):
    menuitem = models.ForeignKey(
        name = 'menuItem',
        verbose_name = 'Menu Item',
        related_name='linkMenuItem',
        help_text = 'Menu Item in der der Link angezeigt werden soll.',
        to = 'MenuItem',
        on_delete = models.CASCADE,
        blank = False,
        null = False,
    )

    label = models.CharField(
        name = 'name',
        verbose_name = 'Name',
        max_length = 200,
        blank = False,
        null = False,
    )

    order = models.IntegerField(
        name = 'order',
        verbose_name = 'Reihenfolge',
        blank = True,
        null = True,
        )

    link = models.CharField(
        name = 'link',
        verbose_name = 'Link',
        max_length = 200,
        default = '#',
        blank = False,
        null = False,
    )