# ========================================================================
from django.contrib import admin
from django.urls import re_path, include
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

from utility.methods import check_server_status

# ========================================================================
schema_view = get_schema_view(
    openapi.Info(
        title="Medical",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r"^site_admin/", admin.site.urls, name="DJANGO_ADMIN"),
    re_path(
        r"^check_server/",
        check_server_status,
        name="CHECK_SERVER_STATUS",
    ),
    re_path(r"^master/", include("app_master.urls")),
    re_path(r"^cdn/", include("app_cdn.urls")),
    re_path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
