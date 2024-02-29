# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_city import CITY


# ========================================================================
class City(Change_Log):
    list_display = (
        "state",
        "eng_name",
        "local_name",
    ) + super(Change_Log).list_display
    search_fields = ("eng_name__icontains", "local_name__icontains")

    def created(self, obj):
        return super().created(CITY.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(CITY.objects.get(id=obj.id))
