# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.master_credential import CREDENTIAL


# ========================================================================
class Credential(Change_Log):
    list_display = (
        "email",
        "is_admin",
        "is_internal_user",
        "is_external_user",
    ) + Change_Log.list_display
    search_fields = ("email__icontains",)
    list_filter = (
        "is_admin",
        "is_internal_user",
        "is_external_user",
    ) + Change_Log.list_filter

    def created(self, obj):
        return super().created(CREDENTIAL.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(CREDENTIAL.objects.get(id=obj.id))
