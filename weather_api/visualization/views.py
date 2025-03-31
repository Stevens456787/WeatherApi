from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Visualization
from .serializers import VisualizationSerializer
from weather.models import WeatherData
from django.utils import timezone
from datetime import timedelta

class VisualizationViewSet(viewsets.ModelViewSet):
    queryset = Visualization.objects.all()
    serializer_class = VisualizationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter visualizations by the authenticated user's locations
        return Visualization.objects.filter(location__user=self.request.user)

    @action(detail=False, methods=['post'])
    def generate(self, request):
        location_id = request.data.get('location_id')
        date_range = request.data.get('date_range', 7)  # Default to 7 days
        chart_type = request.data.get('chart_type', 'line')
        export_format = request.data.get('export_format', 'json')

        if not location_id:
            return Response({'error': 'location_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Fetch weather data for the chart
            end_date = timezone.now()
            start_date = end_date - timedelta(days=int(date_range))
            weather_data = WeatherData.objects.filter(
                location_id=location_id,
                date__range=[start_date, end_date]
            ).order_by('date')

            if not weather_data.exists():
                return Response({'error': 'No weather data available for this location and range'},
                                status=status.HTTP_404_NOT_FOUND)

            # Prepare Chart.js-compatible data
            chart_data = {
                'labels': [data.date.strftime('%Y-%m-%d %H:%M') for data in weather_data],
                'datasets': [{
                    'label': 'Temperature (°C)',
                    'data': [data.temperature for data in weather_data],
                    'borderColor': 'rgba(75, 192, 192, 1)',
                    'fill': False
                }]
            }

            visualization = Visualization.objects.create(
                location_id=location_id,
                chart_type=chart_type,
                data_range=date_range,
                export_format=export_format,
                data=chart_data
            )
            serializer = VisualizationSerializer(visualization)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
