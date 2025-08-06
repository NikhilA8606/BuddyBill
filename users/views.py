from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import GenericViewSet

from . import permissions
from .models import User, UserFriend
from .serializers import UserSerializer, UserFriendSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.UserPermission,)
    lookup_field = "external_id"


class FriendsViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = UserFriend.objects.all()
    serializer_class = UserFriendSerializer
    lookup_field = "external_id"

    def get_user_obj(self):
        return get_object_or_404(User, external_id=self.kwargs.get("users_external_id"))

    def get_queryset(self):
        user = self.get_user_obj()
        qs = super().get_queryset().filter(user=user)
        return qs
