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
        FieldPanel("menu_items",
                   heading=mark_safe(
                       'Конструктор меню'
                        '<div class="help"><p>Категории меню не будут отображаться если страница не опубликована.</p>'
                        '<p>Категорию меню можно также отключить без редактирования, убрав галочку <i>"Показывать в меню"</i></p>'
                        '<p>на вкладке <i>"Продвижение"</i>-><i>"Для меню сайта"</i> в параметрах страницы.</p></div>'),
                   ),
    ]

    class Meta:
        verbose_name = "Меню навигации"
