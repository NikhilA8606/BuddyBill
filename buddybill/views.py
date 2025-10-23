from rest_framework.viewsets import ModelViewSet

from buddybill.models import BuddyGroup
from buddybill.serializers import BuddyGroupSerializer


class BuddyGroupViewSet(ModelViewSet):
    queryset = BuddyGroup.objects.all()
    serializer_class = BuddyGroupSerializer
