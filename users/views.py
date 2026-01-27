from rest_framework.viewsets import ViewSet
from .serializers import UserSerializer, CreateUpdateUserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404

from users import serializers


class UserViewSet(ViewSet):
    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser]
        else:


    def list(self, request):
        queryset = get_user_model().objects.all()
        serializers = UserSerializer(queryset, many=True)
