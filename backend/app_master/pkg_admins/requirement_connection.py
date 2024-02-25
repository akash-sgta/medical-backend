# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.requirement_connection import (
    REQUIREMENT_CONNECTION,
)


# ========================================================================
class Requirement_Connection(Change_Log):
    list_display = (
        "parent_requirement",
        "child_requirement",
        "created",
        "changed",
    )
    search_fields = (
        "parent_req__name__icontains",
        "child_req__name__icontains",
    )
    list_filter = ("parent_req__id",)
    readonly_fields = ("created_on", "changed_on", "created_by", "changed_by")

    def parent_requirement(self, obj):
        return "[{}] [{}] {}".format(
            obj.parent_req.id, obj.parent_req.type.name, obj.parent_req.name
        )

    def child_requirement(self, obj):
        return "[{}] [{}] {}".format(
            obj.child_req.id, obj.child_req.type.name, obj.child_req.name
        )

    def created(self, obj):
        return super().created(REQUIREMENT_CONNECTION.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(REQUIREMENT_CONNECTION.objects.get(id=obj.id))
