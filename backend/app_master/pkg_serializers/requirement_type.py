# ========================================================================
from app_master.pkg_models.check_product_type import REQUIREMENT_TYPE
from utility.abstract_serializer import Serializer


# ========================================================================
class Requirement_Type(Serializer):
    class Meta:
        model = REQUIREMENT_TYPE
        fields = "__all__"
        extra_kwargs = Serializer().extra()
