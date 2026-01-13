from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username} {self.email} {self.password} {self.created_at}"
