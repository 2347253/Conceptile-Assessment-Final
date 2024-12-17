from django.contrib import admin
from .models import Question, UserSession, UserAnswer

admin.site.register(Question)
admin.site.register(UserSession)
admin.site.register(UserAnswer)
