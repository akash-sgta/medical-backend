# ========================================================================
from utility.abstract_admin import Change_Log
from app_transaction.pkg_models.work_note import WORK_NOTE


# ========================================================================
class Work_Note(Change_Log):
    list_display = ("req_id", "name", "created", "changed")
    search_fields = ("eng_name__icontains", "local_name__icontains")
    list_filter = ("req__id",)
    readonly_fields = ("created_on", "changed_on", "created_by", "changed_by")

    def req_id(self, obj):
        return "{}".format(obj.req.id)

    def created(self, obj):
        return super().created(WORK_NOTE.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(WORK_NOTE.objects.get(id=obj.id))
