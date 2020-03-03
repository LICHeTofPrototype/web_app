# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.measurement.models import Measurement
from api.account.models import CustomUser 
from .models import PnnData
from api.account.serializers import UserSerializer
from .serializers import PnnDataSerializer
from . import pnn
from django.utils import timezone
import logging

class CalcPnnAPI(APIView):
  def info(msg):
    logger = logging.getLogger("command")
    logger.info(msg)

  def get(self, request, user_id, format=None):
    user_obj = CustomUser.objects.get(
      id = user_id
    )

    # measurement_obj = Measurement.objects.get(
    #   id = measurement_id,
    #   user = user_obj
    # )

    # pnn_data_obj = PnnData.objects.filter(
    #   measurement = measurement_obj,
    #   id__gt =request_index
    # )


    # serializer = PnnDataSerializer(pnn_data_obj, many=True)
    serializer = UserSerializer(user_obj)
    return Response(serializer.data)#(serializer.data, status=status.HTTP_200_OK)

  def post(self, request, user_id, format=None):
    #print ("VIEWS request.data = ", request.data)
    
    # TO DO Test においてデータを受ける時にrequestがOrderDict型で受けることになるので，下の方式で読み込む必要あり． 
    #time = request.data.getlist("time")
    #heart_beat = request.data.getlist("beat")
    time = request.data["time"]
    heart_beat = request.data["beat"]
    location = "yokohama"
    
    beat_data = [int(s) for s in heart_beat]
    time_data = [int(s) for s in time]
    print ("View Heart_beat = ", beat_data[0:3])
    print ("View Time = ", time_data[0:3])

    peak_time, RRI = pnn.find_RRI(time_data, beat_data)
    print ("In views.py RRI = ", RRI)
    print ("In views.py peak_time = ", peak_time)
    pnn_time, pnn50 = pnn.cal_pnn(peak_time, RRI)
    print ("View Pnn50 = ", pnn50)

    user_obj, created = CustomUser.objects.update_or_create(
      id = user_id
    )
    measurement_obj, created = Measurement.objects.update_or_create(
      user = user_obj
      #location = location
    )
    pnn_data_obj = PnnData.objects.create(
      measurement = measurement_obj,
      pnn = pnn50,
      pnn_time = pnn_time
    )

    res = {"pnn": float(pnn50), "time": float(pnn_time)}
    json_res = json.dumps(res) 
    return Response(json_res, status=status.HTTP_201_CREATED)