from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_quiz, name='start_quiz'),
    path('get-question/', views.get_random_question, name='get_random_question'),
    path('submit-answer/', views.submit_answer, name='submit_answer'),
    path('end-quiz/', views.end_quiz, name='end_quiz'),
]
