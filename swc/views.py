from rest_framework.viewsets import ModelViewSet
from swc.models import Circle
from swc.serializers import CircleSerializer



class CircleViewSet(ModelViewSet):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer
