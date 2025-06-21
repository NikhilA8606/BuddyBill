from django.contrib.auth import get_user_model
import factory
from factory.django import DjangoModelFactory

from ..models import Group

User = get_user_model()


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Faker("bs")
    description = factory.Faker("text")
