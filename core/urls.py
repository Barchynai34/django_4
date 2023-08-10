from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="GeekTech",
        default_version="v1",
        description="Пробуем REST",
        terms_of_service="",
        contact=openapi.Contact(email="test@test.com"),
        license=openapi.License(name="No License"),
    ),
    # patterns=[
    #     path("api/", include("myapi.urls")),
    # ],
    public=True,
    permission_classes=(
        [
            permissions.AllowAny,
        ]
    ),
)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
    path("admin/", admin.site.urls),
    path("", include("posts.urls")),
    path("", include("users.urls")),
    path("", include("examples.urls")),
]
