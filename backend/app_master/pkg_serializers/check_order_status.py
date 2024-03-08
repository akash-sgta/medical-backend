# ========================================================================
from app_master.pkg_models.check_order_status import (
    SALES_ORDER_STATUS,
    INVENTORY_ORDER_STATUS,
)
from utility.abstract_serializer import Serializer


# ========================================================================
class Sales_Order_Status(Serializer):
    class Meta:
        model = SALES_ORDER_STATUS
        fields = "__all__"
        extra_kwargs = Serializer().extra()


class Inventory_Order_Status(Serializer):
    class Meta:
        model = INVENTORY_ORDER_STATUS
        fields = "__all__"
        extra_kwargs = Serializer().extra()
