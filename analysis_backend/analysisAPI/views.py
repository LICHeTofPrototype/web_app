# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers
from rest_framework import viewsets, routers
from analysisAPI.models import HeartBeatData
from analysisAPI.serializers import analysisAPISerializer

# Create your views here.
class analysisAPIViewSet(viewsets.ModelViewSet):
  queryset = HeartBeatData.objects.all()
  serializer_class = analysisAPISerializer

def index(request):
  #とりあえず文字列を返す。
  return HttpResponse("Indexです！")

def pnnResult(request, requestType):
  if requestType == "get":
    return HttpResponse("get")
  elif requestType == "poll":
    return HttpResponse("poll")
  #とりあえず文字列を返す。
  else:
    return HttpResponse("else")