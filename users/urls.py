from django.urls import include, path
from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

from .views import UserViewSet, FriendsViewSet

router = routers.SimpleRouter()

router.register(r"users", UserViewSet, basename="user")

users_router = NestedSimpleRouter(router, r"users", lookup="users")
users_router.register("friends", FriendsViewSet, basename="friends")

app_name = "users"
urlpatterns = [
    path("", include(router.urls)),
    path("", include(users_router.urls)),
]
