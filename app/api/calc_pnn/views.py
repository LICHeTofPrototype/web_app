# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.measurement.models import Measurement
from django.contrib.auth import get_user_model
from django.db import models 
from .models import PnnData
from front.account.serializers import UserSerializer
from .serializers import PnnDataSerializer
from . import pnn
from django.utils import timezone
import logging
from rest_framework.parsers import JSONParser  

User = get_user_model()

class CalcPnnAPI(APIView):
  parser_classes = [JSONParser]
    
  def info(msg):
    logger = logging.getLogger("command")
    logger.info(msg)

  def get(self, request, user_id, format=None):
    user_obj = User.objects.get(
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

  def post(self, request, user_id, format=json):
    #print ("VIEWS request.data = ", request.data)
    print (request.data)
    # TO DO Test においてデータを受ける時にrequestがOrderDict型で受けることになるので，下の方式で読み込む必要あり． 
    #time = request.data.getlist("time")
    #heart_beat = request.data.getlist("beat")
    # print ("Request Data = ", request.data)
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
    print ("User id type =", type(user_id))
    user_id = int(user_id)
    print ("User id Reviced type =", type(user_id))
    user_obj = User.objects.get(
      id = user_id
    )

    measurement_obj, created = Measurement.objects.get_or_create(
      user = user_obj
    )
    pnn_data_obj = PnnData.objects.create(
      measurement = measurement_obj,
      pnn = pnn50,
      pnn_time = pnn_time
    )

    res = {"pnn": float(pnn50), "time": float(pnn_time)}
    json_res = json.dumps(res) 
    return Response("Data was registered", status=status.HTTP_201_CREATED)
