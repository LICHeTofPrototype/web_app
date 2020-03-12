# coding: utf-8
from django.db import models
from django.utils import timezone
from front.user.models import User

class Measurement(models.Model):
  """Measurement Table"""
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  location = models.CharField(max_length=256, verbose_name="location", null=True)
  date = models.DateTimeField(verbose_name="measured_date", auto_now_add=True)
