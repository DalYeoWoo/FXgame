from django.db import models


class Participant(models.Model):
    history = models.CharField(max_length=200, default=':')
    answer = models.CharField(max_length=200, default=':')
    hint = models.CharField(max_length=200, default=':')
    tip = models.CharField(max_length=200, default=':')
    group = models.CharField(max_length=1, default=':')

    def __str__(self):
        return self.group
