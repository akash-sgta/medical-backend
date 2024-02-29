# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_product_type import PRODUCT_TYPE, PRODUCT_TYPE_T


# ========================================================================
class Product_Type(Change_Log):
    list_display = ("name",) + Change_Log.list_display
    search_fields = ("name__icontains",)
    list_filter = ("name",) + Change_Log.list_filter

    def created(self, obj):
        return super().created(PRODUCT_TYPE.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(PRODUCT_TYPE.objects.get(id=obj.id))


class Product_Type_T(Change_Log):
    list_display = (
        "id",
        "type_name",
        "language",
        "description",
    ) + Change_Log.list_display
    list_filter = ("type__name",)
    search_fields = ("type__name__icontains",)

    def type_name(self, obj):
        return obj.type.name

    def language(self, obj):
        return obj.text.lang.eng_name

    def description(self, obj):
        return "{}...".format(obj.text.text[:32])

    def created(self, obj):
        return super().created(PRODUCT_TYPE_T.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(PRODUCT_TYPE_T.objects.get(id=obj.id))
