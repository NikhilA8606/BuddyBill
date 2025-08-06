from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from users.urls import urlpatterns as users_urlpatterns

schema_view = get_schema_view(
    openapi.Info(
        title="BuddyBill API",
        default_version="v1",
        description="Split money app",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api/docs/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/register/", include("dj_rest_auth.registration.urls")),
    path("api/v1/", include("openapi.urls")),
    path("api/v1/", include(users_urlpatterns)),
]
