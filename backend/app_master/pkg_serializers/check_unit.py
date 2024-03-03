# ========================================================================
from app_master.pkg_models.check_unit import UNIT
from utility.abstract_serializer import Serializer


# ========================================================================
class Unit(Serializer):
    """
    Serializer for Unit model.
    """

    class Meta:
        """
        Metadata for Unit serializer.
        """

        model = UNIT
        fields = "__all__"
        extra_kwargs = Serializer().extra()
