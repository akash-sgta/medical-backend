# ========================================================================
from utility.abstract_admin import Change_Log
from app_cdn.pkg_models.master_file import FILE


# ========================================================================
class File(Change_Log):
    list_display = (
        "id",
        "file_type",
        "name",
    ) + Change_Log.list_display
    search_fields = ("name__icontains",)
    list_filter = Change_Log.list_filter + ("type__name",)

    def file_type(self, obj):
        return "{}".format(obj.type.name)

    def created(self, obj):
        return super().created(FILE.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(FILE.objects.get(id=obj.id))
