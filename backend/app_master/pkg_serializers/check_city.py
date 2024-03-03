# ========================================================================
from app_master.pkg_models.check_city import CITY
from utility.abstract_serializer import Serializer


# ========================================================================
class City(Serializer):
    """
    Serializer for City model.
    """

    class Meta:
        """
        Metadata for City serializer.
        """

        model = CITY
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        """
        Customizes the representation of City instances.

        Args:
            instance: The instance of City model.

        Returns:
            dict: Customized representation of the instance.
        """
        data = super().to_representation(instance)
        try:
            data["state"] = f"master/check/state/{instance.state.id}"
        except Exception:
            pass
        return data
