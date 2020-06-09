from django.urls import path, re_path, include
from quiz import views

urlpatterns = [
    path('quiz/', views.question_list),
    path('quiz/<int:pk>/', views.question_detail),
]