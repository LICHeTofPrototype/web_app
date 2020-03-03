from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
import numpy as np
import os
import json

class Test(APITestCase):

  def test_api(self):
    print ("TEST Start")
    print ("-"*40)
    cwd = os.getcwd()
    INPUT_DATA = cwd + "/api/calc_pnn/" + "pulse_test_takamiya3.txt" 
    print ("INPUT DATA = ",INPUT_DATA)
    (minu, sec, msec, beat, IBI) = np.loadtxt(INPUT_DATA, unpack=True, dtype = None, delimiter=" ")
    time = minu * 60 * 1000 + sec *1000 + msec
    # print ("TIME = ", time)
    # print ("\n"*2)
    # print ("BEAT = ", beat)
    time_list = list(time[500:1000])
    beat_list = list(beat[500:1000])
    time_data = [int(s) for s in time_list]
    beat_data = [int(s) for s in beat_list]
    #print ("TEST time_data = ", time_data)
    data = {"time": time_data, "beat": beat_data, "location": "yokohama"}
    print ("Test data = ", data)
    
    data = {"time": list(time), "beat": list(beat)}
    test_file = open("./test_data.txt", "w")
    json.dump(data, test_file, indent=2)
    
    user_id = 1
    measurement_id =2
    request_index = 3
    url = reverse("calc-pnn", args=(user_id, measurement_id, request_index, ))
    print ("URL = ", url)
    response = self.client.post(url, data)
    print(response.data) 
