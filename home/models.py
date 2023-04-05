from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.models import ClusterableModel


class HomePage(Page):
    pass


