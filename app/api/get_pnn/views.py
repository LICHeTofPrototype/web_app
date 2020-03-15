# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.measurement.models import Measurement
from django.db import models
from django.contrib.auth import get_user_model
from api.calc_pnn.models import PnnData
from front.account.serializers import UserSerializer
from api.calc_pnn.serializers import PnnDataSerializer
from django.utils import timezone
import logging

User = get_user_model()

class GetPnnAPI(APIView):
  def info(msg):
    logger = logging.getLogger("command")
    logger.info(msg)

  def get(self, request, user_id, measurement_id, request_index, format=None):
    user_obj = User.objects.get(
      id = user_id
    )
    
    measurement_obj = Measurement.objects.get(
      id = measurement_id,
      user = user_obj
    )

    pnn_data_obj = PnnData.objects.filter(
      measurement = measurement_obj,
      id__gt = request_index
    )
    serializer = PnnDataSerializer(pnn_data_obj, many=True)
    print (serializer.data)
    return Response(serializer.data)
