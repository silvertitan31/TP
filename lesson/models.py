from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, RichTextFieldPanel, InlinePanel, PageChooserPanel
from wagtail.core.models import Page, Orderable

# Create your models here.

class LessonPage(Page):
    
    templates = 'lesson/beta.html'
    parent_page_types = ["subject.SubjectLandingPage","subject.SubjectKSLandingPage"]
    
    lesson_name = models.CharField(
        max_length = 150,
        null=True,
        blank= True
    )
    
    presentation_link = models.URLField(max_length=200,blank=True,null=True)
    
    content_panels  = Page.content_panels + [
        FieldPanel("lesson_name"),
        FieldPanel("presentation_link")        
    ]
    
class Beta(Page):

    templates = 'lesson/beta.html'
    