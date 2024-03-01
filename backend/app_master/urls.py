# ========================================================================
from django.urls import re_path

from app_master.pkg_views.check_city import City
from app_master.pkg_views.check_continent import Continent
from app_master.pkg_views.check_country import Country
from app_master.pkg_views.check_currency import Currency
from app_master.pkg_views.check_language import Language
from app_master.pkg_views.check_product_type import (
    Product_Type,
    Product_Type_T,
)
from app_master.pkg_views.check_state import State
from app_master.pkg_views.master_text import Text

# ========================================================================

urlpatterns = [
    re_path(
        r"city/(?P<pk>\d*)$",
        City.as_view(),
        name="Check_City",
    ),
    re_path(
        r"continent/(?P<pk>\d*)$",
        Continent.as_view(),
        name="Check_Continent",
    ),
    re_path(
        r"country/(?P<pk>\d*)$",
        Country.as_view(),
        name="Check_Country",
    ),
    re_path(
        r"currency/(?P<pk>\d*)$",
        Currency.as_view(),
        name="Check_Currency",
    ),
    re_path(
        r"language/(?P<pk>\d*)$",
        Language.as_view(),
        name="Check_Language",
    ),
    re_path(
        r"product_type/(?P<pk>\d*)$",
        Product_Type.as_view(),
        name="Check_Product_Type",
    ),
    re_path(
        r"product_type/text/(?P<pk>\d*)$",
        Product_Type_T.as_view(),
        name="Check_Product_Type_T",
    ),
    re_path(
        r"state/(?P<pk>\d*)$",
        State.as_view(),
        name="Check_State",
    ),
    re_path(
        r"text/(?P<pk>\d*)$",
        Text.as_view(),
        name="Master_Text",
    ),
]
