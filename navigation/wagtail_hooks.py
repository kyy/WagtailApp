from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import NavigationMenuSetting


class NavigationMenuSettingAdmin(ModelAdmin):
    model = NavigationMenuSetting
    menu_label = 'NavigationMenuSetting'
    menu_icon = 'pilcrow'
    menu_label = 'Меню навигации'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('panels',)
    search_fields = ('menu_items',)
    inspect_view_enabled = True


modeladmin_register(NavigationMenuSettingAdmin)
