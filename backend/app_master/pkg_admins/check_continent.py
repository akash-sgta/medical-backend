# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_continent import CONTINENT


# ========================================================================
class Continent(Change_Log):
    list_display = (
        "eng_name",
        "local_name",
    ) + Change_Log.list_display
    search_fields = (
        "eng_name__icontains",
        "local_name__icontains",
    )

    def created(self, obj):
        return super().created(CONTINENT.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(CONTINENT.objects.get(id=obj.id))
