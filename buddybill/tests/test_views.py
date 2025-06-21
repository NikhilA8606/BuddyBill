from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch

from users.tests.factories import UserFactory
from .factories import GroupFactory
from ..serializers import GroupSerializer


class TestGroup(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = GroupFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Group instances"""

        resp = self.client.get("/api/v1/buddybill/group/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Group collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/buddybill/group/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_list_search(self):
        """Test that Group collection can be searched by"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(
            "/api/v1/buddybill/group/",
            {
                "name__icontains": self.instance.name,
            },
        )
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Group instances"""

        resp = self.client.get(f"/api/v1/buddybill/group/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Group can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/buddybill/group/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Group"""

        resp = self.client.post("/api/v1/buddybill/group/")
        self.assertEqual(resp.status_code, 403)

    @patch("buddybill.views.GroupViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Group"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = GroupSerializer(self.instance).data

        resp = self.client.post("/api/v1/buddybill/group/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Group"""

        resp = self.client.patch(f"/api/v1/buddybill/group/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Group update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(f"/api/v1/buddybill/group/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Group"""

        resp = self.client.delete(f"/api/v1/buddybill/group/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Group deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(f"/api/v1/buddybill/group/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)
