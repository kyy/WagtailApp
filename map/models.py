from django.db.models import CharField, BooleanField, TextField
from wagtail.admin.panels import HelpPanel, FieldPanel, FieldRowPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import StreamField

from .blocks import PhoneBlock, MailBlock, MapBlock


@register_setting
class Map(BaseSiteSetting):
    map = StreamField(
        [
            ('map', MapBlock(requred=False,
                             default='[]',
                             null=True,
                             blank=True,
                             )),
        ],
        use_json_field=True,
        verbose_name='Карта',
        block_counts={
            'map': {'min_num': 0, 'max_num': 1},
        }
    )
    phone = StreamField(
        [
            ('phone', PhoneBlock(requred=False,
                                 default='[]',
                                 null=True,
                                 blank=True,
                                 )),
        ],
        use_json_field=True,
        verbose_name='Телефоны',
        block_counts={
            'phone': {'min_num': 0, 'max_num': 5},
        }

    )

    email = StreamField(
        [
            ('email', MailBlock(requred=False,
                                default='[]',
                                null=True,
                                blank=True,
                                )),
        ],
        use_json_field=True,
        verbose_name='Электронные адреса',
        block_counts={
            'email': {'min_num': 0, 'max_num': 5},
        }
    )

    panels = [
        HelpPanel(
            content='<div class="help-block help-info"><svg class="icon icon-help icon" aria-hidden="true">'
                    '<use href="#icon-help"></use></svg><p>Контактные данные</p></div>',
            heading='Инструкция',
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
            FieldPanel('map'),
        ],
            heading='Карта',
            classname='collapsed'
        ),
    ]

    class Meta:
        verbose_name = "Контакты"
