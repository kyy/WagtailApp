from wagtail.blocks import (
    StructValue, StructBlock, CharBlock, BooleanBlock, ChoiceBlock, EmailBlock, TextBlock, URLBlock
)


class PhoneBlock(StructBlock):
    PROVIDERS = [
        ("МТС", "МТС"),
        ("A1", "A1"),
        ("Life", "Life"),
        ("Work", "Work"),
        ("Fax", "Fax"),
    ]
    title = CharBlock(
        default='Менеджер',
        label='Имя',
        required=False,
        max_length=128,
    )
    type = ChoiceBlock(
        choices=PROVIDERS,
        label='Провайдер',
        required=True,
        default='A1',
    )
    number = CharBlock(
        default='+375 (29) 666 44 22',
        label='Номер',
        required=True,
        max_length=32,
        help_text='Пример: «+375 (29) 666 44 22»'
    )
    ico = CharBlock(
        default='<i class="fa-solid fa-phone"></i>',
        label='Иконка',
        required=False,
        max_length=128,
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
        default='Отдел маркетинга',
        label='Имя',
        required=False,
        max_length=128,
    )
    ico = CharBlock(
        default='<i class="fa-solid fa-envelope"></i>',
        label='Иконка',
        required=False,
        max_length=128,
    )
    e_mail = EmailBlock(
        default='minsk@mail.ru',
        label='e-mail',
        required=True,
        max_length=128,
    )
    live = BooleanBlock(
        default=False,
        required=False,
        label='Скрыть',
        help_text='Включение/отключение отображения адреса',
    )

    class Meta:
        label = "Добавить e-mail"
        icon = "arrow-down-big"
        collapsed = True
        template = "map/blocks/email.html"


class MapBlock(StructBlock):
    title = CharBlock(
        default='Главный офис',
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
        default='<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2416.025752575022!2d27.'
                '448263451715075!3d52.731727706084875!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sru!'
                '2sby!4v1682684391133!5m2!1sru!2sby"width="100%" height="320" style="border:0;" allowfullscr'
                'een="" loading="lazy"referrerpolicy="no-referrer-when-downgrade" title="Карта"></iframe>',
        label='<HTML>',
        required=False,
        help_text='Установите width=100% height=320'
    )

    class Meta:
        label = "Добавить карту"
        icon = "arrow-down-big"
        collapsed = True
        template = "map/blocks/map.html"


class BrandsBlock(StructBlock):
    title = CharBlock(
        default='',
        label='Имя',
        required=False,
        max_length=128,
    )
    ico = CharBlock(
        default='',
        label='Иконка',
        required=False,
        max_length=128,
    )
    url = URLBlock(
        default='',
        label='url',
        required=True,
    )

    class Meta:
        label = "Добавить социальную сеть"
        icon = "arrow-down-big"
        collapsed = True
        template = "map/blocks/brands.html"
