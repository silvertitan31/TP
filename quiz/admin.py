from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from .models import Quiz

# Register your models here.
class QuizAdmin(ModelAdmin):
    
    model = Quiz
    menu_label = "Quizzes"
    menu_icon = "placeholder"
    menu_order = 300
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("question", "answer")
    search_fielkd  = ("question",)
    
modeladmin_register(QuizAdmin)