# ========================================================================
from django.contrib import admin

from app_transaction.pkg_admins.work_note import Work_Note

from app_transaction.pkg_models.work_note import WORK_NOTE

# ========================================================================

admin.site.register(WORK_NOTE, Work_Note)
