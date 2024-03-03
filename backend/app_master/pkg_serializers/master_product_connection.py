# ========================================================================
from app_master.pkg_models.master_product_connection import PRODUCT_CONNECTION
from utility.abstract_serializer import Serializer


# ========================================================================
class Product_Connection(Serializer):
    """
    Serializer for Product_Connection model.
    """

    class Meta:
        """
        Metadata for Product_Connection serializer.
        """

        model = PRODUCT_CONNECTION
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        """
        Customizes the representation of Product_Connection instances.

        Args:
            instance: The instance of Product_Connection model.

        Returns:
            dict: Customized representation of the instance.
        """
        data = super().to_representation(instance)
        try:
            data["parent"] = f"master/master/product/{instance.parent.id}"
        except Exception:
            pass
        try:
            data["parent_uom"] = f"master/check/uom/{instance.parent_uom.id}"
        except Exception:
            pass
        try:
            data["child"] = f"master/master/product/{instance.child.id}"
        except Exception:
            pass
        try:
            data["child_uom"] = f"master/check/uom/{instance.child_uom.id}"
        except Exception:
            pass
        return data
