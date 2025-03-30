from django.db import models
from users.models import CustomUser


# Create your models here.

class Location(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='locations')
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name