# ========================================================================
from app_master.pkg_models.check_unit_of_measurement import UOM
from utility.abstract_serializer import Serializer


# ========================================================================
class UOM(Serializer):
    class Meta:
        model = UOM
        fields = "__all__"
        extra_kwargs = Serializer().extra()
