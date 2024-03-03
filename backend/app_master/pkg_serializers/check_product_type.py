# ========================================================================
from app_master.pkg_models.check_product_type import PRODUCT_TYPE, PRODUCT_TYPE_T
from utility.abstract_serializer import Serializer


# ========================================================================
class Product_Type(Serializer):
    """
    Serializer for Product_Type model.
    """

    class Meta:
        """
        Metadata for Product_Type serializer.
        """

        model = PRODUCT_TYPE
        fields = "__all__"
        extra_kwargs = Serializer().extra()


class Product_Type_T(Serializer):
    """
    Serializer for Product_Type_T model.
    """

    class Meta:
        """
        Metadata for Product_Type_T serializer.
        """

        model = PRODUCT_TYPE_T
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        """
        Customizes the representation of Product_Type_T instances.

        Args:
            instance: The instance of Product_Type_T model.

        Returns:
            dict: Customized representation of the instance.
        """
        data = super().to_representation(instance)
        try:
            data["type"] = f"/master/check/product_type/{instance.type.id}"
        except Exception:
            pass
        try:
            data["lang"] = f"/master/check/language/{instance.lang.id}"
        except Exception:
            pass
        try:
            data["text"] = f"/master/check/text/{instance.text.id}"
        except Exception:
            pass
        return data
