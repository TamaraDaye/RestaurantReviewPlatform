from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, CreateUpdateUserSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserModelViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()

    def get_serializer_class(self):  # pyright: ignore[]
        if self.action in {"create", "update", "partial_update"}:
            return CreateUpdateUserSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]
