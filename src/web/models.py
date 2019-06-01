from enum import Enum, unique

from django.db import models


@unique
class QuestionType(Enum):
    MultipleChoiceSingleAnswer = 1,
    MultipleChoiceMultipleAnswer = 2,
    Written = 3,
    Other = 4


@unique
class ChoiceType(Enum):
    Selectable = 1,
    Fillable = 2


class Question(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    publisher = models.CharField(max_length=200)
    publish_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    question_type = models.CharField(max_length=1,
                                     default=QuestionType.MultipleChoiceSingleAnswer)
    category = models.TextField(default='general')
    title = models.CharField(max_length=500)
    body = models.TextField(max_length=2000)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_type = models.IntegerField(default=ChoiceType.Selectable)
    value = models.TextField()
    weight = models.IntegerField(default=1)
