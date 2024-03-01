# ========================================================================
from app_master.pkg_models.master_product_connection import PRODUCT_CONNECTION
from utility.abstract_serializer import Serializer


# ========================================================================
class Product_Connection(Serializer):
    class Meta:
        model = PRODUCT_CONNECTION
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data["parent"] = f"master/product/{instance.parent.id}"
        except Exception:
            pass
        try:
            data["parent_uom"] = f"master/uom/{instance.parent_uom.id}"
        except Exception:
            pass
        try:
            data["child"] = f"master/product/{instance.child.id}"
        except Exception:
            pass
        try:
            data["child_uom"] = f"master/uom/{instance.child_uom.id}"
        except Exception:
            pass
        return data
