# ========================================================================
from app_master.pkg_models.master_product import PRODUCT
from utility.abstract_serializer import Serializer


# ========================================================================
class Product(Serializer):
    """
    Serializer for Product model.
    """

    class Meta:
        """
        Metadata for Product serializer.
        """

        model = PRODUCT
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        """
        Customizes the representation of Product instances.

        Args:
            instance: The instance of Product model.

        Returns:
            dict: Customized representation of the instance.
        """
        data = super().to_representation(instance)
        try:
            data["type"] = f"master/check/product_type/{instance.type.id}"
        except Exception:
            pass
        try:
            data["image_01"] = f"cdn/master/file/{instance.image_01.id}"
        except Exception:
            pass
        try:
            data["image_02"] = f"cdn/master/file/{instance.image_02.id}"
        except Exception:
            pass
        try:
            data["image_03"] = f"cdn/master/file/{instance.image_03.id}"
        except Exception:
            pass
        try:
            data["description"] = f"master/master/text/{instance.description.id}"
        except Exception:
            pass
        try:
            data["storage_instructions"] = (
                f"master/master/text/{instance.storage_instructions.id}"
            )
        except Exception:
            pass
        try:
            data["side_effects"] = f"master/master/text/{instance.side_effects.id}"
        except Exception:
            pass
        try:
            data["warnings_precautions"] = (
                f"master/master/text/{instance.warnings_precautions.id}"
            )
        except Exception:
            pass
        return data
