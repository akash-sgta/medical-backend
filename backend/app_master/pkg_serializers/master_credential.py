# ========================================================================
from app_master.pkg_models.master_credential import CREDENTIAL
from utility.abstract_serializer import Serializer


# ========================================================================
class Credential(Serializer):
    """
    Serializer for Credential model.
    """

    class Meta:
        """
        Metadata for Credential serializer.
        """

        model = CREDENTIAL
        fields = "__all__"
        extra_kwargs = (
            Serializer().extra()
            # .update(
            #     {
            #         "pwd": {"write_only": True},
            #     }
            # )
        )

    def to_representation(self, instance):
        """
        Customizes the representation of Credential instances.

        Args:
            instance: The instance of Credential model.

        Returns:
            dict: Customized representation of the instance.
        """
        data = super().to_representation(instance)
        try:
            data["pwd"] = "▓R▓E▓D▓A▓C▓T▓E▓D▓"
        except Exception:
            pass
        return data
