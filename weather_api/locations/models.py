from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class CustomUser(AbstractUser):
    role = models.CharField(max_length=100, default='user', choices=[('user', 'User'), ('admin', 'Admin'), ('staff', 'Staff')])
    api_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)