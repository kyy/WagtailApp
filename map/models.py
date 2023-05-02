from django.db.models import CharField, BooleanField
from wagtail.admin.panels import HelpPanel, FieldPanel, MultiFieldPanel, TabbedInterface, ObjectList, FieldRowPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import StreamField

from .blocks import PhoneBlock, MailBlock, MapBlock, BrandsBlock


@register_setting
class Map(BaseSiteSetting):
    address = CharField(
        blank=True,
        default='Manchester city, Redstreet str. 43-56',
        verbose_name='Адрес',
        max_length=128,
    )
    address_ico = CharField(
        blank=True,
        default='<i class="fa-solid fa-house"></i>',
        verbose_name='Иконка адреса',
        max_length=128,
    )
    work_time = CharField(
        blank=True,
        default='(mon-sut: 8:00-16:00)',
        verbose_name='Рабочее время',
        max_length=128,
    )
    work_time_ico = CharField(
        blank=True,
        default='<i class="fa-solid fa-clock"></i>',
        verbose_name='Иконка рабочего времени',
        max_length=128,
    )
    address_live = BooleanField(
        default=False,
        verbose_name='Скрыть',
        help_text='Включение/отключение отображения контактов и карты',
    )
    brands_live = BooleanField(
        default=False,
        verbose_name='Скрыть',
        help_text='Включение/отключение отображения социальных сетей',
    )
    map = StreamField(
        [
            ('map', MapBlock(default='[]', )),
        ],
        use_json_field=True,
        blank=True,
        collapsed=True,
        verbose_name='Карта',
        block_counts={
            'map': {'min_num': 0, 'max_num': 1},
        },
    )
    phone = StreamField(
        [
            ('phone', PhoneBlock(default='[]', )),
        ],
        use_json_field=True,
        blank=True,
        collapsed=True,
        verbose_name='Телефоны',
        block_counts={
            'phone': {'min_num': 0, 'max_num': 5},
        },
    )
    email = StreamField(
        [
            ('email', MailBlock(default='[]', )),
        ],
        use_json_field=True,
        blank=True,
        collapsed=True,
        verbose_name='Электронные адреса',
        block_counts={
            'email': {'min_num': 0, 'max_num': 5},
        },
    )
    brands = StreamField(
        [
            ('brands', BrandsBlock(default='[]', )),
        ],
        use_json_field=True,
        blank=True,
        collapsed=True,
        verbose_name='Социальные сети',
        block_counts={
            'brands': {'min_num': 0, 'max_num': 10},
        },
    )

    panels = [
        HelpPanel(
            heading='Вспомогательные ресурсы',
            content='<div class="help-block help-info"><svg class="icon icon-help icon" aria-hidden="true">'
                    '<use href="#icon-help"></use></svg><p>При добавлении карты отредактируйте ширину и высоту фрейма!</p></div>'
                    '<p><b>ИКОНКИ: </b><a href="https://fontawesome.com/search?o=r&m=free" target="_blank">Fontawesome</a> / '
                    '<a href="https://icons.getbootstrap.com/" target="_blank">Bootstrap</a></p>'
                    '<p><b>КАРТЫ: </b><a href="https://yandex.ru/maps/" target="_blank">Яндекс Карты</a> / '
                    '<a href="https://www.google.com/maps/?hl=RU" target="_blank">Google Карты</a></p>'
            ,
        ),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('address'),
                FieldPanel('address_ico'),
            ]),
            FieldRowPanel([
                FieldPanel('work_time'),
                FieldPanel('work_time_ico'),
            ]),
            FieldPanel('address_live'),
            FieldPanel('map'),
        ],
            heading='Адрес / Карта / Время работы',
            classname='collapsed'
        ),
        MultiFieldPanel([
            FieldPanel('phone'),
        ],
            heading='Номера телефонные',
            classname='collapsed'
        ),
        MultiFieldPanel([
            FieldPanel('email'),
        ],
            heading='Электронная почта',
            classname='collapsed'
        ),
        MultiFieldPanel([
            FieldPanel('brands_live'),
            FieldPanel('brands'),
        ],
            heading='Социальные сети',
            classname='collapsed'
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(panels, heading='«Контакты»'),
    ])

    class Meta:
        verbose_name = "Контакты"
