from django.db import models
from django.utils import timezone


# Create your models here.
class Restaurant:
    name = models.CharField(max_length=200)
    location = models.TextField()
    capacity = models.IntegerField()


class Review:
    comment = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    restaurant = models.ForeignKey("restaurant.Restaurant", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "restaurant"], name="unique_user_restaurant_review"
            )
        ]
