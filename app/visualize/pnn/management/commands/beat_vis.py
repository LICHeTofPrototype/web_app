from django.core.management.base import BaseCommand, CommandError
import matplotlib.pyplot as plt
from api.calc_pnn.models import BeatData
from api.measurement.models import Measurement
from django.db import models
from django.contrib.auth import get_user_model
from api.calc_pnn import pnn
import numpy as np

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(id=2)
        measurement = Measurement.objects.get(user=user)

        # Beat data
        beats_data = BeatData.objects.filter(measurement=measurement).values_list("beat_data", flat=True)
        for beat_data in beats_data:
            beat_data = beat_data.split(",")
            beat_data = [int(s) for s in beat_data]
            beat_data = np.array(beat_data)
            max_value = np.max(beat_data)
            min_value = np.min(beat_data)   
            normalized_data = (beat_data - min_value)/(max_value - min_value)
            time_data = [i for i in range(0, len(beat_data)*10, 10)]
            peak_time, _, peaks = pnn.find_RRI(time_data, normalized_data)
            time_data = np.array(time_data) * 0.001
            plt.plot(time_data, beat_data)
            plt.plot(peak_time, beat_data[peaks], "o",color="red")
            plt.show()