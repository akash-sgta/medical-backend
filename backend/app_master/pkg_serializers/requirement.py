# ========================================================================
from app_master.pkg_models.master_product import REQUIREMENT
from utility.abstract_serializer import Serializer


# ========================================================================
class Requirement(Serializer):
    class Meta:
        model = REQUIREMENT
        fields = "__all__"
        extra_kwargs = Serializer().extra()
