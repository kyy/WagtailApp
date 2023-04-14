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
            heading='Конструктор меню',
            help_text='Категории меню не будут отображаться если страница не опубликована.\n'
                      'При необходимости можно указать свои имена, по умолчанию используется заголовок стрницы'
                   ),
    ]

    class Meta:
        verbose_name = "Меню навигации"
