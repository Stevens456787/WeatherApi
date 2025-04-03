from django.test import TestCase
from .models import Alert
from django.contrib.auth import get_user_model
from locations.models import Location

class AlertModelTest(TestCase):
    def test_alert_creation(self):
        
        User = get_user_model()
        # create a dummy user
        user = User.objects.create_user(username="testuser", password="password123")
        
        
        # Create a dummy Location instance
        location = Location.objects.create(name="Test Location", latitude=0.0, longitude=0.0, user = user)
        
        # Create an Alert instance
        alert = Alert.objects.create(
            location=location,
            severity="high",
            description="Test alert description",
        )
        
        # Assert that the alert was created successfully
        self.assertEqual(alert.severity, "high")
        self.assertTrue(alert.is_active)
# Create your tests here.
