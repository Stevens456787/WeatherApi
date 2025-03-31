from django.db import models
from locations.models import Location

# Create your models here.

class WeatherData(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    date = models.DateField()
    conditions = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"WeatherData at {self.date}"