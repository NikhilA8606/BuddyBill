from django.urls import include, path
from rest_framework import routers

from users.urls import users_router
from buddybill.urls import buddybill_router

router = routers.DefaultRouter()
router.registry.extend(buddybill_router.registry)
router.registry.extend(users_router.registry)

urlpatterns = [
    path("api/docs/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/register/", include("dj_rest_auth.registration.urls")),
    path("api/v1/", include("openapi.urls")),
    path("api/v1/", include(router.urls)),
]
