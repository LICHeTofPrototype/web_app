from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from api.calc_data.models import *
from api.measurement.models import Measurement
#from django.contrib.auth import get_user_model                                                                                                                                     
#from django.db import models
from front.account.models import User
import numpy as np
import os
import json
import matplotlib.pyplot as plt 
from front.account.models import User

#User = get_user_model()

class Test(APITestCase):

	def test_api(self):
		print ("TEST Start")
		print ("-"*40)
		#cwd = os.getcwd()
		#INPUT_DATA = cwd + "/api/calc_pnn/" + "pulse_test_takamiya3.txt" 
		#INPUT_DATA = cwd + "/api/calc_pnn/" + "test_data_0305.json"
		#print ("INPUT DATA = ",INPUT_DATA)
		#jfile = open(INPUT_DATA, "r")
		#json_load = json.load(jfile)
		#print (json_load)
		user = User.objects.get(id=2)
		measurement = Measurement.objects.get(user=user)
		pnn_time = PnnData.objects.filter(measurement=measurement).values_list('pnn_time', flat=True)
		pnn_data = PnnData.objects.filter(measurement=measurement).values_list('pnn', flat=True)

		#time = json_load["time"]
		#beat = json_load["beat"]
		plt.plot(pnn_time, pnn_data)
		plt.show()
		# (minu, sec, msec, beat, IBI) = np.loadtxt(INPUT_DATA, unpack=True, dtype = None, delimiter=" ")
		# time = minu * 60 * 1000 + sec *1000 + msec
		# # print ("TIME = ", time)
		# # print ("\n"*2)
		# # print ("BEAT = ", beat)
		# time_list = list(time[500:1000])
		# beat_list = list(beat[500:1000])
		# time_data = [int(s) for s in time_list]
		# beat_data = [int(s) for s in beat_list]
		# #print ("TEST time_data = ", time_data)
		# data = {"time": time_data, "beat": beat_data, "location": "yokohama"}
		# print ("Test data = ", data)

		# data = {"time": list(time), "beat": list(beat)}
		# test_file = open("./test_data.txt", "w")
		# json.dump(data, test_file, indent=2)
		
		# user_id = 1
		# measurement_id =2
		# request_index = 3
		# url = reverse("calc-pnn", args=(user_id, measurement_id, request_index, ))
		# print ("URL = ", url)
		# response = self.client.post(url, data)
		# print(response.data) 
