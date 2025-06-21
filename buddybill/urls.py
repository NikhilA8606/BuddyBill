from rest_framework import routers

from .views import (
    GroupViewSet,
)

buddybill_router = routers.SimpleRouter()
buddybill_router.register(r"buddybill/group", GroupViewSet)
