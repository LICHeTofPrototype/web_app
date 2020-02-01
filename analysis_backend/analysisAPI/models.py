# coding: utf-8
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
  """ユーザー情報"""
  # user_id = models.IntegerField("ユーザーid", blank=True, default=None)
  user_name = models.CharField("ユーザー名", max_length=255)
  created_at = models.DateTimeField("", default=timezone.now)

class HeartBeat(models.Model):
  """心拍数データ"""
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  measured_at = models.DateTimeField("計測日時", null=True, default=timezone.now)
  heart_beat_peak_time = models.FloatField('心拍ピーク値データ', blank=True, default=0)
  pnn_data = models.TextField("PNNデータ", blank=True, default=0)

  def __str__(self):
    return self.user