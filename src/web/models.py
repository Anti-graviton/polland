from django.db import models


class Question(models.Model):
    creation_date = models.DateTimeField(auto_now=True)
    creator = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    body = models.TextField(max_length=2000)

    def __str__(self):
        return "[{}]: {}".format(self.title, self.body)


class Choice(models.Model):
    value = models.TextField(max_length=500)
    question = models.ForeignKey(to=Question,
                                 on_delete=models.CASCADE,
                                 related_name='choices')

    def __str__(self):
        return self.value
