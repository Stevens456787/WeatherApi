import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from weather.models import WeatherData
from django.utils import timezone

def generate_temperature_chart(location_id, date_range):
    end_date = timezone.now()
    start_date = end_date - timedelta(days=int(date_range))
    
    weather_data = WeatherData.objects.filter(
        location_id=location_id,
        date__range=[start_date, end_date]
    ).order_by('date')
    
    dates = [data.date for data in weather_data]
    temps = [data.temperature for data in weather_data]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temps, marker='o')
    plt.title('Temperature Trend')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    
    # Save to buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()
    
    # Convert to base64
    image_base64 = base64.b64encode(image_png).decode('utf-8')
    return image_base64