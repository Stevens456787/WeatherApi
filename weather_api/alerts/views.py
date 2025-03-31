from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Alert
from .serializers import AlertSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

    def get_permissions(self):
        # Only admins can create, update, or delete alerts
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdminUser()]
        # Any authenticated user can view alerts
        return [IsAuthenticated()]

    def get_queryset(self):
        # Filter alerts by the authenticated user's locations
        return Alert.objects.filter(location__user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the alert with the user's location
        serializer.save()
