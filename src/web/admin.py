from django.contrib import admin

from .models import Question, Choice, UserAnswer,UserAnswerHistory

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserAnswer)
admin.site.register(UserAnswerHistory)
# Register your models here.
