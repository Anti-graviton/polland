from enum import Enum, unique

from django.db import models


@unique
class ChoiceType(Enum):
    Selectable = 1
    Fillable = 2


class Question(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    publisher = models.CharField(max_length=200)
    publish_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    category = models.TextField(default='general')
    title = models.CharField(max_length=500)
    body = models.TextField(max_length=2000)

    def __str__(self):
        return "[{}]: {}".format(self.title, self.body)


class Choice(models.Model):
    choice_type = models.IntegerField(default=1,
                                      choices=[(member.value, name) for name, member in ChoiceType.__members__.items()])
    value = models.TextField()
    weight = models.IntegerField(default=1)

    question = models.ForeignKey(to=Question,
                                 on_delete=models.CASCADE,
                                 related_name='choices')

    def __str__(self):
        return self.value
