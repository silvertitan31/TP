"""Flexible Page"""
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from streams import blocks


class FlexPage(Page):
    """Flexible Page Class"""

    templates = "flex/flex_page.html"

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichTextBlock()),
            ("simple_richtext", blocks.LimitedRichTextBlock()),
            
        ],
        null=True,
        blank=True
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Flexible Page"
        verbose_name_plural = "Flexible Pages"
