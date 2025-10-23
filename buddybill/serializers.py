from rest_framework.serializers import ModelSerializer, Serializer

from buddybill.models import BuddyGroup
from users.models import User


class UserSerializer(Serializer):
    class Meta:
        model = User
        fields = ["id", "email", "name"]


class BuddyGroupSerializer(ModelSerializer):
    created_by = UserSerializer()

    class Meta:
        model = BuddyGroup
        fields = [
            "name",
            "created_by",
            "created_at",
            "updated_at",
            "external_id",
        ]
