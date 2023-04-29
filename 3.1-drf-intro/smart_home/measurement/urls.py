from django.urls import path

from measurement.serializers import SensorDetailSerializer
from measurement.views import ListCreateAPIView, SensorListCreateAPIView, SensorUpdateAPIView, SensorAPIDetailView, \
    SensorsAPIView, MeasurementCreateAPIView, SensorAPIDetailView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorListCreateAPIView.as_view()),
    # path('sensors/<int:pk>/', SensorUpdateAPIView.as_view()),
    path('measurements/', MeasurementCreateAPIView.as_view()),
    path('sensors/<int:pk>/',  SensorAPIDetailView.as_view()),
    # path('change_info/<pk>/', RetrieveUpdateAPIView),
    # path('add/', RetrieveUpdateAPIView),

]
