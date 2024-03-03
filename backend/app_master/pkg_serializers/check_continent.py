# ========================================================================
from app_master.pkg_models.check_continent import CONTINENT
from utility.abstract_serializer import Serializer


# ========================================================================
class Continent(Serializer):
    """
    Serializer for Continent model.
    """

    class Meta:
        """
        Metadata for Continent serializer.
        """

        model = CONTINENT
        fields = "__all__"
        extra_kwargs = Serializer().extra()
