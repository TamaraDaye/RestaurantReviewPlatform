from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers import CreateUpdateUserSerializer, UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import Http404
import logging

logger = logging.getLogger("app")


class UserDetailView(APIView):
    """
    View for handling specific user in detail
    *Requires user to be authentication
    """

    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)

        except User.DoesNotExist:
            logger.info("specified user not found")
            raise Http404()

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = CreateUpdateUserSerializer(user, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
