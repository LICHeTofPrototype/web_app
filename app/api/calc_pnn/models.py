# coding: utf-8
from django.db import models
from django.utils import timezone
from api.measurement.models import Measurement


class BeatData(models.Model):
  measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
  time = models.TimeField(verbose_name="beat_time")
  beat_data = models.CharField(max_length=6105, verbose_name="beat_data")

class PnnData(models.Model):
  """心拍数データ"""
  measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
  time = models.TimeField(verbose_name="time")
  pnn_time = models.FloatField(verbose_name="pnn_time")
  pnn_data = models.FloatField(verbose_name="pnn")
  


