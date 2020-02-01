# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers
from rest_framework import viewsets, routers

from analysisAPI.models import User
from analysisAPI.models import HeartBeat
from analysisAPI.serializers import analysisAPISerializer

import pnn
from django.utils import timezone

# Create your views here.
# class analysisAPIViewSet(viewsets.ModelViewSet):
  # queryset = HeartBeat.objects.all()
  # serializer_class = analysisAPISerializer

def index(request):
  #とりあえず文字列を返す。
  return HttpResponse("Indexです！")

def get_heart_beat_data(request, requestType):
  if requestType == "get":
    raw_data = json.loads(request.text)
    time = []
    heart_beat = []
    user_name = raw_data["meta_data"]["name"]
    measured_time = raw_data["meta_data"]["measured_time"]
    for data in raw_data:
      time.append(data["status"]["time_stamp"])
      heart_beat.append(data["heart_beat"])
    
    peak_time, RRI = pnn.find_RRI(time, heart_beat)
    pnn_time, pnn50 = pnn.cal_pnn(peak_time, RRI)

    pnn_data = []
    temp_data = {}
    for i in range(len(pnn50)):
      temp_data["time"] = pnn_time[i]
      temp_data["data"] = pnn_data[i]
      pnn_data.append(temp_data)

    this_pnn_data = json.dumps(pnn_data)
    
    try:
      this_user = User.objects.filter(user_name = user_name)[0]
    except:
      this_user = User.object.create(user_name=user_name, created_at=timezone.now)  
      this_user.save()

    this_data = HeartBeat(user=this_user, masured_at=measured_time, pnn_data=this_pnn_data)
    this_data.save()
    return HttpResponse(this_pnn_data)
  else:
    return HttpResponse("Please poll data, not request data here.")