from wagtail.contrib.settings.models import BaseSiteSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.models import Page, Orderable
from wagtail.admin.panels import (
    ObjectList, TabbedInterface,
)
from modelcluster.models import ClusterableModel
from navigation.models import NavigationMenuSetting


class HomePage(Page):
    show_in_menus_default = True


@register_setting
class SettingsDesign(NavigationMenuSetting):
    burger_menu = getattr(NavigationMenuSetting, 'panels')
    edit_handler = TabbedInterface([
        ObjectList(burger_menu, heading='«Меню-Бургер»'),
    ])

    class Meta:
        verbose_name = "Дизайн"
        proxy = True
