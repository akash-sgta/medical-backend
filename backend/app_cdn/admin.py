# ========================================================================
from django.contrib import admin

from app_cdn.pkg_admins.file_type import File_Type
from app_cdn.pkg_admins.file import File

from app_cdn.pkg_models.file_type import FILE_TYPE
from app_cdn.pkg_models.file import FILE

# ========================================================================

admin.site.register(FILE_TYPE, File_Type)
admin.site.register(FILE, File)
