# coding: utf-8
from django.db import models
from django.utils import timezone
# from api.account.models import User
from api.measurement.models import Measurement

class PnnData(models.Model):
  """心拍数データ"""
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
  time = models.TimeField()
  pnn_time = models.FloatField(verbose_name="pnn_time")
  pnn = models.FloatField(verbose_name="pnn")
