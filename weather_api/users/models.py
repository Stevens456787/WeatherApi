from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class CustomUser(AbstractUser):
    role = models.CharField(max_length=100, default='user', choices=[('user', 'User'), ('admin', 'Admin'), ('Developer', 'Developer')])
    api_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

class Visualization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name