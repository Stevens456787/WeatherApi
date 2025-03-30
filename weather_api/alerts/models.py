from django.db import models
from locations.models import Location

# Create your models here.


class Alert(models.Model):
    SEVERITY_CHOICES = [
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high'),
    ]
    
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='alerts')
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    description = models.TextField()
    triggered_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.location.name} - {self.severity} - {self.triggered_at}"