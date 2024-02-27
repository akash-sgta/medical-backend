# ========================================================================
from django.contrib import admin

from app_master.pkg_admins.requirement_type import (
    Requirement_Type,
    Requirement_Type_T,
)
from app_master.pkg_admins.check_product_type import Requirement, Requirement_T
from app_master.pkg_admins.requirement_connection import (
    Requirement_Connection,
)
from app_master.pkg_admins.check_language import Language
from app_master.pkg_admins.text import Text

from app_master.pkg_models.check_product_type import (
    REQUIREMENT_TYPE,
    REQUIREMENT_TYPE_T,
)
from app_master.pkg_models.master_product import REQUIREMENT, REQUIREMENT_T
from app_master.pkg_models.requirement_connection import (
    REQUIREMENT_CONNECTION,
)
from app_master.pkg_models.check_language import LANGUAGE
from app_master.pkg_models.master_text import TEXT

# ========================================================================

admin.site.register(REQUIREMENT, Requirement)
admin.site.register(REQUIREMENT_T, Requirement_T)
admin.site.register(REQUIREMENT_TYPE, Requirement_Type)
admin.site.register(REQUIREMENT_TYPE_T, Requirement_Type_T)
admin.site.register(REQUIREMENT_CONNECTION, Requirement_Connection)
admin.site.register(LANGUAGE, Language)
admin.site.register(TEXT, Text)
