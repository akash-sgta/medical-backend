# ========================================================================
from utility.abstract_admin import Change_Log
from app_cdn.pkg_models.check_file_type import FILE_TYPE


# ========================================================================
class File_Type(Change_Log):
    list_display = ("name",) + Change_Log.list_display
    search_fields = ("name__icontains",)

    def created(self, obj):
        return super().created(FILE_TYPE.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(FILE_TYPE.objects.get(id=obj.id))
