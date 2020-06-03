from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, RichTextFieldPanel, InlinePanel
from wagtail.core.fields import StreamField, RichTextField
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable

from streams import blocks


class SubjectLandingPage(Page):
    '''Subject Landing Page (Brief Overview of Subjects with more details'''

    templates = 'subject/subject_landing_page.html'

    subject = models.CharField(
        blank=False, null=False, max_length=20, unique=True, help_text='Enter the Subject Name')

    content_panels = Page.content_panels + [
        FieldPanel('subject', heading='Subject Name'),
        InlinePanel('key_stage_card', max_num=4, min_num=1)
    ]

    class Meta:
        verbose_name = 'Subject Overview Page'
        verbose_name_plural = 'Subject Overview Pages'


class SubjectKeyStageCard(Orderable):
    '''Between 1 and 4 '''

    page = ParentalKey('subject.SubjectLandingPage', related_name='key_stage_card')
    title = models.CharField(max_length=20, null=False, blank=False, unique=True, help_text="Enter the Key Stage Level")
    description = RichTextField(max_length=200, null=False, blank=False, help_text="Enter information about what this Key Stage covers", features=['h4', 'h5', 'bold', 'italic', ])

    
    content = StreamField(
        [
            ("test", blocks.SubjectModuleBlock()),
            
        ],
        null=True,
        blank=True
    )
    
    
    panels = [
        FieldPanel('title', heading="Key Stage"),
        RichTextFieldPanel('description'),
        StreamFieldPanel('content'),
    ]

    