from django.db import models

from wagtail.core.models import Page, Orderable

# Create your models here.

class LessonPage(Page):
    
    templates = 'subject/subject_landing_page.html'
    parent_page_types = ["subject.SubjectLandingPage"]
    
    lesson_name = models.CharField(max_length = 150, null=True, blank= True)
    