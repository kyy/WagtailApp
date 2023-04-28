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
    ico = CharBlock(
        default='<i class="fa-solid fa-phone"></i>',
        label='ico',
        required=False,
        max_length=128,
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
        max_length=32,
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
        template = "map/blocks/phone.html"


class MailBlock(StructBlock):
    title = CharBlock(
        default='',
        label='Имя',
        required=False,
        max_length=128,
    )
    ico = CharBlock(
        default='<i class="fa-solid fa-envelope"></i>',
        label='ico',
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
        template = "map/blocks/email.html"


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
        help_text='Установите width=100% height=320'
    )

    class Meta:
        label = "Добавить карту"
        icon = "arrow-down-big"
        collapsed = True
        template = "map/blocks/map.html"
