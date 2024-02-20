from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'url', 'named_url', 'menu_name')

admin.site.register(MenuItem, MenuItemAdmin)
