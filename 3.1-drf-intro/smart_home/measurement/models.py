from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='mesurement', on_delete=models.CASCADE, null=False)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
