# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_currency import CURRENCY


# ========================================================================
class Currency(Change_Log):
    list_display = (
        "code",
        "eng_name",
        "local_name",
        "symbol",
    ) + Change_Log.list_display
    search_fields = (
        "code__icontains",
        "eng_name__icontains",
        "local_name__icontains",
        "symbol__icontains",
    )

    def created(self, obj):
        return super().created(CURRENCY.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(CURRENCY.objects.get(id=obj.id))
