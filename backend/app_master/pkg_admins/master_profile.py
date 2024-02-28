# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.master_profile import PROFILE


# ========================================================================
class Profile(Change_Log):
    list_display = (
        "id",
        "email",
        "first_name",
        "middle_name",
        "last_name",
        "phone_number",
        "address_short",
    ) + super().list_display
    search_fields = (
        "cred__email__icontains",
        "first_name__icontains",
        "middle_name__icontains",
        "last_name__icontains",
    )

    def email(self, obj):
        return obj.cred.email

    def address_short(self, obj):
        return obj.address.street[:32]

    def created(self, obj):
        return super().created(PROFILE.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(PROFILE.objects.get(id=obj.id))
