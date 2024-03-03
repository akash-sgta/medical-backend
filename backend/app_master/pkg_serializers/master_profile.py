# ========================================================================
from app_master.pkg_models.master_profile import PROFILE
from utility.abstract_serializer import Serializer


# ========================================================================
class Profile(Serializer):
    """
    Serializer for Profile model.
    """

    class Meta:
        """
        Metadata for Profile serializer.
        """

        model = PROFILE
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        """
        Customizes the representation of Profile instances.

        Args:
            instance: The instance of Profile model.

        Returns:
            dict: Customized representation of the instance.
        """
        data = super().to_representation(instance)
        try:
            data["cred"] = f"master/master/credential/{instance.cred.id}"
        except Exception:
            pass
        try:
            data["address"] = f"master/master/address/{instance.address.id}"
        except Exception:
            pass
        try:
            data["image"] = f"cdn/master/file/{instance.image.id}"
        except Exception:
            pass
        try:
            data["bio"] = f"master/master/text/{instance.bio.id}"
        except Exception:
            pass
        return data
