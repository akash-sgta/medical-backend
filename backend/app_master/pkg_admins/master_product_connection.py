# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.master_product_connection import PRODUCT_CONNECTION


# ========================================================================
class Product_Connection(Change_Log):
    list_display = (
        "id",
        "parent_name",
        "parent_uom",
        "parent_quantity",
        "child_name",
        "child_uom",
        "child_quantity",
    ) + super().list_display
    search_fields = (
        "parent__name__icontains",
        "child__name__icontains",
    )
    list_filter = (
        "parent__name",
        "child__name",
    )

    def parent_name(self, obj):
        return obj.parent.name

    def parent_uom(self, obj):
        return obj.parent_uom.name

    def child_name(self, obj):
        return obj.child.name

    def child_uom(self, obj):
        return obj.child_uom.name

    def created(self, obj):
        return super().created(PRODUCT_CONNECTION.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(PRODUCT_CONNECTION.objects.get(id=obj.id))
