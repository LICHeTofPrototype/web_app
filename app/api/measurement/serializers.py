from rest_framework import serializers
from .models import Measurement
from api.api_account.serializers import UserSerializer

class MeasurementSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Measurement
        fields = [
            'id',
            'user',
            'start_time',
        ]
        