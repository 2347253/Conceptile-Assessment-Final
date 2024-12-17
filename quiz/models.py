from django.db import models
from django.contrib.auth.models import User

# Questons from questions.json
class Question(models.Model):
    question_text = models.TextField()  
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1, choices=[
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    ]) 

    def __str__(self):
        return self.question_text

# User's Session
class UserSession(models.Model):
    user = models.CharField(max_length=255, unique=True)  # Use CharField for username
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user 

# User's ANSWERS 
class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Links to the question being answered
    selected_option = models.CharField(max_length=1)  # Stores the selected option (A, B, C, D)
    is_correct = models.BooleanField()  # Checks if answer is correct

    def __str__(self):
        return f"Question: {self.question}, Correct: {self.is_correct}"
