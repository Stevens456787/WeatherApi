from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import WeatherData
from .serializers import WeatherDataSerializer
from rest_framework.permissions import IsAuthenticated
import requests
from django.conf import settings

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def current(self, request):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        
        if not lat or not lon:
            return Response({'error': 'Latitude and longitude are required'}, 
                            status=status.HTTP_400_BAD_REQUEST)

        # Fetch data from OpenWeatherMap
        api_key = settings.OPENWEATHERMAP_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            weather_data = {
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'conditions': data['weather'][0]['description']
            }
            return Response(weather_data, status=status.HTTP_200_OK)
            
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
