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
from app_master.pkg_views.check_unit import Unit
from app_master.pkg_views.check_unit_of_measurement import Uom
from app_master.pkg_views.master_address import Address
from app_master.pkg_views.master_credential import Credential
from app_master.pkg_views.master_product import Product
from app_master.pkg_views.master_product_connection import Product_Connection
from app_master.pkg_views.master_profile import Profile
from app_master.pkg_views.master_text import Text

# ========================================================================

urlpatterns = [
    re_path(
        r"check/city/(?P<pk>\d*)$",
        City.as_view(),
        name="Check_City",
    ),
    re_path(
        r"check/continent/(?P<pk>\d*)$",
        Continent.as_view(),
        name="Check_Continent",
    ),
    re_path(
        r"check/country/(?P<pk>\d*)$",
        Country.as_view(),
        name="Check_Country",
    ),
    re_path(
        r"check/currency/(?P<pk>\d*)$",
        Currency.as_view(),
        name="Check_Currency",
    ),
    re_path(
        r"check/language/(?P<pk>\d*)$",
        Language.as_view(),
        name="Check_Language",
    ),
    re_path(
        r"check/product_type/(?P<pk>\d*)$",
        Product_Type.as_view(),
        name="Check_Product_Type",
    ),
    re_path(
        r"check/product_type/text/(?P<pk>\d*)$",
        Product_Type_T.as_view(),
        name="Check_Product_Type_T",
    ),
    re_path(
        r"check/state/(?P<pk>\d*)$",
        State.as_view(),
        name="Check_State",
    ),
    re_path(
        r"check/unit/(?P<pk>\d*)$",
        Unit.as_view(),
        name="Check_Unit",
    ),
    re_path(
        r"check/uom/(?P<pk>\d*)$",
        Uom.as_view(),
        name="Check_Uom",
    ),
    re_path(
        r"master/address/(?P<pk>\d*)$",
        Address.as_view(),
        name="Master_Address",
    ),
    re_path(
        r"master/credential/(?P<pk>\d*)$",
        Credential.as_view(),
        name="Master_Credential",
    ),
    re_path(
        r"master/product/(?P<pk>\d*)$",
        Product.as_view(),
        name="Master_Product",
    ),
    re_path(
        r"master/product_connection/(?P<pk>\d*)$",
        Product_Connection.as_view(),
        name="Master_Product_Connection",
    ),
    re_path(
        r"master/profile/(?P<pk>\d*)$",
        Profile.as_view(),
        name="Master_Profile",
    ),
    re_path(
        r"master/text/(?P<pk>\d*)$",
        Text.as_view(),
        name="Master_Text",
    ),
]
