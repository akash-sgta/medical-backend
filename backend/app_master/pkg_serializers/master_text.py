# ========================================================================
from app_master.pkg_models.master_text import TEXT
from utility.abstract_serializer import Serializer


# ========================================================================
class Text(Serializer):
    """
    Serializer for Text model.
    """

    class Meta:
        """
        Metadata for Text serializer.
        """

        model = TEXT
        fields = "__all__"
        extra_kwargs = Serializer().extra()
