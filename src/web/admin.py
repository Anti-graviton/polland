from django.contrib import admin

from .models import Question, Choice, UserAnswer

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserAnswer)
# Register your models here.
