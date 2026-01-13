from rest_framework import routers
from .views import UserModelViewSet

router = routers.DefaultRouter()
router.register(r"users", UserModelViewSet, basename="users")

urlpatterns = router.urls
