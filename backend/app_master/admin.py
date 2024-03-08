# ========================================================================
from django.contrib import admin

from app_master.pkg_admins.check_city import City
from app_master.pkg_admins.check_continent import Continent
from app_master.pkg_admins.check_country import Country
from app_master.pkg_admins.check_currency import Currency
from app_master.pkg_admins.check_product_type import Product_Type, Product_Type_T
from app_master.pkg_admins.check_state import State
from app_master.pkg_admins.check_unit import Unit
from app_master.pkg_admins.check_unit_of_measurement import Uom
from app_master.pkg_admins.master_address import Address
from app_master.pkg_admins.master_credential import Credential
from app_master.pkg_admins.master_product import Product
from app_master.pkg_admins.master_product_connection import Product_Connection
from app_master.pkg_admins.master_profile import Profile
from app_master.pkg_admins.master_text import Text
from app_master.pkg_admins.master_company import Company

from app_master.pkg_models.master_company import COMPANY
from app_master.pkg_models.check_city import CITY
from app_master.pkg_models.check_continent import CONTINENT
from app_master.pkg_models.check_country import COUNTRY
from app_master.pkg_models.check_currency import CURRENCY
from app_master.pkg_models.check_product_type import PRODUCT_TYPE, PRODUCT_TYPE_T
from app_master.pkg_models.check_state import STATE
from app_master.pkg_models.check_unit import UNIT
from app_master.pkg_models.check_unit_of_measurement import UOM
from app_master.pkg_models.master_address import ADDRESS
from app_master.pkg_models.master_credential import CREDENTIAL
from app_master.pkg_models.master_product import PRODUCT
from app_master.pkg_models.master_product_connection import PRODUCT_CONNECTION
from app_master.pkg_models.master_profile import PROFILE
from app_master.pkg_models.master_text import TEXT


# ========================================================================

admin.site.register(
    COMPANY,
    Company,
)
admin.site.register(
    CONTINENT,
    Continent,
)
admin.site.register(
    CITY,
    City,
)

admin.site.register(
    COUNTRY,
    Country,
)
admin.site.register(
    CURRENCY,
    Currency,
)
admin.site.register(
    PRODUCT_TYPE,
    Product_Type,
)
admin.site.register(
    PRODUCT_TYPE_T,
    Product_Type_T,
)
admin.site.register(
    STATE,
    State,
)
admin.site.register(
    UNIT,
    Unit,
)
admin.site.register(
    UOM,
    Uom,
)
admin.site.register(
    ADDRESS,
    Address,
)
admin.site.register(
    CREDENTIAL,
    Credential,
)
admin.site.register(
    PRODUCT,
    Product,
)
admin.site.register(
    PRODUCT_CONNECTION,
    Product_Connection,
)
admin.site.register(
    PROFILE,
    Profile,
)
admin.site.register(
    TEXT,
    Text,
)
