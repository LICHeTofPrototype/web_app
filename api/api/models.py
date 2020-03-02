# coding: utf-8
from django.db import models
from django.utils import timezone

class HeartBeat(models.Model):
  """心拍数データ"""
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  measured_at = models.DateTimeField("計測日時", default=timezone.now)
  heart_beat_peak_time = models.FloatField('心拍ピーク値データ', default=0)
  pnn_data = models.FloatField("PNNデータ", default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)