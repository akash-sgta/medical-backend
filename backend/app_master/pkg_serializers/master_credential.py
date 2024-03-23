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
        extra_kwargs = Serializer().extra()

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
            del data["pwd"]
        except Exception:
            pass
        try:
            del data["is_admin"]
        except Exception:
            pass
        try:
            del data["is_internal_user"]
        except Exception:
            pass
        try:
            del data["is_external_user"]
        except Exception:
            pass
        return data
