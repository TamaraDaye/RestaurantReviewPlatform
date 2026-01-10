from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, CreateUserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model()
    lookup_field = get_user_model().pk

    def create(self, request):
        input_serializer = self.get_serializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        self.perform_create(input_serializer)

        output_serializer = UserSerializer(input_serializer.instance)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        user = get_object_or_404(self.get_queryset(), pk=pk)

        output_serializer = CreateUserSerializer(user)

        return Response(output_serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        users = get_list_or_404(self.get_queryset())
        output_serializer = CreateUserSerializer(users, many=True)
        return Response(output_serializer.data, status=status.HTTP_200_OK)


user_create = UserViewSet.as_view({"post": "create"})
get_user = UserViewSet.as_view({"get": "retrieve"})
list_user = UserViewSet.as_view({"get": "list"})
