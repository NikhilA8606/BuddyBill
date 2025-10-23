from django.urls import include, path
from rest_framework import routers

from buddybill.views import BuddyGroupViewSet

buddybill_router = (
    routers.SimpleRouter()
)  # default router & simplerouter are present , default router is mostly used for debugging purpose

buddybill_router.register("groups", BuddyGroupViewSet)

urlpatterns = [
    path(
        "",
        include(buddybill_router.urls),
    )
]
