# ========================================================================
from django.contrib import admin
from django.urls import re_path, include
from utility.methods import check_server_status

# ========================================================================

urlpatterns = [
    re_path(r"^site_admin/", admin.site.urls, name="DJANGO_ADMIN"),
    re_path(
        r"^check_server/",
        check_server_status,
        name="CHECK_SERVER_STATUS",
    ),
    re_path(r"^master/", include("app_master.urls")),
]
