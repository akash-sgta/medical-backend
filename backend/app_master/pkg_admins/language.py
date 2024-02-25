# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_language import LANGUAGE


# ========================================================================
class Language(Change_Log):
    list_display = ("eng_name", "local_name", "created", "changed")
    search_fields = ("eng_name__icontains", "local_name__icontains")
    readonly_fields = ("created_on", "changed_on", "created_by", "changed_by")

    def created(self, obj):
        return super().created(LANGUAGE.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(LANGUAGE.objects.get(id=obj.id))
