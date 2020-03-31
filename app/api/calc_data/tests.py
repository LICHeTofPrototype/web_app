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
		
		user_obj = User.objects.create(
			username= "yukin",
			first_name="yuki", 
			last_name="nakagawa", 
			email="abc@def.com", 
			password="abc123def", 
			which_sex="M", 
			birth_date="1992-7-14", 
			age=27,
			dev_id ="1021"
		)
		measurement = Measurement.objects.create(
			user=user_obj,
			start_time = "2012-12-2 12:20:2"
		)

		data1 = [
			"beat": [1,2,3],
			"time": "12:10:2",
			"dev_id": "1021"
		]
		
		