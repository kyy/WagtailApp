from wagtail.blocks import (
    StructValue, StructBlock, CharBlock, URLBlock, BooleanBlock, StreamBlock, PageChooserBlock
)


class NavigationExternalLinkStructValue(StructValue):
    def href(self):
        """Construct a URL with anchor if exists, otherwise use URL"""
        url = self.get("url")
        anchor = self.get("anchor")
        href = f"{url}#{anchor}" if anchor else url
        return href

    def is_external(self):
        return True

    def is_live(self):
        return True


class NavigationExternalLinkBlock(StructBlock):
    title = CharBlock(
        label='Имя внешней ссылки',
        required=True,
    )
    live = BooleanBlock(
        default=False,
        required=False,
        label='Скрыть меню',
        help_text='Включение/отключение отображения меню',
    )
    url = URLBlock(
        label='Внешняя ссылка'
    )
    anchor = CharBlock(
        label='Якорь',
        required=False,
        help_text="Для ссылки на определенные элементы страницы. Введите текст привязки без символа «#».",
    )

    class Meta:
        template = "navigation/blocks/nav_link.html"
        label = "Внешняя ссылка"
        icon = "link-external"
        value_class = NavigationExternalLinkStructValue


class NavigationPageChooserStructValue(StructValue):
    def href(self):
        """Construct a URL with anchor if exists, otherwise use URL"""
        url = self.get("page").url
        anchor = self.get("anchor")
        href = f"{url}#{anchor}" if anchor else url
        return href

    def is_live(self):
        live = self.get("page").live
        show_in_menu = self.get("page").show_in_menus
        return all([live, show_in_menu])


class NavigationPageChooserBlock(StructBlock):
    title = CharBlock(
        required=False,
        label='Изменить имя обычного меню',
        help_text='Поумолчанию используется имя страницы.',
    )
    page = PageChooserBlock(
        label='Страница',
    )
    live = BooleanBlock(
        default=False,
        required=False,
        label='Скрыть меню',
        help_text='Включение/отключение отображения категории меню',
    )
    anchor = CharBlock(
        required=False,
        label='Якорь',
        help_text="Для ссылки на определенные элементы страницы, введите текст привязки без символа «#».",
    )

    class Meta:
        template = "navigation/blocks/nav_link.html"
        label = "Обычное меню"
        icon = "doc-empty"
        value_class = NavigationPageChooserStructValue


class NavigationDropdownMenuBlock(StructBlock):
    title = CharBlock(
        label='Имя выпадающего меню',
    )
    live = BooleanBlock(
        default=False,
        required=False,
        label='Скрыть выпадающее меню',
        help_text='Включение/отключение отображения выпадающего меню (субменю не будут отображаться)',
    )

    menu_items = StreamBlock(
        [
            ("page", NavigationPageChooserBlock()),
            ("external_link", NavigationExternalLinkBlock()),
        ],
        label='Добавить обычное меню или внешнюю ссылку',
        collapsed=True

    )

    class Meta:
        template = "navigation/blocks/dropdown_menu.html"
        label = "Выпадающее меню"
        icon = "collapse-down"
        collapsed = True
