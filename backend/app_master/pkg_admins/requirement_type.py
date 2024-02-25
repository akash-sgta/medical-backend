# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_product_type import (
    REQUIREMENT_TYPE,
    REQUIREMENT_TYPE_T,
)


# ========================================================================
class Requirement_Type(Change_Log):
    list_display = ("name", "created", "changed")
    search_fields = ("name__icontains",)
    readonly_fields = ("created_on", "changed_on", "created_by", "changed_by")

    def created(self, obj):
        return super().created(REQUIREMENT_TYPE.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(REQUIREMENT_TYPE.objects.get(id=obj.id))


class Requirement_Type_T(Change_Log):
    list_display = (
        "req_type_name",
        "language",
        "description",
        "created",
        "changed",
    )
    search_fields = ("req__name__icontains",)
    readonly_fields = ("created_on", "changed_on", "created_by", "changed_by")

    def req_type_name(self, obj):
        result = REQUIREMENT_TYPE_T.objects.get(id=obj.id)
        text = "{}".format(result.req_type.name)
        return text

    def language(self, obj):
        result = REQUIREMENT_TYPE_T.objects.get(id=obj.id)
        text = "{}".format(result.text.lang.eng_name)
        return text

    def description(self, obj):
        result = REQUIREMENT_TYPE_T.objects.get(id=obj.id)
        text = "{}...".format(result.text.text[:32])
        return text

    def created(self, obj):
        return super().created(REQUIREMENT_TYPE_T.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(REQUIREMENT_TYPE_T.objects.get(id=obj.id))
