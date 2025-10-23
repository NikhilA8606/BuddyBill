from model_bakery import baker
from rest_framework.test import APITestCase


class APITestBase(APITestCase):

    def create_user(self, **kwargs):
        from users.models import User

        return baker.make(User, **kwargs)

    def create_friendship(self, user, *friends):
        from users.models import UserFriend

        for friend in friends:
            UserFriend.objects.create(user=user, friend=friend)
            UserFriend.objects.create(user=friend, friend=user)
