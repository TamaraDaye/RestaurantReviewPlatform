from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "created_at"]


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user
