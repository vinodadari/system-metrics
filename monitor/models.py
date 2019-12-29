from django.contrib.auth.models import AbstractUser
from django.db import models

# for custom user
class CustomUser(AbstractUser):
    pass

#  Adding subscriber model for RAM usage realtime email notifications
class Subscriber(models.Model):
    mail = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)