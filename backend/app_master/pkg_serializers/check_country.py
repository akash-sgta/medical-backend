# ========================================================================
from app_master.pkg_models.check_country import COUNTRY
from utility.abstract_serializer import Serializer


# ========================================================================
class Country(Serializer):
    """
    Serializer for Country model.
    """

    class Meta:
        """
        Metadata for Country serializer.
        """

        model = COUNTRY
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        """
        Customizes the representation of Country instances.

        Args:
            instance: The instance of Country model.

        Returns:
            dict: Customized representation of the instance.
        """
        data = super().to_representation(instance)
        try:
            data["continent"] = f"master/check/continent/{instance.continent.id}"
        except Exception:
            pass
        return data
