from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import UserFriend

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "external_id",
            "name",
            "email",
            "is_active",
        )


class UserFriendSerializer(serializers.ModelSerializer):
    friend = UserSerializer(read_only=True)

    class Meta:
        model = UserFriend
        fields = (
            "external_id",
            "friend",
        )
