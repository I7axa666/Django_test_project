# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView, CreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerialaizer, MeasurementSerializer, SensorDetailSerializer


class SensorsAPIView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        sensors_list = SensorSerialaizer(sensors, many=True)
        return Response(sensors_list.data)
#
#     def post(self, request):
#         serializer = SensorSerialaizer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'errot': 'Method PUT not allowed'})
#
#         try:
#             instance = Sensor.objects.get(pk=pk)
#         except:
#             return Response({'errot': 'Object does not exists'})
#
#         serializer = SensorSerialaizer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})

class SensorListCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialaizer

class SensorUpdateAPIView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialaizer

class SensorAPIDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialaizer

class MeasurementCreateAPIView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class SensorAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer