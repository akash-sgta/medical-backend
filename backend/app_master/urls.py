# ========================================================================
from django.urls import re_path

from app_master.pkg_views.check_city import City
from app_master.pkg_views.check_language import Language
from app_master.pkg_views.master_text import Text

# ========================================================================

urlpatterns = [
    re_path(
        r"language/(?P<pk>\d*)$",
        Language.as_view(),
        name="Check_Language",
    ),
    re_path(
        r"city/(?P<pk>\d*)$",
        City.as_view(),
        name="Check_City",
    ),
    re_path(
        r"text/(?P<pk>\d*)$",
        Text.as_view(),
        name="Master_Text",
    ),
]
