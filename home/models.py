from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    pass


class Mix(models.Model):
    info = models.TextField(null=False, blank=True, max_length=128, default='...')

    class Meta:
        abstract = True

@register_snippet
class PhonesNumbers(Mix):
    OPERATOR = (
        ('A1', 'A1'),
        ('MTС', 'MTС'),
        ('Life', 'Life'),
        ('City', 'City'),
    )
    operator = models.CharField(max_length=16, null=False, choices=OPERATOR, default=OPERATOR[0])
    number = models.CharField(null=False, blank=True, max_length=32, default='+375291112233')


    panels = [
        FieldPanel('operator'),
        FieldPanel('number'),
        FieldPanel('info'),
    ]

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'

    def __str__(self):
        return self.operator + self.number + self.info


@register_snippet
class ElectricMails(Mix):
    e_mail = models.EmailField(max_length=256, null=True)

    panels = [
        FieldPanel('e_mail'),
        FieldPanel('info'),
    ]

    class Meta:
        verbose_name = 'e-mail'
        verbose_name_plural = 'Адреса электрической почты'

    def __str__(self):
        return self.e_mail + self.info


