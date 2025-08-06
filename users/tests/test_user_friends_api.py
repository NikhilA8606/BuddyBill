from django.urls import reverse
from rest_framework import status

from utils.tests import BuddyBillAPITestBase


class TestUserFriendsApi(BuddyBillAPITestBase):
    def setUp(self):
        super().setUp()
        self.user = self.create_user()
        self.friend = self.create_user()
        self.create_friendship(self.user, self.friend)
        self.client.force_authenticate(user=self.user)
        self.base_url = reverse(
            "friends-list", kwargs={"users_external_id": self.user.external_id}
        )

    def test_list_friends(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
