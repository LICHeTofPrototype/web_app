# coding: utf-8
from django.db import models
from django.utils import timezone
from api.account.models import CustomUser

class HeartBeat(models.Model):
  """心拍数データ"""
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  measured_at = models.DateField(verbose_name="measured_date")
  pnn_time = models.FloatField(verbose_name="pnn_time")
  pnn = models.FloatField(verbose_name="pnn")
  