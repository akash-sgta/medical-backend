# ========================================================================
from django.urls import re_path

from app_master.pkg_views.language import Language
from app_master.pkg_views.text import Text

# ========================================================================

urlpatterns = [
    re_path(
        r"language/(?P<pk>\d*)",
        Language.as_view(),
        name="Master_Language",
    ),
    re_path(
        r"text/(?P<pk>\d*)",
        Text.as_view(),
        name="Master_Text",
    ),
]
