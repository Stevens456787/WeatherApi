# filepath: c:\Users\Rnyamari\CAPSTONE PROJECT\WeatherApi\weather_api\weather\serializers.py
from rest_framework import serializers
from .models import WeatherData  # Ensure this model exists

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'