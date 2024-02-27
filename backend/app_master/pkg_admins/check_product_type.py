# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_product_type import PRODUCT_TYPE, PRODUCT_TYPE_T


# ========================================================================
class Product_Type(Change_Log):
    list_display = ("name",) + super().list_display
    list_filter = ("name",)
    search_fields = ("name__icontains",)

    def created(self, obj):
        return super().created(PRODUCT_TYPE.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(PRODUCT_TYPE.objects.get(id=obj.id))


class Product_Type_T(Change_Log):
    list_display = (
        "type_name",
        "language",
        "description",
        "created",
        "changed",
    )
    list_filter = ("req__id",)
    search_fields = ("req__name__icontains",)
    readonly_fields = ("created_on", "changed_on", "created_by", "changed_by")

    def type_name(self, obj):
        return PRODUCT_TYPE_T.objects.get(id=obj.id).type.name

    def language(self, obj):
        return PRODUCT_TYPE_T.objects.get(id=obj.id).text.lang.eng_name

    def description(self, obj):
        return "{}...".format(PRODUCT_TYPE_T.objects.get(id=obj.id).text.text[:32])

    def created(self, obj):
        return super().created(PRODUCT_TYPE_T.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(PRODUCT_TYPE_T.objects.get(id=obj.id))
