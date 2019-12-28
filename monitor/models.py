from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

class Metrics(models.Model):
    platform = models.TextField(default='')
    cpu_utlization = models.IntegerField(default='')
    ram_utilization = models.IntegerField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)