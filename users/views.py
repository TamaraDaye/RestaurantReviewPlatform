from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, CreateUpdateUserSerializer
from django.contrib.auth import get_user_model


class UserModelViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()

    def get_serializer_class(self):
        if self.action in {"create", "update", "partial_update"}:
            return CreateUpdateUserSerializer
        return UserSerializer
