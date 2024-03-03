# ========================================================================
from app_master.pkg_models.check_unit_of_measurement import UOM
from utility.abstract_serializer import Serializer


# ========================================================================
class Uom(Serializer):
    """
    Serializer for UOM model.
    """

    class Meta:
        """
        Metadata for Uom serializer.
        """

        model = UOM
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        """
        Customizes the representation of UOM instances.

        Args:
            instance: The instance of UOM model.

        Returns:
            dict: Customized representation of the instance.
        """
        data = super().to_representation(instance)
        try:
            data["unit"] = f"master/check/unit/{instance.unit.id}"
        except Exception:
            pass
        return data
