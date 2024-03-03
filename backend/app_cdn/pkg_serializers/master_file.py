# ========================================================================
from app_cdn.pkg_models.master_file import FILE
from utility.abstract_serializer import Serializer


# ========================================================================
class File(Serializer):
    """
    Serializer for File model.
    """

    class Meta:
        """
        Metadata for File serializer.
        """

        model = FILE
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        """
        Customizes the representation of File instances.

        Args:
            instance: The instance of File model.

        Returns:
            dict: Customized representation of the instance.
        """
        data = super().to_representation(instance)
        try:
            data["type"] = f"/cdn/check/file_type/{instance.type.id}"
        except Exception:
            pass
        return data
