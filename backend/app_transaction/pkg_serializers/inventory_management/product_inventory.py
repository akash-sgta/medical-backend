# ========================================================================
from app_transaction.pkg_models.inventory_management.product_inventory import (
    PRODUCT_INVENTORY_SUMMARY,
    PRODUCT_INVENTORY_ITEM,
)
from utility.abstract_serializer import Serializer


# ========================================================================
class Product_Inventory_Summary(Serializer):
    class Meta:
        model = PRODUCT_INVENTORY_SUMMARY
        fields = "__all__"
        extra_kwargs = Serializer().extra()


class Product_Inventory_Item(Serializer):
    class Meta:
        model = PRODUCT_INVENTORY_ITEM
        fields = "__all__"
        extra_kwargs = Serializer().extra()
