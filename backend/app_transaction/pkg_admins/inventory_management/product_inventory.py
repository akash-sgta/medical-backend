# ========================================================================
from utility.abstract_admin import Change_Log
from app_transaction.pkg_models.inventory_management.product_inventory import (
    PRODUCT_INVENTORY_SUMMARY,
    PRODUCT_INVENTORY_ITEM,
)


# ========================================================================
class Product_Inventory_Summary(Change_Log):
    list_display = (
        "buyer",
        "id",
    ) + Change_Log.list_display
    search_fields = ("buyer__email__icontains",)
    list_filter = ("buyer__email",)
    ordering = (
        "buyer",
        "-id",
    )

    def created(self, obj):
        return super().created(PRODUCT_INVENTORY_SUMMARY.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(PRODUCT_INVENTORY_SUMMARY.objects.get(id=obj.id))


class Product_Inventory_Item(Change_Log):
    list_display = (
        "summary",
        "product",
        "id",
    ) + Change_Log.list_display
    search_fields = (
        "summary__buyer__email__icontains",
        "product__eng_name",
    )
    list_filter = ("summary__buyer__email",)
    ordering = (
        "summary",
        "product",
        "-id",
    )

    def created(self, obj):
        return super().created(PRODUCT_INVENTORY_ITEM.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(PRODUCT_INVENTORY_ITEM.objects.get(id=obj.id))
