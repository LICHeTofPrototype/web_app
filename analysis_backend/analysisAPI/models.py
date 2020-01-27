# coding: utf-8
from django.db import models
from django.utils import timezone

# Create your models here.
class HeartBeatData(models.Model):
  """心拍数データ"""
  name = models.CharField('ユーザー名', max_length=255)
  measured_at = models.DateTimeField("計測日時", null=True, default=timezone.now)
  heart_beat_data = models.IntegerField('心拍数データ', blank=True, default=0)

  def __str__(self):
    return self.name