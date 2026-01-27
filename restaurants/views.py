from rest_framework.viewsets import ModelViewSet
from .serializers import RestaurantSerializer, ReviewSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .models import Restaurant, Review
import rabbit.producer
# Create your views here.


class RestaurantModelViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_permissions(self):
        if self.action not in ["destroy", "create"]:
            return [IsAuthenticated()]
        return [IsAdminUser()]


class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action not in ["destroy", "create"]:
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
