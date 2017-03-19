from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Time(models.Model):
    user = models.ForeignKey(User)
    time = models.IntegerField(default=3600)
    total_spent = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)