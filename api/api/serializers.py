from rest_framework import serializers
from .models import HeartBeat

class analysisAPISerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'train_model_id',
            'pp_test_data_id',
            'status',
            'strage_file_name',
        )
        model = HeartBeat