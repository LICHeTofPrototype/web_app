# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HeartBeat
from .serializers import analysisAPISerializer
from . import pnn
from django.utils import timezone

class HeartBeatAPI(APIView):
  def get(self, request, format=None):
    return Response("OK!!!!!!!!!!!!!!!!!!!!!!")
  def post(self, request, format=None):
    #print ("VIEWS request.data = ", request.data)
    
    # time = request.data.getlist("time")
    # heart_beat = request.data.getlist("beat")
    
    time = request.data["time"]
    heart_beat = request.data["beat"]
    # user_name = raw_data["meta_data"]["name"]
    # measured_time = raw_data["meta_data"]["measured_time"]
    # for data in raw_data:
    #   time.append(data["status"]["time_stamp"])
    #   heart_beat.append(data["heart_beat"])
    beat_data = [int(s) for s in heart_beat]
    time_data = [int(s) for s in time]
    print ("View Heart_beat = ", beat_data[0:3])
    print ("View Time = ", time_data[0:3])

    peak_time, RRI = pnn.find_RRI(time_data, beat_data)
    print ("In views.py RRI = ", RRI)
    print ("In views.py peak_time = ", peak_time)
    pnn_time, pnn50 = pnn.cal_pnn(peak_time, RRI)
    print ("View Pnn50 = ", pnn50)
    # pnn_data = []
    # temp_data = {}
    # for i in range(len(pnn50)):
    #   temp_data["time"] = pnn_time[i]
    #   temp_data["data"] = pnn_data[i]
    #   pnn_data.append(temp_data)

    # this_pnn_data = json.dumps(pnn_data)
    
    # try:
    #   this_user = User.objects.filter(user_name = user_name)[0]
    # except:
    #   this_user = User.object.create(user_name=user_name, created_at=timezone.now)  
    #   this_user.save()

    # this_data = HeartBeat(user=this_user, masured_at=measured_time, pnn_data=this_pnn_data)
    # this_data.save()
    res = {"pnn": str(pnn50), "time": str(pnn_time)}
    json_res = json.dumps(res) 
    return Response(json_res, status=status.HTTP_201_CREATED)