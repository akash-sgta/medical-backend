# ========================================================================
from app_master.pkg_models.check_currency import CURRENCY
from utility.abstract_serializer import Serializer


# ========================================================================
class Currency(Serializer):
    """
    Serializer for Currency model.
    """

    class Meta:
        """
        Metadata for Currency serializer.
        """

        model = CURRENCY
        fields = "__all__"
        extra_kwargs = Serializer().extra()
