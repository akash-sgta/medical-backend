# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.text import TEXT


# ========================================================================
class Text(Change_Log):
    list_display = ("id", "lang_name", "created", "changed")
    search_fields = ("id__icontains",)
    readonly_fields = ("created_on", "changed_on", "created_by", "changed_by")

    def lang_name(self, obj):
        return "{}_{}".format(obj.lang.eng_name, obj.lang.local_name)

    def created(self, obj):
        return super().created(TEXT.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(TEXT.objects.get(id=obj.id))
