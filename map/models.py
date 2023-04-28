from django.db.models import CharField
from wagtail.admin.panels import HelpPanel, FieldPanel, MultiFieldPanel, TabbedInterface, ObjectList
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import StreamField

from .blocks import PhoneBlock, MailBlock, MapBlock


@register_setting
class Map(BaseSiteSetting):
    address = CharField(
        blank=True,
        default='',
        verbose_name='Адрес',
        max_length=128,
    )
    work_time = CharField(
        blank=True,
        default='',
        verbose_name='Рабочее время',
        max_length=128,
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

    panels = [
        HelpPanel(
            heading='Инструкция',
            content='<div class="help-block help-info"><svg class="icon icon-help icon" aria-hidden="true">'
                    '<use href="#icon-help"></use></svg><p>Контактные данные</p></div>',
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
            FieldPanel('address'),
            FieldPanel('work_time'),
            FieldPanel('map'),
        ],
            heading='Адрес / Карта / Время работы',
            classname='collapsed'
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(panels, heading='«Контакты»'),
    ])

    class Meta:
        verbose_name = "Контакты"
