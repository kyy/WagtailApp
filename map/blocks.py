from wagtail.blocks import (
    StructValue, StructBlock, CharBlock, BooleanBlock, ChoiceBlock, EmailBlock, TextBlock,
)


class PhoneBlock(StructBlock):
    PROVIDERS = [
        ("МТС", "МТС"),
        ("A1", "A1"),
        ("Life", "Life"),
        ("Work", "Work"),
        ("Fax", "Fax"),
    ]
    type = ChoiceBlock(
        choices=PROVIDERS,
        label='Провайдер',
        required=True,
        default='A1',
    )
    title = CharBlock(
        default='',
        label='Имя',
        required=False,
        max_length=128,
    )
    number = CharBlock(
        default='',
        label='Номер',
        required=True,
        max_length=17,
        help_text='Пример: «+375-29-666-44-22»'
    )
    live = BooleanBlock(
        default=False,
        required=False,
        label='Скрыть',
        help_text='Включение/отключение отображения номера',
    )

    class Meta:
        label = "Добавить телефон"
        icon = "arrow-down-big"
        collapsed = True


class MailBlock(StructBlock):
    title = CharBlock(
        default='',
        label='Имя',
        required=False,
        max_length=128,
    )
    e_mail = EmailBlock(
        default='',
        label='e-mail',
        required=True,
        max_length=128,
    )

    class Meta:
        label = "Добавить e-mail"
        icon = "arrow-down-big"
        collapsed = True


class MapBlock(StructBlock):
    title = CharBlock(
        default='',
        label='Имя',
        required=False,
        max_length=128,
    )
    live = BooleanBlock(
        default=False,
        required=False,
        label='Скрыть',
        help_text='Включение/отключение отображения карты',
    )
    html = TextBlock(
        default='',
        label='<HTML>',
        required=False,
    )

    class Meta:
        label = "Добавить карту"
        icon = "arrow-down-big"
        collapsed = True
        template = "map/blocks/map.html"
