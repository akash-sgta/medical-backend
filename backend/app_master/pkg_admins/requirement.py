# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.master_product import REQUIREMENT, REQUIREMENT_T


# ========================================================================
class Requirement(Change_Log):
    list_display = ("type__name", "name", "created", "changed")
    list_filter = ("type__name",)
    search_fields = ("name__icontains",)
    readonly_fields = ("created_on", "changed_on", "created_by", "changed_by")

    def type__name(self, obj):
        result = REQUIREMENT.objects.get(id=obj.id)
        text = "{}".format(result.type.name)
        return text

    def created(self, obj):
        return super().created(REQUIREMENT.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(REQUIREMENT.objects.get(id=obj.id))


class Requirement_T(Change_Log):
    list_display = (
        "req_name",
        "language",
        "description",
        "created",
        "changed",
    )
    list_filter = ("req__id",)
    search_fields = ("req__name__icontains",)
    readonly_fields = ("created_on", "changed_on", "created_by", "changed_by")

    def req_name(self, obj):
        result = REQUIREMENT_T.objects.get(id=obj.id)
        text = "{}".format(result.req.name)
        return text

    def language(self, obj):
        result = REQUIREMENT_T.objects.get(id=obj.id)
        text = "{}".format(result.text.lang.eng_name)
        return text

    def description(self, obj):
        result = REQUIREMENT_T.objects.get(id=obj.id)
        text = "{}...".format(result.text.text[:32])
        return text

    def created(self, obj):
        return super().created(REQUIREMENT_T.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(REQUIREMENT_T.objects.get(id=obj.id))
