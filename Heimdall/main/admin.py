from django.contrib import admin
from django.shortcuts import redirect

from .models import (
    NavigationbarItem,
    MenuItem,
    Link,
)

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Navigationbar
#--------------------------------------------------------------------------------
class LinkAdmin(admin.TabularInline):
    model = Link
    extra = 0
    ordering = ['order',]

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['navigationbarItem','name','order','link',]
    search_fields = ['name',]
    list_filter = ['navigationbarItem',]
    list_editable = ['order',]
    ordering = ['order',]
    fieldsets = (
        ('Allgemein', {'fields':(
            'name',
            'order',
            'link',
            )}),
    )
    inlines = [
        LinkAdmin,
    ]
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/admin/main/navigationbaritem/'+str(obj.navigationbarItem.id)+'/change/')

    def response_change(self, request, obj):
        return redirect('/admin/main/navigationbaritem/'+str(obj.navigationbarItem.id)+'/change/')

class MenuItemInlineAdmin(admin.TabularInline):
    model = MenuItem
    extra = 0
    ordering = ['order',]
    show_change_link = True

@admin.register(NavigationbarItem)
class NavigationbarItemAdmin(admin.ModelAdmin):
    list_display = ['id','name','order','link',]
    list_display_links = ('name',)
    search_fields = ['name',]
    list_filter = ['name']
    list_editable = ['order',]
    ordering = ['order',]
    fieldsets = (
        ('Allgemein', {'fields':(
            'name',
            'order',
            'link',
            )}),
    )
    inlines = [
        MenuItemInlineAdmin,
    ]
    filter_horizontal = []
    radio_fields = {}
#--------------------------------------------------------------------------------
