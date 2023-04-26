from wagtail.contrib.settings.models import BaseSiteSetting
from wagtail.models import Page


class HomePage(Page):
    show_in_menus_default = True
