from wagtail.admin.panels import FieldPanel, HelpPanel
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
        collapsed=True
    )

    panels = [
        HelpPanel(
            content='<div class="help-block help-info"><svg class="icon icon-help icon" aria-hidden="true">'
                    '<use href="#icon-help"></use></svg><p>Категория меню не будет отображаться если страница не '
                    'опубликована или</p><p> отсутствует отметка - <i>"Показывать в меню" </i>в параметрах страницы '
                    'на вкладке: </p><p><i>"Продвижение"</i>-><i>"Для меню сайта"</i></p></div>',
            heading='',
        ),
        FieldPanel(
            "menu_items",
            heading='Конструктор категорий меню',
        ),
    ]

    class Meta:
        verbose_name = "Меню навигации"
