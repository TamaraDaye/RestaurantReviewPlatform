from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.username} {self.email} {self.password} {self.created_at}"
