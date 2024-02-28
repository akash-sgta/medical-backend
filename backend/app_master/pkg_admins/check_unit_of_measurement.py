# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_unit_of_measurement import UOM


# ========================================================================
class UOM(Change_Log):
    list_display = (
        "unit_name",
        "name",
    ) + super().list_display
    search_fields = (
        "unit__name__icontains",
        "name__icontains",
    )
    list_filter = ("unit__name",) + super().list_filter

    def unit_name(self, obj):
        return obj.unit.name

    def created(self, obj):
        return super().created(UOM.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(UOM.objects.get(id=obj.id))
