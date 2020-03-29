from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db import models
from django.contrib.auth import get_user_model
from api.measurement.models import Measurement
from api.calc_data.models import PnnData
from api.calc_data.serializers import PnnDataSerializer
import logging

User = get_user_model()

class GetPnnAPI(APIView):
    permission_classes = (AllowAny,)

    def info(self, msg):
        logger = logging.getLogger("command")
        logger.info(msg)

    def post(self, request, format=None):
        measurement_obj = Measurement.objects.get(
            id = request.data["measurement_id"],
            #user = request.user
        )
        pnn_data_obj = PnnData.objects.filter(
            measurement = measurement_obj,
            id__gt = request.data["request_index"]
        )
        serializer = PnnDataSerializer(pnn_data_obj, many=True)
        print (serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
