from django.db import models
from django.utils import timezone

# Create your models here.
class TimeModel(models.Model):
    time = models.DateTimeField(auto_now=True)