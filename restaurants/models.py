from django.db import models
from django.utils import timezone
from rest_framework.fields import MaxValueValidator, MinValueValidator


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    location = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Review(models.Model):
    comment = models.TextField()
    rating = models.SmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    restaurant = models.ForeignKey("restaurants.Restaurant", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.restaurant} has a {self.rating} star"
