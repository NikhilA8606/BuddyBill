from rest_framework.serializers import ModelSerializer, Serializer

from swc.models import Circle
from users.models import User


class UserSerializer(Serializer):
    class Meta:
        model = User
        fields = ["id", "email", "name"]


class CircleSerializer(ModelSerializer):
    created_by = UserSerializer()

    class Meta:
        model = Circle
        fields = [
            "name",
            "created_by",
            "created_at",
            "updated_at",
            "external_id",
        ]
