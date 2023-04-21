import wagtail.models
from wagtail.admin.panels import FieldPanel, HelpPanel, TabbedInterface, ObjectList
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import StreamField
from .blocks import (
    NavigationDropdownMenuBlock,
    NavigationExternalLinkBlock,
    NavigationPageChooserBlock,
)
from django.shortcuts import get_object_or_404


@register_setting
class NavigationMenuSetting(BaseSiteSetting):
    menu_items = StreamField(
        [
            ("internal_page", NavigationPageChooserBlock()),
            ("external_link", NavigationExternalLinkBlock()),
            ("drop_down", NavigationDropdownMenuBlock()),
        ],
        use_json_field=True,
        collapsed=True,
    )

    panels = [
        HelpPanel(
            content='<div class="help-block help-info"><svg class="icon icon-help icon" aria-hidden="true">'
                    '<use href="#icon-help"></use></svg><p>Категория меню не будет отображаться если страница не '
                    'опубликована или</p><p> отсутствует отметка - <i>«Показывать в меню» </i>в параметрах страницы '
                    'на вкладке: </p><p><i>«Продвижение»</i> --> <i>«Для меню сайта»</i></p></div>',
            heading='Инструкция',
        ),
        FieldPanel(
            "menu_items",
            heading='Конструктор категорий меню',
        ),
    ]
    edit_handler = TabbedInterface([
        ObjectList(panels, heading='«Меню-Бургер»'),
    ])

    class Meta:
        verbose_name = "Меню навигации"
