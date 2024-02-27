# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_unit import UNIT


# ========================================================================
class Unit(Change_Log):
    list_display = ("name",) + super().list_display
    search_fields = ("name__icontains",)

    def created(self, obj):
        return super().created(UNIT.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(UNIT.objects.get(id=obj.id))
