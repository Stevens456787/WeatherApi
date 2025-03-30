from django.db import models
from locations.models import Location

# Create your models here.
class Visualization(models.Model):
    CHART_TYPES = [
        ('line', 'Line Chart'),
        ('bar', 'Bar Chart'),
        ('pie', 'Pie Chart'),
        ('scatter', 'Scatter Plot'),
    ]
    EXPORT_FORMATS = [
        ('csv', 'CSV'),
        ('json', 'JSON'),
        ('xlsx', 'XLSX'),
    ]
    
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    chart_type = models.CharField(max_length=10, choices=CHART_TYPES)
    data_range = models.JSONField()  # Store chart data in JSON format
    export_format = models.CharField(max_length=10, choices=EXPORT_FORMATS)
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()  # Store chart data in JSON format