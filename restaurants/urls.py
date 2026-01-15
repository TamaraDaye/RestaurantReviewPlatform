from rest_framework import routers
from .views import RestaurantModelViewSet, ReviewModelViewSet

router = routers.DefaultRouter()
router.register(r"restaurants", RestaurantModelViewSet, basename="restaurants")
router.register(r"reviews", ReviewModelViewSet, basename="reviews")

urlpatterns = router.urls
