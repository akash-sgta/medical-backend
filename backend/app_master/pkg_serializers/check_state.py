# ========================================================================
from app_master.pkg_models.check_state import STATE
from utility.abstract_serializer import Serializer


# ========================================================================
class State(Serializer):
    """
    Serializer for State model.
    """

    class Meta:
        """
        Metadata for State serializer.
        """

        model = STATE
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        """
        Customizes the representation of State instances.

        Args:
            instance: The instance of State model.

        Returns:
            dict: Customized representation of the instance.
        """
        data = super().to_representation(instance)
        try:
            data["country"] = f"master/check/country/{instance.country.id}"
        except Exception:
            pass
        return data
