from rest_framework import serializers
from .models import Visualization, Location

class VisualizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visualization
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'