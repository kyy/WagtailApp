from wagtail import blocks as wagtail_blocks
from wagtail.blocks import StructValue


class NavigationExternalLinkStructValue(StructValue):
    def href(self):
        """Construct a URL with anchor if exists, otherwise use URL"""
        url = self.get("url")
        anchor = self.get("anchor")
        href = f"{ url }#{ anchor }" if anchor else url
        return href


class NavigationExternalLinkBlock(wagtail_blocks.StructBlock):
    title = wagtail_blocks.CharBlock()
    url = wagtail_blocks.URLBlock()
    anchor = wagtail_blocks.CharBlock(
        required=False,
        help_text="Для ссылки на определенные элементы страницы. Введите текст привязки без символа «#».",
    )

    class Meta:
        template = "navigation/blocks/nav_link.html"
        label = "Внутренняя ссылка"
        icon = "link-external"
        value_class = NavigationExternalLinkStructValue


class NavigationPageChooserStructValue(StructValue):
    def href(self):
        """Construct a URL with anchor if exists, otherwise use URL"""
        url = self.get("page").url
        anchor = self.get("anchor")
        href = f"{ url }#{ anchor }" if anchor else url
        return href

    def is_live(self):
        is_live = self.get("page").live
        is_show_in_menus = self.get("page").show_in_menus
        return all([is_live, is_show_in_menus])

    def title_page(self):
        title_page = self.get("page").title
        return title_page


class NavigationPageChooserBlock(wagtail_blocks.StructBlock):
    title = wagtail_blocks.CharBlock(
        required=False,
        label='Изменить имя обычного меню',
        help_text='Поумолчанию используется имя страницы.',
    )
    page = wagtail_blocks.PageChooserBlock(
        label='Страница',
    )
    anchor = wagtail_blocks.CharBlock(
        required=False,
        label='Якорь',
        help_text="Для ссылки на определенные элементы страницы. Введите текст привязки без символа «#».",
    )

    class Meta:
        template = "navigation/blocks/nav_link.html"
        label = "Обычное меню"
        icon = "doc-empty"
        value_class = NavigationPageChooserStructValue


class NavigationDropdownMenuBlock(wagtail_blocks.StructBlock):
    title = wagtail_blocks.CharBlock(
        label='Имя выпадающего меню',
    )
    menu_items = wagtail_blocks.StreamBlock(
        [
            ("page", NavigationPageChooserBlock()),
            ("external_link", NavigationExternalLinkBlock()),
        ]
    )

    class Meta:
        template = "navigation/blocks/dropdown_menu.html"
        label = "Выпадающее меню"
        icon = "arrow-down-big"
