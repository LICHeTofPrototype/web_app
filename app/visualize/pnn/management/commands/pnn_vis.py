from django.core.management.base import BaseCommand, CommandError
import matplotlib.pyplot as plt
from api.calc_pnn.models import PnnData
from api.measurement.models import Measurement
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(id=2)
        measurement = Measurement.objects.get(user=user)
        pnn_time = PnnData.objects.filter(measurement=measurement).values_list('pnn_time', flat=True)
        pnn_data = PnnData.objects.filter(measurement=measurement).values_list('pnn', flat=True)
        time = PnnData.objects.filter(measurement=measurement).values_list('time', flat=True)
        pnn_time = list(pnn_time)
        pnn_data = list(pnn_data)
        time = list(time)
        data_time = []

        for time_oclock, delta_time in zip(time, pnn_time):
            data_time.append(time_oclock.minute*60 + time_oclock.second + delta_time)

        plt.plot(data_time[1:], pnn_data[1:])
        plt.show()
