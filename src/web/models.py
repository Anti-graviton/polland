"""
Import models from django db package
"""
from django.db import models


class Question(models.Model):
    """
    Question model
    """
    creation_date = models.DateTimeField(auto_now=True)
    creator = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    body = models.TextField(max_length=2000)


class Choice(models.Model):
    """
    Choice model
    """
    value = models.TextField(max_length=500)
    question = models.ForeignKey(to=Question,
                                 on_delete=models.CASCADE,
                                 related_name='choices')


class UserAnswer(models.Model):
    """
    User answers for each question
    """
    class Meta:
        unique_together = (('user_id', 'question_id'),)

    answer_date = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    question_id = models.IntegerField()
    answer_id = models.IntegerField()
