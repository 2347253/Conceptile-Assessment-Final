from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page (localhost/)
    path('quiz/start/', views.start_quiz, name='start_quiz'),  # Start quiz
    path('quiz/get-question/', views.get_random_question, name='get_question'),  # Fetch a question
    path('quiz/submit-answer/', views.submit_answer, name='submit_answer'),  # Submit an answer
    path('quiz/end-quiz/', views.end_quiz, name='end_quiz'),  # End the quiz
]
