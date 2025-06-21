from django.test import TestCase

from ..models import Group
from .factories import GroupFactory


class GroupTestCase(TestCase):
    def test_create_group(self):
        """Test that Group can be created using its factory."""

        obj = GroupFactory()
        assert Group.objects.all().get() == obj
