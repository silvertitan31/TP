from django.db import models

from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    '''Home Page Model'''

    templates = "templates/home_page/html"
    max_count = 1

    banner_title = models.CharField(max_length=50, blank=False, null=True)

    banner_subtitle = RichTextField(
        features=['bold', 'italic'], max_length=100, blank=True, null=True)

    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+"
    )

    banner_cta_studying = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel('banner_image'),
        PageChooserPanel('banner_cta_studying'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
