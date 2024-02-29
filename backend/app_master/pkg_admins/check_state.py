# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_state import STATE


# ========================================================================
class State(Change_Log):
    list_display = (
        "country_name",
        "eng_name",
    ) + Change_Log.list_display
    search_fields = (
        "country__eng_name__icontains",
        "eng_name__icontains",
    )
    list_filter = ("country__eng_name",) + Change_Log.list_filter

    def country_name(self, obj):
        return obj.country.eng_name

    def created(self, obj):
        return super().created(STATE.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(STATE.objects.get(id=obj.id))
