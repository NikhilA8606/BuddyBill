from django.urls import include, path
from rest_framework import routers
from swc.views import CircleViewSet

swc_router = (
    routers.SimpleRouter()
)  # default router & simplerouter are present , default router is mostly used for debugging purpose

swc_router.register("circles", CircleViewSet)

urlpatterns = [
    path("", include(swc_router.urls))
]
