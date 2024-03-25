# ========================================================================
from django.urls import re_path

from app_cdn.pkg_views.check_file_type import (
    File_Type,
    File_Type_Batch,
)
from app_cdn.pkg_views.master_file import File

# ========================================================================

urlpatterns = [
    # ------------------------------------------------------
    # CHECK
    # ------------------------------------------------------
    re_path(
        r"check/file_type/(?P<pk>\d*)$",
        File_Type.as_view(),
        name="Check_File_Type",
    ),
    re_path(
        r"check/file_type/batch/$",
        File_Type_Batch.as_view(),
        name="Check_File_Type_Batch",
    ),
    # ------------------------------------------------------
    # MASTER
    # ------------------------------------------------------
    re_path(
        r"master/file/(?P<pk>\d*)$",
        File.as_view(),
        name="Master_File",
    ),
]
