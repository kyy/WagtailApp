from django.utils.safestring import mark_safe
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import StreamField
from .blocks import (
    NavigationDropdownMenuBlock,
    NavigationExternalLinkBlock,
    NavigationPageChooserBlock,
)


@register_setting
class NavigationMenuSetting(BaseSiteSetting):
    menu_items = StreamField(
        [
            ("internal_page", NavigationPageChooserBlock()),
            ("external_link", NavigationExternalLinkBlock()),
            ("drop_down", NavigationDropdownMenuBlock()),
        ],
        use_json_field=True,
    )

    panels = [
        FieldPanel(
            "menu_items",
            heading=mark_safe(
                'Конструктор меню'
                '<div class="help"><p>Категория меню не будет отображаться если страница не опубликована или</p>'
                '<p>отсутствует "галочка" <i>"Показывать в меню"</i>в параметрах страницы на вкладке:</p>'
                '<p><i>"Продвижение"</i>-><i>"Для меню сайта"</i></p></div>'),
        ),
    ]

    class Meta:
        verbose_name = "Меню навигации"
